from pathlib import Path
from dfault.objects import Dfault
from terminaltables import AsciiTable
from time import sleep
import click
import boto3
import configparser



home = str(Path.home())
config = configparser.ConfigParser()
config.read(home + "/.aws/config")
default_config = config["default"]
d = Dfault(default_config)
g = {}

# get default values where can
client = boto3.client("ec2")
g["availabilityzone"] = client.describe_availability_zones()["AvailabilityZones"][0]["ZoneName"]
security_groups = client.describe_security_groups()["SecurityGroups"]
security_groups = [(group["GroupId"], group["GroupName"]) for group in security_groups]

def get_spot_instance_id(response):
    ids = []
    for response in response["SpotInstanceRequests"]:
        ids.append(response["SpotInstanceRequestId"])
    return ids

def get_spot_state(client, fulfilled_ids, pending_spot_ids, instancecount):
    response = client.describe_spot_instance_requests(SpotInstanceRequestIds=pending_spot_ids)
    print("Launching spot states " + ", ".join(pending_spot_ids), end="\r", flush=True)

    for spot_instance in response["SpotInstanceRequests"]:
        for i, pending_spot_id in reversed(list(enumerate(pending_spot_ids))):
            if spot_instance["Status"]["Code"] == "fulfilled" and pending_spot_id == spot_instance["SpotInstanceRequestId"] and "InstanceId" in spot_instance.keys():
                fulfilled_ids.append(spot_instance["InstanceId"])
                del pending_spot_ids[i]

def get_url_from_instance_id(client, instance_ids):
    response = client.describe_instances(
            InstanceIds = instance_ids
            )
    urls = []
    for resv in response["Reservations"]:
        for instance in resv["Instances"]:
            privateip = instance["PrivateIpAddress"]
            publicip = instance["PublicIpAddress"]
            instanceid = instance["InstanceId"]
            urls.append({"privateip": privateip, "publicip": publicip, "instanceid": instanceid})
    return urls

def print_urls(urls):
    table_data = [
        ["Instance Id", "Private IP", "Public IP"]
    ]
    for url in urls:
        table_data.append([url["instanceid"], url["privateip"], url["publicip"]])
    table = AsciiTable(table_data)
    print(table.table)

@click.command()
@click.option("--InstanceType", prompt="Instance Type", default=d.get("instancetype", "t2.micro"), help="The instance type of the spot instance")
@click.option("--SpotPrice", prompt="Spot Price", help="The spot price you're willing to pay")
@click.option("--InstanceCount", prompt="Instance Count", default=1, help="Number of spot instances to be created")
@click.option("--AvailabilityZone", prompt="Availability Zone", default=d.get("availabilityzone", g["availabilityzone"]), help="Availability Zone of the spot instance")
@click.option("--LaunchImageId", prompt="Launch Image Id", default=d.get("launchimageid", "ami-d29e25b6"), help="Launch Image of the spot instance")
@click.option(
        "--SecurityGroup", 
        prompt="Security Group, pick from:\n\t" + "\n\t".join([group[0]+"("+group[1]+")" for group in security_groups]) +"\nDefault is",
        default=d.get("securitygroup", security_groups[0][0]),
        help="Security Group to put the spot instance"
        )
def main(instancetype, spotprice, instancecount, availabilityzone, launchimageid, securitygroup):
    interval = 3
    client = boto3.client("ec2")
    response = client.request_spot_instances(
            SpotPrice=spotprice,
            InstanceCount=int(instancecount),
            LaunchSpecification = {
                    "ImageId": launchimageid,
                    "Placement": {
                        "AvailabilityZone": availabilityzone
                        },
                    "InstanceType": instancetype,
                    "SecurityGroupIds": [securitygroup]
                }
            )
    pending_spot_ids = get_spot_instance_id(response)
    fulfilled_ids = []

    print("")
    for i in range(12):
        get_spot_state(client, fulfilled_ids, pending_spot_ids, instancecount)
        if len(pending_spot_ids) == 0:
            break
        sleep(5)

    print("\n")
    if len(pending_spot_ids) > 0:
        print("Spot Instances taking too long! Check your console to get full spot instances details\n")

    urls = get_url_from_instance_id(client, fulfilled_ids)
    print_urls(urls)

if __name__ == '__main__':
        main()

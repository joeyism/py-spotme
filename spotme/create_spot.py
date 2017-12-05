import boto3
import datetime
import click

# http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.request_spot_instances

client = boto3.client('ec2')

# client.describe_spot_price_history
# http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.request_spot_instances

response = client.request_spot_instances(
    DryRun=False,
    SpotPrice='0.10',
    ClientToken='string',
    InstanceCount=1,
    Type='one-time',
    LaunchSpecification={
        'ImageId': 'ami-fce3c696',
        'KeyName': 'awskey.pem',
        'SecurityGroups': ['sg-709f8709'],
        'InstanceType': 'm4.large',
        'Placement': {
            'AvailabilityZone': 'us-east-1a',
        },
        'BlockDeviceMappings': [
            {
                'Ebs': {
                    'SnapshotId': 'snap-f70deff0',
                    'VolumeSize': 100,
                    'DeleteOnTermination': True,
                    'VolumeType': 'gp2',
                    'Iops': 300,
                    'Encrypted': False
                },
            },
        ],

        'EbsOptimized': True,
        'Monitoring': {
            'Enabled': True
        },
        'SecurityGroupIds': [
            'sg-709f8709',
        ]
    }
)
response = client.request_spot_instances(
    AvailabilityZoneGroup='string',
    BlockDurationMinutes=123,
    ClientToken='string',
    DryRun=True|False,
    InstanceCount=123,
    LaunchGroup='string',
    LaunchSpecification={
        'SecurityGroupIds': [
            'string',
        ],
        'SecurityGroups': [
            'string',
        ],
        'AddressingType': 'string',
        'BlockDeviceMappings': [
            {
                'DeviceName': 'string',
                'VirtualName': 'string',
                'Ebs': {
                    'Encrypted': True|False,
                    'DeleteOnTermination': True|False,
                    'Iops': 123,
                    'KmsKeyId': 'string',
                    'SnapshotId': 'string',
                    'VolumeSize': 123,
                    'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
                },
                'NoDevice': 'string'
            },
        ],
        'EbsOptimized': True|False,
        'IamInstanceProfile': {
            'Arn': 'string',
            'Name': 'string'
        },
        'ImageId': 'string',
        'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge',
        'KernelId': 'string',
        'KeyName': 'string',
        'Monitoring': {
            'Enabled': True|False
        },
        'NetworkInterfaces': [
            {
                'AssociatePublicIpAddress': True|False,
                'DeleteOnTermination': True|False,
                'Description': 'string',
                'DeviceIndex': 123,
                'Groups': [
                    'string',
                ],
                'Ipv6AddressCount': 123,
                'Ipv6Addresses': [
                    {
                        'Ipv6Address': 'string'
                    },
                ],
                'NetworkInterfaceId': 'string',
                'PrivateIpAddress': 'string',
                'PrivateIpAddresses': [
                    {
                        'Primary': True|False,
                        'PrivateIpAddress': 'string'
                    },
                ],
                'SecondaryPrivateIpAddressCount': 123,
                'SubnetId': 'string'
            },
        ],
        'Placement': {
            'AvailabilityZone': 'string',
            'GroupName': 'string',
            'Tenancy': 'default'|'dedicated'|'host'
        },
        'RamdiskId': 'string',
        'SubnetId': 'string',
        'UserData': 'string'
    },
    SpotPrice='string',
    Type='one-time'|'persistent',
    ValidFrom=datetime(2015, 1, 1),
    ValidUntil=datetime(2015, 1, 1),
    InstanceInterruptionBehavior='hibernate'|'stop'|'terminate'
)

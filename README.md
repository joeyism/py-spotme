# SpotMe
A command line tool that allows you to spin up AWS EC2 Spot Instances instantly

## Background
I do a lot of computation, but my computer is pretty crappy, so often I have to spin up ec2 spot instances to do some computation. [Spot Instances](https://aws.amazon.com/ec2/spot/) are a good resource to use AWS EC2 instances for fairly cheap, and I am very frugal. I created this tool because I didn't want to have to develop something on my commandline, go to my browser and create a spot instance, then go back to my commandline to rsync/scp everything up. This tool allows me to stay in my commandline the whole way.

## Installation
To install, simply run

```bash
pip3 install --user spotme
```

## Setup
Since `spotcheck` uses boto3, you'll have to setup the same way. You can view the [docs here](http://boto3.readthedocs.io/en/latest/guide/quickstart.html)

A sample `config` file that is to in `~/.aws/config` is also in this repository.


## Usage
To use, run

```bash
spotme
```

and a series of questions will be prompted.

The result is of the form


```
Launching spot states sir-123abcde

+---------------------+---------------+---------------+
| Instance Id         | Public IP     | Private IP    |
+---------------------+---------------+---------------+
| i-05f10faefc833c643 | x.x.x.x       | x.x.x.x       |
+---------------------+---------------+---------------+

```

### Repeatable Usage
If you don't want to enter the CLI prompt every time, you can run the CLI with the options

```bash
spotme --InstanceType=t2.micro --SpotPrice=0.006 --InstanceCount=1 --AvailabilityZone=ca-central-1a --LaunchImageId=ami-d29e25b6 --SecurityGroup=sg-123abcd --KeyName=yourkeypair

```

## Version
* **1.2.0**
    * Added Key-pair name

* **1.1.0**
    * Added customization security group

* **1.0.x**
    * Fix Bugs

* **1.0.0**
    * First publish

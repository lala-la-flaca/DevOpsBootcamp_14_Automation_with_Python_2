import boto3

#Setting up Clients
ec2_client_paris  = boto3.client('ec2', region_name="eu-west-3")
ec2_client_frankfurt = boto3.client('ec2', region_name="eu-central-1")

#Setting Up Resources
ec2_resource_frankfurt = boto3.resource('ec2',region_name="eu-central-1")
ec2_resource_paris = boto3.resource('ec2',region_name="eu-west-3")

#Getting Information about instances
all_available_instances_frankfurt = ec2_client_frankfurt.describe_instances()
all_available_instances_paris = ec2_client_paris.describe_instances()

#Emtpy list to save instance IDs
#This avoids making a request per each instance to create tags.
instances_ids_frankfurt = []
instances_ids_paris = []

#Getting Reservations to access EC2 instances available
reservations_frankfurt = all_available_instances_frankfurt["Reservations"]
reservations_paris = all_available_instances_paris["Reservations"]

for reservation in reservations_frankfurt:
    instances_frankfurt = reservation['Instances']

    for instance in instances_frankfurt:
        #EC2 Instance parameters
        ec2_id = instance["InstanceId"]
        instances_ids_frankfurt.append(ec2_id)

#Creating Tags for Frankfurt Instances
response_frankfurt = ec2_resource_frankfurt.create_tags(
    Resources=instances_ids_frankfurt,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
        ]
)

for reservation in reservations_paris:
    instances_paris = reservation['Instances']

    for instance in instances_paris:
        #EC2 Instance parameters
        ec2_id = instance["InstanceId"]
        instances_ids_paris.append(ec2_id)

#Creating Tags for Paris Instances
response_paris = ec2_resource_paris.create_tags(
    Resources=instances_ids_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
        ]
)


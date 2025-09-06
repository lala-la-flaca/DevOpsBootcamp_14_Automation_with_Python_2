# 🐍Module 14 – Automation with Python
This exercise is part of Module 14: Automation with Python. Module 14 focuses on automating cloud operations with Python. The demos showcase how to interact with AWS services (EC2, EKS, snapshots), perform monitoring tasks, and implement recovery workflows. By the end of this module, you will have practical experience in scripting infrastructure automation, monitoring, and recovery solutions.

# 📦Demo 1 – Health Check: EC2 Status Checks
# 📌 Objective
Create a Python script to fetch and display EC2 instance statuses and extend it to run checks at regular intervals.

# 🚀 Technologies Used
* Python: programming language.
* IntelliJ-PyCharm: IDE used for development.
* AWS: Cloud provider.
* Boto3 AWS SDK for Python.
* Terraform: Infrastructure provisioning tool.
  
# 🎯 Features
🐍 Create a Python script that adds tags to all EC2 instances

# Prerequisites
* AWS account
* Terraform from previous Demos.
* Python and PyCharm installed.
  
# 🏗 Project Architecture

# ⚙️ Project Configuration
   
## Adding Tags to EC2 Instances
1. Add instances in Paris and Frankfurt in the AWS cosole.
2. Import boto3 module.
   ```bash
   import boto3
   ``` 
4. Initialize clients for each region
   ```bash
     #Setting up Clients
    ec2_client_paris  = boto3.client('ec2', region_name="eu-west-3")
    ec2_client_frankfurt = boto3.client('ec2', region_name="eu-central-1")
   ```
6. Initialize resources for each region
   ```bash
   #Setting Up Resources
   ec2_resource_frankfurt = boto3.resource('ec2',region_name="eu-central-1")
   ec2_resource_paris = boto3.resource('ec2',region_name="eu-west-3")
   ```
8. Getting all available instances.
   ```bash
   #Getting Information about instances
  all_available_instances_frankfurt = ec2_client_frankfurt.describe_instances()
  all_available_instances_paris = ec2_client_paris.describe_instances()
   ```
10. Create an empty list to save the instance IDs for each region
   ```bash
    #Emtpy list to save instance IDs
    #This avoids making a request per each instance to create tags.
    instances_ids_frankfurt = []
    instances_ids_paris = []
   ```
11. Obtain reservations to access available instances
    ```bash
    #Getting Reservations to access EC2 instances available
    reservations_frankfurt = all_available_instances_frankfurt["Reservations"]
    reservations_paris = all_available_instances_paris["Reservations"]
    ```
13. Iterate to obtain the store instance id.
    ```bash
      for reservation in reservations_frankfurt:
      instances_frankfurt = reservation['Instances']
  
      for instance in instances_frankfurt:
          #EC2 Instance parameters
          ec2_id = instance["InstanceId"]
          instances_ids_frankfurt.append(ec2_id)

    ```
15. Add tags to EC2
    ```bash
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
  ```
16. Apply the same logic to instances in Paris.
```bash
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

```

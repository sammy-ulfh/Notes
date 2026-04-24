## The goal

The goal of this task is to create a secure, isolated network within AWS by utilizing different components of AWS VPC. This network could potentially be used to run web servers along with a database server.

## Task resources

You should create a VPC with a number of resources inside it. You must tag each resource with a __Name__ tag. The list of resources, along with their __Name__ tags, is:

- VPC: `cmtr-3kqa67jd-vpc`
- Public Subnet: `cmtr-3kqa67jd-public_subnet`
- Private Subnet: `cmtr-3kqa67jd-private_subnet`
- Internet Gateway: `cmtr-3kqa67jd-internet_gateway`
- Public Route Table: `cmtr-3kqa67jd-route_public`
- Private Route Table: `cmtr-3kqa67jd-route_private`
- Public EC2 Instance: `cmtr-3kqa67jd-public`
- Private EC2 Instance: `cmtr-3kqa67jd-private`

## Objectives

1. Create VPC with CIDR block: `10.0.0.0/16`
2. Create a public subnet with CIDR block: `10.0.1.0/24`
3. Create a private subnet with CIDR block: `10.0.1.0/24`
4. Create an Internet Gateway and attach it to your VPC.
5. Create and Configure the Route Table for the public subnet. Add a route that directs all traffic destined outside the VPC (0.0.0.0/0) to the Internet Gateway.
6. Create and configure the Route Table for the private subnet. Ensure that the Private Route Table does not allow direct internet access.
7. Launch the public  EC2 instance in the public subnet using the `t2.micro` instance type and Amazon Linux 2023 AMI. Assign the `default` security group and an instance profile that allows AWS session manager connection (you may need to create a new instance profile).
8. Launching the private EC2 instance in the Private Subnet using the `t2.micro` instance type and Amazon Linux 2023 AMI. Assign the `default` security group.
9. Install nginx web server on the public EC2 instance. No additional configuration for nginx is required.

## Validation

1. Ensure all resources are created with the correct tags and configurations.
2. Confirm that the Public Subnet has access buth to the Private Subnet and to the Internet as well. You may connect to the Public EC2 instance terminal and use `ping` command to check the conectivity.
3. Connect to the Public EC2 instance terminal and verify that the nginx web server is installed and running. You may use `curl localhost` command to check the default web server page.

## Practical

1. Configuration of IAM profile
   
   Create the 'trust-policy.json' file:
   
	```json
	{
		"Version": "2012-10-17",
		"Statement": [
			{
				"Effect": "Allow",
				"Principal": { "Service": "ec2.amazonaws.com" },
				"Action": "sts:AssumeRole"
			}
		]
	}
	```

	- Create the Role
	  ```shell
	  aws iam create-role --role-name cmtr-3kqa67jd-ssm-role --assume-role-policy-document file://trust-policy.json
	  ```

	- Attach SSM policy
	  ```shell
	  aws iam attach-role-policy --role-name cmtr-3kqa67jd-ssm-role --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
	  ```

	- Create instance profile and assign the role
	  ```shell
	  aws iam create-instance-profile --instance-profile-name cmtr-3kqa67jd-ssm-profile 
	  
	  aws iam add-role-to-instance-profile --instance-profile-name cmtr-3kqa67jd-ssm-profile --role-name cmtr-3kqa67jd-ssm-role
	  ```

2. Create the VPC and enable the DNS

	```shell
	# Create VPC and save it's ID
	VPC_ID=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=cmtr-3kqa67jd-vpc}]' --query 'Vpc.VpcId' --output text) 
	
	# Enable DNS hostnames
	aws ec2 modify-vpc-attribute --vpc-id $VPC_ID --enable-dns-hostnames "{\"Value\":true}"
	
	echo "Created VPC: $VPC_ID"
	```


3. Create subnets

	```shell
	# A. Create public subnet
	PUB_SUB_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.1.0/24 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=cmtr-3kqa67jd-public_subnet}]' --query 'Subnet.SubnetId' --output text)
	
	# Enable auto-assign for public IP
	aws ec2 modify-subnet-attribute --subnet-id $PUB_SUB_ID --map-public-ip-on-launch
	
	# B. Create private subnet
	PRIV_SUB_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.2.0/24 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=cmtr-3kqa67jd-private_subnet}]' --query 'Subnet.SubnetId' --output text)
	
	echo "Public subnet: $PUB_SUB_ID | Private subnet: $PRIV_SUB_ID"
	```

4. Configure the Internet Gateway (IGW)

	```shell
	# Create IGW
	IGW_ID=$(aws ec2 create-internet-gateway --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=cmtr-3kqa67jd-internet_gateway}]' --query 'InternetGateway.InternetGatewayId' --output text)
	
	# Assign to the VPC
	aws ec2 attach-internet-gateway --vpc-id $VPC_ID --internet-gateway-id $IGW_ID
	
	echo "IGW connected: $IGW_ID"
	```

5. Configure Route Tables

	```shell
	# Public ROUTE TABLE
	PUB_RT_ID=$(aws ec2 create-route-table --vpc-id $VPC_ID --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=cmtr-3kqa67jd-route_public}]' --query 'RouteTable.RouteTableId' --output text)
	
	# Assign route to internet
	aws ec2 create-route --route-table-id $PUB_RT_ID --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID
	
	# Assign the public subnet
	aws ec2 associate-route-table --subnet-id $PUB_SUB_ID --route-table-id $PUB_RT_ID
	
	# Private Route Table
	PRIV_RT_ID=$(aws ec2 create-route-table --vpc-id $VPC_ID --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=cmtr-3kqa67jd-route_private}]' --query 'RouteTable.RouteTableId' --output text)
	
	# Assign private subnet
	aws ec2 associate-route-table --subnet-id $PRIV_SUB_ID --route-table-id $PRIV_RT_ID
	```

6. Variables and script

	```shell
	# Get default security group ID
	SG_ID=$(aws ec2 describe-security-groups --filters "Name=vpc-id,Values=$VPC_ID" "Name=group-name,Values=default" --query 'SecurityGroups[0].GroupId' --output text)
	
	# Get the current AMI ID of Amazon Linux 2023
	AMI_ID=$(aws ec2 describe-images --owners amazon --filters "Name=name,Values=al2023-ami-2023.*-x86_64" "Name=state,Values=available" "Name=architecture,Values=x86_64" --query "sort_by(Images, &CreationDate)[-1].ImageId" --output text)	
	```

	- Create the script for nginx

	```shell
	#!/bin/bash
	dnf update -y
	dnf install -y nginx
	systemctl enable nginx
	systemctl start nginx
	```

	- Lanzar instancias EC2

	```shell
	# Launch Public Instance
	aws ec2 run-instances \
	    --image-id $AMI_ID \
	    --count 1 \
	    --instance-type t2.micro \
	    --subnet-id $PUB_SUB_ID \
	    --security-group-ids $SG_ID \
	    --iam-instance-profile Name="cmtr-3kqa67jd-ssm-profile" \
	    --user-data file://userdata.sh \
	    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=cmtr-3kqa67jd-public}]'
	
	# Launch Private Instace
	aws ec2 run-instances \
	    --image-id $AMI_ID \
	    --count 1 \
	    --instance-type t2.micro \
	    --subnet-id $PRIV_SUB_ID \
	    --security-group-ids $SG_ID \
	    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=cmtr-3kqa67jd-private}]'
	```



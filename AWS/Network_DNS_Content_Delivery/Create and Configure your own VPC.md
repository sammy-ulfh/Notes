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
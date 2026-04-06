# Index

- [[#Goal]]
- [[#Tasks]]
- [[#Objectives]]
- [[#Manual verification]]
- [[#Practice]]
- [[#Manual verification]]
## Goal

The goal is to configure required permissions for a given user group and verify that users within this group have inherited these permissions.

## Tasks


- IAM GROUP: Create an IAM user Group.
- IAM Users: These users are added to the ${group_developers} group.

## Objectives

In the one move, you must grant the correct permissions to the ${group_developers} group so that each user in the group has full access to the EC2 service. User an AWS-managed policy and follow the principle of least privilege. Do not create your own policy.

One "move" is the creation, updating, or deletion of an AWS resource. Some validation steps may pass without any action, but to complete the tasks, you must ensure that all steps are passed.

## Manual verification

To make sure everything has been done correctly, you can a console password for one of the users, sign in as this user, and verify that the ${group_developers} group has full access to the EC2 service.

## Practice

1. Creations of IAM Groups:
   
```
   aws iam create-group --group-name ${group_developers}
```

2. Creation of IAM Users:

```
aws iam create-user --user-name <nombre-del-usuario>
```

3. Adding IAM Users to IAM Group:
   
```
aws iam add-user-to-group \
    --user-name <nombre-del-usuario> \
    --group-name ${group_developers}
```

4. Group Policy:

```
aws iam attach-group-policy \
    --group-name ${group_developers} \
    --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess
```
### Manual verification

1. Get Account ID:
   
```
aws sts get-caller-identity
```

2. Create password for a specific user:

```
aws iam create-login-profile --user-name ${user_name} --password "PASSWORD" --no-password-reset-required
```

3. Get Web Console in the URL by changing the number ID (the first serie of numbers):
   
```
https://123456789012.signin.aws.amazon.com/console
```

4. Another option to check correct EC2 access configuration in CLI:
   
```
aws ec2 describe-instances --region your-region --profile <name-of-username-profile>
```

Write the correct user credentials to login and finally go to searcher and type EC2, if you see all without API Error...

That's it!


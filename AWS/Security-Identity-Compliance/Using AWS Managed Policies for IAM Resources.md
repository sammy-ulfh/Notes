# Index

## Lab Description

The goal of this task is to configure two IAM roles by attaching AWS managed policies.

## Task Resources

Region: eu-west-1

In this task, you will work with the following resources:

- __Read-only Role__; `cmtr-3kqa67jd-iam-mp-iam_role-readonly` - This role will have read-only access to AWS resources.
- __Administrator Role__: `cmtr-3kqa67jd-iam-mp-iam_role-administrator` - This role will have full administration access to AWS.

## Objectives

In two moves, you must grant access for each role according to their names by using AWS managed policies. Please use existing AWS policies and do not create your own.

One "move" is the creation, updating, or deletion of the AWS resource. Some validation steps may pass without any action, but to complete the task, you must ensure that all steps are passed.

## Practical

### Read-Only

To attach read only policy arn to a existing role:

1.  __Attach the AWS managed read-only policy__ to the role:

```shell
aws iam attach-role-policy --role-name name --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess
```

2. __Verify attachment__ to ensure the policy is correctly assigned:
   
```shell
aws iam list-attached-role-policies --role-name name 
```   

### Administrator

Next, to attach administrator role:

1. __Attach AWS managed Administrator policy__ to a role:
   
   ```shell
   aws iam attach-role-policy --role-name cmtr-3kqa67jd-iam-mp-iam_role-administrator --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
   ```

2. __Verify attachment__ to ensure the policy is correctly assigned:
   
```shell
aws iam list-attached-role-policies --role-name name 
```   
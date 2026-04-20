# Index

## The goal of the task

The goal of this task is to explore the process of evaluating policies and to configure both identity-based policy and resource-based policy for a specific role.

## Task resources

In this task you will work with the following:

- **IAM Role:** `cmtr-3kqa67jd-iam-peld-iam_role` You will grant specific permissions for this role and check to make sure they are applied successfully.
- **S3 Bucket**: `cmtr-3kqa67jd-iam-peld-bucket-9719716` A bucket with a existing policy.

## Task flow

In two moves, you must:

1. Grant full access to amazon S3 Service for the `cmtr-3kqa67jd-iam-peld-iam_role` role. **Please use an existing AWS policy; do not create your own**.
2. Update the resource-based S3 bucket policy to prohibit the deletion of any objects inside the `cmtr-3kqa67jd-iam-peld-bucket-9719716` bucket specifically for `cmtr-3kqa67jd-iam-peld-iam_role` role.

One move is to create, update, or delete the AWS resource. Some verification steps may pass without any action, but to complete the task, you must ensure that all steps are passed.

## Practical

1. Grant full access with an existing policy

```shell
aws iam attach-role-policy --role-name cmtr-3kqa67jd-iam-peld-iam_role --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```


2. Update resource-based S3

Get Account ID: 

```
aws sts get-caller-identity --query "Account" --output text
```

Create inline-policy.json file

```txt
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "arn:aws:iam::ID:role/cmtr-3kqa67jd-iam-peld-iam_role"
      },
      "Action": [
        "s3:DeleteObject",
        "s3:DeleteObjectVersion"
      ],
      "Resource": "arn:aws:s3:::cmtr-3kqa67jd-iam-peld-bucket-9719716/*"
    }
  ]
}
```

```shell
aws s3api put-bucket-policy --bucket cmtr-3kqa67jd-iam-peld-bucket-9719716 --policy file://inline-policy.json
```


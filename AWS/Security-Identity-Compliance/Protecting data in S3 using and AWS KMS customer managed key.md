
# Index

## The goal

The goal of this task is to encrypt the contents of an S3 bucket using a KMS automatically created in your account and to add a new object to encrypted bucket. An IAM role must also be configured to work with the KMS key.

## Task resources

In this task, you will work with the following resources:

- __IAM Role__ `cmtr-3kqa67jd-iam-sewk-iam_role`: A role with full access to IAM S3 services. CloudMentor will assume this role during the task validation.
- __S3 Bucket__ `cmtr-3kqa67jd-iam-sewk-bucket-18396-1` and `cmtr-3kqa67jd-iam-sewk-bucket-18396-2`: The first bucket contains an object, which you need to copy to the second bucket.
- __KMS Key__ `arn:aws:kms:eu-west-1:160885290237:key/ec2a5ed9-e1ce-4a22-a7c2-3838733cdd34`: This key can only be used to encrypt objects in the second bucket; encrypting objects and the bucket itself with other keys is prohibited.

## Task flow

In three moves, you must:

1. Grant all necessary permissions for the `cmtr-3kqa67jd-iam-sewk-iam_role` to work with the key. Do not grant full administrator access.
2. Enable server-side encryption for the `cmtr-3kqa67jd-iam-sewk-bucket-18396-2` bucket using the AWS KMS key with the `arn:aws:kms:eu-west-1:ACCOUNT_ID:key/ec2a5ed9-e1ce-4a22-a7c2-3838733cdd34` ARN.

## Validation

To make sure you can put a new encrypted object in the encrypted bucket. To do this, copy the _confidential_credentials.csv_ file from the `cmtr-3kqa67jd-iam-sewk-bucket-18396-1` bucket to the `cmtr-3kqa67jd-iam-sewk-bucket-18396-2` bucket using AWS CLI or by downloading an object from `cmtr-3kqa67jd-iam-sewk-bucket-18396-1` and uploading it to `cmtr-3kqa67jd-iam-sewk-bucket-18396-2`. As a result, the copied file _confidential_credentials.csv_ should be encrypted.

## Practical

1. Grant all necessary permissions for the `cmtr-3kqa67jd-iam-sewk-iam_role` to work with the key. Do not grant full administrator access.

	policy.json
	
```json
{
  "Version": "2012-10-17",
  "Id": "key-console-policy-3",
  "Statement": [
    {
      "Sid": "Enable IAM User Permissions",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUUNT_ID:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "Allow use of the key",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT_ID:role/cmtr-3kqa67jd-iam-sewk-iam_role"
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt",
        "kms:GenerateDataKey",
        "kms:DescribeKey"
      ],
      "Resource": "*"
    }
  ]
}
```

```shell
aws kms put-key-policy --key-id ec2a5ed9-e1ce-4a22-a7c2-3838733cdd34 --policy-name default --policy file://policy.json
```

2. Enable server-side encryption for the `cmtr-3kqa67jd-iam-sewk-bucket-18396-2` bucket using the AWS KMS key with the `arn:aws:kms:eu-west-1:160885290237:key/ec2a5ed9-e1ce-4a22-a7c2-3838733cdd34` ARN.

rules.json

```json
{
  "Rules": [
    {
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms",
        "KMSMasterKeyID": "arn:aws:kms:eu-west-1:ACCOUNT_ID:key/ec2a5ed9-e1ce-4a22-a7c2-3838733cdd34"
      },
      "BucketKeyEnabled": true
    }
  ]
}
```

```shell
aws s3 cp s3://cmtr-3kqa67jd-iam-sewk-bucket-18396-1/confidential_credentials.csv s3://cmtr-3kqa67jd-iam-sewk-bucket-18396-2/confidential_credentials.csv --sse aws:kms --sse-kms-key-id arn:aws:kms:eu-west-1:ACCOUNT_ID:key/ec2a5ed9-e1ce-4a22-a7c2-3838733cdd34
```
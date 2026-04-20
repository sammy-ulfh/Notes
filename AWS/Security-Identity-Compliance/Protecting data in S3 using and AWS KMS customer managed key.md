
# Index

## The goal

The goal of this task is to encrypt the contents of an S3 bucket using a KMS automatically created in your account and to add a new object to encrypted bucket. An IAM role must also be configured to work with the KMS key.

## Task resources

In this task, you will work with the following resources:

- __IAM Role__ `role`: A role with full access to IAM S3 services. CloudMentor will assume this role during the task validation.
- __S3 Bucket__ `bucket_1` and `bucket_2`: The first bucket contains an object, which you need to copy to the second bucket.
- __KMS Key__ `kms_key_arn`: This key can only be used to encrypt objects in the second bucket; encrypting objects and the bucket itself with other keys is prohibited.

## Task flow

In three moves, you must:

1. Grant all necessary permissions for the `iam_role` to work with the key. Do not grant full administrator access.
2. Enable server-side encryption for the `s3_bucket_2` bucket using the AWS KMS key with the `kms_key_arn` ARN.

## Validation

To make sure you can put a new encrypted object in the encrypted bucket. To do this, copy the _confidential_credentials.csv_ file from the `${s3_bucket_1}` bucket to the `${s3_bucket_2}` bucket using AWS CLI or by downloading an object from `${s3_bucket_1}` and uploading it to `${s3_bucket_2}`. As a result, the copied file _confidential_credentials.csv_ should be encrypted.

## Practical


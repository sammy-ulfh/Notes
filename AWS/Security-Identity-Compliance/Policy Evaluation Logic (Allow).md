# Index

## The goal

The goal of this tasks are to explore the process of evaluating policies and to configure both and identity-based policy and a resource-based policy for a specific role.

## Task resources

In this task, you will work with the following resources:

- __IAM ROLE__ `cmtr-3kqa67jd-iam-pela-iam_role`: You will grant specific permissions to this role and verify that they are applied successfully.
- __S3 Bucket__ `cmtr-3kqa67jd-iam-pela-bucket-1-497758`: A bucket with default configuration and one object inside. A resoucmtr-3kqa67jd-iam-pela-bucket-2-497758rce-based S3 bucket policy should be created for this bucket.
- __S3 Bucket__ `cmtr-3kqa67jd-iam-pela-bucket-2-497758`: An empty bucket used solely for task verification purposes. Do not attach any policies to this bucket or change its configuration.

## Task flow

In two moves, you must:

1. Create and attach an inline identity-based policy to the `cmtr-3kqa67jd-iam-pela-iam_role` role that allows all buckets to be listed.
2. Create a resource-based S3 bucket policy that allows to get and put an object as well as list the objects in the `cmtr-3kqa67jd-iam-pela-bucket-1-497758` bucket. The `cmtr-3kqa67jd-iam-pela-iam_role` role must be allowed to perform all of these actions for the `cmtr-3kqa67jd-iam-pela-bucket-1-497758` bucket only; do not allow access to all principals.


One move is to create, update or delete AWS resource. Some verification steps may pass without any action, but to complete the task, you must ensure that all the steps are passed.

## Practical

1. Create and attach an inline identity-based policy to the `cmtr-3kqa67jd-iam-pela-iam_role` role that allows all buckets to be listed:

	First, create policy document that allow list all of the buckets:
	
	```json
	{
	  "Version": "2012-10-17",
	  "Statement": [
	    {
	      "Effect": "Allow",
	      "Action": "s3:ListAllMyBuckets",
	      "Resource": "*"
	    }
	  ]
	}
	```

	Second, put the policy to the `cmtr-3kqa67jd-iam-pela-iam_role` role:
	
	```bash
	aws iam put-role-policy --role-name cmtr-3kqa67jd-iam-pela-iam_role --policy-name ListAllBucketsPolicy --policy-document file://policy-document.json
	```

2. Create a resource-based S3 bucket policy that allows to get and put an object as well as list the objects in the `cmtr-3kqa67jd-iam-pela-bucket-1-497758` bucket. The `cmtr-3kqa67jd-iam-pela-iam_role` role must be allowed to perform all of these actions for the `cmtr-3kqa67jd-iam-pela-bucket-1-497758` bucket only; do not allow access to all principals.

	First, create policy document for the bucket to allow get, put and list inside:
	
	```json
	{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT_ID:role/cmtr-3kqa67jd-iam-pela-iam_role"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::cmtr-3kqa67jd-iam-pela-bucket-1-497758",
        "arn:aws:s3:::cmtr-3kqa67jd-iam-pela-bucket-1-497758/*"
      ]
    }
  ]
}
	```


Put your account id inside principal.

To get account ID:

```bash
aws sts get-caller-identity --query 'Account' --output text   
```

Finally, assign the policy to the bucket

```bash
aws s3api put-bucket-policy --bucket cmtr-3kqa67jd-iam-pela-bucket-1-497758 --policy file://bucket-policy.json   
```

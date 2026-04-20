# Index

## The goal

The goal of this task is to grant the correct permission to a lambda function so that it can access the necessary resources and other resources can access it as well.

## Task Resources

In this task you will work with the following resources:

- __Lambda function__ `cmtr-3kqa67jd-iam-lp-lambda`: Returns a list of lambda functions in the AWS account. This function has an execution role `cmtr-3kqa67jd-iam-lp-iam_role` and a resource-based policy and services as the HTTP API back end.
- __Lambda execution role__ `cmtr-3kqa67jd-iam-lp-iam_role`.
- __API Gateway__ `cmtr-3kqa67jd-iam-lp-apigwv2_api`: An HTTP API integrated with the `cmtr-3kqa67jd-iam-lp-lambda` function.

## Task flow

You must achieve the following objectives in two moves:

1. Grant the correct permissions to the Lambda function so it can access the resources it needs based on the function code. Use the AWS managed policy that grant access to Lambda API actions, and follow the principle of least privilege. __Use the existing AWS policy; do not create your own__.
2. Grant the correct permissions to the Lambda function so that the HTTP API can invoke it.
   
## Practical


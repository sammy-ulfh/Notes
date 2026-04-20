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

1. Set minimum permissions for lambda role
   
```shell
   aws iam attach-role-policy --role-name cmtr-3kqa67jd-iam-lp-iam_role --policy-arn awn:aws:iam::aws:policy/AWSLambda_ReadOnlyAccess
```

2. Get Account ID and API ID and save into a variable
   
Account ID:

```shell
ACCOUNT_ID=$(aws sts get-callet-identity --query "Account" --output text)
```

API ID:

```shell
API_ID$(aws apigatewayv2 get-apis --region eu-west-1 --query "Items[?Name=='cmtr-3kqa67jd-iam-lp-apigwv2_api'].ApiId" --output text) 
```

3. Set api gateway perssions to invoke lambda

```shell
aws lambda add-permission --function-name cmtr-3kqa67jd-iam-lp-lambda --statement-id apigw-invoke-permission --action Lambda:InvokeFunction --principal apigateway.amazonaws.com --source-arn "arn:aws:execute-api:eu-west-1:${ACCOUNT_ID}:${API_ID}/*/*" --region eu-west-1
```

4. Get web URL to check if it is working
   
```shell
aws apigatewayv2 get-api --api-id $API_ID --region eu-west-1 --query "ApiEndpoint" --output text
```

Finally use the url with the '/get_list' path. If it return the function name, it's working.
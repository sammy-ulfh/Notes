# Index


#### The Goal of the Task

The goal of this task is to configure role chaining using two roles, allowing one dedicated role to assume another role with read-only access.

#### Resources

Region-specific resources are created in the `eu-west-1` region.

The following roles have been created for you:

- **Assume Role `cmtr-3kqa67jd-iam-ar-iam_role-assume`**: This role should be assumed by any user in your AWS account.
- **Read-Only Role `cmtr-3kqa67jd-iam-ar-iam_role-readonly`**: This role should be assumed only by the `cmtr-3kqa67jd-iam-ar-iam_role-assume` role.

---
#### Flow

Your task is to:

1. Configure proper permissions for the `cmtr-3kqa67jd-iam-ar-iam_role-assume` role, allowing it to assume the `cmtr-3kqa67jd-iam-ar-iam_role-readonly` role. Do not grant full administrator access!
2. Grant full read-only access for the `cmtr-3kqa67jd-iam-ar-iam_role-readonly` role. Please use an existing AWS policy; do not create your own.
3. Configure the correct trust policy for the `cmtr-3kqa67jd-iam-ar-iam_role-readonly` role to allow it to be assumed by the `cmtr-3kqa67jd-iam-ar-iam_role-assume` role.

One "move" is the _creation_, _updating_, or _deletion_ of an AWS resource. Some verification steps may pass without any action, but to complete the task, you must ensure that all the steps are passed.

## Execution

❯ aws iam attach-role-policy \
  --role-name cmtr-3kqa67jd-iam-ar-iam_role-readonly \
  --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess

❯ mv trust-policy.json

```TXT
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT_ID:role/cmtr-3kqa67jd-iam-ar-iam_role-assume"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

❯ aws iam update-assume-role-policy \
  --role-name cmtr-3kqa67jd-iam-ar-iam_role-readonly \
  --policy-document file://trust-policy.json

❯ nvim assume-policy.json

```txt
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::ACCOUNT_ID:role/cmtr-3kqa67jd-iam-ar-iam_role-readonly"
    }
  ]
}  
```

❯ aws iam put-role-policy \
  --role-name cmtr-3kqa67jd-iam-ar-iam_role-assume \
  --policy-name AllowAssumeReadonlyRole \
  --policy-document file://assume-policy.json
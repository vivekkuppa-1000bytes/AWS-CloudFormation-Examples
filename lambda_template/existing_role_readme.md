This AWS CloudFormation template sets up a serverless architecture on AWS to convert JSON files stored in an S3 bucket to Parquet format using an AWS Lambda function. The setup includes an SNS topic for notifications and utilizes an existing IAM role for Lambda execution.

## Prerequisites
- An existing IAM role with necessary permissions for Lambda execution.
- Basic understanding of AWS CloudFormation.

## Parameters
- **TopicNamePlaceholder:** Name for the SNS topic.
- **FunctionNamePlaceholder:** Name for the Lambda function.
- **BucketNamePlaceholder:** Name for the S3 bucket.
- **PrefixPlaceholder:** Prefix for the S3 key filter.
- **SuffixPlaceholder:** Suffix for the S3 key filter.
- **RoleArnPlaceholder:** ARN of the existing IAM role.
- **EmailPlaceholder:** Email address for SNS topic subscription.

## Resources
- **SNS Topic (`SNSTopic`):** Creates an SNS topic with a subscription for email notifications.
- **Lambda Function (`LambdaFunction`):** Defines a Lambda function with necessary configurations for JSON to Parquet conversion triggered by S3 events.
- **S3 Bucket (`S3Bucket`):** Creates an S3 bucket to store JSON and Parquet files.

## Outputs
- **TopicArn:** ARN of the created SNS topic.
- **BucketName:** Name of the created S3 bucket.

## Usage
1. Fill in the required parameters in the CloudFormation template.
2. Deploy the template using AWS CloudFormation.
3. Once deployed, upload JSON files to the specified S3 bucket. The Lambda function will automatically convert them to Parquet format.
   
## License

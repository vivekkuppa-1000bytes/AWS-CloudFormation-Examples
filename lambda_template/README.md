### s3lambdatrigger.yaml

<u>This AWS CloudFormation template creates a serverless solution for converting JSON files stored in an S3 bucket to Parquet format using AWS Lambda and AWS SNS</u>
### Parameters
- **BucketName**: Name for the S3 bucket where JSON files are stored.
- **PrefixPlaceholder**: Prefix for the S3 key filter.
- **SuffixPlaceholder**: Suffix for the S3 key filter (default: ".json").
- **snstopicname**: Name of the SNS topic.
- **snsemail**: Email ID for SNS subscription.
- **lambdafunctionname**: Name of the Lambda function.
- **pythonruntime**: Python runtime version (e.g., python3.12).
- **pandaslayerversion**: Version of the Pandas layer.
- **lambdarolename**: Name of the Lambda execution role.

### Resources
- **LambdaExecutionRole**: IAM role for Lambda function execution.
- **MyJsonParquetBucket**: S3 bucket for storing Parquet files.
- **s3Permission**: Lambda permission to invoke function triggered by S3 events.
- **MyJsonToParquetTopic**: SNS topic for notifications.
- **MyLambdaFunction**: Lambda function to convert JSON to Parquet.

### Outputs
- **SnsTopicArn**: SNS Topic ARN.

### How to Use
1. Modify parameters according to your requirements.
2. Deploy the CloudFormation stack using the AWS Management Console or AWS CLI.

For detailed instructions on deploying CloudFormation stacks, refer to the AWS documentation.


### JSONtoParquetConversionTemplate.yaml
This AWS CloudFormation template defines a serverless architecture to convert JSON files stored in an Amazon S3 bucket into Parquet files using an AWS Lambda function triggered by S3 events. Let's break down the components and their functionalities:

### Parameters:
- **RoleNamePlaceholder:** Name for the IAM role.
- **TopicNamePlaceholder:** Name for the SNS topic.
- **FunctionNamePlaceholder:** Name for the Lambda function.
- **BucketNamePlaceholder:** Name for the S3 bucket.
- **PrefixPlaceholder:** Prefix for filtering S3 key names.
- **SuffixPlaceholder:** Suffix for filtering S3 key names.
- **EmailPlaceholder:** Email address for SNS notifications.

### Resources:
1. **SNSTopic (AWS::SNS::Topic):**
   - A simple notification service (SNS) topic to send notifications.
   - Subscribed to an email endpoint for receiving notifications.

2. **LambdaExecutionRole (AWS::IAM::Role):**
   - IAM role allowing Lambda to execute actions on AWS resources.
   - Trust policy allowing Lambda service to assume this role.
   - Managed policy granting permissions for Lambda to log to CloudWatch, access S3 objects, and publish to SNS.

3. **LambdaFunction (AWS::Serverless::Function):**
   - AWS Lambda function definition.
   - Code to convert JSON to Parquet using Pandas and Boto3.
   - Linked to the IAM role for execution permissions.
   - Configured with a layer containing additional dependencies.
   - Set with memory and timeout configurations.
   - EventInvokeConfig to specify SNS destinations for success and failure invocations.
   - Triggered by S3 events (object creation) with optional prefix and suffix filters.

4. **S3Bucket (AWS::S3::Bucket):**
   - S3 bucket for storing JSON and Parquet files.

### Outputs:
- **TopicArn:** ARN of the SNS topic for notifications.
- **BucketName:** Name of the S3 bucket for file storage.

### Explanation:
- The template enables the creation of necessary AWS resources to automate the process of converting JSON files to Parquet format.
- SNS notifications are used for alerting about successful and failed invocations.
- IAM role ensures Lambda has the necessary permissions to interact with AWS services securely.
- Event-driven architecture triggers the Lambda function upon new objects being uploaded to the specified S3 bucket.
- The template promotes scalability, cost-effectiveness, and automation through serverless architecture.

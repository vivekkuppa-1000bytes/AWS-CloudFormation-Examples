# AWS CloudFormation Template: DBT Pipeline for Lambda Function

## Description
This CloudFormation template sets up a serverless data pipeline using AWS Lambda, AWS EventBridge (formerly known as CloudWatch Events), AWS API Gateway, AWS ECS (Elastic Container Service), and other AWS services. The pipeline fetches data from public APIs, processes it, and stores it in an Amazon S3 bucket.

## Parameters
- `BucketNameapi`: Name for the S3 bucket to store the files.
- `layerbucketname`: Name of the bucket which has layers.
- `requestslayername`: Name of the requests layer in the bucket.
- `pytzlayername`: Name of the pytz layer in the bucket.
- `repositoryname`: Name of the repository.
- `clustername`: Name of the ECS cluster.
- `runtimename`: Python runtime version. Default: 'python3.12'.
- `Timeout`: Lambda function timeout. Default: '300'.
- `MemorySize`: Lambda function memory in MB. Default: '256'.
- `TaskCpu`: CPU units for ECS task. Default: '256'.
- `TaskMemory`: Memory units for ECS task in MB. Default: '512'.
- `startingdate`: Start date for the scheduler in yyyy-mm-ddTHH:MM:SS.000Z. Default: '2024-03-29T00:00:00.000Z'.
- `EndDate`: End date for the scheduler in yyyy-mm-ddTHH:MM:SS.000Z. Default: '2025-01-01T23:59:59.000Z'.
- `Schedule`: Schedule for the EventBridge scheduler in format 'cron(expression)'. Default: 'cron(0 10 * * ? *)'.
- `restapiname`: Name of the REST API.
- `snowflakeiamarn`: Snowflake IAM ARN.
- `snowflakeexternalid`: Snowflake external ID.

## Resources
- `lambdaapirole`: IAM role for the Lambda function.
- `ecsrole`: IAM role for ECS.
- `ecslambdarole`: IAM role for Lambda function to trigger ECS.
- `snowflakeapigatewayrole`: IAM role for Snowflake API Gateway.
- `MyBucket`: S3 Bucket.
- `LambdaLayerReq`: Lambda layer for requests library.
- `LambdaLayerPytz`: Lambda layer for pytz library.
- `TriggerTheApi`: Lambda function to trigger data fetch and storage.
- `ScheduleLambda`: EventBridge schedule for invoking Lambda function.
- `MyECRRepository`: ECS Repository.
- `MyECSCluster`: ECS Cluster.
- `MyLogGroup`: CloudWatch Log Group.
- `MyTaskDefinition`: ECS Task Definition.
- `MyLambdaFunctionToTriggerECS`: Lambda function to trigger ECS task.
- `MyLambdaPermission`: Lambda permission for API Gateway.
- `TestApi`: API Gateway for testing.
- `Stack`: API Gateway resource stack.
- `PostMethod`: API Gateway method for POST requests.
- `Deployment`: API Gateway deployment.
- `ProdStage`: API Gateway stage for production.

## Usage
1. Customize the parameters as per your requirements.
2. Deploy the CloudFormation stack.
3. Monitor the pipeline through AWS services.
4. Test the API endpoints.

## Notes
- Ensure that necessary IAM permissions are granted to the roles and policies.
- Make sure to set up Snowflake IAM ARN and external ID correctly if applicable.
- Adjust scheduling parameters as needed for your use case.
- Review and adjust resource configurations for performance and cost optimization.


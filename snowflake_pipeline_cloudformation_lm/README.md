**AWS CloudFormation Template: DBT Pipeline for Lambda Function**

**Description**
This CloudFormation template sets up a serverless data pipeline using AWS Lambda, AWS EventBridge (formerly known as CloudWatch Events), AWS API Gateway, AWS ECS (Elastic Container Service), and other AWS services. The pipeline fetches data from public APIs, processes it, and stores it in an Amazon S3 bucket.

**Parameters**
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

**Resources**
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

 **Usage**
1. Customize the parameters as per your requirements.
2. Deploy the CloudFormation stack.
3. Monitor the pipeline through AWS services.
4. Test the API endpoints.


**GitHub Actions Workflow**
This repository includes a GitHub Actions workflow for automating the deployment of the CloudFormation stack defined in cloud_formation_pipeline.yaml. The workflow is triggered on every push event to the repository, specifically when changes are made to the cloud_formation_pipeline.yaml file.

**Workflow Steps**:

`Checkout:`
This step checks out the repository code to the runner machine, enabling subsequent steps to access the repository content.

`Configure AWS Credentials:`
Uses the aws-actions/configure-aws-credentials action to configure AWS credentials required for deploying the CloudFormation stack. The credentials are fetched securely from GitHub Secrets.

`Deploy CloudFormation Stack:`
Utilizes the aws-actions/aws-cloudformation-github-deploy action to deploy the CloudFormation stack named cloud_formation_pipeline using the template cloud_formation_pipeline.yaml. This step automates the deployment process, ensuring that infrastructure changes are applied promptly.

**Usage:**
Ensure that AWS credentials are properly configured in the GitHub repository secrets to enable access to AWS resources.
Modify the cloud_formation_pipeline.yaml file as needed to define or update your CloudFormation stack.
Commit and push changes to trigger the deployment workflow.
Monitor the workflow execution in the GitHub Actions tab to ensure successful deployment.
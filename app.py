import os
import subprocess
import json

def lambda_handler(event, context):
    # Run dbt
    run_process = subprocess.run(["dbt", "run"], capture_output=True, text=True)
    print(run_process.stdout)

    # Test dbt
    test_process = subprocess.run(["dbt", "test"], capture_output=True, text=True)
    print(test_process.stdout)


    return {
        'statusCode': 200,
        'body': json.dumps('DBT run and test completed.')
    }
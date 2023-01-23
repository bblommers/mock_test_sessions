from moto import mock_sts, mock_cloudformation
import boto3


EXAMPLE_AMI_ID = "ami-12c6146b"
cf_template_body = {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Stack 1",
    "Resources": {
        "EC2Instance1": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "ImageId": EXAMPLE_AMI_ID,
                "KeyName": "dummy",
                "InstanceType": "t2.micro",
            },
        }
    },
}


@mock_sts
@mock_cloudformation
def test_a_test_for_moto():
    cf_client = boto3.client("cloudformation", region_name="eu-west-1")
    response_create = cf_client.create_change_set(
        StackName="test",
        TemplateBody=str(cf_template_body),
        Capabilities=["CAPABILITY_IAM"],
        ChangeSetName="test",
    )
    print(response_create)

    #event_executechangeset["requestParameters"]["changeSetName"] = response_create["Id"]

    # I added here the mock part I mention, ignored for now

    # We test something here. Ignored for privacy purposes. That calls the other piece of code.

    # We assert things here
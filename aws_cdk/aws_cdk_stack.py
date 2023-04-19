from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_ssm as ssm

    # aws_sqs as sqs,
)
from constructs import Construct

class AwsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        parameter_name = '/cre/arane'
        ami_id = ssm.StringParameter.value_for_string_parameter(self, parameter_name)
        
        my_vpc = ec2.Vpc.from_lookup(self, "vpc-sandbox", vpc_id='vpc-0514d9d757a7a5dac')

        instance = ec2.Instance(self, 'Instance',
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.generic_linux(ami_id),
            vpc= my_vpc,
            key_name='my-cdk-key'
        )

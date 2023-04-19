import aws_cdk as core
import unittest
import aws_cdk.assertions as assertions

from aws_cdk.aws_cdk_stack import AwsCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk/aws_cdk_stack.py
class TestSSMParameter(unittest.TestCase):

    def test_parameter_value(self):
        # Replace 'my-parameter' with the name of the parameter you want to test
        parameter_name = '/cre/arane'
        parameter_value = self.ssm.get_parameter(Name=parameter_name)['Parameter']['Value']
        self.assertEqual(parameter_value, 'unittest_testing')

if __name__ == '__main__':
    unittest.main()
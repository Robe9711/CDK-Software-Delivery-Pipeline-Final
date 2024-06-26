from aws_cdk import core
from aws_cdk import aws_s3 as s3

class S3Bucket(core.Construct):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        self.bucket = s3.Bucket(self, "MyBucket")

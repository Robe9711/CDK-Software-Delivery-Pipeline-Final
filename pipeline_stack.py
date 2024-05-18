from aws_cdk import core
from .s3_bucket import S3Bucket
from repository import CodeCommitRepository
from codbuild import CodeBuild
from pipeline import CodePipeline

class SoftwarePipeline(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        my_bucket = S3Bucket(self, "MyBucket").bucket
        repository = CodeCommitRepository(self, "JavaRepository").repository
        codebuild = CodeBuild(
            self, "AppBuildProject",
            repository_arn=repository.repository_arn
        ).project
        CodePipeline(
            self, "Pipeline",
            repository=repository,
            codebuild=codebuild,
            my_bucket=my_bucket
            
            
        )
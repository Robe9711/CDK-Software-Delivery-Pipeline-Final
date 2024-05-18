from aws_cdk import core
from aws_cdk import aws_codecommit as codecommit

class CodeCommitRepository(core.Construct):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        
        super().__init__(scope, id, **kwargs)

        self.repository = codecommit.Repository(
            self, "JavaRepository",
            repository_name="java-project",
            code=codecommit.Code.from_zip_file("https://seis665-public.s3.amazonaws.com/java-project.zip")
        )

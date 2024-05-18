from aws_cdk import core
from aws_cdk import aws_codebuild as codebuild
from aws_cdk import aws_iam as iam

class CodeBuildProject(core.Construct):

    def __init__(self, scope: core.Construct, id: str, repository_arn: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.project = codebuild.PipelineProject(
            self, "AppBuildProject",
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml"),
            environment=codebuild.BuildEnvironment(build_image=codebuild.LinuxBuildImage.STANDARD_4_0),
        )
        self.project.add_to_role_policy(iam.PolicyStatement(
            actions=["codecommit:GitPull"],
            resources=[repository_arn]
        ))
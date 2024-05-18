from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as codepipeline_actions
from aws_cdk import aws_iam as iam

class CodePipeline(core.Construct):

    def __init__(self, scope: core.Construct, id: str, repository, codebuild, mybucket, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()
        self.pipeline = codepipeline.Pipeline(
            self, "Pipeline",
            stages=[
                codepipeline.StageProps(
                    stage_name="Source",
                    actions=[
                        codepipeline_actions.CodeCommitSourceAction(
                            action_name="Source",
                            repository=repository,
                            output=source_output
                        )
                    ]
                ),
                codepipeline.StageProps(
                    stage_name="Build",
                    actions=[
                        codepipeline_actions.CodeBuildAction(
                            action_name="Build",
                            project=codebuild,
                            input=source_output,
                            outputs=[build_output]
                        )
                    ]
                )
                
                
            ]
        )
        

        mybucket.grant_read_write(self.pipeline.role)
        repository.grant_read(self.pipeline.role)
        codebuild.role.add_managed_policy(
        iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
        )

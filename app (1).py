from aws_cdk import core
from pipeline_stack import SoftwarePipeline
app = core.App()
SoftwarePipeline(app, "SoftwarePipeline")

app.synth()

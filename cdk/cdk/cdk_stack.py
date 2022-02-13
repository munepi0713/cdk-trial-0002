from aws_cdk import (
    Duration,
    aws_lambda as lambda_,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks,
    Stack,
    CfnOutput,
    # aws_sqs as sqs,
)
from constructs import Construct


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        async_task_function = lambda_.Function(
            self,
            "EchoTwiceFunction",
            code=lambda_.Code.from_asset(path="../async-task/src"),
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="app.handler",
            timeout=Duration.seconds(25),
        )

        state_machine = sfn.StateMachine(
            self,
            "EchoTwiceStateMachine",
            definition=tasks.LambdaInvoke(
                self, "EchoTwiceTask", lambda_function=async_task_function
            ).next(sfn.Succeed(self, "Success")),
        )

        # Output state machine's ARN.
        CfnOutput(
            self,
            "EchoTwiceStateMachineArn",
            value=state_machine.state_machine_arn,
            export_name="C0002:EchoTwiceStateMachineArn",
        )

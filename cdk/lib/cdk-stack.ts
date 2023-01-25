import * as apigwv2 from '@aws-cdk/aws-apigatewayv2-alpha'
import { HttpLambdaIntegration } from '@aws-cdk/aws-apigatewayv2-integrations-alpha'
import * as cdk from 'aws-cdk-lib'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import { Construct } from 'constructs'
import * as fs from 'fs'
import * as yaml from 'js-yaml'
import * as _ from 'lodash'

function toHttpMethod(method: string): apigwv2.HttpMethod {
  switch (method.toLocaleLowerCase()) {
    case 'get': return apigwv2.HttpMethod.GET
    case 'post': return apigwv2.HttpMethod.POST
    case 'put': return apigwv2.HttpMethod.PUT
    case 'head': return apigwv2.HttpMethod.HEAD
    case 'options': return apigwv2.HttpMethod.OPTIONS
    case 'delete': return apigwv2.HttpMethod.DELETE
    case 'patch': return apigwv2.HttpMethod.PATCH
    default: return apigwv2.HttpMethod.GET
  }
}

export class TryCdk0002Stack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    // Load context parameters from cdk.json.
    const environment = this.node.tryGetContext("environment")
    const params = this.node.tryGetContext(environment)

    const swagger: any = yaml.load(fs.readFileSync("../api/swagger.yaml", 'utf8'))
    const api = new apigwv2.HttpApi(this, "Api")

    for (const path in swagger.paths) {
      const pathDef = swagger.paths[path]
      for (const method in pathDef) {
        const funcDef = pathDef[method]

        const tag = funcDef.tags[0] || 'unclassified'
        const operationId = funcDef.operationId

        const funcNameCamel = _.camelCase(operationId)
        const funcNameSnake = _.snakeCase(operationId)

        const func = new lambda.Function(
          this, `${funcNameCamel}Function`,
          {
            code: lambda.Code.fromAssetImage("../api/src", {
              cmd: [`${tag}.${funcNameSnake}`],
            }),
            runtime: lambda.Runtime.FROM_IMAGE,
            handler: lambda.Handler.FROM_IMAGE,
            timeout: cdk.Duration.seconds(10),
            description: funcDef.description,
          }
        )
        api.addRoutes({
          path: path,
          methods: [toHttpMethod(method)],
          integration: new HttpLambdaIntegration(`${funcNameCamel}Integration`, func)
        })
      }
    }

    // Output value: API URL.
    new cdk.CfnOutput(
      this, "OutputApiGatewayUrl",
      {
        value: api.url!,
      }
    )
  }
}

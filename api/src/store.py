import json


def get_inventory(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "getInventory"})}


def place_order(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "placeOrder"})}


def get_order_by_id(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "getOrderById"})}


def delete_order(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "deleteOrder"})}

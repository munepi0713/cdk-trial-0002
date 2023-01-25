import json


def create_user(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "createUser"})}


def create_users_with_list_input(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "createUsersWithListInput"})}


def login_user(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "loginUser"})}


def logout_user(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "logoutUser"})}


def get_user_by_name(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "getUserByName"})}


def update_user(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "updateUser"})}


def delete_user(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "deleteUser"})}

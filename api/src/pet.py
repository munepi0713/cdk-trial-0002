import json

def update_pet(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "updatePet"})}


def add_pet(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "addPet"})}


def find_pets_by_status(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "findPetsByStatus"})}


def find_pets_by_tags(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "findPetsByTags"})}


def get_pet_by_id(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "getPetById"})}


def update_pet_with_form(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "updatePetWithForm"})}


def delete_pet(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "deletePet"})}


def upload_file(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "uploadFile"})}

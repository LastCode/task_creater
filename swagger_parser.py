import json
import openapi_spec_parser

def parser():

    # Load the Swagger JSON file
    with open("swagger.json", "r") as file:
        swagger_json = json.load(file)

    # Parse the Swagger JSON file
    spec = openapi_spec_parser.load_spec_from_dict(swagger_json)

    # Extract the request payload for a specific endpoint
    endpoint = "/example/{id}"
    method = "post"
    operation = spec.get_path(endpoint).operations[method]
    payload = operation.request_body.to_dict()

    # Print the extracted payload
    print(payload)



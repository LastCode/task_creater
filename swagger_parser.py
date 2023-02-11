import json


def get_payload_parameters(file_path=None):
    payload_parameters={}
    with open(file_path) as f:
        swagger_data = json.load(f)
    
    # Get the payload parameters information from the Swagger data
    parameters = swagger_data["paths"]["/example"]["post"]["parameters"]
    
    # Iterate over the parameters and print each one
    for parameter in parameters:
        print("Name:", parameter["name"])
        print("In:", parameter["in"])
        print("Required:", parameter.get("required", False))
        print("Type:", parameter["schema"]["type"])
        print("\n")
        
if __name__ == '__main__':
    get_payload_parameters('')


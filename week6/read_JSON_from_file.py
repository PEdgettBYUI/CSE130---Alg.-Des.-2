import json

def read_data_from_json(filename):
    with open(filename, "rt") as filehandle:
        file_data = filehandle.read()
        json_data = json.loads(file_data)
        return json_data
    
# NOTE: Print the Rows then columns after decompressing the data to print in the correct viewing angle.
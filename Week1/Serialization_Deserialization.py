"""

Serialization: Converting state of object into byte stream, this byte stream can be further stored in any file-like object such as disk file or memory stream
Deserialization: Reconstructing the objects from the byte stream
Marshal Module,
Pickle Module,
JSON module
"""

import json

data = {
    "id": "877",
    "name": "Mayuri",
    "department": "Comp"
}

print(type(data))
# Serializing json
json_object = json.dumps(data)
print(json_object)
print(type(json_object))
print('Serialization Completed.!! Converted the JSON file to String')

# convert string to Python dict
student_dict = json.loads(json_object)
print(student_dict)

print(student_dict['name'])
print('Deserialization Completed!! Converted back to JSON file from the String')
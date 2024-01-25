import json
from json import JSONDecodeError, JSONEncoder

jsonString = '{"a": "apple", "b": "banana", "s": "strawberry"}'

try:
    json.loads(jsonString)
except JSONDecodeError:
    print('Could not parse JSON') 

pythonDict = {"a": "apple", "b": "banana", "s": "strawberry",}
print(json.dumps(pythonDict))

# Simple class example
class Animal:
    def __init__(self, name):
        self.name = name

# Overwrite the default encoder for the above class so we can serialize it later
class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        return super().default(o)

# JSONdumps an object with classes that would have otherwise failed without the above encoder
pythonDict = {'a': Animal('Aardvark'), 'b': Animal('Bear'), 'c': Animal('Cat'),}
print(json.dumps(pythonDict, cls=AnimalEncoder))

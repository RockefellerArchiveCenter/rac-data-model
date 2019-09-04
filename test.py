import json
import jsonschema


with open('schema.json', 'r') as sf:
    schema = json.load(sf)
    cls = jsonschema.validators.validator_for(schema)
    cls.check_schema(schema)

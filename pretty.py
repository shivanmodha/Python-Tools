''' Module to prettify text '''
import sys
import json

for line in sys.stdin:
    print(json.dumps(json.loads(line), sort_keys=False, indent=4))

import os

import json
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "/data/config.json"), "r") as f:
    settings = json.load(f)['options']

# import yaml
# with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.yaml"), "r") as f:
#     settings = yaml.safe_load(f)
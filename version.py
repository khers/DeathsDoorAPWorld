import json
import pkgutil

# archipelago.json is the single source of truth; pkgutil works inside the zipped apworld.
deathsdoor_version: str = json.loads(pkgutil.get_data(__package__, "archipelago.json"))["world_version"]

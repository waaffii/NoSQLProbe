import itertools

OPERATORS = ["$ne", "$gt", "$lt", "$gte", "$lte", "$regex"]

def generate_probes(target_field: str) -> list:
    probes = []
    for op in OPERATORS:
        probes.append({
            "payload": {target_field: {op: ""}},
            "description": f"Empty string with {op}"
        })
        probes.append({
            "payload": {target_field: {op: "a"}},
            "description": f"'a' with {op}"
        })
    return probes
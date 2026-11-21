ERROR_MARKERS = ["mongo", "bson", "casterror", "unknown operator", "$where", "syntaxerror"]

def compare_responses(baseline: dict, probe: dict) -> dict:
    if probe.get("error"):
        return {"verdict": "error", "reasons": [probe["error"]]}
    
    reasons = []
    status_changed = probe["status"] != baseline["status"]
    length_changed = probe["length"] != baseline["length"]
    
    if status_changed:
        reasons.append(f"Status changed: {baseline['status']} -> {probe['status']}")
    if length_changed:
        reasons.append(f"Length changed: {baseline['length']} -> {probe['length']}")
        
    lowered = probe["body"].lower()
    found_errors = [m for m in ERROR_MARKERS if m in lowered and m not in baseline["body"].lower()]
    if found_errors:
        reasons.append(f"Error markers found: {', '.join(found_errors)}")
        
    if not reasons:
        verdict = "clean"
    elif found_errors or (status_changed and probe["status"] in (200, 201)):
        verdict = "vulnerable"
    else:
        verdict = "possibly_vulnerable"
        
    return {"verdict": verdict, "reasons": reasons}
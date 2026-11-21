import requests
from probes import generate_probes
from comparator import compare_responses

TARGET_URL = "http://127.0.0.1:5050/vuln-login"
BASELINE = {"status": 401, "length": 55, "body": '{"authenticated":false,"message":"Invalid credentials"}'}

def run_scan():
    probes = generate_probes("password")
    for p in probes:
        try:
            resp = requests.post(TARGET_URL, json={"username": "alice", **p["payload"]}, timeout=10)
            probe_data = {"status": resp.status_code, "length": len(resp.text), "body": resp.text}
        except Exception as e:
            probe_data = {"error": str(e)}
        
        result = compare_responses(BASELINE, probe_data)
        print(f"[{p['description']}] Verdict: {result['verdict']} | Reasons: {result['reasons']}")

if __name__ == "__main__":
    run_scan()
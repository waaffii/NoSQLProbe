from comparator import compare_responses

base = {"status": 401, "length": 55, "body": '{"authenticated":false,"message":"Invalid credentials"}'}
changed = {"status": 200, "length": 49, "body": '{"authenticated":true,"role":"user","user":"alice"}'}

print("Test Result:", compare_responses(base, changed))
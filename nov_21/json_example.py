import json

with open("./example.json", "r") as f:
    json_str = f.read()
    py_obj = json.loads(json_str)
    print(f"Python Dictionary: {py_obj}")

    py_obj["object"]["key3"] = "value3"

with open("./example.json", "w") as f:
    json_str = json.dumps(py_obj, sort_keys=True, indent=4)
    f.write(json_str)

import csv
from os.path import exists

def log_call(call_id, convo):
    file = "call_logs.csv"
    headers = ["call_id", "content"]
    with open(file, "a", newline='') as f:
        writer = csv.writer(f)
        if not exists(file):
            writer.writerow(headers)
        content = "\n".join([f"{a}: {b}" for a, b in convo])
        writer.writerow([call_id, content])

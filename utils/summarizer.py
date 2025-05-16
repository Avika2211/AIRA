import subprocess

def summarize(convo):
    summary_prompt = "Summarize this conversation briefly:\n"
    summary_prompt += "\n".join([f"{a}: {b}" for a, b in convo])
    result = subprocess.run(["ollama", "run", "mistral", summary_prompt], capture_output=True, text=True)
    return result.stdout.strip()

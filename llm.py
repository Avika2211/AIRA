import subprocess

with open("prompts/context.txt") as f:
    CONTEXT = f.read()

def get_response(text, history):
    prompt = CONTEXT + "\n"
    for speaker, line in history[-5:]:
        prompt += f"{speaker}: {line}\n"
    prompt += f"User: {text}\nAIRA:"
    result = subprocess.run(["ollama", "run", "mistral", prompt], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

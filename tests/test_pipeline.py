from stt import transcribe
from llm import get_response
from tts import speak

def test_chain():
    text = transcribe("sample.wav")
    print("User:", text)
    reply = get_response(text, [("User", text)])
    print("AIRA:", reply)
    out = speak(reply)
    print("Spoken output saved to", out)

#!/usr/bin/env python3
import agi, stt, llm, tts, emailer, os, time, uuid
from utils.logger import log_call
from utils.summarizer import summarize

agi = agi.AGI()

CALL_ID = time.strftime("%Y%m%d_%H%M%S") + "_" + str(uuid.uuid4())[:6]
AUDIO_PATH = f"recordings/call_{CALL_ID}.wav"
TRANSCRIPT_PATH = f"transcripts/call_{CALL_ID}.txt"
SUMMARY_PATH = f"transcripts/call_{CALL_ID}_summary.txt"

conversation = []

agi.verbose("Starting AIRA session", 1)
agi.stream_file("beep")
agi.say_text("Hi! I am AIRA from Agritroniix India, how may I help you today?")

while True:
    agi.record_file(AUDIO_PATH, 'wav', '#', 8000, 5000)
    user_input = stt.transcribe(AUDIO_PATH)
    if not user_input.strip():
        agi.say_text("I'm sorry, I couldn't hear you. Could you repeat that?")
        continue
    conversation.append(("User", user_input))
    ai_response = llm.get_response(user_input, conversation)
    conversation.append(("AIRA", ai_response))
    reply_path = tts.speak(ai_response)
    agi.stream_file(reply_path.replace(".wav", ""))
    if "thank you" in user_input.lower() or "bye" in user_input.lower():
        break

with open(TRANSCRIPT_PATH, "w") as f:
    for speaker, line in conversation:
        f.write(f"{speaker}: {line}\n")

summary = summarize(conversation)
with open(SUMMARY_PATH, "w") as f:
    f.write(summary)

emailer.send_email(TRANSCRIPT_PATH, SUMMARY_PATH)
log_call(CALL_ID, conversation)

from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ek1/tacotron2", progress_bar=False)

def speak(text, out_path="reply.wav"):
    tts.tts_to_file(text=text, file_path=out_path)
    return out_path

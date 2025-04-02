from transformers import pipeline
import scipy
import time

start_time = time.time()
print("Loading model...")
synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")
print("Model loaded in %s seconds" % (time.time() - start_time))
music = synthesiser("", forward_params={"do_sample": True})
print("Generating audio...")
scipy.io.wavfile.write("musicgen_out.wav", rate=music["sampling_rate"], data=music["audio"])
print("Audio generated in %s seconds" % (time.time() - start_time))
print("Done!")

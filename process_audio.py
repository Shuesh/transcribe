"""
Processes the audio and outputs as a spectrogram
"""

import time
import pyaudio # type: ignore

# Create a PyAudio object
pa = pyaudio.PyAudio()
# Initialize the variable we'll use to find the input device
chosen_device_index = -1
# Loop over all devices and get info about each of them. Then, choose the one that matches the PROAR microphone
for x in range(0,pa.get_device_count()):
    info = pa.get_device_info_by_index(x)
    print (pa.get_device_info_by_index(x))
    if info["name"] == "PROAR S-21U Microphone: USB Audio (hw:1,0)":
        chosen_device_index = info["index"]
print ("Chosen index: ", chosen_device_index)

# Make a PyAudio object
p = pyaudio.PyAudio()
# Start a stream using the information gathered from the above loop.
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input_device_index=chosen_device_index, input=True, output=False)
stream.start_stream()

# While the stream is active, keep waiting. Need to figure out how to set the stream to inactive in orer to stop...
while stream.is_active():
    time.sleep(0.1)

# Stop and close the stream
stream.stop_stream()
stream.close()

# Cleanup by terminating the PyAudio object (I think to release control over the input device)
p.terminate()

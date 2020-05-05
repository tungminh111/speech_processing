
import os

import pyaudio
import wave
import pynput
# Set chunk size of 1024 samples per data frame

class AudioPlayer:

    def __init__(self, f1, wordName):
        self.stop = False
        self.frames = []
        self.filename = f1
        self.chunk = 1024
        self.wf = wave.open(self.filename, 'rb')

        self.RATE = self.wf.getframerate()
        self.SAMPLEWIDTH = self.wf.getsampwidth()
        self.NCHANNELS = self.wf.getnchannels()
        self.holding = False
        self.output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output_data', wordName)
        self.result = True

    def count_file(self):
        return sum(1 for i in os.listdir(self.output_path))

    def on_press(self, key):
        if key == pynput.keyboard.Key.shift:
            if not self.holding:
                print("Start Recording")
            self.holding = True

    def on_release(self, key):
        if key == pynput.keyboard.Key.shift:
            print("Stop recording")
            self.writeFile(str(self.count_file()) + '.wav')
            self.holding = False
        if key == pynput.keyboard.Key.esc:
            # Stop listener
            self.stop = True
            self.result = False
            return False
        if key == pynput.keyboard.Key.right:
            # Stop listener
            self.stop = True
            self.result = True
            return False


    def record(self):
        # Open the soundm file
        # Create an interface to PortAudio

        p = pyaudio.PyAudio()
        # Open a .Stream object to write the WAV file to
        # 'output = True' indicates that the sound will be played rather than recorded
        instream = p.open(format = p.get_format_from_width(self.SAMPLEWIDTH),
                        channels = self.NCHANNELS,
                        rate = int(self.RATE * 0.7),
                        output = True)

        # Read data in chunks
        listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        data = self.wf.readframes(self.chunk)
        self.stop = False
        # Play the sound by writing the audio data to the stream
        while not self.stop:
            instream.write(data)
            if self.holding:
                self.frames.append(data)
            data = self.wf.readframes(self.chunk)

        listener.join()

        # Close and terminate the stream
        instream.close()
        p.terminate()
        self.wf.close()

    def writeFile(self, outpath):
        of = wave.open(os.path.join(self.output_path, outpath), 'wb')
        of.setnchannels(self.wf.getnchannels())
        of.setsampwidth(self.SAMPLEWIDTH)
        of.setframerate(self.RATE)
        of.writeframes(b''.join(self.frames))
        of.close()

    def process(self):
        self.record()
        return self.result

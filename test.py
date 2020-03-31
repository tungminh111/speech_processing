import tkinter as tk
import threading
import pyaudio
import wave
import re
import os
import pywt


class App():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    currentSen = 0
    article = ""
    frames = []
    sentences = []

    def __init__(self, master):
        self.isrecording = False
        tk.Label(master,
                 text="Article").grid(row=0)

        self.articleEntry = tk.Entry(master)

        self.articleEntry.grid(row=0, column=1, columnspan=2)

        tk.Button(master,
                  text='Load',
                  command=self.initArticle).grid(row=3,
                                                           column=0,
                                                           sticky=tk.W,
                                                           pady=4)
        tk.Button(master,
                  text='Record', command=self.startrecording).grid(row=3,
                                                                   column=1,
                                                                   sticky=tk.W,
                                                                   pady=4)
        tk.Button(master,
                  text='Stop', command=self.stoprecording).grid(row=3,
                                                                column=2,
                                                                sticky=tk.W,
                                                                pady=4)

        self.sentenceLabel = tk.Message(master, text="Label", width=100)
        self.sentenceLabel.grid(row=4,columnspan=3)

    def split(self, texts):

        pattern1 = re.compile(r"[.]\n+|\n")
        pattern2 = re.compile(r"[.]+\s|\n")

        # Tach thanh tung doan nho
        blocks = re.split(pattern1, texts)

        # Tach cac cau trong doan nho
        result = []
        for block in blocks:
            result += re.split(pattern2, block)
        result = [res for res in result if res != '']
        self.sentences = result

    def initArticle(self):
        self.article = None
        article = self.articleEntry.get()

        path = os.path.dirname(__file__)
        filename = path + "/data/" + str(article) + "/" + str(article) + ".txt"
        with open(filename, "r", encoding='utf-8') as f:
            texts = f.read()
            self.article = article
        self.split(texts)

        self.currentSen = 0
        if len(self.sentences) > 0:
            self.sentenceLabel.config(text = self.sentences[self.currentSen])


    def startrecording(self):
        if self.article == "" or self.currentSen == len(self.sentences):
            return

        if self.isrecording:
            self.isrecording = False
            self.t.join()
            self.frames.clear()

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.sample_format, channels=self.channels, rate=self.fs,
                                  frames_per_buffer=self.chunk, input=True)
        self.isrecording = True

        print('Recording')
        self.t = threading.Thread(target=self.record)
        self.t.start()

    def stoprecording(self):
        if not self.isrecording:
            return
        self.isrecording = False
        print('recording complete')

        path = os.path.dirname(__file__)
        filename = path + "/data/" + str(self.article) + "/" + str(self.article) + "_" + str(self.currentSen) + ".wav"
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        filename = str(self.article) + "_" + str(self.currentSen) + ".wav"
        textpath = path + "/data/" + str(self.article) + "/" + str(self.article) + "_result.txt"
        print(textpath)
        f = open(textpath, 'a', encoding='utf-8')
        f.write(filename + '\n' + self.sentences[self.currentSen] + '\n')
        f.close()

        self.frames.clear()
        self.currentSen += 1
        if self.currentSen >= len(self.sentences):
            self.sentenceLabel['text'] = "Da ghi am xong"
        else:
            self.sentenceLabel['text'] = self.sentences[self.currentSen]


    def record(self):
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

if __name__ == "__main__":
    # Get list of topics
    main = tk.Tk()
    main.title('recorder')
    main.geometry('500x500')
    app = App(main)
    main.mainloop()

import csv
import os
import re
from AudioPlayer import AudioPlayer

class CSVReader:
    def __init__(self, listID):
        self.reader = None
        self.mssv = listID
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def recordWord(self, s):
        with open('text-data.csv', mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['Mã SV'] not in self.mssv:
                    continue
                for key, value in row.items():
                    if key != 'STT' and key != 'Mã SV' and key != 'Họ và tên':
                        lineList = value.split('\n')

                        dirname = os.path.join(self.dir_path, 'assignment1')
                        for subdirname in os.listdir(dirname):
                            if not os.path.isdir(os.path.join(dirname, subdirname)):
                                continue
                            if subdirname[:8] == row['Mã SV']:
                                dirname = os.path.join(dirname, subdirname)
                                break

                        for id in range((len(lineList) - 1) // 2):

                            filename = lineList[1 + id * 2]
                            sentence = lineList[2 + id * 2]
                            sentence = str(sentence).lower()

                            wordList = re.split('\.|,| * ',sentence)
                            if s in wordList:
                                filename = self.findFile(dirname, filename)
                                print("Current sentence: " + sentence)
                                con = False
                                while not con:
                                    ap = AudioPlayer(filename, s)
                                    con = ap.process()


    def findFile(self, dirpath, filename):
        for subdir, dirs, files in os.walk(dirpath):
            for file in files:
                if file == filename:
                    return os.path.join(subdir, filename)

reader = CSVReader(['17020709'])
reader.recordWord('chiếc')

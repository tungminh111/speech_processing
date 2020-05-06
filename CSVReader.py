import csv
import os
import re

class CSVReader:
    def __init__(self):
        self.reader = None
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.mssv = []
        dirname = os.path.join(self.dir_path, 'assignment1')
        for subdirname in os.listdir(dirname):
            if subdirname[:8] not in self.mssv:
                self.mssv.append(subdirname[:8])

        self.ouput_path = os.path.join(self.dir_path, "output_data")


    def recordWord(self, s):
        output_path = os.path.join(self.ouput_path, s)
        output_path = os.path.join(output_path, s + ".txt")
        wf = open(output_path, 'w', encoding='utf-8')
        orgS = s
        s = s.lower()
        s = re.split('  *', s)
        c = 0
        with open('text-data.csv', mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['Mã SV'] not in self.mssv:
                    continue

                dirname = os.path.join(self.dir_path, 'assignment1')
                for subdirname in os.listdir(dirname):
                    if not os.path.isdir(os.path.join(dirname, subdirname)):
                        continue
                    if subdirname[:8] == row['Mã SV']:
                        dirname = os.path.join(dirname, subdirname)
                        break
                for key, value in row.items():
                    if key != 'STT' and key != 'Mã SV' and key != 'Họ và tên':
                        lineList = value.split('\n')

                        for id in range((len(lineList) - 1) // 2):

                            filename = lineList[1 + id * 2]
                            sentence = lineList[2 + id * 2]
                            sentence = str(sentence).lower()

                            wordList = re.split('\.|,| * ',sentence)
                            if self.match(s, wordList):
                                filename = self.findFile(dirname, key, filename)
                                if filename == 'not found':
                                    continue
                                c += 1
                                self.writeFile(wf, filename)
        wf.close()
        print(c)

    def match(self, s, t):
        for i in range(len(t) - len(s) + 1):
            cur = True
            for j in range(len(s)):
                if s[j] != t[i + j]:
                    cur = False
                    break
            if cur:
                return True
        return False

    def writeFile(self, wf, filename):
        wf.write(os.fsdecode(filename) + "\n")

    def no_accent_vietnamese(self, s):
        s = re.sub(u'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
        s = re.sub(u'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
        s = re.sub(u'èéẹẻẽêềếệểễ', 'e', s)
        s = re.sub(u'ÈÉẸẺẼÊỀẾỆỂỄ', 'E', s)
        s = re.sub(u'òóọỏõôồốộổỗơờớợởỡ', 'o', s)
        s = re.sub(u'ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ', 'O', s)
        s = re.sub(u'ìíịỉĩ', 'i', s)
        s = re.sub(u'ÌÍỊỈĨ', 'I', s)
        s = re.sub(u'ùúụủũưừứựửữ', 'u', s)
        s = re.sub(u'ƯỪỨỰỬỮÙÚỤỦŨ', 'U', s)
        s = re.sub(u'ỳýỵỷỹ', 'y', s)
        s = re.sub(u'ỲÝỴỶỸ', 'Y', s)
        s = re.sub(u'Đ', 'D', s)
        s = re.sub(u'đ', 'd', s)
        return s.encode('utf-8')

    def findFile(self, dirpath, dirname, filename):
        dirname = re.split('-|  *|_', dirname)
        for i in range(len(dirname)):
            dirname[i] = dirname[i].lower()
            dirname[i] = self.no_accent_vietnamese(dirname[i])

        for subdir, dirs, files in os.walk(dirpath):
            basename = os.path.basename(subdir)
            basename = re.split('-|  *|_', basename)
            same = True
            for i in range(len(basename)):
                basename[i] = basename[i].lower()
                basename[i] = self.no_accent_vietnamese(basename[i])
            if len(basename) != len(dirname):
                same = False
            else:
                for i in range(len(basename)):
                    if basename[i] != dirname[i]:
                        same = False
            if not same:
                continue
            for file in files:
                if file == filename:
                    return os.path.join(subdir, filename)
        return 'not found'

if __name__ == '__main__':
    reader = CSVReader()
    reader.recordWord('')

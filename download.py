import sys
from PyQt5.QtWidgets import *
from pytube import YouTube
import os

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Download Music")
        self.setGeometry(30, 30, 800, 500)
        self.arayuz()

    def arayuz(self):
        self.buton1 = QPushButton("Click to Download", self)
        self.buton1.move(200, 180)
        self.buton1.clicked.connect(self.mainFunction)

        self.yazi = QLabel("Enter the URL", self)
        self.yazi.move(200, 130)

        self.yazi3 = QLabel(" ", self)
        self.yazi3.move(200, 250)

        self.urlKutusu = QLineEdit(self)
        self.urlKutusu.resize(400, 25)
        self.urlKutusu.move(200, 150)

        self.show()

    def mainFunction(self):
        link = self.urlKutusu.text()
        directory = "Musics"

        try:
            yt = YouTube(link)
            mp3 = yt.streams.filter(only_audio = True).first()
            output = mp3.download(directory)
            base, ext = os.path.splitext(p = output)
            to_mp3 = base + ".mp3"
            self.yazi3.setText("Such a song already exists")
            self.yazi3.resize(400, 25)
            os.rename(output, to_mp3)
            self.yazi3.resize(600, 25)
            self.yazi3.setText(f"{os.path.split(to_mp3)[1]} has been downloaded")

        except:
            self.yazi3.setText("There is no such url.")
            self.yazi3.resize(400, 25)
        


uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())

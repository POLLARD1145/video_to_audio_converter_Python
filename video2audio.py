##########################################################################
# Developer: Pollard Samba
# Email: pollardsamba1@gmail.com
# Gitub: POLLARD1145
#
#
# Description: 
#       Convert MP4 files to MP3 files using python moviepy library
#       and PyQt library for user interface 
#
#
#############################################################################

import os, re
from PyQt6 import QtCore, QtGui, QtWidgets

from moviepy.editor import VideoFileClip



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 15, 471, 61))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(345, 111, 251, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.notice = QtWidgets.QLabel(self.centralwidget)
        self.notice.setGeometry(QtCore.QRect(70, 360, 541, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notice.setFont(font)
        self.notice.setText("click on 'Choose Video' button to open/select the folder containing the video you want to convert")
        self.notice.setWordWrap(True)
        self.notice.setObjectName("notice")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 90, 180, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(60, 110, 256, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setAcceptDrops(True)
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.itemDoubleClicked.connect(self.convertVideo)
        self.listWidget_2.itemClicked.connect(self.clickedonce)
        self.filedial =QtWidgets.QFileDialog(self.centralwidget)
        self.popup =QtWidgets.QMessageBox(self.centralwidget)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(340, 310, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.convertButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("arrow")
        self.convertButton.setIcon(icon)
        self.convertButton.setObjectName("pushButton")
        self.convertButton.clicked.connect(self.convertVideo1)
        self.selectVideo = QtWidgets.QPushButton(self.centralwidget)
        self.selectVideo.setGeometry(QtCore.QRect(60, 310, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectVideo.setFont(font)
        self.selectVideo.setAcceptDrops(True)
        self.selectVideo.setObjectName("selectVideo")
        self.selectVideo.clicked.connect(self.openVideo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video to Audio Converter - Pollard Samba"))
        self.label.setText(_translate("MainWindow", "Video to Audio converter"))
        self.label_3.setText(_translate("MainWindow", "Videos"))
        self.label_4.setText(_translate("MainWindow", "Converted Audios"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.selectVideo.setText(_translate("MainWindow", "Choose Video Folder"))
    
    def clickedonce(self,item):
        self.path2 = self.path1
        self.song = item.text()
        pass

    def openVideo(self):
        
        self.path1 = self.filedial.getExistingDirectory(None,"Choose folder containing video")

        import os
        folder = os.listdir(self.path1)
        mp4 = re.compile(".*.mp4"); mp4s = list(filter(mp4.match,folder))
        vob = re.compile(".*.VOB"); vobs = list(filter(vob.match,folder))
        videos = mp4s + vobs
        
        for i in videos:
            self.listWidget_2.addItem(i)
        self.notice.setText("Choose folder to save in by double clicking on the video you want to convert or click it once and click on convert button")
        pass
        

    def convertVideo(self,item):
        #
    
        os.chdir(self.path1) #set the path to that of the current folder where you want to get videos from
        video = VideoFileClip(item.text()) #this is the video selected by user
        self.notice.setText("Converting video please wait ....")
        #extract audio from the video file
        audioextract = video.audio
        #add mp3 extension to your new audio to save it as an mp3 file
        songname = str(item.text()).removesuffix(".mp4") + ".mp3"
        #get new path where user wants to save audio
        pathsave = self.filedial.getExistingDirectory(None,"Choose folder to save in")
        #change to the new folder selected by user 
        os.chdir(pathsave)
        #convert now by writing the audio 
        audioextract.write_audiofile(songname)        
        #make a string for the info to guide user where to find their converted audio
        lasttxt = "Video converted successfully and saved as " + songname + " in " + str(pathsave)
        #display the converted audio to the other list
        self.listWidget.addItem(songname)
        #show user the location of their new audio
        self.notice.setText(lasttxt)
        pass
    
    def convertVideo1(self):
        self.notice.setText("Choose folder to save in")
        os.chdir(self.path2) #set the path to that of the current folder where you want to get videos from
        video = VideoFileClip(self.song) #this is the video selected by user
        self.notice.setText("Converting video please wait ....")
        #extract audio from the video file
        audioextract = video.audio
        #add mp3 extension to your new audio to save it as an mp3 file
        songname = str(self.song).removesuffix(".mp4") + ".mp3"
        #get new path where user wants to save audio
        pathsave = self.filedial.getExistingDirectory(None,"Choose folder to save in")
        #change to the new folder selected by user 
        os.chdir(pathsave)
        #convert now by writing the audio 
        a = 1
        audioextract.write_audiofile(songname,verbose=False)
        
        #make a string for the info to guide user where to find their converted audio
        lasttxt = "Video converted successfully and saved as " + songname + " in " + str(pathsave)
        #display the converted audio to the other list
        self.listWidget.addItem(songname)
        #show user the location of their new audio
        self.notice.setText(lasttxt)
        pass   
        
#END OF THE PROGRAM, ALLOW SYSTEM TO DISPLAY YOUR PROGRAM
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

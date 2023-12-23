import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from yt_dlp import YoutubeDL
from webbrowser import open

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.QualityCombo = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.QualityCombo.setFont(font)
        self.QualityCombo.setMouseTracking(False)
        self.QualityCombo.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.QualityCombo.setAcceptDrops(False)
        self.QualityCombo.setStyleSheet("background-color: rgb(192, 191, 188);\n"
"color: rgb(192, 97, 203);")
        self.QualityCombo.setObjectName("QualityCombo")
        self.QualityCombo.addItem("")
        self.QualityCombo.addItem("")
        self.QualityCombo.addItem("")
        self.QualityCombo.addItem("")
        self.QualityCombo.addItem("")
        self.gridLayout_3.addWidget(self.QualityCombo, 1, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 4, 0, 1, 4)
        self.BrowseButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.BrowseButton.setFont(font)
        self.BrowseButton.setStyleSheet("background-color: rgb(192, 191, 188);\n"
"color: rgb(61, 56, 70);")
        self.BrowseButton.setObjectName("BrowseButton")
        self.gridLayout_3.addWidget(self.BrowseButton, 2, 3, 1, 1)
        self.BrowseFilelabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.BrowseFilelabel.setFont(font)
        self.BrowseFilelabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.BrowseFilelabel.setObjectName("BrowseFilelabel")
        self.gridLayout_3.addWidget(self.BrowseFilelabel, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 2)
        self.browseaddress = QtWidgets.QLineEdit(self.frame)
        self.browseaddress.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(36, 31, 49);")
        self.browseaddress.setText("")
        self.browseaddress.setClearButtonEnabled(False)
        self.browseaddress.setObjectName("browseaddress")
        self.gridLayout_3.addWidget(self.browseaddress, 2, 1, 1, 2)
        self.Youtubelabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Youtubelabel.setFont(font)
        self.Youtubelabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.Youtubelabel.setObjectName("Youtubelabel")
        self.gridLayout_3.addWidget(self.Youtubelabel, 0, 0, 1, 2)
        self.startbutton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.startbutton.setFont(font)
        self.startbutton.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color:white\n"
"")
        self.startbutton.setObjectName("startbutton")
        self.gridLayout_3.addWidget(self.startbutton, 3, 3, 1, 1)
        self.Youtubelink = QtWidgets.QLineEdit(self.frame)
        self.Youtubelink.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(36, 31, 49);")
        self.Youtubelink.setText("")
        self.Youtubelink.setClearButtonEnabled(False)
        self.Youtubelink.setObjectName("Youtubelink")
        self.gridLayout_3.addWidget(self.Youtubelink, 0, 2, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 22))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDeveloper = QtWidgets.QAction(MainWindow)
        self.actionDeveloper.setObjectName("actionDeveloper")
        self.actionrequest_new_app = QtWidgets.QAction(MainWindow)
        self.actionrequest_new_app.setObjectName("actionrequest_new_app")
        self.menuOption.addAction(self.actionDeveloper)
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QualityCombo.setItemText(0, _translate("MainWindow", "Highest quality"))
        self.QualityCombo.setItemText(1, _translate("MainWindow", "720p"))
        self.QualityCombo.setItemText(2, _translate("MainWindow", "480p"))
        self.QualityCombo.setItemText(3, _translate("MainWindow", "360p"))
        self.QualityCombo.setItemText(4, _translate("MainWindow", "Lowest quality"))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.BrowseFilelabel.setText(_translate("MainWindow", "Output :"))
        self.browseaddress.setPlaceholderText(_translate("MainWindow", "paste your link here"))
        self.Youtubelabel.setText(_translate("MainWindow", "Youtube link:"))
        self.startbutton.setText(_translate("MainWindow", "Start "))
        self.Youtubelink.setPlaceholderText(_translate("MainWindow", "paste your link here"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionDeveloper.setText(_translate("MainWindow", "Developer"))
        self.actionrequest_new_app.setText(_translate("MainWindow", "request new app"))

class YouTubeDownloader(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.BrowseButton.clicked.connect(self.browse_output_path)
        self.ui.startbutton.clicked.connect(self.start_download)
        self.ui.actionDeveloper.triggered.connect(self.dev)

    def browse_output_path(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if download_path:
            self.ui.browseaddress.setText(download_path)

    def update_progress_bar(self, data):
        if data['status'] == 'downloading':
            percent = round((data['downloaded_bytes'] / data['total_bytes']) * 100)
            self.ui.progressBar.setValue(percent)

    def dev(self):
        open("https://www.linkedin.com/in/aadarsh-chandra-70a06429b/")
    def start_download(self):
        video_url = self.ui.Youtubelink.text()
        quality_preference = self.ui.QualityCombo.currentText().lower()
        download_path = self.ui.browseaddress.text()

        if not video_url or not download_path:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please provide a valid YouTube link and output path.")
            return

        try:
            options = {
                'outtmpl': download_path + '/%(title)s.%(ext)s',
                'progress_hooks': [self.update_progress_bar]
            }

            with YoutubeDL(options) as ydl:
                info_dict = ydl.extract_info(video_url, download=False)
                formats = info_dict.get('formats', [])
                
                if not formats:
                    QtWidgets.QMessageBox.warning(self, "Warning", "No available formats found for this video.")
                    return

                available_formats = [format_item.get('format_note', 'Unknown') for format_item in formats]

                if quality_preference == "highest quality":
                    selected_format = available_formats[0]
                elif quality_preference == "lowest quality":
                    selected_format = available_formats[-1]
                else:
                    # Let the user choose from available formats
                    selected_format, ok = QtWidgets.QInputDialog.getItem(self, "Select Quality", "Available Formats:", available_formats, 0, False)
                    if not ok:
                        return

                format_index = available_formats.index(selected_format)
                selected_format_id = formats[format_index]['format_id']

                options['format'] = selected_format_id
                ydl.download([video_url])

            QtWidgets.QMessageBox.information(self, "Success", f"Video downloaded successfully to: {download_path}")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec_())
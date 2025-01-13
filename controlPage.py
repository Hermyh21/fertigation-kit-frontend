from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FertigationControlPanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setStyleSheet("background-color: #f9f9f9;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Header
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 600, 60))
        self.header.setStyleSheet("background-color: #109d4c;")
        self.header.setObjectName("header")

        self.title = QtWidgets.QLabel(self.header)
        self.title.setGeometry(QtCore.QRect(20, 15, 300, 30))
        self.title.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.title.setText("Fertigation Control Panel")

        self.aboutButton = QtWidgets.QPushButton(self.header)
        self.aboutButton.setGeometry(QtCore.QRect(500, 15, 80, 30))
        self.aboutButton.setStyleSheet("background-color: white; color: #109d4c; border-radius: 5px;")
        self.aboutButton.setText("About")

        # AI Recommendation Section
        self.aiSection = QtWidgets.QGroupBox(self.centralwidget)
        self.aiSection.setGeometry(QtCore.QRect(20, 80, 550, 150))
        self.aiSection.setTitle("AI Recommendation")
        self.aiSection.setStyleSheet("font-size: 14px;")

        self.cropLabel = QtWidgets.QLabel(self.aiSection)
        self.cropLabel.setGeometry(QtCore.QRect(20, 30, 100, 20))
        self.cropLabel.setText("Select Crop:")

        self.cropDropdown = QtWidgets.QComboBox(self.aiSection)
        self.cropDropdown.setGeometry(QtCore.QRect(120, 30, 150, 25))
        self.cropDropdown.addItems(["Corn", "Wheat", "Rice", "Tomato", "Potato"])

        self.sensorDataLabel = QtWidgets.QLabel(self.aiSection)
        self.sensorDataLabel.setGeometry(QtCore.QRect(20, 70, 250, 20))
        self.sensorDataLabel.setText("Sensor Data: pH: 7.0 | NPK: 12-6-8 | Weather: Sunny")

        self.recommendedLabel = QtWidgets.QLabel(self.aiSection)
        self.recommendedLabel.setGeometry(QtCore.QRect(20, 100, 300, 20))
        self.recommendedLabel.setText("AI Recommended: NPK: 14-7-10 | Water: 2.5L")

        self.adjustButton = QtWidgets.QPushButton(self.aiSection)
        self.adjustButton.setGeometry(QtCore.QRect(400, 100, 120, 30))
        self.adjustButton.setText("Adjust Values")

        # Fertilizer Controls
        self.fertilizerSection = QtWidgets.QGroupBox(self.centralwidget)
        self.fertilizerSection.setGeometry(QtCore.QRect(20, 250, 550, 100))
        self.fertilizerSection.setTitle("Fertilizer Controls")
        self.fertilizerSection.setStyleSheet("font-size: 14px;")

        self.fertilizerSlider = QtWidgets.QSlider(self.fertilizerSection)
        self.fertilizerSlider.setGeometry(QtCore.QRect(20, 50, 400, 20))
        self.fertilizerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fertilizerSlider.setMinimum(0)
        self.fertilizerSlider.setMaximum(100)

        self.applyFertilizerButton = QtWidgets.QPushButton(self.fertilizerSection)
        self.applyFertilizerButton.setGeometry(QtCore.QRect(430, 45, 100, 30))
        self.applyFertilizerButton.setText("Apply")

        # Mixer Controls
        self.mixerSection = QtWidgets.QGroupBox(self.centralwidget)
        self.mixerSection.setGeometry(QtCore.QRect(20, 370, 260, 100))
        self.mixerSection.setTitle("Mixer Controls")
        self.mixerSection.setStyleSheet("font-size: 14px;")

        self.mixerStatus = QtWidgets.QLabel(self.mixerSection)
        self.mixerStatus.setGeometry(QtCore.QRect(20, 30, 200, 20))
        self.mixerStatus.setText("Status: Idle")

        self.startMixerButton = QtWidgets.QPushButton(self.mixerSection)
        self.startMixerButton.setGeometry(QtCore.QRect(20, 60, 100, 30))
        self.startMixerButton.setText("Start Mixer")

        # Water Controls
        self.waterSection = QtWidgets.QGroupBox(self.centralwidget)
        self.waterSection.setGeometry(QtCore.QRect(310, 370, 260, 100))
        self.waterSection.setTitle("Water Controls")
        self.waterSection.setStyleSheet("font-size: 14px;")

        self.waterSlider = QtWidgets.QSlider(self.waterSection)
        self.waterSlider.setGeometry(QtCore.QRect(20, 50, 200, 20))
        self.waterSlider.setOrientation(QtCore.Qt.Horizontal)
        self.waterSlider.setMinimum(0)
        self.waterSlider.setMaximum(100)

        self.startWateringButton = QtWidgets.QPushButton(self.waterSection)
        self.startWateringButton.setGeometry(QtCore.QRect(20, 75, 100, 30))
        self.startWateringButton.setText("Start Watering")

        # Footer
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(20, 480, 80, 30))
        self.backButton.setStyleSheet("background-color: #109d4c; color: white; border-radius: 5px;")
        self.backButton.setText("Back")

        self.languageDropdown = QtWidgets.QComboBox(self.centralwidget)
        self.languageDropdown.setGeometry(QtCore.QRect(500, 480, 80, 30))
        self.languageDropdown.addItems(["English", "Amharic", "Afan Oromo", "Swahili"])

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "Fertigation Control Panel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FertigationControlPanel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from aiRecommendation import AiRecommendationPage  
from fertilizerPage import FertilizerPage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #f9f9f9;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Vertical Menu Bar
        self.menuBar = QtWidgets.QFrame(self.centralwidget)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 200, 600))
        self.menuBar.setStyleSheet("background-color: #109d4c;")
        self.menuBar.setObjectName("menuBar")

        self.menuLayout = QtWidgets.QVBoxLayout(self.menuBar)
        self.menuLayout.setContentsMargins(0, 0, 0, 0)

        # Menu Buttons
        self.menuButtons = {}
        self.menuOptions = ["AI Recommendation", "Fertilizer", "Mixer", "Water"]
        for option in self.menuOptions:
            button = QtWidgets.QPushButton(option)
            button.setStyleSheet("color: white; font-size: 16px; border: none; padding: 10px; text-align: left;")
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            button.clicked.connect(self.updateContent)
            self.menuButtons[option] = button
            self.menuLayout.addWidget(button)

        # Content Area
        self.contentArea = QtWidgets.QFrame(self.centralwidget)
        self.contentArea.setGeometry(QtCore.QRect(200, 0, 600, 600))
        self.contentArea.setStyleSheet("background-color: white;")
        self.contentArea.setObjectName("contentArea")

        self.contentLayout = QtWidgets.QVBoxLayout(self.contentArea)

        # Initialize with default content
        self.currentPage = None
        self.loadPage("AI Recommendation")

        MainWindow.setCentralWidget(self.centralwidget)

        # Set default selected button
        self.updateMenuStyles("AI Recommendation")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fertigation Control Panel"))

    def updateContent(self):
        # Update the content area based on the selected menu option
        sender = self.sender()
        if sender:
            selectedOption = sender.text()
            self.loadPage(selectedOption)
            self.updateMenuStyles(selectedOption)

    def loadPage(self, pageName):
        # Remove existing content
        if self.currentPage:
            self.contentLayout.removeWidget(self.currentPage)
            self.currentPage.deleteLater()

        # Load the appropriate page
        if pageName == "AI Recommendation":
            self.currentPage = AiRecommendationPage()
        else:
            self.currentPage = QtWidgets.QLabel(pageName)
            self.currentPage.setStyleSheet("font-size: 24px; color: #109d4c;")
            self.currentPage.setAlignment(QtCore.Qt.AlignCenter)

        self.contentLayout.addWidget(self.currentPage)

    def updateMenuStyles(self, selectedOption):
        # Highlight the selected menu button
        for option, button in self.menuButtons.items():
            if option == selectedOption:
                button.setStyleSheet("background-color: white; color: #109d4c; font-size: 16px; border: none; padding: 10px; text-align: left;")
            else:
                button.setStyleSheet("color: white; font-size: 16px; border: none; padding: 10px; text-align: left;")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

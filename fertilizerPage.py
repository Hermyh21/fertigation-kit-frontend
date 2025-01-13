from PyQt5 import QtWidgets

class FertilizerPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(FertilizerPage, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        # Pipe Input Fields
        self.pipeALabel = QtWidgets.QLabel("Pipe A (Nitrogen):")
        self.pipeAInput = QtWidgets.QLineEdit()

        self.pipeBLabel = QtWidgets.QLabel("Pipe B (Phosphorous):")
        self.pipeBInput = QtWidgets.QLineEdit()

        self.pipeCLabel = QtWidgets.QLabel("Pipe C (Potassium):")
        self.pipeCInput = QtWidgets.QLineEdit()

        self.pipeDLabel = QtWidgets.QLabel("Pipe D (Water):")
        self.pipeDInput = QtWidgets.QLineEdit()

        # Buttons
        self.proceedButton = QtWidgets.QPushButton("Proceed to mixing")
        self.proceedButton.setStyleSheet("background-color: #007bff; color: white; font-size: 16px; padding: 10px;")

        self.backButton = QtWidgets.QPushButton("Back")
        self.backButton.setStyleSheet("background-color: #007bff; color: white; font-size: 16px; padding: 10px;")

        # Add Widgets to Layout
        layout.addWidget(self.pipeALabel)
        layout.addWidget(self.pipeAInput)
        layout.addWidget(self.pipeBLabel)
        layout.addWidget(self.pipeBInput)
        layout.addWidget(self.pipeCLabel)
        layout.addWidget(self.pipeCInput)
        layout.addWidget(self.pipeDLabel)
        layout.addWidget(self.pipeDInput)
        layout.addWidget(self.proceedButton)
        layout.addWidget(self.backButton)

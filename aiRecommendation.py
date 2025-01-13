from PyQt5 import QtWidgets

class AiRecommendationPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AiRecommendationPage, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        # Example layout with a dropdown and recommendation details
        self.cropLabel = QtWidgets.QLabel("Select Crop:")
        self.cropDropdown = QtWidgets.QComboBox()
        self.cropDropdown.addItems(["Crop A", "Crop B", "Crop C"])

        self.recommendationLabel = QtWidgets.QLabel("Recommended NPK Ratio:")
        self.recommendationValue = QtWidgets.QLabel("N: 10, P: 20, K: 30")

        self.confirmButton = QtWidgets.QPushButton("Apply Recommendation")

        layout.addWidget(self.cropLabel)
        layout.addWidget(self.cropDropdown)
        layout.addWidget(self.recommendationLabel)
        layout.addWidget(self.recommendationValue)
        layout.addWidget(self.confirmButton)

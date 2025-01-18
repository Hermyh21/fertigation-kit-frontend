import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFormLayout, QComboBox
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt

class AiRecommendationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("AI Crop Recommendation")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setStyleSheet("color: white;")
        title.setAlignment(Qt.AlignCenter)

        # Input form layout
        form_layout = QFormLayout()

        # Input fields
        self.weather_input = QLineEdit()
        self.npk_input = QLineEdit()
        self.ph_input = QLineEdit()
        self.crop_type_input = QComboBox()
        self.crop_type_input.addItems(["Wheat", "Corn", "Rice", "Soybean", "Teff"])  # Example crop types

        # Add fields to the form
        # form_layout.addRow("Weather:", self.weather_input)
        # form_layout.addRow("Soil NPK Levels:", self.npk_input)
        form_layout.addRow("Soil pH Level:", self.ph_input)
        form_layout.addRow("Crop Type:", self.crop_type_input)

        # Recommendation Button
        recommend_button = QPushButton("Show Recommendation")
        recommend_button.setStyleSheet("""
            background-color: #109d4c;
            color: white;
            border-radius: 8px;
            padding: 8px;
        """)
        recommend_button.clicked.connect(self.show_recommendation)

        # Output Area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet("background-color: #f4f4f4; color: black; padding: 10px;")
        self.output_area.setFont(QFont("Arial", 12))

        # Add widgets to the main layout
        layout.addWidget(title)
        layout.addLayout(form_layout)
        layout.addWidget(recommend_button)
        layout.addWidget(QLabel("Recommendation Output:"))
        layout.addWidget(self.output_area)

        # Set layout to the main window
        self.setLayout(layout)
        self.setWindowTitle("AI Crop Recommendation")
        self.setStyleSheet("background-color: #109d4c;")

    def show_recommendation(self):
        # Get input values
        weather = self.weather_input.text()
        npk_levels = self.npk_input.text()
        ph_level = self.ph_input.text()
        crop_type = self.crop_type_input.currentText()

        # Validate inputs
        if not weather or not npk_levels or not ph_level:
            self.output_area.setText("Please fill in all the fields.")
            return

        # Example recommendation logic (simplified)
        try:
            ph_level = float(ph_level)
            npk_ratio = "NPK ratio of 4:3:2" if ph_level < 7 else "NPK ratio of 3:4:3"
            water_requirement = "High" if weather.lower() in ["hot", "dry"] else "Moderate"

            # Display recommendations
            self.output_area.setText(
                f"Crop: {crop_type}\n"
                f"Recommended {npk_ratio}\n"
                f"Water Requirement: {water_requirement}\n"
                f"(Weather: {weather}, pH Level: {ph_level})"
            )
        except ValueError:
            self.output_area.setText("Invalid input. Please ensure pH level is a number.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Set application palette for consistent styling
    palette = QPalette()
    # palette.setColor(QPalette.Window, QColor("#109d4c"))
    palette.setColor(QPalette.WindowText, Qt.white)
    app.setPalette(palette)

    window = AiRecommendationPage()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())

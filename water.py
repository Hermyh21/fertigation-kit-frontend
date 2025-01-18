from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFormLayout, QLineEdit, QHBoxLayout, QStackedWidget
)
from PyQt5.QtCore import Qt

class WaterPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Title
        title = QLabel("Water Management")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #109d4c;")
        self.layout.addWidget(title)

        # Form Layout for Water Input
        form_layout = QFormLayout()

        self.water_input = QLineEdit()
        self.water_input.setPlaceholderText("Enter the amount of water in liters")
        form_layout.addRow("Water (L):", self.water_input)
        self.layout.addLayout(form_layout)

        # Button Layout
        button_layout = QHBoxLayout()

        # Back Button
        back_button = QPushButton("Back")
        back_button.setStyleSheet(
            "padding: 10px; font-size: 14px; background-color: white; color: #109d4c; "
            "border: 2px solid #109d4c; border-radius: 5px;"
        )
        back_button.clicked.connect(self.go_back)
        button_layout.addWidget(back_button)

        # Release to Field Button
        release_button = QPushButton("Release to Field")
        release_button.setStyleSheet(
            "padding: 10px; font-size: 14px; background-color: #109d4c; color: white; border-radius: 5px;"
        )
        release_button.clicked.connect(self.release_to_field)
        button_layout.addWidget(release_button)

        self.layout.addLayout(button_layout)

    def go_back(self):
        # Placeholder for navigation back to the previous page
        print("Back button clicked. Implement navigation to the previous page.")

    def release_to_field(self):
        water_amount = self.water_input.text().strip()

        if not water_amount.isdigit():
            print("Please enter a valid numeric value for water.")
        else:
            print(f"Released {water_amount}L of water to the field!")
            # Placeholder for release logic

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFormLayout, QLineEdit, QHBoxLayout, QSpinBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import QTimer


class MixerPage(QWidget):
    def __init__(self, nitrogen=0, phosphorous=0, potassium=0, water=0):
        super().__init__()
        self.nitrogen = nitrogen
        self.phosphorous = phosphorous
        self.potassium = potassium
        self.water = water
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Title
        title = QLabel("Mixer Page")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #109d4c;")
        self.layout.addWidget(title)

        # Fertilizer amounts
        amounts_label = QLabel(f"""
        Nitrogen: {self.nitrogen}L\n
        Phosphorous: {self.phosphorous}L\n
        Potassium: {self.potassium}L\n
        Water: {self.water}L
        """)
        amounts_label.setAlignment(Qt.AlignCenter)
        amounts_label.setStyleSheet("font-size: 16px; color: black;")
        self.layout.addWidget(amounts_label)

        # Mixing timer input
        form_layout = QFormLayout()
        self.timer_input = QSpinBox()
        self.timer_input.setRange(1, 300)  # Timer range from 1 to 300 seconds
        self.timer_input.setValue(30)  # Default value
        form_layout.addRow("Set Mixing Timer (seconds):", self.timer_input)
        self.layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()

        back_button = QPushButton("Back")
        back_button.setStyleSheet("padding: 10px; font-size: 14px; background-color: white; color: #109d4c; border: 2px solid #109d4c; border-radius: 5px;")
        back_button.clicked.connect(self.go_back)
        button_layout.addWidget(back_button)

        self.confirm_button = QPushButton("Confirm and Mix")
        self.confirm_button.setStyleSheet("padding: 10px; font-size: 14px; background-color: #109d4c; color: white; border-radius: 5px;")
        self.confirm_button.clicked.connect(self.start_mixing)
        button_layout.addWidget(self.confirm_button)

        self.layout.addLayout(button_layout)

        # Mixing status label
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 16px; color: black; margin-top: 20px;")
        self.layout.addWidget(self.status_label)

        # Release to field button (hidden initially)
        self.release_button = QPushButton("Release to Field")
        self.release_button.setStyleSheet("padding: 10px; font-size: 14px; background-color: #109d4c; color: white; border-radius: 5px;")
        self.release_button.clicked.connect(self.release_to_field)
        self.release_button.hide()  # Initially hidden
        self.layout.addWidget(self.release_button)

        # Timer setup
        self.timer = QTimer()
        self.timer.timeout.connect(self.complete_mixing)

    def start_mixing(self):
        mixing_time = self.timer_input.value()
        self.status_label.setText("Mixing... Please wait.")
        self.status_label.setStyleSheet("font-size: 16px; color: orange; margin-top: 20px;")
        self.timer.start(mixing_time * 1000)  # Convert seconds to milliseconds
        self.confirm_button.setEnabled(False)  # Disable confirm button during mixing

    def complete_mixing(self):
        self.timer.stop()
        self.status_label.setText("Mixing successful!")
        self.status_label.setStyleSheet("font-size: 16px; color: green; margin-top: 20px;")
        self.release_button.show()  # Show the release button
        self.confirm_button.setEnabled(True)  # Re-enable confirm button

    def release_to_field(self):
        self.status_label.setText("Released to the field.")
        self.status_label.setStyleSheet("font-size: 16px; color: blue; margin-top: 20px;")
        self.release_button.setEnabled(False)  # Disable release button after use

    def go_back(self):
        from fertilizersPage import FertilizerPage  # Update the import if necessary
        fertilizer_page = FertilizerPage()
        self.window().setCentralWidget(fertilizer_page)

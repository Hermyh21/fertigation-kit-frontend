from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QDialogButtonBox
from PyQt5.QtCore import QTimer, QTime, Qt  
class MixerPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Timer Display
        self.timer_label = QLabel("00:00:00", self)
        self.timer_label.setStyleSheet("font-size: 24px; color: #109d4c;")
        self.timer_label.setAlignment(Qt.AlignCenter)  
        self.layout.addWidget(self.timer_label)

        # Buttons
        self.start_button = QPushButton("Start Mixing", self)
        self.start_button.setStyleSheet("background-color: #109d4c; color: white; font-size: 16px;")
        self.start_button.clicked.connect(self.start_mixing)
        self.layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Mixing", self)
        self.stop_button.setStyleSheet("background-color: #d9534f; color: white; font-size: 16px;")
        self.stop_button.clicked.connect(self.stop_mixing)
        self.layout.addWidget(self.stop_button)

        self.release_button = QPushButton("Release to Field", self)
        self.release_button.setStyleSheet("background-color: #f0ad4e; color: white; font-size: 16px;")
        self.release_button.clicked.connect(self.confirm_release)
        self.layout.addWidget(self.release_button)

        # Timer Setup
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_elapsed = QTime(0, 0, 0)

    def start_mixing(self):
        self.timer.start(1000)  # Timer updates every second

    def stop_mixing(self):
        self.timer.stop()

    def update_timer(self):
        self.time_elapsed = self.time_elapsed.addSecs(1)
        self.timer_label.setText(self.time_elapsed.toString("hh:mm:ss"))

    def confirm_release(self):
        # Dialog for release confirmation
        dialog = QDialog(self)
        dialog.setWindowTitle("Confirm Release")

        layout = QVBoxLayout(dialog)
        message = QLabel("Are you sure you want to release to the field?")
        layout.addWidget(message)

        buttons = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        buttons.accepted.connect(lambda: self.release_action(dialog, True))
        buttons.rejected.connect(lambda: self.release_action(dialog, False))
        layout.addWidget(buttons)

        dialog.exec_()

    def release_action(self, dialog, confirmed):
        if confirmed:
            print("Released to the field!") 
        dialog.close()

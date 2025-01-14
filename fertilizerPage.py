from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFormLayout, QLineEdit, QHBoxLayout, QStackedWidget
)
from PyQt5.QtCore import Qt

class FertilizerPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Stacked Widget for managing views
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Initial View
        self.initial_view = QWidget()
        self.init_initial_view()

        # AI Recommendation View
        self.ai_recommendation_view = QWidget()
        self.init_ai_recommendation_view()

        # User Preferences View
        self.user_preferences_view = QWidget()
        self.init_user_preferences_view()

        # Add views to stacked widget
        self.stacked_widget.addWidget(self.initial_view)
        self.stacked_widget.addWidget(self.ai_recommendation_view)
        self.stacked_widget.addWidget(self.user_preferences_view)

        # Show initial view by default
        self.stacked_widget.setCurrentWidget(self.initial_view)

    def init_initial_view(self):
        layout = QVBoxLayout()
        self.initial_view.setLayout(layout)

        title = QLabel("Fertilizer Options")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #109d4c;")
        layout.addWidget(title)

        accept_ai_button = QPushButton("Accept AI Fertilizer Ratio Recommendation")
        accept_ai_button.setStyleSheet("padding: 10px; font-size: 16px; background-color: #109d4c; color: white; border-radius: 5px;")
        accept_ai_button.clicked.connect(self.show_ai_recommendation_view)
        layout.addWidget(accept_ai_button)

        user_preferences_button = QPushButton("Take User Preferences")
        user_preferences_button.setStyleSheet("padding: 10px; font-size: 16px; background-color: #109d4c; color: white; border-radius: 5px;")
        user_preferences_button.clicked.connect(self.show_user_preferences_view)
        layout.addWidget(user_preferences_button)

    def init_ai_recommendation_view(self):
        layout = QVBoxLayout()
        self.ai_recommendation_view.setLayout(layout)

        title = QLabel("AI Fertilizer Ratio Recommendation")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #109d4c;")
        layout.addWidget(title)

        recommendations = QLabel("Nitrogen: 20L (40%)\nPhosphorous: 15L (30%)\nPotassium: 10L (20%)\nWater: 5L (10%)")
        recommendations.setAlignment(Qt.AlignCenter)
        recommendations.setStyleSheet("font-size: 16px; color: black;")
        layout.addWidget(recommendations)

        button_layout = QHBoxLayout()

        back_button = QPushButton("Back")
        back_button.setStyleSheet("padding: 10px; font-size: 14px; background-color: white; color: #109d4c; border: 2px solid #109d4c; border-radius: 5px;")
        back_button.clicked.connect(self.show_initial_view)
        button_layout.addWidget(back_button)

        proceed_button = QPushButton("Proceed to Mixing")
        proceed_button.setStyleSheet("padding: 10px; font-size: 14px; background-color: #109d4c; color: white; border-radius: 5px;")
        proceed_button.clicked.connect(self.proceed_to_mixing)
        button_layout.addWidget(proceed_button)

        layout.addLayout(button_layout)

    def init_user_preferences_view(self):
        layout = QVBoxLayout()
        self.user_preferences_view.setLayout(layout)

        title = QLabel("Enter Fertilizer Preferences")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #109d4c;")
        layout.addWidget(title)

        form_layout = QFormLayout()

        self.nitrogen_input = QLineEdit()
        form_layout.addRow("Nitrogen (L):", self.nitrogen_input)

        self.phosphorous_input = QLineEdit()
        form_layout.addRow("Phosphorous (L):", self.phosphorous_input)

        self.potassium_input = QLineEdit()
        form_layout.addRow("Potassium (L):", self.potassium_input)

        self.water_input = QLineEdit()
        form_layout.addRow("Water (L):", self.water_input)

        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()

        back_button = QPushButton("Back")
        back_button.setStyleSheet("padding: 10px; font-size: 14px; background-color: white; color: #109d4c; border: 2px solid #109d4c; border-radius: 5px;")
        back_button.clicked.connect(self.show_initial_view)
        button_layout.addWidget(back_button)

        proceed_button = QPushButton("Proceed to Mixing")
        proceed_button.setStyleSheet("padding: 10px; font-size: 14px; background-color: #109d4c; color: white; border-radius: 5px;")
        proceed_button.clicked.connect(self.proceed_to_mixing)
        button_layout.addWidget(proceed_button)

        layout.addLayout(button_layout)

    def show_initial_view(self):
        self.stacked_widget.setCurrentWidget(self.initial_view)

    def show_ai_recommendation_view(self):
        self.stacked_widget.setCurrentWidget(self.ai_recommendation_view)

    def show_user_preferences_view(self):
        self.stacked_widget.setCurrentWidget(self.user_preferences_view)

    def proceed_to_mixing(self):
        print("Proceeding to Mixing...")  # Placeholder for mixing page navigation

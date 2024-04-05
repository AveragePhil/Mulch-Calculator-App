import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mulch Calculator")
        self.setContentsMargins(10,10,10,10)

        layout = QVBoxLayout()
        title_label = QLabel("Mulch Calculator")
        title_label.setFont(QFont("Arial", 14, 500))
        
        area_layout = QHBoxLayout()
        area_label = QLabel("Total area: ")
        area_line = QLineEdit()
        area_units = QLabel("square meters")
        area_layout.addWidget(area_label)
        area_layout.addWidget(area_line)
        area_layout.addWidget(area_units)
        area_layout.setContentsMargins(0,30,0,0)


        depth_layout = QHBoxLayout()
        depth_label = QLabel("Mulch Layer Depth: ")
        depth_line = QLineEdit()
        depth_units = QLabel("centimeters")
        depth_layout.addWidget(depth_label)
        depth_layout.addWidget(depth_line)
        depth_layout.addWidget(depth_units)
        depth_layout.setContentsMargins(0,0,0,25)

        buttons_layout = QHBoxLayout()
        calculate_button = QPushButton("Calculate")
        clear_button = QPushButton("Clear")
        buttons_layout.addWidget(calculate_button)
        buttons_layout.addWidget(clear_button)

        layout.addWidget(title_label)
        layout.addLayout(area_layout)
        layout.addLayout(depth_layout)
        layout.addLayout(buttons_layout)
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
app.setFont(QFont("Arial",9))
window = MainWindow()
window.show()

app.exec()
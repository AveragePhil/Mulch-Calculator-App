import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mulch Calculator")
        self.setContentsMargins(20,30,20,20)

        layout = QVBoxLayout()
        title_label = QLabel("Mulch Calculator")
        title_label.setContentsMargins(130,0,0,30)
        title_label.setFont(QFont("Roboto", 18, 700))

        top_line_label = QLabel("__________________________________________________")
        bottom_line_label = QLabel("__________________________________________________")
        
        area_layout = QHBoxLayout()
        area_label = QLabel("Total area: ")
        area_label.setFont(QFont("Roboto", 12, 600))
        self.area_line = QLineEdit()
        area_units = QLabel("square meters")
        area_units.setFont(QFont("Roboto", 12, 600))
        area_layout.addWidget(area_label)
        area_layout.addWidget(self.area_line)
        area_layout.addWidget(area_units)
        area_layout.setContentsMargins(62,15,0,0)


        depth_layout = QHBoxLayout()
        depth_label = QLabel("Mulch layer depth: ")
        depth_label.setFont(QFont("Roboto", 12, 600))
        self.depth_line = QLineEdit()
        depth_units = QLabel("centimeters")
        depth_units.setFont(QFont("Roboto", 12, 600))
        depth_layout.addWidget(depth_label)
        depth_layout.addWidget(self.depth_line)
        depth_layout.addWidget(depth_units)
        depth_layout.setContentsMargins(0,0,0,10)

        buttons_layout = QHBoxLayout()
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setStyleSheet("background-color: lime;" "color: white;")
        self.calculate_button.setFont(QFont("Roboto", 12, 700))
        self.calculate_button.clicked.connect(self.calculate_mulch)
        clear_button = QPushButton("Clear")
        buttons_layout.addWidget(self.calculate_button)
        buttons_layout.addWidget(clear_button)
        result_label = QLabel("The amount of mulch needed is ")
        result_label.setFont(QFont("Roboto", 12, 600))
        result_label.setContentsMargins(0,10,10,10)

        layout.addWidget(title_label)
        layout.addWidget(top_line_label)
        layout.addLayout(area_layout)
        layout.addLayout(depth_layout)
        layout.addLayout(buttons_layout)
        layout.addWidget(bottom_line_label)
        layout.addWidget(result_label)
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def calculate_mulch(self):
        # Area
        area = self.area_line.value()
        print(area)
        self.result_label.setText(f"The amount of mulch needed is (area) liters/square decimeters.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Roboto",12))
    window = MainWindow()
    window.show()

    app.exec()
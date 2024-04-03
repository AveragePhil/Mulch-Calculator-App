import sys

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

        layout = QVBoxLayout()
        title_label = QLabel("Mulch Calculator")
        
        area_layout = QHBoxLayout()
        area_label = QLabel("Total area: ")
        area_line = QLineEdit()
        area_layout.addWidget(area_label)
        area_layout.addWidget(area_line)

        depth_layout = QHBoxLayout()
        depth_label = QLabel("Mulch Layer Depth: ")
        depth_line = QLineEdit()
        depth_layout.addWidget(depth_label)
        depth_layout.addWidget(depth_line)

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
window = MainWindow()
window.show()

app.exec()
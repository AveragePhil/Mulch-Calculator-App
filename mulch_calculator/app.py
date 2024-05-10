
import controller
import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QSpinBox,
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
        # Title
        title_label = QLabel("Mulch Calculator")
        title_label.setContentsMargins(185,0,0,30)
        title_label.setFont(QFont("Roboto", 18, 700))

        # Add the top and bottom line
        top_line_label = QLabel("______________________________________________________________")
        bottom_line_label = QLabel("_______________________________________________________________")
        
        # Setup the area input spinbox and the area label widgets
        area_layout = QHBoxLayout()
        area_label = QLabel("Total area: ")
        area_label.setFont(QFont("Roboto", 12, 600))
        self.area_spinbox = QSpinBox()
        self.area_spinbox.setMaximum(10000)
        area_units = QLabel("square meters")
        area_units.setFont(QFont("Roboto", 12, 600))
        area_layout.addWidget(area_label)
        area_layout.addWidget(self.area_spinbox)
        area_layout.addWidget(area_units)
        area_layout.setContentsMargins(0,10,0,0)

        # Setup the depth input spinbox and the depth label widgets
        depth_layout = QHBoxLayout()
        depth_label = QLabel("Mulch layer depth: ")
        depth_label.setFont(QFont("Roboto", 12, 600))
        self.depth_spinbox = QSpinBox()
        self.depth_spinbox.setMaximum(1000)
        depth_units = QLabel("centimeters")
        depth_units.setFont(QFont("Roboto", 12, 600))
        depth_layout.addWidget(depth_label)
        depth_layout.addWidget(self.depth_spinbox)
        depth_layout.addWidget(depth_units)
        depth_layout.setContentsMargins(0,0,0,10)

        # Setup the CALCULATE and CLEAR button widgets
        buttons_layout = QHBoxLayout()
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setStyleSheet("background-color: lime;" "color: white;")
        self.calculate_button.setFont(QFont("Roboto", 12, 700))
        self.calculate_button.clicked.connect(self.calculate_mulch)
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_screen)
        buttons_layout.addWidget(self.calculate_button)
        buttons_layout.addWidget(self.clear_button)
        
        # Add the result label below
        self.result_label = QLabel("The amount of mulch needed is ")
        self.result_label.setFont(QFont("Roboto", 12, 600))
        self.result_label.setContentsMargins(0,10,10,10)

        # Add all the widgets to the layout and set them in order
        layout.addWidget(title_label)
        layout.addWidget(top_line_label)
        layout.addLayout(area_layout)
        layout.addLayout(depth_layout)
        layout.addLayout(buttons_layout)
        layout.addWidget(bottom_line_label)
        layout.addWidget(self.result_label)
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    # Calculate function
    def calculate_mulch(self):
        # Get inputs
        area = self.area_spinbox.value()
        depth = self.depth_spinbox.value()
        
        # Call the calculate function from controller
        mulch = controller.calculate_mulch(area, depth)
        
        # Format the results
        output = controller.display_results(mulch)
        
        # Display results
        self.result_label.setText(output)

    # Clear/reset values
    def clear_screen(self):
        self.area_spinbox.setValue(0)
        self.depth_spinbox.setValue(0)
        self.result_label.setText("")

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    app.setFont(QFont("Roboto",12))
    window = MainWindow()
    window.show()
    app.exec()
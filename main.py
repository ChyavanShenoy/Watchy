import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    text_label = QLabel(widget)
    text_label.setText("Hello World!")
    text_label.move(110, 85)
    widget.setGeometry(500, 50, 320, 200)
    widget.setWindowTitle("PyQt6 Example")
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    window()

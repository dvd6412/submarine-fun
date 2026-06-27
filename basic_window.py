import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

import logging

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display it's contents to the screen.
        """
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Empty window in PyQT')
        self.show()

class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display it's contents to the screen.
        """
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('QLabel example')
        self.displayLabels()
        self.show()

    def displayLabels(self):
        """
        Display text and images using QLabels.
        """
        text = QLabel(self)
        text.setText("Hello")
        text.move(105, 15)
        image = 'images/world.png'
        try:
            with open(image, "r"):
                world_image = QLabel(self)
                pixmap = QPixmap(image)
                world_image.setPixmap(pixmap)
                world_image.move(25, 40)
        except FileNotFoundError:
            logging.debug("Image not found")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())

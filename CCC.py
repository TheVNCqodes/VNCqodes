import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("I love Carabonara")
        self.setGeometry(450, 90, 1000, 850)
        self.setWindowIcon(QIcon("spderman pfp.png"))

        label = QLabel("Hello Pretty Cali", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0, 1000, 850)
        label.setStyleSheet("color: #791ed4;"
                            "background-color: #370b54;")

        label.setAlignment(Qt.AlignBottom |Qt.AlignCenter)

        label = QLabel(self)
        label.setGeometry(0, 0, 500, 500)

        pixmap = QPixmap("calicali.png")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                        (self.height() - label.height()) // 2,
        label.width(), label.height())

       # label.setAlignment(Qt.AlignTop)
       # label.setAlignment(Qt.AlignBottom)
     #   label.setAlignment(Qt.AlignVCenter)

        # label.setAlignment(Qt.AlignHCenter)

       # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QProgressBar
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import Qt, QTimer, QPoint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        gif_width = 800
        gif_height = 400
        progress_height = 5

        # Window size matches gif + progress bar
        self.setFixedSize(gif_width, gif_height + progress_height)
        self.setWindowTitle("SPIKIE")
        self.setWindowIcon(QIcon("resources/icon.jpg"))

        # Remove title bar & keep window on top
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # --- GIF Label ---
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, gif_width, gif_height)

        self.movie = QMovie("resources/loading_screen.gif")
        self.label.setMovie(self.movie)
        self.label.setScaledContents(True)
        self.movie.start()

        # --- Progress Bar (sticks right below GIF) ---
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, gif_height, gif_width, progress_height)
        self.progress.setRange(0, 100)
        self.progress.setTextVisible(False)

        # 🔥 Style to remove edges & keep it square
        self.progress.setStyleSheet("""
            QProgressBar {
                border: none;
                background-color: #e0e0e0; /* light gray background */
            }
            QProgressBar::chunk {
                background-color: #3498db; /* blue progress */
                margin: 0px;  /* removes spacing between chunks */
            }
        """)

        # --- Timer to simulate loading ---
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(50)
        self.counter = 0

        # For dragging
        self.drag_pos = QPoint()

    def handleTimer(self):
        self.counter += 1
        self.progress.setValue(self.counter)
        if self.counter >= 100:
            self.timer.stop()
            self.close()  # close splash screen when done

    # --- Enable dragging for frameless window ---
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_pos)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    # Center the window on screen
    qr = window.frameGeometry()
    cp = app.desktop().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

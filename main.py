import sys
from PyQt5 import QtWidgets
from ui.app_ui import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Example: connect tab logic later
        # self.control_tab = ControlTab(self.ui)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    # Make full screen
    window.showMaximized()   # or window.showFullScreen()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

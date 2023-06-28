import sys 
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from SSHLogJournalClass import SSHLogJournal
from list8_MainWindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow()

window.show()
sys.exit(app.exec())

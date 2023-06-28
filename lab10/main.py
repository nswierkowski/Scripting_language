from singleton_database import Database_name
import sys

db = None
if len(sys.argv) >= 2:
    db = Database_name(sys.argv[1])
else:
    db = Database_name('default_database_name')

import sys 
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from mainWindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow()

window.show()
sys.exit(app.exec())

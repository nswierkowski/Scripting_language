import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit

class ScrollableText(QMainWindow):
    def __init__(self, text):
        super().__init__()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.setCentralWidget(self.text_edit)
        self.setText(text)

    def setText(self, text):
        self.text = text
        self.text_edit.setPlainText(text)


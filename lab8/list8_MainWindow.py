from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QTextEdit
from SSHLogJournalClass import SSHLogJournal
from SSHLogJournalClass import to_datetime
from PySide6.QtCore import Qt, QTimer
from list8_ScrollableText import ScrollableText

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Log Browser")
        self.setFixedHeight(1000)
        self.setFixedWidth(1000)

        self.index = 0
        self.path_label = QLabel("Enter path to file:")
        self.path_input = QLineEdit("/home/nikodem/Uczelnia/Języki_Skryptowe/lab8/SSH.log")
        self.button = QPushButton("Open")
        self.logs_label = ScrollableText("None")

        #from and to
        self.from_label = QLabel("from:")
        self.from_input = QLineEdit("Dec 10 19:21:00")
        self.to_label = QLabel("to:")
        self.to_input = QLineEdit("Dec 12 21:32:40")

        #Details
        self.host_label = QLabel("Host: None")
        self.date_label = QLabel("Data: None")
        self.message_label = QLabel("Message: None")
        self.pID_label = QLabel("ID: None") 
        self.ip_label = QLabel("IP: None") 

        #Next and previous
        self.next_button = QPushButton("Next")
        self.previous_button = QPushButton("Previous")
        self.reset_button = QPushButton("Reset")
        self.log_list = None

        layout = QVBoxLayout()
        layout.addWidget(self.path_label)
        layout.addWidget(self.path_input)
        layout.addWidget(self.from_label)
        layout.addWidget(self.from_input)
        layout.addWidget(self.to_label)
        layout.addWidget(self.to_input)
        layout.addWidget(self.button)
        layout.addWidget(self.logs_label)
        layout.addWidget(self.host_label)
        layout.addWidget(self.date_label)
        layout.addWidget(self.message_label)
        layout.addWidget(self.pID_label)
        layout.addWidget(self.ip_label)
        layout.addWidget(self.next_button)
        layout.addWidget(self.previous_button)
        layout.addWidget(self.reset_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button.clicked.connect(self.read_logs_from_file)
        self.next_button.clicked.connect(self.next_log)
        self.previous_button.clicked.connect(self.previous_log)
        self.reset_button.clicked.connect(self.reset)

    def reset(self):
        self.index = 0
        self.path_input.setText("/home/nikodem/Uczelnia/Języki_Skryptowe/lab8/SSH.log")
        self.button = QPushButton("Open")
        self.logs_label.setText("None")

        #from and to
        self.from_label = QLabel("from:")
        self.from_input.setText("Dec 10 19:21:00")
        self.to_label = QLabel("to:")
        self.to_input.setText("Dec 20 21:32:40")

        #Details
        self.host_label.setText("Host: None")
        self.date_label.setText("Data: None")
        self.message_label.setText("Message: None")
        self.pID_label.setText("ID: None")     
        self.ip_label.setText("IP: None")       

        #Next and previous
        self.next_button = QPushButton("Next")
        self.previous_button = QPushButton("Previous")
        self.reset_button = QPushButton("Reset")
        self.log_list = None

    def next_log(self):
        self.index += 1
        if self.index >= len(self.log_list):
            self.reset()
        self.update_details()

    def previous_log(self):
        self.index -= 1
        if self.index <= 0:
            self.reset()
        self.update_details()

    def update_details(self):
        try:
            log = self.log_list[self.index]
        except IndexError:
            print(self.index)
            self.reset()
        self.host_label.setText("Host: " + str(log.hostName))
        self.date_label.setText("Date: " + str(log.date))
        self.message_label.setText("Message: " + str(log.message))
        self.pID_label.setText("ID: " + str(log.pID))
        self.ip_label.setText("IP: " + str(log.get_ipv4()))  

    def show_logs(self):
        print("I really try")
        all_logs_in_str = ""
        self.log_list = self.log_list.get(to_datetime(self.from_input.text()), to_datetime(self.to_input.text()))
        print("Hey I found every single log")
        for log in self.log_list:
            if len(log) > 200:
                all_logs_in_str = "".join([all_logs_in_str, "".join([str(log)[:200], "..."]), "\n"])
            else:
                all_logs_in_str = "".join([all_logs_in_str, str(log), "\n"])
        print("Loop ended")
        self.logs_label.setText(all_logs_in_str)
        print("Text set")
        self.update_details()

    def read_logs_from_file(self):
        path = self.path_input.text()
        if not path:
            path = '/home/nikodem/Uczelnia/Języki_Skryptowe/lab8/SSH2.log'
        self.log_list = SSHLogJournal()
        with open(path) as f:
            for line in f:
                self.log_list.append(line)
        print("Ready")
        self.show_logs()
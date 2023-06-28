from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QTextEdit
from PySide6.QtCore import Qt, QTimer
from scrollableText import ScrollableText
import peewee as pe
from database_classes import Stations, Rentals, get_average_duration_at, get_average_duration_to, get_number_of_bicycles, get_rental_difference
import logging

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Stations")
        self.setFixedHeight(500)
        self.setFixedWidth(500)

        self.index = 0
        self.stations_label = ScrollableText("None")

        #Details
        self.station_name = QLabel("Stations name: ")
        self.journey_starting_at_a_given_station = QLabel("Average duration of a journey starting at a given station: None")
        self.journey_ending_at_a_given_station = QLabel("Average duration of the trip ending at the station: None")
        self.number_of_bicycles = QLabel("Number of different bicycles parked at a given station: None")
        self.diff_rentaled_returned = QLabel("Total change in the number of bicycles at a station: None")

        #Next and previous
        self.next_button = QPushButton("Next")
        self.previous_button = QPushButton("Previous")
        self.stations_list = None

        layout = QVBoxLayout()
        layout.addWidget(self.stations_label)
        layout.addWidget(self.station_name)
        layout.addWidget(self.journey_starting_at_a_given_station)
        layout.addWidget(self.journey_ending_at_a_given_station)
        layout.addWidget(self.number_of_bicycles)
        layout.addWidget(self.diff_rentaled_returned)
        layout.addWidget(self.next_button)
        layout.addWidget(self.previous_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.next_button.clicked.connect(self.next)
        self.previous_button.clicked.connect(self.previous)

        self.show_stations()

    def next(self):
        self.index += 1
        if self.index >= len(self.stations_list):
            self.index -= 1
        self.update_details()

    def previous(self):
        self.index -= 1
        if self.index < 0:
            self.index += 1
        self.update_details()


    def update_details(self):
        try:
            station = self.stations_list[self.index]
        except IndexError:
            logging.error(f"INDEX ERROR: {self.index}")

        avg_duration_at = get_average_duration_at(station['station_id'])
        avg_duration_to = get_average_duration_to(station['station_id'])
        num_bikes = get_number_of_bicycles(station['station_id'])
        diff_rental_return = get_rental_difference(station['station_id'])

        self.station_name.setText(f"Stations name: {station['station_name']}")
        self.journey_starting_at_a_given_station.setText(f"Average duration of a journey starting at a given station: {avg_duration_at} minutes")
        self.journey_ending_at_a_given_station.setText(f"Average duration of the trip ending at the station: {avg_duration_to} minutes")
        self.number_of_bicycles.setText(f"Number of different bicycles parked at a given station: {num_bikes}")
        self.diff_rentaled_returned.setText(f"Total change in the number of bicycles at a station: {diff_rental_return}")

    def show_stations(self):
        all_stations_in_str = ""
        self.stations_list = [station for station in Stations.select().dicts()]
        for station in self.stations_list:
            all_stations_in_str = "".join([all_stations_in_str, str(station['station_name']), "\n"])
        self.stations_label.setText(all_stations_in_str)
        self.update_details()
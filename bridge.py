from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, Property
from PySide6.QtGui import QIcon, QGuiApplication
import sys
import sqlite3
import qml_rc
from database import Database
from source import Source
import locale
import threading


def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


class Bridge(QObject):
    view_array_changed = Signal()
    view_table_changed = Signal()
    catalogue_changed = Signal()
    isotope_list_changed = Signal()
    shields_list_changed = Signal()
    dose_types_changed = Signal()
    wait_changed = Signal()
    db_exists_changed = Signal()

    def __init__(self):
        QObject.__init__(self)
        locale.setlocale(locale.LC_ALL, '')

        self._wait = False
        self._view_array = []
        self._view_table = []
        self._catalogue = []
        self._isotope_list = []
        self._shields_list = []
        self._dose_types = ["Ambient", "Personal"]

        self._db_exists = True

        try:
            self._db = Database('DoseCalculator_DB.db')
            self._source = Source(self._db)

            self._source.data_changed_changed.connect(self.source_data_changed)
            self._source.wait_changed.connect(self.wait_value_changed)

            temp = []

            for item in self._db.halflife:
                temp.append(item[0])

            self._isotope_list = temp

            temp = []

            for item in self._db.sources:
                temp.append(f'{item[1]}\t{item[2]}')

            self._catalogue = temp

            self._shields_list = self._db.materials

            self.source_data_changed()
        except sqlite3.OperationalError:
            self._db_exists = False

    @Property(list, notify=view_array_changed)
    def view_array(self):
        return self._view_array

    @view_array.setter
    def view_array(self, value):
        self._view_array = value

    @Property(list, notify=view_table_changed)
    def view_table(self):
        return self._view_table

    @Property(list, notify=catalogue_changed)
    def catalogue(self):
        return self._catalogue

    @Property(list, notify=shields_list_changed)
    def shields_list(self):
        return self._shields_list

    @Property(list, notify=isotope_list_changed)
    def isotope_list(self):
        return self._isotope_list

    @Property(list, notify=dose_types_changed)
    def dose_types(self):
        return self._dose_types

    @Property(bool, notify=wait_changed)
    def wait(self):
        return self._wait

    @Property(bool, notify=db_exists_changed)
    def db_exists(self):
        return self._db_exists

    def __setattr__(self, name, value):
        match name:
            case '_view_array':
                super().__setattr__(name, value)
                self.view_array_changed.emit()
            case '_view_table':
                super().__setattr__(name, value)
                self.view_table_changed.emit()
            case '_isotope_list':
                super().__setattr__(name, value)
                self.isotope_list_changed.emit()
            case '_catalogue':
                super().__setattr__(name, value)
                self.catalogue_changed.emit()
            case '_shields_list':
                super().__setattr__(name, value)
                self.shields_list_changed.emit()
            case '_wait':
                super().__setattr__(name, value)
                self.wait_changed.emit()
            case '_db_exists':
                super().__setattr__(name, value)
                self.db_exists_changed.emit()
            case _:
                super().__setattr__(name, value)

    def source_data_changed(self):
        temp = [self._source.number, self._source.name, self._source.halflife, self._source.prod_date,
                self._source.original_activity, self._source.cur_date, self._source.current_activity,
                self._source.material, self._source.thickness, self._source.distance, self._source.type,
                self._source.sum_flux, self._source.sum_dose_rate]
        self._view_array = temp

        temp = []
        for i in range(len(self._source.lines)):
            temp.append(f'{round(self._source.lines[i][0]*1000, 3)}\t{self._source.lines[i][1]}\t'
                        f'{round(self._source.dose_rate[i], 3)}\t{round(self._source.flux[i], 3)}')
        self._view_table = temp

    @Slot(str)
    def on_action(self, action):
        match action:
            case "source":
                self._source.name = self._view_array[1]
                self._source.prod_date = self._view_array[3]
                self._source.original_activity = int(self._view_array[4])
                self._source.cur_date = self._view_array[5]
                self._source.current_activity = int(self._view_array[6])
                self._source.parameters_changed()
            case "activity":
                if is_number(self._view_array[8]) and is_number(self._view_array[9]):
                    self._source.current_activity = int(self._view_array[6])
                    self._source.material = self._view_array[7]
                    self._source.thickness = self._view_array[8]
                    self._source.distance = self._view_array[9]
                    self._source.type = self._view_array[10]
                    self._source.calculate()
            case "der":
                if is_number(self._view_array[12]):
                    self._source.sum_dose_rate = locale.atof(self._view_array[12])
                    calc_thread = threading.Thread(target=self._source.reverse_calculation)
                    calc_thread.daemon = True
                    calc_thread.start()
            case _:
                self._source.index_changed(int(action))

    def wait_value_changed(self):
        if self._db_exists:
            self._wait = self._source.wait


def run_app():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    app.setWindowIcon(QIcon('img/icon.ico'))

    bridge = Bridge()

    engine.rootContext().setContextProperty('bridge', bridge)

    engine.load("main.qml")

    if not engine.rootObjects():
        return -1

    return app.exec()

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
from sample.core import ModsController
import json
import sys
import MainWindow
import pathlib


class App(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.__json_path = pathlib.Path.cwd() / "config.json"
        self.__mod_config_path = pathlib.Path(self.rootPath.text())/"data/mods.cfg"

        if self.__json_path.exists():
            with open('config.json') as json_file:
                paths = json.load(json_file)
                self.rootPath.setText(paths['rootPath'])
                self.workshopPath.setText(paths['workshopPath'])

        self.add_mods_to_list()
        self.pathButton.clicked.connect(self.slot_save_paths)
        self.configButton.clicked.connect(self.save_config)

    def show_message(self, message, title):
        error_dialogue = QtWidgets.QMessageBox()
        error_dialogue.setText(message)
        error_dialogue.setWindowTitle(title)
        error_dialogue.exec_()

    def add_mods_to_list(self):
        mc = ModsController(self.rootPath.text(), self.workshopPath.text())
        for mod in mc.get_mods():
            self.listWidget.addItem(self.list_item(mod, QtCore.Qt.Unchecked))

    @staticmethod
    def list_item(text, checkstate):
        list_item = QtWidgets.QListWidgetItem()
        list_item.setText(text)
        list_item.setCheckState(checkstate)
        return list_item

    def save_config(self):
        lw = self.listWidget
        mod_list = []

        for x in range(lw.count()):
            if lw.item(x).checkState() != QtCore.Qt.Unchecked:
                mod_list.append(lw.item(x).text() + "\n")

        with open(self.__mod_config_path, 'w') as file:
            file.writelines(mod_list)

        self.show_message("Config saved.", "Saved!")

    def slot_save_paths(self):
        if self.rootPath.text() == "":
            self.show_message("ERROR: Root path is required!", "ERROR")
        else:
            paths_data = {'rootPath': self.rootPath.text(),
                          'workshopPath': self.workshopPath.text()}

            with open('config.json', 'w', encoding='utf-8') as f:
                json.dump(paths_data, f)

            self.show_message("Paths are saved, when you open up the mod manager it will use the specified paths.",
                              "Paths saved!")


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

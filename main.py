from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
from sample.core import ModsController
import json
import sys
import MainWindow
from pathlib import Path
import subprocess
import os


class App(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.__json_path = Path.cwd() / "config/config.json"

        if self.__json_path.exists():
            with open('config/config.json') as json_file:
                paths = json.load(json_file)
                self.rootPath.setText(paths['rootPath'])
                self.workshopPath.setText(paths['workshopPath'])
                self.steamPath.setText(paths['steamPath'])

        self.add_mods_to_list()
        self.pathButton.clicked.connect(self.slot_save_paths)
        self.configButton.clicked.connect(self.save_config)
        self.playButton.clicked.connect(self.start_kenshi)
        self.selectRootPath.clicked.connect(self.find_directory)
        self.selectWorkshopPath.clicked.connect(self.find_directory)
        self.selectSteamPath.clicked.connect(self.find_directory)

    def find_directory(self):
        directory = QtWidgets.QFileDialog().getExistingDirectory(self, "Choose a folder")
        sender = self.sender().objectName()
        if sender == "selectRootPath":
            self.rootPath.setText(str(Path(directory)))
        elif sender == "selectWorkshopPath":
            self.workshopPath.setText(str(Path(directory)))
        elif sender == "selectSteamPath":
            self.steamPath.setText(str(Path(directory)))
        else:
            pass

    def show_message(self, message, title):
        error_dialogue = QtWidgets.QMessageBox()
        error_dialogue.setText(message)
        error_dialogue.setWindowTitle(title)
        error_dialogue.exec_()

    @staticmethod
    def pathify(input_widget, turn_to_path=False):
        if turn_to_path is True:
            return Path(input_widget.text())
        else:
            return input_widget.text()

    def start_kenshi(self):
        if len(self.pathify(self.steamPath)) != 0:
            if self.pathify(self.steamPath, True).exists():
                subprocess.run(cwd=self.pathify(self.steamPath, True), args=["steam", "steam://run/233860"], shell=True)
            else:
                self.show_message("ERROR: Path does not exist, perhaps you put in the wrong path?")
        else:
            self.show_message("ERROR: Steam path is required!", "ERROR")

    @staticmethod
    def list_item(text, checkstate):
        list_item = QtWidgets.QListWidgetItem()
        list_item.setText(text)
        list_item.setCheckState(checkstate)
        return list_item

    def add_mods_to_list(self):
        mc = ModsController(self.rootPath.text(), self.workshopPath.text())
        mod_config_path = self.pathify(self.rootPath, True)/"data/mods.cfg"

        # Turn installed_mods into a set so it can be used comparing
        # NOTE: Turning this into a set causes the list to be unordered, so every time the app gets restarted the
        # unchecked mods are in a different order

        installed_mods = set(mc.get_mods())
        with open(mod_config_path) as file:
            file_lines = file.readlines()
            mods_in_mod_config = [line.strip() for line in file_lines]
            # Use difference to see which mods arent in the current load order and load them after
            diff = installed_mods.difference(mods_in_mod_config)
            for mod in mods_in_mod_config:
                self.listWidget.addItem(self.list_item(mod, QtCore.Qt.Checked))

            for mod in list(diff):
                self.listWidget.addItem(self.list_item(mod, QtCore.Qt.Unchecked))

    def save_config(self):
        lw = self.listWidget
        mod_list = []
        mod_config_path = self.pathify(self.rootPath, True)/"data/mods.cfg"

        for x in range(lw.count()):
            if lw.item(x).checkState() != QtCore.Qt.Unchecked:
                mod_list.append(lw.item(x).text() + "\n")

        if mod_config_path.exists():
            mod_config_path.replace(mod_config_path.parent/"mods.cfg.backup")

        with open(mod_config_path, 'w') as file:
            file.writelines(mod_list)

        self.show_message("Config saved.", "Saved!")

    def slot_save_paths(self):
        if self.pathify(self.rootPath) == "":
            self.show_message("ERROR: Root path is required!", "ERROR")
        else:
            print(self.pathify(self.workshopPath))
            paths_data = {'rootPath': self.pathify(self.rootPath),
                          'workshopPath': self.pathify(self.workshopPath),
                          'steamPath': self.pathify(self.steamPath)}

            os.makedirs("config", exist_ok=True)
            with open('config/config.json', 'w', encoding='utf-8') as f:
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

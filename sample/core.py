from pathlib import Path


class ModsController:
    def __init__(self, root, workshoppath=""):
        self.__rootstring = root
        self.__workshopstring = workshoppath

    @staticmethod
    def __validate_path(path):
        path_object = Path(path)
        if path != "" and path_object.exists():
            return True
        else:
            return False

    def get_mods_path(self):
        if self.__validate_path(self.__rootstring):
            kenshi_exe = Path(self.__rootstring + "/kenshi_x64.exe")
            if kenshi_exe.exists():
                mods_path = Path(self.__rootstring) / "mods"
                return mods_path
        else:
            return ""

    def get_workshop_path(self):
        if self.__validate_path(self.__workshopstring):
            workshop_name = Path(self.__workshopstring)
            if workshop_name.name == "233860":
                return Path(self.__workshopstring)
        else:
            return ""

    def get_config_path(self):
        path = Path(self.__rootstring) / "data/mods.cfg"
        return path

    def __collect_mods(self, path, arr):
        """
        This looks odd so might change it in the future. But for now i'll explain:
        variable mods are all the child folders in the parent path folder
        eg: parent/child1, parent/child2
        variable mod is the child folder path of the the parent, in the last example child 1 and child 2 would be mod
        mod would then be checked if there are no suffixes
        (This is done for the readme.txt that doesnt belong in the list)
        then for every mod in the mods folder we will check all the files for a file with a .mod extension
        then we append that file to the array

        path: Root path where are the mods are stored
        arr: Array to store the mods
        """
        if path != "":
            mods = path.iterdir()
            for mod in mods:
                if not mod.suffix:
                    for file in mod.iterdir():
                        if file.suffix == ".mod":
                            arr.append(file.name)

    def get_mods(self):
        mods_list = []

        self.__collect_mods(self.get_mods_path(), mods_list)
        self.__collect_mods(self.get_workshop_path(), mods_list)

        return mods_list

import unittest
from sample.core import ModsController
from pathlib import Path
import json

collector = ModsController("C:/Casual/Steam/steamapps/common/Kenshi/")


class CollectorTests(unittest.TestCase):
    def assertIsFileType(self, file_type, file):
        if file_type in file:
            is_type = True
        else:
            is_type = False
        self.assertTrue(is_type)

    def test_get_mods_path(self):
        mods_path = collector.get_mods_path()
        self.assertTrue(mods_path.exists())
        self.assertIsInstance(mods_path, Path)
        self.assertTrue(mods_path.name == "mods")

    def test_get_config_path(self):
        config_path = collector.get_config_path()
        self.assertTrue(config_path.exists())
        self.assertIsInstance(config_path, Path)
        self.assertIsFileType(".cfg", config_path.suffix)

    def test_get_workshop_path(self):
        if collector.get_workshop_path() != "":
            workshop_path = collector.get_workshop_path()
            self.assertTrue(workshop_path.exists())
            self.assertIsInstance(workshop_path, Path)
            self.assertEqual(int(collector.get_workshop_path().name), 233860)

    def test_get_mods(self):
        # Test if every string in the list of mods ends with .mod
        list_of_mods = collector.get_mods()
        self.assertIsInstance(list_of_mods, list)
        for mod in list_of_mods:
            self.assertIsInstance(mod, str)
            self.assertIsFileType(".mod", mod)


if __name__ == '__main__':
    unittest.main()

"""Tests for scripts/common.py. Run: python3 -m unittest discover tests/py"""
import importlib
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
common = importlib.import_module("common")


class FilterDataTest(unittest.TestCase):

    def test_types_each_setting_for_libreoffice(self):
        data = json.loads(common.filter_data({
            "ExportNotes": False,  # a bool is also an int, so it comes first
            "SelectPdfVersion": 17,
            "PageRange": "1-2",
        }))
        self.assertEqual(data, {
            "ExportNotes": {"type": "boolean", "value": "false"},
            "SelectPdfVersion": {"type": "long", "value": "17"},
            "PageRange": {"type": "string", "value": "1-2"},
        })


if __name__ == "__main__":
    unittest.main()

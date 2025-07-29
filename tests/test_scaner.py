import unittest
import tempfile
import os
from pathlib import Path
from src.core.scanner import FileScanner

class TestScanner(unittest.TestCase):
    def setUp(self):
        self.scanner = FileScanner()
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b"test content")
        self.temp_file.close()
    
    def test_scan_clean_file(self):
        malicious, _ = self.scanner.scan_file(self.temp_file.name)
        self.assertFalse(malicious)
    
    def tearDown(self):
        os.unlink(self.temp_file.name)

if __name__ == "__main__":
    unittest.main()

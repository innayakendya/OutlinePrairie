# test_outlineprairie.py
"""
Tests for OutlinePrairie module.
"""

import unittest
from outlineprairie import OutlinePrairie

class TestOutlinePrairie(unittest.TestCase):
    """Test cases for OutlinePrairie class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OutlinePrairie()
        self.assertIsInstance(instance, OutlinePrairie)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OutlinePrairie()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

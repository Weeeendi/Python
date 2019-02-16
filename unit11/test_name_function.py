import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test name_function"""

    def test_first_last_name(self):
        """Can names like Janis Joplin be correctly addressed?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Can names like Janis Joplin Lee be correctly addressed?"""
        formatted_name = get_formatted_name('janis','lee', 'joplin')
        self.assertEqual(formatted_name,'Janis Joplin Lee')

unittest.main()
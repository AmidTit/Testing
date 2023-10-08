import unittest
from test_task import get_file, do_replacement


class TestPackageTask(unittest.TestCase):

    def test_get_file_type(self):
        
        data_url = "https://api.github.com/repos/thewhitesoft/student-2023-assignment/contents/data.json"
        self.assertEqual(get_file(data_url)['type'], "file")

    
    def test_get_file_encoding(self):
        
        data_url = "https://api.github.com/repos/thewhitesoft/student-2023-assignment/contents/data.json"
        self.assertEqual(get_file(data_url)['encoding'], "base64")

    
    def test_get_file_with_empty_url(self):
        
        data_url = "https://api.github.com//"
        self.assertEqual(get_file(data_url), "No file")

    
    def test_do_replacement(self):
        
        data = ["Hello wtf"]
        replacement = [{"replacement": "wtf", "source": "World"}]

        self.assertEqual(do_replacement(replacement, data), ["Hello World"])

    
    def test_do_replacement_with_None(self):
        
        data = ["Hello wtf", "Looks like I hacked you buddy"]
        
        replacement = [
            {"replacement": "wtf", "source": "World"},
            {"replacement": "Looks like I hacked you buddy", "source": None}
                      ]
        
        self.assertEqual(do_replacement(replacement, data), ["Hello World"])

    
    def test_do_replacement_with_repetition(self):
        
        data = ["Hello wtf", "Looks like I hacked you buddy", "Let`s rock this srgrbbxf546"]
        
        replacement = [
            {"replacement": "wtf", "source": "Girls and Boys"},
            {"replacement": "Looks like I hacked you buddy", "source": None},
            {"replacement": "wtf", "source": "World"},
            {"replacement": "srgrbbxf546", "source": "dump"}
                      ]

        self.assertEqual(do_replacement(replacement, data), ["Hello World", "Let`s rock this dump"])

if __name__ == '__main__':
    unittest.main()

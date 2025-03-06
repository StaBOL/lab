import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.print_string("bab"), "bab")  # add assertion here
    def test_something2(self):
            self.assertEqual(main.count_vowels("сом"), 1)
    def test_something3(self):
            self.assertEqual(main.onefunc("hello"),"olleh")
    def test_something4(self):
                self.assertEqual(main.removeduplicates("сонн"),"сон")
#проверка изменения
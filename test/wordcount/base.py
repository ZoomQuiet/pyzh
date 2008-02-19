#coding=utf-8

import unittest

class BaseTest(unittest.TestCase):
    def test_count_eng_only(self):
        text = "ABCDEFG"        
        self.assertEqual(self.counter.count(text), 7)
        
    def test_count_chs_only(self):
        text = "作者"        
        self.assertEqual(self.counter.count(text), 2)
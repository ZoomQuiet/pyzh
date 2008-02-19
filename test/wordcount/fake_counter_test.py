import base
from wordcount import fake_counter

class FakeCounterTest(base.BaseTest):
    def setUp(self):        
        self.counter = fake_counter
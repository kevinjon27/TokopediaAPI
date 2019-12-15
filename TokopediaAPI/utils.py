import json
import os

class Utils(object):
    
    script_dir = os.path.dirname(__file__)
    
    def get_something(self):
        return self.script_dir
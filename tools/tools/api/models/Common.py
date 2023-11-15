import json

import logging

log = logging.getLogger()
    
class KeyDollarListDict(dict):
    def __init__(self, input_list=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key_prefix = "@key"
        self.value_prefix = "$"
        if input_list:
            self.deserialize(input_list)
        log.debug(self)

       
    def deserialize(self, input_list):
        print(input_list)
        for item in input_list:
            key = item[self.key_prefix]
            value = item[self.value_prefix]
            super().__setitem__(key, value)
    
    def serialize(self):
        return [{self.key_prefix: key, self.value_prefix: value} for key, value in self.items()]
    
    def __str__(self):
        return json.dumps(self.serialize())

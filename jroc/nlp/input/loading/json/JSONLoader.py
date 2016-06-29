import json

class JSONLoader(object):
    """
    JSON data loader. It expects a 'data' key in input
    e.g.

    {"data": ...}
    """
    def __init__(self, json_string=""):
        self.jsonObj = json.loads(json_string)

    def getData(self):
        """
        It returns the data inside the json object
        If data does not exist, it will return an exception
        """
        data = self.jsonObj.get('data', None)
        
        if data is None:
            raise Exception("Data key is not present in the input")
        return self.jsonObj.get('data', None)

import uuid

class RocksDB():
    def __init__(self, db_name="app.db"):
        self.db_name = db_name
    
    def put(self, value):
        key = uuid.uuid4().hex
        print("PUT:key={} value={}".format(key, value))
    
    def get(self, key):
        print("GET:key={} value={}".format(key, "Fixme"))
        return "FixMe"
        
    def delete(self, key):
        print("DELETE:key={}".format(key))


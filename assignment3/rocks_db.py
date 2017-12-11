import uuid
# import rocksdb

class RocksDB():
    def __init__(self, db_name="app.db"):
        self.db_name = db_name
        print("initialized a RocksDB {}".format(self.db_name))
        # self.db = rocksdb.DB(db_name, rocksdb.Options(create_if_missing=True))

    def put(self, value):
        key = uuid.uuid4().hex
        print("PUT:key={} value={}".format(key, value))
        # TODO rocksDB.put()
        return key
    
    def get(self, key):
        print("GET:key={} value={}".format(key, "Fixme"))
        # TODO rocksDB.get()
        return "TODO"
        
    def delete(self, key):
        print("DELETE:key={}".format(key))
        # TODO rocksDB.delete()


class InMemoryDB:
    def __init__(self):
        self.main = {}
        self.storage = None
        self.active = False

    def begin_transaction(self):
        if self.active:
            raise Exception("Null")
        self.storage = {}
        self.active = True

    def put(self, key, value):
        if not self.active:
            raise Exception("Null")
        self.storage[key] = value

    def get(self, key):
        if self.active and key in self.storage:
            return self.storage[key]
        return self.main.get(key, None)

    def commit(self):
        if not self.active:
            raise Exception("Null")
        for key, value in self.storage.items():
            self.main[key] = value
        self.storage = None
        self.active = False

    def rollback(self):
        if not self.active:
            raise Exception("Null")
        self.storage = None
        self.active = False

#Testing
#if __name__ == "__main__":
    # db = InMemoryDB()
    # print(db.get("A"))
    # db.put("A", 5)
    # db.begin_transaction()
    # db.put("A", 5)
    # print(db.get("A"))
    # db.put("A", 6)
    # db.commit()
    # print(db.get("A"))
    # db.commit()
    # db.rollback()
    # print(db.get("B"))
    # db.begin_transaction()
    # db.put("B", 10)
    # db.rollback()
    # print(db.get("B"))
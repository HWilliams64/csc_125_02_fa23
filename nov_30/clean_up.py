import random

class DataBase:
    connections = []

    def connect(self, user):
        if len(self.connections) < 2:
            self.connections.append(user)
        else:
            raise ConnectionError("Unable to connect to database because there are not enough connections available")
        print(f"{user} - Connected to database")

    def disconnect(self, user):
        self.connections.remove(user)
        print(f"{user} - Disconnected from database")

    def do_something(self, user):
        exc = random.choice((ValueError, IndexError, KeyError, TypeError))

        if random.uniform(0, 1) < .8:
            raise exc()
        print(f"{user} - Database operation successful")


db = DataBase()

for user in ['user 1', 'user 2', 'user 3', 'user 4', 'user 5', 'user 6', 'user 7', 'user 8', 'user 9']:
    try:
        print(f"{user} - Connecting to database...")
        db.connect(user)
        db.do_something(user)
    except Exception as e:
        print(f"{user} - Database operation error {e}")
    finally:
        db.disconnect(user)

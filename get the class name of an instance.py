class vehicle:
    def name(self, name):
        return name
v = vehicle()
print(v.__class__.__name__)

#Using type() and __name__ attribute
class vehicle:
    def name(self, name):
        return name
v = vehicle()
print(type(v).__name__)
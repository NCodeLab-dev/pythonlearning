
#class syntax
class employee:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

    def displayEmployee(self):
        print(self.id);
        print(self.name);
        print(self.location)


jina = employee(123,"narayan Sahu","bangalore")
jina.displayEmployee()




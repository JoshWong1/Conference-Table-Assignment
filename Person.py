class Person:    
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        self.tables = []
        
    def addTable(self, n):
        self.tables.append(n)
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getTables(self):
        return self.tables
    
    def toString(self):
        s = self.fname + " " + self.lname + ": "
        for table in self.tables:
            s += str(table.getNumber()) + " "
        return s
    
    def toList(self):
        l = [self.lastName + ", " + self.firstName]
        for table in self.tables:
            l.append(str(table.getNumber()))
        return l

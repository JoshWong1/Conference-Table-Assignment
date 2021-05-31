class Table:    
    def __init__(self, capacity, number):
        self.members = []
        self.tables = []
        self.size = 0
        self.capacity = capacity
        self.number = number
    
    def clearMembers(self):
        self.tables.append(self.members)
        self.members = []
        self.size = 0
        
    def addMember(self, person):
        self.members.append(person)
        person.addTable(self)
        self.size += 1
    
    def getSize(self):
        return self.size
    
    def getNumber(self):
        return self.number
    
    def getMembers(self):
        return self.members
    
    def getCapacity(self):
        return self.capacity
    
    def toString(self):
        meals = [["Lunch:", "Dinner:"], ["Breakfast:", "Lunch:"], \
                 ["Breakfast:", "Lunch:"]]
        s = ""
        Days = [[self.tables[0], self.tables[1]], [self.tables[2], self.tables[3]]]
        
        for i in range(2):
            s += "Day " + str(i + 1) + "\n"
            for k in range(len(meals[i])):
                s += "{0: <24}".format(meals[i][k])
            s += "\n"
            for j in range(self.capacity):
                for item in Days[i]:
                    name = item[j].getFirstName() + " " + item[j].getLastName() if j < len(item) else ""
                    s += "{0: <24}".format(name)
                s += "\n"
            s+= "\n"
   
        return s    

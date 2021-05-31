import random
import math
import xlsxwriter
from Person import Person
from Table import Table

# Given a list of tables, list of people, and list of families, assigns each
# person to a table randomly
def assignTables (tables, people, families):
    random.shuffle(people)    
    for j, family in enumerate(families):
        for member in family:
            tables[j].addMember(member)    
    i = 0
    for x in people:
        while tables[i].getSize() >= 8:
            i = (i + 1) % len(tables)
        tables[i].addMember(x)
        i = (i + 1) % len(tables)    
    return tables   

# Randomly assigns people to tables 4 times (once per meal)
def createTables(tables, people, families, n):
    for i in range(n):
        tables = assignTables(tables, people, families)
        for table in tables:     
            table.clearMembers()      
    return tables

# Write each table's data to its corresponding table file   
def writeTableFiles(tables, tableFiles):
    for i in range(len(tables)):
        tableFiles[i].write("Table %i\n\n" % (i + 1))
        tableFiles[i].write(tables[i].toString())
        tableFiles[i].close() 
        
# Find famlies if any exist
def findFamilies(li):
    j = 0
    families = []
    for name in li:
        l = name.split()
        if len(l[-1]) == 1:    
            lname, fname = l[0], l[1]
            if len(families) < int(l[-1]) + 1:
                families.append([Person(fname, lname)])
            else:
                families[int(l[-1])].append(Person(fname, lname))
            j += 1
        else:
            break
    return families, j

# Create Table Arrangements spreadsheet
def outputToSpreadsheet(people, families):
    workbook = xlsxwriter.Workbook("Winter Retreat 2019 Table Arrangements.xlsx")
    worksheet = workbook.add_worksheet()

    people = sorted(sum(families, []) + people, key=lambda x:x.getLastName()) 
    data = [person.toList() for person in people]  
        
    name_format = workbook.add_format({"font_size": 10, "font_name": "Arial"})
    num_format = workbook.add_format({"font_size": 10, "font_name": "Arial", "center_across": 1})
    title_format = workbook.add_format({"font_size": 12, "font_name": "Arial", "bold": 1})
        
    worksheet.set_column(1, 4, 9, name_format) #set_column(first column, last column, width, format)
    worksheet.set_column(0, 0, 16, name_format) #for title
   
    worksheet.write(0, 0, "Summer Retreat 2019 - Table Arrangements", title_format)
    worksheet.add_table("A3:E41", {"data" : data, "style": "Table Style Medium 15", "columns": \
    [{"header": "Name"}, {"header": "Day 1 L", "format": num_format}, {"header": "Day 1 D", "format": num_format},\
     {"header": "Day 2 B", "format": num_format}, {"header": "Day 2 L", "format": num_format}]})
     #{"header": "Day 2 D", "format": num_format}, {"header": "Day 3 B", "format": num_format}, \
     #{"header": "Day 3 L", "format": num_format}]})  
    workbook.close()  

# Table files
def createTableFiles(numTables):
    tableFiles = []
    for i in range(numTables):
        filename = "Winter Retreat Table " + str(i + 1) + ".txt"
        tableFiles.append(open(filename, 'w')) 
    return tableFiles
    
if __name__ == "__main__":    
    #Input file
    filename = "names3.txt"     
    li = open(filename, "r").readlines() 
    
    size = 8
    numTables = math.ceil(len(li) / size)
    tables = [Table(size, t+1) for t in range(numTables)]      
     
    families, j = findFamilies(li)    
    li = [l.split() for l in li[j:]]
    people = [Person(l[1], l[0]) for l in li] 
    tables = createTables(tables, people, families, 4)
    
    #Create a table file for each table
    tableFiles = createTableFiles(numTables)  
    writeTableFiles(tables, tableFiles)
    
    #Create seating arrangement spreadsheet
    outputToSpreadsheet(people, families)

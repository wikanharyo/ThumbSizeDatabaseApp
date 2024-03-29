import sqlite3
db = sqlite3.connect("ThumbSize.db")
# function to create a table
def CreateTable():
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists Data(Name str, ThumbLength float, ThumbDiameter float)")
    db.commit()

# function to record input data
def AddValue(Name,ThumbLength,ThumbDiameter):
    db.row_factory = sqlite3.Row
    db.execute("insert into Data(Name,ThumbLength,ThumbDiameter) values(?,?,?)", (Name,ThumbLength,ThumbDiameter))
    db.commit()

#function to print list from Data
def ListData():
    printdb= db.execute("select * from Data")
    for row in printdb:
        print("Name: {}, Thumb Length: {}, Thumb Diameter: {}".format(row["Name"],row["ThumbLength"],row["ThumbDiameter"]))

def main():
# main function
    CreateTable()
    inputdb = input("Do you want to add data? (yes/no):")
    while inputdb=="yes":
        Name = input("Enter name:")
        ThumbLength = float(input("Enter Thumb length (in cm):"))
        ThumbDiameter = float(input("Enter Thumb diameter (in cm):"))
        AddValue(Name,ThumbLength,ThumbDiameter)
        print("Data has been added")
        inputdb = input("Do you want to add data again? (yes/no):")
    print("Thankyou, your data has been recorded")
    ListData()
#call main function
if __name__ == '__main__': main()

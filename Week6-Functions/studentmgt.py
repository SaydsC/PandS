# student management programme
# (a) add new students
# (v) view students
# (q) Quit
# Type one letter (a/v/q):d

def displayMenu ():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):") .strip()
    return choice
def doAdd ():
    print ("in adding")
def doView ():
    print ("in viewing")
choice = displayMenu ()
while (choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()



def checkword(word:str,count:int,ch:str)->bool:
    n = 0
    for c in word:
        if(c == ch):
            n += 1
    return(count == n)

wordscollection = []
def insert():
    print("insert")
    word = input("Please enter word : ")
    wordscollection.append(word)

def search():
    print("search")  
    letter = input("Enter letter: ")
    ch = letter[0]
    number = int(input("Enter number: "))
    for w in wordscollection:
        if(checkword(w,number,ch)):
            print(w)

def listwords():
    print("listwords") 
    print("=====================")
    for w in wordscollection:
        print(w)
    print()


while (True):
    action = input("Please select Insert,Search,List,End: ").lower()
    match action:
        case "insert":
            insert()
        case "search":
            search()
        case "list":
            listwords()
        case "end":
            print("By by")
            exit()
        case _:
            print("Error action")

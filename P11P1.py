def list(mylist):
    n = int(input("Please enter the number of items on your list "))
    for n in range(0,n,1):
     s = int(input("Enter an integer "))
     mylist.append(s)
    return mylist 
def displaylist(mylist):
    for item in mylist:
        print(item)





#main
mylist = []#defining empty list
mylist = list(mylist)
displaylist(mylist)#display each item on list 
print(mylist)

#problem2
mylist.insert(0,99)
print(mylist)
#problem3
mylist[0]= 100
print(mylist)
#problem4
second_list = [500,600,700,800,900]
print(second_list)
mylist.extend(second_list)
print(mylist)
#problem5
mylist.remove(800)
print(mylist)
#problem6
del mylist [4]
print(mylist)
#problem7 
list_grades = ["A", "B", "C", "A", "A", "C"]
print(list_grades)
#problem8
list_count = list_grades.count("A")
print(list_count)
#problem9
list_b = list_grades.index("B")
print(list_b)
#problem10
list_f = list_grades.count("F")
if list_f == "F":
    print("F")
else:
    print("F is not on this list ")
#problem11
second_list.clear()
print(second_list)
#problem12
del second_list
#problem 13
list_players = ["Rizzo","Davis", "Baez", "Happ", "Bryan"]
#problem14
list_players.sort()
print(list_players)
#problem15
players_copy = ["Rizzo","Davis", "Baez", "Happ", "Bryan"]
print(players_copy)
#problem16
players_copy.reverse()
print(players_copy)

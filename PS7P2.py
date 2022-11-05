def totalavg(hits,bats):
    average = int(hits) / int(bats)
    
    
    
    return average


last_name  = input("please enter your last name ")
hits = int(input("please enter number of hits "))
bats = int(input("Please enter number of bats "))


average = totalavg(hits,bats)

print(last_name)
print("This is your averagabe batting ", average)
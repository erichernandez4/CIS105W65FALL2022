
totalint = 0 

response = input("Do you want to calculate interest (yes or no)")

while response == "yes":
    principle = float(input("amount to invest"))
    rate = float(input("please enter interest rate"))
    
    
    
    print( "year ", "beginning balance", "ending balance")
    for count in range (1,6,):
        intamt = principle * rate 
        totalint = totalint + intamt
        eb = principle +intamt
        print( count, " ", principle  , " ", eb  , "     ")
        principle  = eb


    response = input("Do you want to calculate interest (yes or no)")  
print ("total interest earned", totalint ) 

#Caitlin Farley, 4/10/19, Redo Suit cost loop- program calculates cost of 2 suits
#with cheaper half off with functions

anotherPurchase = ('y','Y','Yes','yes')
goAgain = 'y'
while goAgain in anotherPurchase:
    suitone = float(input("Enter price of first suit ")) #get input from user 
    suittwo = float(input("Enter price of second suit "))
#calculations of suits cost
    if suitone > suittwo:
        newprice = (suittwo/2)
        total = suitone + newprice
    else:
        newprice = (suitone/2)
        total = suittwo + newprice
    print('The cost is ${:.2f}'.format(total)) #output cost to user
    goAgain = input('Would you like to make another purchase? Press Y' )
    
    
    
 

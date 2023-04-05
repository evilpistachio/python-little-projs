#Caitlin Farley, 4/11/19- redo of suit cost program with half off discount
# with functions

#create loop so program can be repeated if user wants
anotherPurchase = ('y','Y','Yes','yes')
goAgain = 'y'
while goAgain in anotherPurchase:

    def main(): #define main function to call the other functions

   
    
    #get price of first suit
        suitOne = getFirst()

    #get price of second suit
        suitTwo = getSecond()

    #calculate total cost with discount
        total = calculateCost(suitOne, suitTwo)
    

    #output total to customer
        totalCost = finalCost(total)

    def getFirst():  #define function to get price of first suit
        suitOne = float(input("Enter price of first suit: "))
        return suitOne

    def getSecond(): #define function to get price of second suit
        suitTwo = float(input("Enter price of second suit: "))
        return suitTwo

    def calculateCost(suitOne, suitTwo): #define function to calculate total
        if suitOne > suitTwo:
            newprice = (suitTwo / 2)
            total = suitOne + newprice    #calculations for total
            return total
        else:
            newprice = (suitOne / 2)
            total = suitTwo + newprice
            return total

    def finalCost(total): 
        print('The cost is ${:.2f}'.format(total))

    main()
#give user option to repeat program
    goAgain = input('Would you like to make another purchase? Press Y ' )



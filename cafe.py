#Intiializing the menu
menu_list=['Burger','salad','desert','drinks']
#intializing  the Stocks in the cafe
stock_dict={'Burger' :8 ,
            'salad': 6,
            'desert' : 5,
            'drinks' : 12}
#intialising the prices of each item
price_dict={'Burger': 6.99,
            'salad' : 4.55,
            'desert' : 3,
            'drinks' : 2}
print('Each burger cost:',price_dict['Burger'])
print('Each salad cost:',price_dict['salad'])
print('Each desert cost:',price_dict['desert'])
print('Each drinks cost:',price_dict['drinks'])
# Total stock worth in the cafe
overallTotal = 0 
for i in menu_list:
    itemTotal = stock_dict.get(i) * price_dict.get(i)
    overallTotal = itemTotal + overallTotal
print('total stock worth in the cafe: ', overallTotal) #print the total stock
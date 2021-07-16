finished_sandwiches = []
sandwich_orders = ["Ruben","Grilled Cheese","Pastrami Rye","Egg Slut"]
doing_order = True

#printing out menu.
print("Heres out menu:")
for menu in sandwich_orders:
    print("\t\t" + menu)

#looping through users order.
while doing_order:
    order = str(input("\nWhat would you like to order: "))
    order = order.title()
#error handling for user input
    if ((order in sandwich_orders) and (order =='Pastrami Rye')):
        print("\nMaking your Pastrami on Rye sandwich")
        finished_sandwiches.append(order)
        
    elif order in sandwich_orders:
        print("\nMaking your",order,"sandwich")
        finished_sandwiches.append(order)
        
    else:
         order not in sandwich_orders
         print("Sorry we dont have that\n")
    
    repeat = input("\nAnything else (yes/no)")
    if repeat.lower() == "no":
        doing_order = False
    elif repeat.lower() == "n":
        doing_order = False
        
#Printing out users order
print ("Here's your")
for order in finished_sandwiches:
    print(order)


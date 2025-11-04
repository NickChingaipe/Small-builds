# shopping list

def shopping_list():
    items = []
    for i in range(3):
        item = input("enter item" + str(i +1) + ":")
        items.append(item)

    print("\nYour Shopping List")    
    for thing in items:
        print("-", thing)

shopping_list()        
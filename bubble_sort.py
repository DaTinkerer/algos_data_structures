def bubble_sort(elements, key):
    # store the size of the array 
    size = len(elements)
    # means for each index in the array, I want to run the sorting loop
    for k in range (size - 1):
    
        # for each index in the array, 
        for i in range(size - 1):
            # I want to see if it is greater than the very next index in the array
            if elements[i][key] > elements[i + 1][key]:
                 # if it is, store temporarily in tmp,
                tmp = elements[i]
                # then I swap the 2 indexes out putting the bigger one in front
                elements[i] = elements[i + 1]
                elements[i + 1] = tmp
    
# elements = [5, 8, 100, 500, 50, 434, 8, 20, 60, 25, 3, 1]

elements = [
    {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
    {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    {'name': 'amir', 'transaction_amount': 800, 'device': 'iphone-8'},
    {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
]

bubble_sort(elements,'name')
print(elements, 'name')    
def selectionSort (input):
    for i in range(0,len(input)):
        # Let first index be minimum
        min = i
        temp = input[i]

        for j in range(i+1,len(input)):
            if input[j] < input[min]:
                # update the minimum if current value is lower than minimum
                min = j


        input[i] = input[min]
        input[min] = temp
    return input
                

a = [99,1,34,54,234,67,32,5]
print(selectionSort(a))
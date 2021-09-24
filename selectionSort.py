def selectionSort (input):
    for i in range(0,len(input)):
        for j in range(i,len(input)):
            if input[i]> input[j] :
                tmp = input[i]
                input[i] = input[j]
                input[j] = tmp
    return input
                

a = [99,1,34,54,234,67,32,5]
print(selectionSort(a))
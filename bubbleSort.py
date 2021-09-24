def bubbleSort (input):
    for i in range(0,len(input)):
        for j in range(0,len(input)-1):
            if input[j]> input[j+1] :
                tmp = input[j]
                input[j] = input[j+1]
                input[j+1] = tmp
    return input
                

a = [99,1,34,54,234,67,32,5]
print(bubbleSort(a))
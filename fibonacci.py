def fibonacciByRecursion(index):
    '''
    Function will take index as input and 
    return the fibinacci number in series 
    '''
    fibValue=0
    index_first = 0
    index_second = 1
    if index < 2:
        return index
    else:
        return fibonacciByRecursion(index -1) + fibonacciByRecursion(index -2)
        

def fibonacciByIteration(index):
    fibValues=[0,1]
    for i in range(2,index+1):
        fibValues.append(fibValues[i-1]+fibValues[i-2])
    return fibValues[index]

print(fibonacciByRecursion(6))

print(fibonacciByIteration(4))
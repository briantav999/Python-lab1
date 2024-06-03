def reverseString(): 
    string = 'that man looked cool with the revolver and horse'
    # Initalize an empty string to hold the reversed string
    reverse = ''
    # For loop that starts at index 0 and travels the length of the string
    for c in range(0, len(string)):
        #len(string) gives me the length of the string and - (c+1) makes it so that im starting from the end of the string and counting towards the beginning
        reverse += string[len(string) - (c+1)]

    print(reverse)

# reverseString()

def getName():
    name = input('What is your name? ')
    print('hello ' + name )
    return name
    
getName()


def swap_em():
    a = 10
    b = 30

    temp = b
    b = a
    a = temp

    print('a is now ' + str(a) + ', and b is now ' + str(b))


def multiplyArr(arr):
    if len(arr) == 0:  # Check if the array is empty
        print(1)       # If it's empty, print 1 and return

    total = arr[0]     # Start with the first element of the array as the total

    for i in range(0, len(arr)):  # Iterate through each element in the array
        total = total * arr[i]     # Multiply the current total by the current element

    print(total)  # Print the final total



def fizzbuzzer(x):
    if (x % 3) == 0 and (x % 5) == 0:
        return 'fizzbuzz'
    elif (x % 3) == 0:
        return 'fizz'
    elif (x % 5) == 0:
        return 'buzz'
    else:
        return 'archer'



def fibonacci(n):
    if n == 0:
      return 0
    elif n == 1 or n == 2:
        return 1    
    
    return fibonacci(n - 1) + fibonacci(n - 2)


def searchArray(array, value):
    for index in array:
        if index == value:
            return True
        


def hasDupes(arr):
    obj = {}
    for num in arr:
        if num in obj.keys():
            return 'true'
        else:
            obj[num] = 1
    return 'false'
#Create a list of numbers
my_list = [2, 4, 3, 7, 9, 11, 88, 33, 34, 35, 36]

#Input element
x = input("Enter a number: ")
x = int(x);

#Function binary search
def binarySearch(my_list, l, h, x):
    if h>=l:
        m = (h+l)//2
        
        if my_list[m] == x:
            return m
        
        elif my_list[m] > x:
            return binarySearch(my_list, l, m-1, x)
        else:
            return binarySearch(my_list, m+1, h, x)
    else:
        return -1
    
r = binarySearch(my_list, 0, len(my_list) -1, x)

if r != -1:
    print("Number is present at index", str(r))
    
else:
    print("Number is not present in list")
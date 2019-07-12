pos = -1

def BinarySearch(lst,n):
    '''
    This is a Binary search program.
    :param lst:
    :param n:
    :return: Nothing
    '''
    l=0
    u=len(lst)-1

    while l <= u:
        mid = (l+u)//2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False

lst1 = [2,1,34,55,7,6,58,4,43,23]
lst = sorted(lst1)
print(lst)
n= 58

if BinarySearch(lst,n):
    print("Found at :",pos+1)
else:
    print("Not Found")

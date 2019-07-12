lst = [2,4,3,6,8,7,5]
print(lst)
n=int(input("Enter a serach value : "))
j=0
for i in lst:
    if i == n:
        print("Found at {}".format(j))
    j+=1



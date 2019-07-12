
# f1 = open('Create','w')
# f1.write("Hello Javed!!")


f = open('Image.PNG','rb')
f2 = open('MyPic.PNG','wb')
for i in f:
    f2.write(i)
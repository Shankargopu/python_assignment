data ="Welcome to "
fd=open("a.txt","w")
fd.write(data)
fd= open("a.txt","r+")
print(fd.read())
fd=open("a.txt","a+")
fd.write("Quantiphi")
fd=open("a.txt","r")
print(fd.read())

employeee_file = open("/home/ok/Projektz/__pycache__/Readingfiles/employees1.txt", "r")           #r- read, w- write, a - apend, r+ - read and write
print(employeee_file.readlines()[1])            #readline vytiskne prvni linku kdyz to dam znova vytiskne dalsi, readlines vytiskne vse, muzu si rict kolikatou chci
employeee_file = open("/home/ok/Projektz/__pycache__/Readingfiles/emloyees1.txt", "r") #on to precte jednou udela to co jsi mu rekne a konec proto je to dvakrat 
for line in employeee_file.readlines():
    print(line)    
#print(employeee_file.readline())
employeee_file.close()
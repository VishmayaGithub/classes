intro = input("Enter something : ")
characters = 0
words = 1
for value in intro :
    characters=characters+1
    if(value==' '):
        words = words+1

       
print("number of words : ",words)

print("Characters : ",characters)




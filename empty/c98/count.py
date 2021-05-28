
def location():
    count = 0
    getting = input("Enter file location : ")
    file=open(getting,"r") 
    

    for line in file:
        spitting = line.split()
        count = count+len(spitting)
        print(count)

        

    

location()
 
initialNumber = 1000;
def createAnswer(initialNumber):
    counter = 1
    initialNumber -= counter
    while(initialNumber>=0):
        #counter = 1;
        if(initialNumber%10 == 0):
            print(counter,initialNumber)
            counter += 1
        initialNumber -= counter

print("Done.")
createAnswer(1000);

import sys
from string import ascii_lowercase
def calculateVal():
    fileName = sys.argv[1]
    print("File Name entered is :",fileName)
    f = open(fileName);
    # print(type(f));
    dictionary = initializeDict()

    answer = 0
    for line in f:
        line =line.lower()
        for c in line:
            if(c in dictionary):
                answer += dictionary[c]
        print(line)
        print(answer)
    f.close();
 #   open()

def initializeDict():
    dictionary = {};
    counter = 1;
    feed = 1
    countedTen = False
    for c in ascii_lowercase:
        if(counter/10 == 1 and counter %10 == 0 and not countedTen):
            counter = 0
            feed = 10
            countedTen = True

        dictionary[c] = counter;
        counter += feed
    return dictionary


if __name__ == '__main__':
    calculateVal()
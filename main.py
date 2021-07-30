import os

def convert(string):
    list = []
    list[:0] = string
    return list


if __name__ == '__main__':
    word = "EVAPORATE"
    wordl = convert(word)
    hidwor = []
    for _ in wordl:
        hidwor.append("_")
    print(hidwor)
    gamecounter = 0
    while True:
        userin = input("Guess Your letter: ")
        os.system('clear')
        userin = userin.capitalize()
        count = 0
        good = False
        for i in wordl:
            if wordl[count] == userin:
                hidwor[count] = userin
                good = True
            count += 1
        if good == False:
            gamecounter += 1
            print("Wrong!!")
        if gamecounter == 6:
            print("Word: " + word + "\nYou lose!!")
            break
        print(hidwor)
        ## print(wordl)
        win = True
        count = 0
        for i in hidwor:
            if hidwor[count] == "_":
                win = False
            count += 1
        if win:
            print("Word: " + word + "\nYou win!!")
            break


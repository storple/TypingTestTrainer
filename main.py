from typingtest import TypingTest

def main():

    typingTest = TypingTest()
    while True:
        userInput = input("Press enter to start your test (-1 to exit): ")
        if userInput == "-1":
            exit()
        typingTest.startTest()

if __name__ == "__main__":
    main()
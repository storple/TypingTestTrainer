import time
import requests

def main():
    
    while True:
        userInput = input("Press enter to start your test (-1 to exit): ")
        
        if userInput == "-1":
            break
        
        countdown()

def calculateResults(quoteContent: str, quoteAuthor: str, timeElapsed: float, userContent: str) -> None:

    correctCharacters = 0
    wrongCharacters = 0

    quote = quoteContent.split(" ")
    userInput = userContent.split(" ")

    correctCharacters += min(quoteContent.count(" "), userContent.count(" ")) # include spaces to correct characters

    for (oWord, uWord) in zip(quote, userInput):
        if oWord == uWord:
            correctCharacters += len(oWord)
        else:
            for (ogChar, userChar) in zip(oWord, uWord):
                if ogChar != userChar:
                    wrongCharacters += 1


    wpm = "{:.2f}".format(correctCharacters/5 / (timeElapsed/60))
    rawWPM = "{:.2f}".format(len(userContent)/5 / (timeElapsed/60))
    accuracy = "{:.2f}%".format((correctCharacters / len(quoteContent)) * 100)

    displayResults(quoteAuthor, timeElapsed, wpm, rawWPM, accuracy, correctCharacters, wrongCharacters)

def displayResults(quoteAuthor: str, timeElapsed: float, wpm: str, rawWPM: str, accuracy: str, correctCharacters: int, wrongCharacters: int) -> None:
    print("\nFinished! Here are your results:")
    print("\nWPM: " + wpm)
    print("Accuracy: " + accuracy)
    print("Raw WPM: " + rawWPM)
    print("Time: {:.2f}s".format(timeElapsed))
    print("\nCorrect Characters: {}".format(correctCharacters))
    print("Incorrect Characters: {}".format(wrongCharacters))
    print("\nQuote by {}\n".format(quoteAuthor))

def generateRandomQuote() -> (str, str):

    quoteInfo = requests.get("https://api.quotable.io/quotes/random").json()[0]
    quote = quoteInfo["content"]
    author = quoteInfo["author"]
    
    return (quote, author)

def countdown() -> None:

    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("GO!\n")
    startTest()

def startTest() -> None:

    quoteContent, quoteAuthor = generateRandomQuote()

    timeStart = time.perf_counter()
    print("Type the following quote below:\n")
    print(quoteContent + "\n")
    userInput = input()
    timeElapsed = time.perf_counter() - timeStart
    
    calculateResults(quoteContent, quoteAuthor, timeElapsed, userInput)

main()
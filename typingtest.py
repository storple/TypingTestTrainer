import time
import requests

class TypingTest():
    def __init__(self):
        self.accuracy = 0.0
        self.correctCharacters = 0
        self.quoteAuthor = ""
        self.quoteContent = ""
        self.rawWPM = 0.0
        self.timeElapsed = 0.0
        self.userContent = ""
        self.wpm = 0.0
        self.wrongCharacters = 0

    def calculateResults(self) -> None:

        quote = self.quoteContent.split(" ")
        userInput = self.userContent.split(" ")

        self.correctCharacters += min(self.quoteContent.count(" "), self.userContent.count(" ")) # include spaces to correct characters

        for (oWord, uWord) in zip(quote, userInput):
            if oWord == uWord:
                self.correctCharacters += len(oWord)
            else:
                for (ogChar, userChar) in zip(oWord, uWord):
                    if ogChar != userChar:
                        self.wrongCharacters += 1

        
        self.wpm = "{:.2f}".format(self.correctCharacters/5 / (self.timeElapsed/60))
        self.rawWPM = "{:.2f}".format(len(self.userContent)/5 / (self.timeElapsed/60))
        self.accuracy = "{:.2f}%".format((self.correctCharacters / len(self.quoteContent)) * 100)

        print()
    
        self.displayResults()

    def displayResults(self) -> None:
        print("\nFinished! Here are your results:")
        print("\nWPM: " + self.wpm)
        print("Accuracy: " + self.accuracy)
        print("Raw WPM: " + self.rawWPM)
        print("Time: {:.2f}s".format(self.timeElapsed))
        print("\nCorrect Characters: {}".format(self.correctCharacters))
        print("Incorrect Characters: {}".format(self.wrongCharacters))
        print("\nQuote by {}\n".format(self.quoteAuthor))

    def generateRandomQuote(self) -> None:

        quoteInfo = requests.get("https://api.quotable.io/quotes/random").json()[0]
        self.quoteContent = quoteInfo["content"]
        self.quoteAuthor = quoteInfo["author"]

    def printIntro(self) -> None:
        print("Created by storple on GitHub (https://github.com/storple). Put your typing skills to the test!")
        
    def resetStats(self) -> None:
        self.accuracy = 0.0
        self.correctCharacters = 0
        self.quoteAuthor = ""
        self.quoteContent = ""
        self.rawWPM = 0.0
        self.timeElapsed = 0.0
        self.userContent = ""
        self.wpm = 0.0
        self.wrongCharacters = 0
        
    def startTest(self) -> None:
        
        self.resetStats()

        print("3")
        time.sleep(0.5)
        print("2")
        time.sleep(0.5)
        print("1")
        time.sleep(0.5)
        print("GO!\n")

        self.generateRandomQuote()

        timeStart = time.perf_counter()
        print("Type the following quote below:\n")
        print(self.quoteContent + "\n")
        self.userContent = input()
        self.timeElapsed = time.perf_counter() - timeStart
        
        self.calculateResults()

import datetime
import time

def printTimeTaken(function):
    def runFunction(*args, **kwargs):
        startTime = datetime.datetime.now()
        ans = function(*args, **kwargs)
        endTime = datetime.datetime.now()
        print("Time taken by function is ", endTime-startTime)
        return ans
    return runFunction

@printTimeTaken
def randomFunction(firstName, lastName):
    print("function started")
    # time.sleep(5)
    print("my first name is ", firstName, "my last name is ", lastName)
    print("function finished")
    return "function executed"

print(randomFunction("Jatin", "Goyal"))


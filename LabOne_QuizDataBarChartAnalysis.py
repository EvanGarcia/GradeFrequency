'''
Evan Garcia
Professor Tindall
CSC 4800
January 10, 2017

This program prompts the user to enter in a quiz score data file, and then reads in the scores and their frequencies.
It outputs the smallest score, the largest score and the largest frequency, and a score-frequency bar chart and a frequency-score bar chart.

'''


def readFile(filename): 

    #This function reads the data file (passed in as filename), prints out the file's contents to the console,
    #places the contents of the file into a dictionary (ScoresAndFrequencies, where the score is the key, and the frequency is the value),
    #adds any repeated keys' values together, and returns ScoresAndFrequencies

    quizScores = open(filename, "r")
    readData = quizScores.readlines()
    ScoresAndFrequencies = {}
   
    #Prints Scores and Frequencies
    for i in range(len(readData)):
        print(readData[i].strip('\n')) 

    #Places file contents into dictionary, and removes duplicate keys but adds their values together
    for line in readData:
        key, val = line.split()
        if key not in ScoresAndFrequencies:
            ScoresAndFrequencies[key] = int(val)
        else:
            ScoresAndFrequencies[key] += int(val)

    quizScores.close()
    
    return ScoresAndFrequencies

       
def findLowestScore(ScoreData):
    
    #This function calculates the lowest score in the data set (ScoreData: A list of the scores from the data file),
    #it returns this score back to the call as lowestScore.

    #Calculates lowest score in data set
    lowestScore = min(val for val in ScoreData)
    print("\nThe smallest score value is {} \n".format(lowestScore))

    return lowestScore

def findHighestScore(ScoreData):

    #This function calculates the highest score in the data set (ScoreData: A list of the scores from the data file),
    #it returns this score back to the call as highestScore.

    #Calculates highest score in data set
    highestScore = max(val for val in ScoreData)
    print("The largest score value is {} \n".format(highestScore))

    return highestScore

def findLargestFrequency(FrequencyData):

    #This function calculates the highest frequency in the data set (FrequencyData: A list of the frequencies from the data file),
    #it returns this score back to the call as highestFrequency.

    #Calculates highest frequency in data set
    highestFrequency = max(val for val in FrequencyData)
    print("The largest frequency count is {} \n".format(highestFrequency))

    return highestFrequency

def fillClassScoresList(ClassScoresList, Scores, ClassDict):

    #This function fills ClassScoresList (A list with 51 elements, one for each possible score) with the scores
    #from ClassDict (The dictionary containing the key value pair of scores:frequency), and returns ClassScoresList once its filled.

    #Fills list with frequencies
    for x, val in enumerate(Scores):
        tempKey = str(val)
        ClassScoresList[val] = ClassDict.get(tempKey)

    return ClassScoresList

def printScoreFrequencyBarChart(ScoreFrequency, lowestScore, highestScore):

    #This function prints the "Score : Frequency Bar Chart". It takes in the ScoreFrequency list that contains
    #the frequencies of the quiz scores, as well as the lowest and highest scores to determine the range of
    #scores we should print out. 

    #Prints scores, frequencies, and as many *s as the frequency value states
    for x in range(lowestScore, highestScore + 1):
        print ("{}:  {:2}  ".format(x, ScoreFrequency[x]) ,"*"*ScoreFrequency[x])
    print("\n\n\n")


def printFrequencyScoreBarChart(ScoreFrequency, lowestScore, highestScore, highestFrequency):

    #This function prints the "Frequency : Score Bar Chart". It takes in the ScoreFrequency list that contains
    #the frequencies of the quiz scores, as well as the lowest and highest scores to determine the range of
    #scores we should print out, it also takes in the highest frequency so we can determine what range of frequencies
    #we should print out.

    #Prints frequency range
    for i in range(highestFrequency, 0, -1):
        if ScoreFrequency[i] < 10:
            print("\n       {:2}:  ".format(i), end = " ")
        
        if ScoreFrequency[i] > 9:
             print("\n       {}:  ".format(i), end = " ")
        currentFrequency = i
        
        #Prints as many *s as the frequency value states
        for x in range(lowestScore, highestScore + 1):
            if ScoreFrequency[x] >= currentFrequency:
                print(" *", end = " ")
            else:
                print("  ", end = " ")
        

    #Formating for the chart
    print("\n---------: " , "--^" * (highestScore + 1 -lowestScore))
    
    #Prints the quiz scores according to their range
    for x in range(lowestScore, highestScore + 1):
        if x == lowestScore:
            print("    Score:  ", end = " ")
        if x >= lowestScore:
            print("{}".format(x), end = " ")  
        

def main():
    
    #Calls the functions listed above to achieve the desired result

    print("Welcome to the Quiz Score Frequency Analyzer, written by Evan Garcia")
    print("Please Enter a Valid Data Filename: ")
    filename = input()
    #filename = "QuizscoresAndFrequency.txt"
    print("Reading Data File: '{}' ".format(filename))
    print("Input:\n")
    fileData =  readFile(filename)
    Scores = list(map(int,fileData.keys()))
    Frequencies = list(fileData.values())
    lowestscore = findLowestScore(Scores)
    highestscore = findHighestScore(Scores)
    highestFrequency = findLargestFrequency(Frequencies)
    print("---Input Data---\n")
    print("Score: Frequency Bar Chart\n")
    ScoreFrequency = [0] * 51 
    ScoreFrequency = fillClassScoresList(ScoreFrequency, Scores, fileData)
    printScoreFrequencyBarChart(ScoreFrequency, lowestscore, highestscore)
    print("Frequency: Score Bar Chart\n")
    printFrequencyScoreBarChart(ScoreFrequency, lowestscore, highestscore, highestFrequency)
    print("\n")


if __name__ == "__main__":
    main()
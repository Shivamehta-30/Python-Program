AGE = "Age"
WORKCLASS = "Work-class"
EDUCATIONNUM = "Education-num"
MARITAL = "Marital-status"
OCCUPATION = "Occupation"
RELATIONSHIP = "Relationship"
RACE = "Race"
SEX = "Sex"
CAPITALGAIN = "Capital-gain"
CAPITALLOSS = "Capital-loss"
HOURS = "Hours-per-week"
CLASS = "Class"
PREDICTED = "Predicted Class"
def makeTrainingSet(filename):
    trainingSet = []

    fin = open(filename, 'r')
    for line in fin:
        line = line.strip()
        line_list = line.split(',')
        record = {}
        record[AGE] = float(line_list[0])
        record[WORKCLASS] = line_list[1]
        record[EDUCATIONNUM] = float(line_list[4])
        record[MARITAL] = line_list[5]
        record[OCCUPATION] = line_list[6]
        record[RELATIONSHIP] = line_list[7]
        record[RACE] = line_list[8]
        record[SEX] = line_list[9]
        record[CAPITALGAIN] = float(line_list[10])
        record[CAPITALLOSS] = float(line_list[11])
        record[HOURS] = float(line_list[12])
        record[CLASS] = line_list[14]

        trainingSet.append(record)

    fin.close()
    return trainingSet
def trainClassifier(trainingSet):
    pass

def makeTestSet(filename):

    testset = makeTrainingSet(filename)

    for record in testset:
        record[PREDICTED] = 'unknown'

    return testset

def main():
    # TODO
    print("Reading in training data...")
    trainingSet = []
    trainingFile = "annual-income-training.data"
    trainingSet = makeTrainingSet(trainingFile)
    print("Done reading training data.\n")
    print("Training classifier...")
    print( "Done training classifier.\n")
    print("Reading in test data...")
    testFile = "annual-income-test.data"
    testSet = makeTestSet(testFile)
    print("Done reading test data.\n")
    print("Classifying records...")
    print ("Done classifying.\n")
    print("Program finished.")



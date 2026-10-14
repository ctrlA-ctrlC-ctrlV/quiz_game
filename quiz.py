# Project plan
# 1. read in "quiz_questions"
# 2. convert data in to a list
# 3. [mvp]
#   - terminal ask user random question from list
#   - terminal get user input (must be a, b, c, d, and not case sensitive)
#   - terminal compare user input with anser
#   - terminal if correct print correct_message, if wrong pring wrong message
import csv      # for file read
import random   # for random number generation

# read data in file and convert to list using csv library (csv.DictReader())
def csv_reader(file_name:str) -> list:  # take in string, return list
    try:
        with open(file_name, 'r', newline='') as file:  # open "file_name"
            loaded_list = list(csv.DictReader(file))    # read and covert
            return(loaded_list)                         # return list

    except FileNotFoundError:
        print("Error: File not found")                  # warn if file not found

# generate random number from between 
def rng_generator(start_from:int=0, end_to:int=0) -> int: # take in two int to generate a 
                                                          # number in between
    try:
        if end_to <= start_from:    # if start_from is less or equal to end_to the 
                                    # random function will fail
            raise ValueError(f"Error: end_to({end_to}) cannot be less or the same with start_from({start_from})")
        return random.randint(start_from, end_to)   # return the random number from the range
    except ValueError as e:
        print(str(e))   # print error message  

# return a random item from the input array
# function depends on rng_generator()
def get_random_list_item(aList:list=[]):    # take in a list but return an any type since
                                            # what's in the array is unknown
    n:int = rng_generator(start_from=0, end_to=len(aList))  # use rng_generator() to get a 
                                                            # random int 'n' within size of list
    random_item = aList[n]  # get the n item from list
    return(random_item)     # return the n item

def main():
    # quiz question location
    file_location = './quiz_questions.csv'

    # read in question list and convert to list
    question_list = csv_reader(file_location)

    # get a random question from list
    random_question = get_random_list_item(question_list)
    print(random_question)
    #print(question_list)
    
    # num = rng_generator(start_from=0, end_to=len(question_list))
    # print(rng_generator(20,19))
    # print(f"A random number from 0 to {len(question_list)} is {num}")

if __name__ == "__main__":
    main()

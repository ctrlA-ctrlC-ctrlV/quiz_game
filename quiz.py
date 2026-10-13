# Project plan
# 1. read in "quiz_questions"
# 2. convert data in to a list
# 3. [mvp]
#   - terminal ask user random question from list
#   - terminal get user input (must be a, b, c, d, and not case sensitive)
#   - terminal compare user input with anser
#   - terminal if correct print correct_message, if wrong pring wrong message
import csv

# read data in file and convert to list using csv library (csv.DictReader())
def csv_reader(file_name:str) -> list:
    try:
        with open(file_name, 'r', newline='') as file:  # open "file_name"
            loaded_list = list(csv.DictReader(file))    # read and covert
            return(loaded_list)                         # return list

    except FileNotFoundError:
        print("Error: File not found")                  # warn if file not found

def main():
    file_name = 'quiz_questions.csv'

    question_list = csv_reader('./'+file_name)
    print("Hello, World!")
    print(question_list)

if __name__ == "__main__":
    main()

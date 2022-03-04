"""
Assignment: Dictionary Update Assignment
Program: main.py
Author: Colby Boell
Last date modified: 03/04/2022

The purpose of this program is to that prompts a user for test score inputs and stores
them in a dictionary (first function) and then uses a second function to return the average
test scores.
"""


# function that gets user input for scores
def get_test_scores():
    # dictionary
    scores_dict = dict()
    # while true loop
    while True:
        # try statement to get proper input
        try:
            num_scores = int(input('Enter the number of scores you would like to input (must be at least 1): '))
            if num_scores > 0:
                break
        except ValueError:
            print('Invalid, entry must be a number')
    # for loop to enter scores to be stored in dictionary
    for i in range(num_scores):
        while True:
            try:
                score = int(input('Enter the score:'))
                score_key = f'Score {i + 1}'
                entry = {score_key: score}
                scores_dict.update(entry)
                break
            except ValueError:
                print('Invalid, enter valid number')
    # returns the dictionary
    return scores_dict


# function to calculate average score
def average_scores(scores_dictionary):
    # use length of dictionary to get count
    scores_count = len(scores_dictionary)
    the_sum = 0
    # for loop to add each number to the sum
    for value in scores_dictionary.values():
        the_sum = the_sum + value
    # math to get average
    average = the_sum / scores_count
    # return average
    return average


# main where we call our functions
if __name__ == '__main__':
    the_scores = get_test_scores()
    print('Average score: ', average_scores(the_scores))

"""
Tests
1.)
Enter the number of scores you would like to input (must be at least 1): 0
Enter the number of scores you would like to input (must be at least 1): 2
Enter the score:12
Enter the score:r
Invalid, enter valid number
Enter the score:34
Average score:  23.0
2.)
Enter the number of scores you would like to input (must be at least 1): 3
Enter the score:13
Enter the score:46
Enter the score:77
Average score:  45.333333333333336
"""

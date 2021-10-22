#!usr/bin/env python3
import json
import sys
import os

INPUT_FILE = 'testdata.json' # Constant variables are usually in ALL CAPS

class User:
    def __init__(self, name, gender, preferences, grad_year, responses):
        self.name = name
        self.gender = gender
        self.preferences = preferences
        self.grad_year = grad_year
        self.responses = responses


# Takes in two user objects and outputs a float denoting compatibility
def compute_score(user1, user2):
    #first check gender compatibility
    if user1.preferences[0] != user2.gender:
        return 0
    if user2.preferences[0] != user1.gender:
        return 0
        
    # Add points for responses: 20 questions, each question is worth 5 points
    # Determine how many of their answers are the same
    numbersame = 0
    length = len(user1.responses)
    for i in range(0,length):
        if user1.responses[i] == user2.responses[i]:
            numbersame += 1

    # Assign a score for compability based on similarity of numbers
    # This creates a score out of 1 (20 questions * 5 = 100 points)
    if numbersame <= 15:
        score = (numbersame * 5) / 100
    # If they're 3/4 similar, maybe too similar, so lower score by 10%.
    else:
        score = numbersame * .9

    # Account for graduation year--lower score the greater the difference in years.
    difference = user1.grad_year - user2.grad_year
    if difference == 1:
        score *= .9
    elif difference == 2:
        score *= .8
    elif difference == 3:
        score *= .7

    score = round(score, 2)

    # Normalize so outputs are between .5 and 1
    score *= 2



    stringscore = f"{round(score*100)}%"
    # Returns compability value
    return stringscore

    # More information I don't have from this data that I would want to take into account:
    # If some questions should be weighted more heavily than others
    # If your answers are relevant, not just if you answered the same vs different -- ex if someone who answers A is more compatible with answer "D" than "C"
    # How to judge how similar is too similar, how different is too different

    # We could get input from people on (add to preferences or evaluate from answers):
    # Are there questions that matter more to you?
    # Do you have a preference in terms of grad year? (older vs younger? same year?)
    # Preference for how similar/different someone is to you?
    


if __name__ == '__main__':
    # Make sure input file is valid
    if not os.path.exists(INPUT_FILE):
        print('Input file not found')
        sys.exit(0)

    users = []
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
        for user_obj in data['users']:
            new_user = User(user_obj['name'], user_obj['gender'],
                            user_obj['preferences'], user_obj['gradYear'],
                            user_obj['responses'])
            users.append(new_user)

    for i in range(len(users)-1):
        for j in range(i+1, len(users)):
            user1 = users[i]
            user2 = users[j]
            score = compute_score(user1, user2)
            print('Compatibility between {} and {}: {}'.format(user1.name, user2.name, score))

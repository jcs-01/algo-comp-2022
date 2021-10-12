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
    if user1.preferences[0] != user2.gender
        return 0
    if user2.preferences[0] != user1.gender
        return 0
    
    #account for grad year compatibility--lower points the farther apart their grad years are
    
    #add points for responses: 20 questions, each question is worth 5 points (5 possible answers, depending on compatibility) -- total possible 100 points
    #then account for grad year compatibility by multiplying by a decimal: 1 if they're the same year, then smaller numbers as they get father apart. 
    #scores are out of 100. Or at this point, if we want them out of a smaller number, possible to normalize.
    
    #need to know if different questions should be weighted more heavily
    #need to know if someone who answers A is more compatible with someone who answers C, or only people who answer A/A are compatible
    #probably people who give all the same answers are also not the most compatible, it's too similar
    
    #things I would want to add to preferences:
    #if there were questions that are more imp to you
    #if you want to be matched with M or F
    #if you have a preference for older or younger
    #preference for someone different/similar to you
    
    
    # YOUR CODE HERE
    return 0


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

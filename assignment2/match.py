import numpy as np
from typing import List, Tuple
import math

def run_matching(scores: List[List], gender_id: List, gender_pref: List) -> List[Tuple]:
    """
    TODO: Implement Gale-Shapley stable matching!
    :param scores: raw N x N matrix of compatibility scores. Use this to derive a preference rankings.
    :param gender_id: list of N gender identities (Male, Female, Non-binary) corresponding to each user
    :param gender_pref: list of N gender preferences (Men, Women, Bisexual) corresponding to each user
    :return: `matches`, a List of (Proposer, Acceptor) Tuples representing monogamous matches

    Some Guiding Questions/Hints:
        - This is not the standard Men proposing & Women receiving scheme Gale-Shapley is introduced as
        - Instead, to account for various gender identity/preference combinations, it would be better to choose a random half of users to act as "Men" (proposers) and the other half as "Women" (receivers)
            - From there, you can construct your two preferences lists (as seen in the canonical Gale-Shapley algorithm; one for each half of users
        - Before doing so, it is worth addressing incompatible gender identity/preference combinations (e.g. gay men should not be matched with straight men).
            - One easy way of doing this is setting the scores of such combinations to be 0
            - Think carefully of all the various (Proposer-Preference:Receiver-Gender) combinations and whether they make sense as a match
        - How will you keep track of the Proposers who get "freed" up from matches?
        - We know that Receivers never become unmatched in the algorithm.
            - What data structure can you use to take advantage of this fact when forming your matches?
        - This is by no means an exhaustive list, feel free to reach out to us for more help!
    """

    matches = []

    length = len(gender_id)
    # say it's 4 long, we get 2 --> range will go 0, 1
    # say it's 5 long, we get 3 --> range will go 0, 1, 2
    half = math.ceil(length/2)
    halffl = math.floor(length/2)

    while(len(matches) < halffl):

        # change to half and do half each way
        for i in range(0, half):
            print("i ", i)
            # Does this list need to be universal?
            proposed = ["f"] * length
            proposergender = gender_id[i]
            proposergenderpref = gender_pref[i]
            # Propose to first index hasn't proposed to

            for j in range(0, length):
                print("j ", j)
                proposeto = scores[i][j]
                proposedgender = gender_id[j]
                proposedgenderpref = gender_pref[j]
                print("proposeRgender ", proposergender, "proposeRgenderpref ", proposergenderpref)
                print("proposeDgender ", proposedgender, "proposeDgenderpref ", proposedgenderpref)

                # Assumed nonbinary could match with either, but not actually sure that's a fair assumption to make?
                gendict = {"Female": ["Women"], "Male": ["Men"], "Nonbinary": ["Men", "Women"]}

                if matches != None:
                    a = []
                    b = []
                    for (x,y) in enumerate(matches):
                        if x == i:
                            a.append(x)
                        if y == i:
                            b.append(y)
                    print("a ", a)
                    print("b ", b)
                    #print ("x, y ", x, ",", y)

                    #b = [y for x,y in enumerate(matches) if x == i]
                    #print("b ", b)

                    if a != None:
                        print("matches ", matches)
                        print("break ")

                        break
                    if b != None:
                        print("matches ", matches)


                if i == j:
                    # can't match
                    # i = incompatible
                    print("incomp i = j")
                    proposed[j] = "i"

                elif proposergenderpref not in gendict[proposedgender][0]:
                    # can't match
                    print("incomp1")
                    proposed[j] = "i"

                elif proposedgenderpref not in gendict[proposergender][0]:
                    # can't match
                    proposed[j] = "i"
                    print("incomp2")


                elif proposed[j] == "f":
                    # Propose to first person he/she/they hasn't proposed to--they're both free
                    # Match them!
                    print("match")
                    matches.append([i, j])
                    print("appended")

                else:
                    if matches != None:
                        b = []
                        for (x,y) in enumerate(matches):
                            if y == i:
                                xprop = x
                                yreci = y
                                b.append([x,y])
                    # check if j prefers i even though j is already matched
                    # syntax: https://stackoverflow.com/questions/946860/using-pythons-list-index-method-on-a-list-of-tuples-or-objects


                    # get j & match compability score
                    oldscore = scores[x][y]
                    # get j & i compability score
                    ijscore = scores[i][j]
                    # compare them

                    if ijscore > oldscore:
                        # remove old match from matches
                        matches.remove((x,y))

                        # add i, j to matches
                        matches.append(i, j)
                    else:
                        proposed[j] = "t"


        for i in range(half, length):
            print("i ", i)
            # Does this list need to be universal?
            proposed = ["f"] * length
            proposergender = gender_id[i]
            proposergenderpref = gender_pref[i]
            # Propose to first index hasn't proposed to

            for j in range(0, length):
                print("j ", j)
                proposeto = scores[i][j]
                proposedgender = gender_id[j]
                proposedgenderpref = gender_pref[j]
                print("proposeRgender ", proposergender, "proposeRgenderpref ", proposergenderpref)
                print("proposeDgender ", proposedgender, "proposeDgenderpref ", proposedgenderpref)

                # Assumed nonbinary could match with either, but not actually sure that's a fair assumption to make?
                gendict = {"Female": ["Women"], "Male": ["Men"], "Nonbinary": ["Men", "Women"]}

                if matches != None:
                    a = []
                    b = []
                    for (x,y) in enumerate(matches):
                        if x == i:
                            a.append(x)
                        if y == i:
                            b.append(y)
                    print("a ", a)
                    print("b ", b)
                    #print ("x, y ", x, ",", y)

                    #b = [y for x,y in enumerate(matches) if x == i]
                    #print("b ", b)

                    if a != None:
                        print("matches ", matches)
                        print("break ")

                        break
                    if b != None:
                        print("matches ", matches)


                if i == j:
                    # can't match
                    # i = incompatible
                    print("incomp i = j")
                    proposed[j] = "i"

                elif proposergenderpref not in gendict[proposedgender][0]:
                    # can't match
                    print("incomp1")
                    proposed[j] = "i"

                elif proposedgenderpref not in gendict[proposergender][0]:
                    # can't match
                    proposed[j] = "i"
                    print("incomp2")


                elif proposed[j] == "f":
                    # Propose to first person he/she/they hasn't proposed to--they're both free
                    # Match them!
                    print("match")
                    matches.append([i, j])
                    print("appended")

                else:
                    if matches != None:
                        b = []
                        for (x,y) in enumerate(matches):
                            if y == i:
                                xprop = x
                                yreci = y
                                b.append([x,y])
                    # check if j prefers i even though j is already matched
                    # syntax: https://stackoverflow.com/questions/946860/using-pythons-list-index-method-on-a-list-of-tuples-or-objects


                    # get j & match compability score
                    oldscore = scores[x][y]
                    # get j & i compability score
                    ijscore = scores[i][j]
                    # compare them

                    if ijscore > oldscore:
                        # remove old match from matches
                        matches.remove((x,y))

                        # add i, j to matches
                        matches.append(i, j)
                    else:
                        proposed[j] = "t"

        print("matches ", matches)



    
    return matches

# Loads all genders into the file, then calls the matching function above
if __name__ == "__main__":
    raw_scores = np.loadtxt('raw_scores.txt').tolist()
    genders = []
    with open('genders.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            genders.append(curr)

    gender_preferences = []
    with open('gender_preferences.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            gender_preferences.append(curr)

    gs_matches = run_matching(raw_scores, genders, gender_preferences)

# Sources:
# https://www.programiz.com/python-programming/methods/list/remove
# https://www.codegrepper.com/code-examples/python/for+x%2C+y+in+enumerate%28lst%29
# https://www.tutorialspoint.com/python/python_dictionary.htm
# https://stackoverflow.com/questions/946860/using-pythons-list-index-method-on-a-list-of-tuples-or-objects
# https://www.programiz.com/python-programming/methods/list/index
# https://stackoverflow.com/questions/8528178/list-of-zeros-in-python

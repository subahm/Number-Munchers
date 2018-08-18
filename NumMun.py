import random, pygame, sys
from pygame.locals import *

# set constants
questionsList = ['Find all multiples of', 'Find all even numbers', 'Find all odd numbers', 'Find all prime numbers']
#8x8 = 64 boxes
# assertions

# set up major colors

# set up font

'''def main():


def blankField():


def placeNumbers(field):'''


def questionAndOptions():
    ''' Gets a random question from the list
        Adds a random number to the question if necessary
        Generates options accordingly
    '''
    randomQuestion = randomGenerator(0, 3, 1)
    question = questionsList[randomQuestion]
    #question = questionsList[0]
    all_options = 0
    correct_options = 0
    list_random = []
    #Case for first queston
    if question == 'Find all multiples of':
        number = randomGenerator(2, 9, 1)
        print(question + " " + str(number))
        while all_options < 64:
            list_random = randomGenerator(2, 99, 64)
            for x in list_random:
                if x % number == 0:
                    correct_options = correct_options + 1
                if correct_options == 4:
                    break
            if correct_options < 4:
                list_length = len(list_random)
                difference_in_number = 4 - correct_options
                for i in range(difference_in_number):
                    random_cell = randomGenerator(0, 63, 1)
                    if list_random[random_cell] % number != 0:
                        list_random[random_cell] = number * randomGenerator(2, 9, 1)
                    else:
                        list_random[random_cell+1] = number * randomGenerator(2, 9, 1)
            random.shuffle(list_random)
            all_options = len(list_random)
        return list_random
    #Case for second queston
    elif question == 'Find all even numbers':
        print(question)
        list_random = randomGenerator(2, 99, 64)
        random.shuffle(list_random)
        all_options = len(list_random)
        return list_random
    #Case for third queston
    elif question == 'Find all odd numbers':
        print(question)
        list_random = randomGenerator(2, 99, 64)
        random.shuffle(list_random)
        all_options = len(list_random)
        return list_random
    #Case for fourth queston
    else:
        print(question)
        list_random = randomGenerator(2, 99, 64)
        random.shuffle(list_random)
        all_options = len(list_random)
        return list_random

def main ():
    list_random2 = questionAndOptions()
    count = 0;
    for y in range(len(list_random2)):
        print list_random2[y]

def randomGenerator(lower, upper, times):
    ''' Generates random number between the limits provided includeing lower and upper.
        It generates number of random numbers equal to times
        Returns a list of random numbers
    '''
    if times > 1:
        randomNumList = [random.randint(lower, upper) for x in range(times)]
        return randomNumList
    else:
        randomNum = random.randint(lower, upper)
        return randomNum

# run code
if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""
Check readme.md for instructions
"""


def is_prime(num):
    """ A helper function that returns true if `num` is prime """
    if num in [None, 0, 1]:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


players_score = {'Maria': 0, 'Ben': 0}


def isWinner(x, nums):
    """ The function """
    if x is None or nums is None or x > len(nums):
        return None
    curr_player = None  # Maria starts the game always
    for i in range(x):
        n = nums[i]
        temp = list(range(1, n + 1))
        for item in temp.copy():
            if temp == [1]:
                if curr_player is None:
                    players_score['Ben'] += 1
                    # >print("{} won this round!\n".format('Ben'))
                else:  # This else block should never run (no matter what)
                    print('-- This code block should not run at all --')
                    curr_player = \
                        'Maria' if curr_player in [None, 'Ben'] else 'Ben'
                    players_score[curr_player] += 1
                    # >print("{} won this round!\n".format(curr_player))
                break

            if is_prime(item):
                curr_player = \
                    'Maria' if curr_player in [None, 'Ben'] else 'Ben'
                # remove multiples of `item` from the list
                temp = list(filter(lambda x: (x % item) != 0, temp))
                # >print("{} removed {}... ==== {}".format(curr_player, item, \
                # temp))
                if temp == [1]:
                    players_score[curr_player] += 1
                    # >print("{} won this round!\n".format(curr_player))
                    curr_player = None
                    break
                continue
    # >print("Maria = {}, Ben = {}".format(players_score['Maria'], \
    # players_score['Ben']))
    if players_score['Maria'] > players_score['Ben']:
        return 'Maria'
    else:
        return 'Ben'

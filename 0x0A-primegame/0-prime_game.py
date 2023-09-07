#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers starting
from `1` up to and including `n`, they take turns choosing a prime number from
the set and removing that number and its multiples from the set. The player
that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round.
Assuming Maria always goes first and both players play optimally, determine who
the winner of each game is.

- Prototype: `def isWinner(x, nums)`
- where `x` is the number of rounds and `nums` is an array of `n`
- Return: name of the player that won the most rounds
- If the winner cannot be determined, return `None`
- You can assume `n` and `x` will not be larger than `10000`
- You cannot import any packages in this task

Example:
x = 3, nums = [4, 5, 1]

First round: 4
- Maria picks 2 and removes 2, 4, leaving 1, 3
- Ben picks 3 and removes 3, leaving 1
- Ben wins because there are no prime numbers left for Maria to choose

Second round: 5
- Maria picks 2 and removes 2, 4, leaving 1, 3, 5
- Ben picks 3 and removes 3, leaving 1, 5
- Maria picks 5 and removes 5, leaving 1
- Maria wins because there are no prime numbers left for Ben to choose

Third round: 1
- Ben wins because there are no prime numbers for Maria to choose

Result: Ben has the most wins
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
                    players_score['Maria'] += 1
                    # >print("{} won this round!\n".format('Maria'))
                else:
                    curr_player = \
                        'Maria' if curr_player in [None, 'Ben'] else 'Ben'
                    players_score[curr_player] += 1
                    # >print("{} won this round!\n".format(curr_player))
                break

            if is_prime(item):
                curr_player = 'Maria' if curr_player in [None, 'Ben'] else \
                    'Ben'
                # remove multiples of `item` from the list
                temp = list(filter(lambda x: (x % item) != 0, temp))
                # >print("{} removed {}... ==== {}".format(curr_player, item,
                # \temp))
                if temp == [1]:
                    players_score[curr_player] += 1
                    # >print("{} won this round!\n".format(curr_player))
                    break
                continue
    # >print("Maria = {}, Ben = {}".format(players_score['Maria'],
    # \players_score['Ben']))
    if players_score['Maria'] > players_score['Ben']:
        return 'Maria'
    else:
        return 'Ben'

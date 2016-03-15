# -*- coding: utf-8 -*-

# 猜数字游戏：预先确定4个数字，每猜一次记录数字和位置都正确的个数，以及数字正确位置错误的个数，如2A2B
# 确定正确猜出4个数字以及位置所的最优步骤


# Game （数字不重复）

import random as rd


def check(guess, answer):
    A = 0
    B = 0
    gue = []
    ans = answer[:]
    for digit in guess:
        gue.append(int(digit))

    for digit in gue:
        if(digit in ans):
            B += 1
            if(gue.index(digit) == ans.index(digit)):
                A += 1
            ans[ans.index(digit)] = -1

    return [A, B - A]


def Number_guess_game(digits):
    N = rd.sample(range(0, 10), digits)
    print "Game start. A %d digits number is generated." % digits
    print "Please make a guess."
    guess = raw_input()
    res = check(guess, N)
    attempt = 1
    while(res[0] != digits):
        print 'Try %d: ' % attempt, res[0], 'A', res[1], 'B'
        print "Please make another guess"
        guess = raw_input()
        res = check(guess, N)
        attempt += 1
    print "Correct! Game is over."

Number_guess_game(4)


# Solution

N = '9753'


def Solve_game(answer):
    ans = []
    for digit in answer:
        ans.append(int(digit))
    print(ans)

    def method1():
        pass

# Solve_game(N)

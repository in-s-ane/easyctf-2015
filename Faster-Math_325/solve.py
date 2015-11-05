#!/usr/bin/env python
import socket
import time
import math
import itertools

def lesser_root(a,b,c):
    return (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

def greater_root(a,b,c):
    return (-b + math.sqrt(b**2 - 4*a*c))/(2*a)

def fill_operators(prompt):
    operators = "+-*"
    expr = prompt[prompt.find(":")+1:prompt.find("=")]
    ans = prompt[prompt.find("=")+1:]
    expr = expr.replace("_", "%s")
    for possibility in itertools.product(operators, repeat=3):
        if str(eval(expr % (possibility[0], possibility[1], possibility[2]))) == ans.strip():
            return "".join(possibility).replace("*", "x")

#rosetta code
def make_change(amt, S):
    ways = [0]*(amt+1)
    ways[0] = 1
    for coin in S:
        for j in xrange(coin, amt+1):
            ways[j] += ways[j-coin]
    return ways[amt]

HOST = 'programming.easyctf.com'
PORT = 10300

def answer(s=None):
    if not s:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST,PORT))
    time.sleep(0.5)
    prob = s.recv(1024)
    print prob
    if "flag" in prob or "{" in prob:
        print prob
    if "seconds" in prob:
        print prob.split("seconds")[0].split()[-1]
    if "Sorry, incorrect" in prob:
        print prob
        s.close()
        answer()
    if "Find the value of the lesser root" in prob:
        halves = prob.split("x^2")
        a = int(halves[0].split()[-1])
        halves2 = halves[1].split("x")
        b = int(halves2[0].split()[-1])
        c = int(halves2[1].split()[1])

        if halves2[0].split()[0] == "-":
            b = -b
        if halves2[1].split()[0] == "-":
            c = -c
        s.sendall(str(int(lesser_root(a,b,c))))
    elif "Find the value of the greater root" in prob:
        halves = prob.split("x^2")
        a = int(halves[0].split()[-1])
        halves2 = halves[1].split("x")
        b = int(halves2[0].split()[-1])
        c = int(halves2[1].split()[1])

        if halves2[0].split()[0] == "-":
            b = -b
        if halves2[1].split()[0] == "-":
            c = -c
        s.sendall(str(int(greater_root(a,b,c))))
    elif "Fill the operations" in prob:
        prob = [x for x in prob.splitlines() if "Fill" in x][0]
        s.sendall(fill_operators(prob))
    elif "first touches the floor" in prob:
        halves = prob.split("m/s")
        v = int(halves[0].split()[-1])
        halves2 = halves[1].split(" m ")
        d = int(halves2[0].split()[-1])
        halves3 = halves2[1].split(" g ")
        w = int(halves3[0].split()[-1])
        halves4 = halves3[1].split(" m/s^2 ")
        a = int(halves4[0].split()[-1])
        s.sendall(str(int(math.sqrt(2*d/a)*v)))
    elif "is projected" in prob:
        halves = prob.split("m/s")
        v = int(halves[0].split()[-1])
        halves2 = halves[1].split(" m ")
        d = int(halves2[0].split()[-1])
        halves3 = halves2[1].split(" g ")
        w = int(halves3[0].split()[-1])
        halves4 = halves3[1].split(" m/s^2 ")
        a = int(halves4[0].split()[-1])
        s.sendall(str(int(math.sqrt(2*a*d))))
    elif "I was going to" in prob:
        S = []
        if "pennies" in prob:
            S += [1]
        if "nickels" in prob:
            S += [5]
        if "dimes" in prob:
            S += [10]
        if "quarters" in prob:
            S += [25]
        if " dollar" in prob:
            S += [100]
        if "five-dollar" in prob:
            S += [500]
        if "ten-dollar" in prob:
            S += [1000]
        amt = prob.split("$")[1].split()[0]
        dollars = int(amt.split(".")[0])
        cents = int(amt.split(".")[1])
        if len(amt.split(".")[1]) == 1: cents *= 10
        print "Change poss:", make_change(dollars*100 + cents, S)
        s.sendall(str(make_change(dollars*100 + cents, S)))
    else:
        print "Couldn't solve:"
        print prob
        s.close()
        answer()

    answer(s)

if __name__ == '__main__':
    answer()
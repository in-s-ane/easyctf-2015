expr = raw_input()
expr = expr.split()
op = expr[0]
num1 = int(expr[1])
num2 = int(expr[2])

res = 0
if op == "add": res = num1 + num2
elif op == "subtract": res = num1 - num2

print res if res>0 else -res


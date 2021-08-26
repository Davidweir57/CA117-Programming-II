from stack_092 import Stack

def calculator(line):
    line = line.split()
    ans = Stack()

    for c in line:
        if c.isdigit() or "." in c:
            ans.push((float(c)))

        elif c == "+":
            curr = ans.l[-2] + ans.l[-1]
            ans.pop()
            ans.pop()
            ans.push(curr)

        elif c == "-":
            curr = ans.l[-2] - ans.l[-1]
            ans.pop()
            ans.pop()
            ans.push(curr)

        elif c == "*":
            curr = ans.l[-2] * ans.l[-1]
            ans.pop()
            ans.pop()
            ans.push(curr)

        elif c == "/":
            curr = ans.l[-2] / ans.l[-1]
            ans.pop()
            ans.pop()
            ans.push(curr)

        elif c == "n":
            curr = -ans.l[-1]
            ans.pop()
            ans.push(curr)

        elif c == "r":
            curr = (ans.l[-1] ** 0.5)
            ans.pop()
            ans.push(curr)

    return ans.l[0]

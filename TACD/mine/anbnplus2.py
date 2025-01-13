stack = ['Z']
pda = 0

def push(a):
    stack.append(a)
    

def pop():
    popped = stack.pop()
    return popped


def peek():
    return stack[-1]


def Q0(c):
    global pda
    if (c == 'a'):
        push('a')
        pda = 0
        print(stack)

    elif (c == 'b' and peek() == 'a'):
        pop()
        pda = 1
        print(stack)

    else:
        pda = -1


def Q1(c):
    global pda
    if (c == 'b' and peek() == 'a'):
        pop()
        pda = 1
        print(stack)

    elif (c == 'b' and peek() == 'Z'):
        pda = 2
        print(stack)

    else:
        pda = -1


def Q2(c):
    global pda
    if (c == 'b' and peek() == 'Z'):
        pda = 3
        print(stack)

    else:
        pda = -1


def Q3():
    pass


def valid(s):
    for c in s:
        if pda == 0:
            Q0(c)
        elif pda == 1:
            Q1(c)
        elif pda == 2:
            Q2(c)
        else:
            return False

    if pda == 3:
        return True
    else:
        return False


def main():
    s = input ("enter the input string: ")
    if valid(s):
        print("input ACCEPTED")
    else:
        print("input NOT ACCEPTED")


if __name__ == "__main__":
    main()
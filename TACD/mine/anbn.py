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
    if (c == '0'):
        push('0')
        pda = 0
    elif (peek() == '0' and c == '1'):
        pop()
        pda = 1
    else: 
        pda = -1


def Q1(c):
    global pda
    if peek() == '0' and c == '1':
        pop()
        pda = 1
    elif peek() == 'Z' and c == 'E':
        pda = 2
        # Q2()
    else:
        pda = -1
    

def Q2():
    # global pda
    # if peek() == 'Z':
    #     pop()
    # else:
    #     pda = -1
    pass


def valid(s):
    for c in s:
        if pda == 0:
            Q0(c)
        elif pda == 1:
            Q1(c)
        else:
            return False
    if pda == 1:
        Q1('E')
    if (pda == 2):
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
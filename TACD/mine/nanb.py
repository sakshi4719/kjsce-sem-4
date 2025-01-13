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
    if (c == 'a' and (peek() == 'Z' or peek() == 'a' )):
        push('a')
        pda = 0

    elif c == 'b' and (peek() == 'Z' or peek() == 'b'):
        push('b')
        pda = 0    

    elif (c == 'a' and peek() == 'b'):
        pop()
        pda = 0

    elif (c == 'b' and peek() == 'a'):
        pop()
        pda = 0

    elif (peek() == 'Z' and c == 'E'):
        pda = 1
        Q1()

    else:
        pda = -1


def Q1():
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
            Q1()
        else:
            return False
    if pda == 0:
        Q0('E')
    if pda == 1:
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

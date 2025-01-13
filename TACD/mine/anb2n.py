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
    
    elif (c == 'b' and peek() == 'a'):
        pda = 1
    
    else:
        pda = -1


def Q1(c):
    global pda 
    if (c == 'b' and peek() == 'a'):
        pop()
        pda = 2
        
    else:
        pda = -1
        
    
def Q2(c):
    global pda
    if (peek() == 'a' and c == 'b'):
        pda = 1
        
    elif (peek() == 'Z' and c == 'E'):
        pda = 3
        
    else:
        pda = -1


def Q3():
    # global pda
    # if (peek() == 'Z'):
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
        elif pda == 2:
            Q2(c)
        else:
            return False
        print(stack)
    if pda == 2:
        Q2('E')
    if (pda == 3):
        return True
    else: 
        return False


def main():
    s = input("enter the string input: ")

    if valid(s):
        print("ACCEPTED")
    else:
        print("NOT ACCEPTED")


if __name__ == "__main__":
    main()
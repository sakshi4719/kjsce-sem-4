stack = ['Z']

pda = 0

def push(a):
    stack.append(a)

def pop():
    popped = stack.pop()
    return popped

def peek():
    return stack[-1]

def Q0(d):
    global pda
    if (d == 'a'):
        push('a')
        pda = 0
        print(stack)

    elif (d == 'b' and peek() == 'a'):
        pda = 1
        pop()
        print(stack)
    
    else:
        pda = -1


def Q1(d):
    global pda    
    if (d == 'b' and peek() == 'a'):
        pda = 1
        pop()
        print(stack)

    elif (d == 'c' and peek() == 'Z'):
        pda = 2
        print(stack)

    else:
        pda = -1 


def Q2(d):
    global pda
    if (d == 'c' and peek() == 'Z'):
        pda = 2
        print(stack)
    else:
        pda = -1


def valid(s):
    for d in s:
        if pda == 0:
            Q0(d)
        elif pda == 1:
            Q1(d)
        elif pda == 2:
            Q2(d)
        else:
            return False
        
    if (pda == 2):
        return True
    else:
        return False
    
def main():
    s = input("enter string: ")
    if valid(s):
        print("Accept")
    else:
        print("Not Accept")

if __name__ == "__main__":
    main()

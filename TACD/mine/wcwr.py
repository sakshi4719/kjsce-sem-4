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

    elif (d == 'b'):
        push('b')
        pda = 0

    elif (d == 'c' and (peek() == 'a' or peek() == 'b')):
        pda = 1
        
    else: 
        pda = -1    


def Q1(d):
    global pda  
    if (peek() == 'b' and d == 'b'):
        pop()
        pda = 1

    elif (peek() == 'a' and d == 'a'):
        pop()
        pda = 1

    elif (peek() == 'Z' and d == 'E'):
        pda = 2

    else: 
        pda = -1


def Q2():
    pass

def valid(s):
    for d in s:
        if pda == 0:
            Q0(d)
        elif pda == 1:
            Q1(d)
        else:
            return False
        
    if pda == 1:
        Q1('E')
    if pda == 2:
        return True
    else:
        return False
    
def main():
    s = input("enter the input string: ")
    if valid(s):
        print("input Accepted")

    else:
        print("input Not Accepted")

if __name__ == "__main__":
    main()
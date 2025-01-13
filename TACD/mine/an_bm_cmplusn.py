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
    if (c == 'a' and peek() == 'a'):
        push('a')
        pda = 0
        
    elif (c == 'a' and peek() == 'Z'):
        push('a')
        pda = 0
        
    elif (c == 'b' and peek() == 'a'):
        push('b')
        pda = 1
        
    else:
        pda = -1
        
def Q1(c):
    global pda
    if (c == 'b' and peek() == 'b'):
        push('b')
        pda = 1
        
    elif (c == 'c' and peek() == 'b'):
        pop()
        pda = 2
        
    else:
        pda = -1
        
def Q2(c):
    global pda
    if (c == 'c' and peek() == 'a'):
        pop()
        pda = 2
        
    elif (c == 'c' and peek() == 'b'):
        pop()
        pda = 2
        
    elif (c == 'E' and peek() == 'Z'):
        pda = 3
        
    else:
        pda = -1
        
def Q3():
    global pda
    if (peek() == 'Z'):
        pop()
    else:
        pda = -1
        
    #pass
    
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
    if pda == 2:
        Q2('E')
    if pda == 3:
        return True
    else:
        return False
    
def main():
    s = input('input: ')
    if valid(s):
        print('valid')
    else:
        print('invalid')
        
if __name__ == "__main__":
    main()

        
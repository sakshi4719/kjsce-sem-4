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
    for i in range(len(s)/2):
        if peek() == 'a':
            push('a')
            pda = 0
            print(stack)
            
        elif peek() == 'b':
            push('b')
            pda = 0
            print(stack)
            
        else: 
            pda = -1
        
def Q1(d):
    global pda  
    for i in range(len(s)/2):
        if (peek() == 'b' and d == 'b'):
            pop()
            pda = 2

        elif (peek() == 'a' and d == 'a'):
            pop()
            pda = 2

        else: 
            pda = -1


def valid(s):
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
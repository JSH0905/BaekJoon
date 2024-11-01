import sys

def push(stack, number):
    return stack.append(number)

def pop(stack):

    if len(stack) == 0:
        print("-1")

    else:
        print(stack[-1])
        stack.pop()


def size(stack):
    print(len(stack))

def empty(stack):

    if len(stack) == 0:
        print("1")
    else:
        print("0")

def top(stack):

    if len(stack) == 0:
        print("-1")
    else:
        print(stack[-1])


n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        push(stack, command[1])

    elif command[0] == "pop":
        pop(stack)

    elif command[0] == "size":
        size(stack)

    elif command[0] == "empty":
        empty(stack)

    elif command[0] == "top":
        top(stack)

    else:
        break

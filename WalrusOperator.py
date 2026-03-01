print("Using walrus operator:")
stack = [1, 2, 3, 4, 5]
while (n := len(stack)) > 0:
    print(stack.pop(), end=" ")
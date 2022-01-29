# Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
def truth_false(x, y):
    if not (x or y) == (not x and not y): print(True)
    else: print (False)
truth_false(x = int(input('Enter x:')), y = int(input('Enter y:')))
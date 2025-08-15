'''
# USANDO LOOPS
def fatorial(n):
    if n < 2:
        return 1
    fat = 1
    for i in range(2, n + 1):
        fat *= i
    return fat

print(fatorial(3))

# USANDO RECURSIVIDADE
def fatorial(n):
    if n < 2:
        return 1

    return n * fatorial(n - 1)

print(fatorial(5))
'''


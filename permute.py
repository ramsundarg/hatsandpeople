from collections import Counter
import sys
def permute(elements, r):
    # Base case: if r is 0, return an empty list
    if r == 0:
        return [[]]

    # Recursive case: generate permutations by selecting each element and permuting the rest
    permutations = []
    for i in range(len(elements)):
        selected = elements[i]
        rest = elements[:i] + elements[i+1:]
        for p in permute(rest, r-1):
            permutations.append([selected] + p)

    return permutations

def apply_scheme(scheme,configs):
    completelyCovered = True
    for config in configs:
        correctGuess = False
        for t in scheme:
            if config[1] in t[0:2] and config[2] in t[0:2] and config[0] == t[2]:
                correctGuess = True
                break
            if config[0] in t[0:2] and config[1] in t[0:2] and config[2] == t[2]:
                correctGuess = True
                break
            if config[0] in t[0:2] and config[2] in t[0:2] and config[1] == t[2]:
                correctGuess = True
                break
        if not correctGuess:
            print(f'{config} has no  correct guess')
            completelyCovered = False
    if completelyCovered:
        print('The scheme is correct')


# Example usage
n = 3

N = 2*n-1 # set to 2n-1
r = (n-1) # set to (n-1) and then fill the nth column
elements = list(range(0, N))

#The "scheme"
table = [[1, 2, 3],
         [1, 3, 5],
         [1, 4, 2],
         [1, 5, 4],
         [2, 3, 5],
         [2, 4, 3],
         [2, 5, 1],
         [3, 4, 1],
         [3, 5, 4],
         [4, 5, 2]]

new_table = []
S = N*(N+1)/2
for config in table:
    U = sum(config[0:2])
    guess = round(abs(U-S)/n) 
    while guess in config[0:2]:
        guess = (guess%n)+1
    new_table.append([config[0], config[1], guess])





result = permute(elements, n)
result = [[x+1 for x in sublist] for sublist in result]
print(f'Applying Ram scheme to the permutations')
apply_scheme(table, result)



apply_scheme(new_table, result)


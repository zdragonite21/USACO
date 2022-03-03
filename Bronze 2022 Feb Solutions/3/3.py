from collections import Counter

# Brute force method as the low time constraints don't require further optimization

# inputs
n = int(input())
words = []

a = set(input())
b = set(input())
c = set(input())
d = set(input())

for i in range(n):
    words.append(input().strip())

# main code
def letter_cubes(word):
    my_word = Counter(word)
    for a_ in a:
        for b_ in b:
            for c_ in c:
                for d_ in d:
                    combo = Counter([a_, b_, c_, d_])
                    for letter in my_word:
                        if combo[letter] < my_word[letter]:
                            break
                    else:
                        return "YES"
    return "NO"


# printing the answers
for word in words:
    print(letter_cubes(word))

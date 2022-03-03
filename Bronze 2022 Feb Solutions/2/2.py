import time

# I originally came up with inefficiently inserting and deleting
# values in a list in order to calculute the number of steps
# but the following are the two relatively optimized solutions

# inputs
n = int(input())
a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]


# simple way
def simple(a, b, n):
    steps = 0

    ind = {}

    for x in b:
        ind[x] = True

    if a == b:
        return 0

    for i in range(n):
        # b[i] is the first to be shifted in a[n]
        if a[i] == b[i] or not ind[a[i]]:
            continue
        a.insert(i, b[i])
        ind[b[i]] = False
        steps += 1

    return steps


# optimized way
def optimized(a, b, n):
    steps = 0

    ind = {}

    for x in b:
        ind[x] = True

    if a == b:
        return 0

    i = 0
    j = 0
    while j < n:
        if not ind[a[i]]:
            i += 1
            continue

        elif a[i] == b[j]:
            i += 1
            j += 1
            continue

        else:
            ind[b[i]] = False
            j += 1
            steps += 1

    return steps


# printing answers with time
timer = time.time()
print(simple(a[:], b[:], n))
print(time.time() - timer)

timer = time.time()
print(optimized(a[:], b[:], n))
print(time.time() - timer)

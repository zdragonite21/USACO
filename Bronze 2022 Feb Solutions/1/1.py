# This problem by far took the longest to come up with a formula
# I used the sum of factors as potential final values in the list
# Because we are only adding adjecent numbers, the final answer must
# be a factor of their sum

# inputs
n = int(input())
s = []
for i in range(n):
    q = int(input())
    s.append([int(x) for x in input().strip().split()])


# optimized factors function
def factors(x):
    # generates factors not including 1 or x
    ls = []
    i = 2
    while i * i <= x:
        if x % i == 0:
            ls.append(i)
            if x // i != i:
                ls.append(x // i)
        i += 1
    return sorted(ls)


# main function
def exe(log):
    # first, checks if all the values are the same
    # next, check each factor, stepping left to right and check whether or not it work
    # if none of the above works, calcuate the score based on the log summed up
    if all(log[0] == log[x] for x in range(len(log))):
        return 0

    max_val = max(log)
    sum_log = sum(log)

    fact = factors(sum_log)

    # this filters all factors greater than or equal to the max value in the log
    # we do this because we can only add values, hence the final answer can never be less than the maximum in the log
    fact = list(filter(lambda x: x >= max_val, fact))

    for factor in fact:
        sum_ = 0
        for i in range(len(log)):
            sum_ += log[i]
            if sum_ == factor:
                sum_ = 0
                if i == (len(log) - 1):
                    return (len(log)) - (sum_log // factor)
            elif sum_ > factor:
                break

    # if no factors work, we must return the [sort of] worst case senario which is all the logs combined into one number
    return len(log) - 1


# printing the answers
ans = []

for log in s:
    print(exe(log))

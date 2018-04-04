# Very cheeky recursion problem with memoization
# The trick is to realise that since there are only
# 1 2 or 3 steps per time, thus to get the combination
# of any given number of steps, it's the same as saying
# it's the sum of the n-1, n-2 and n-3 steps, since to get
# to step n, you only need one more operation for each case.

def get_combos(height, dic_steps):
    if height in dic_steps:
        return dic_steps[height], dic_steps
    steps_c = 0
    for i in range(1,4):
        steps, dic_steps = get_combos(height - i, dic_steps)
        steps_c += steps
        if height - i not in dic_steps:
            dic_steps[height - i] = steps
    return steps_c, dic_steps

s = int(input().strip())
dic_steps = {0:0,1:1,2:2,3:4}
for a0 in range(s):
    n = int(input().strip())
    steps, dic_steps = get_combos(n, dic_steps)
    print(steps)

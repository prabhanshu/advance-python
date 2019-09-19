import time
def sum_of_N(n):
    start = time.time()
    thesum = 0
    for i in range(1, n+1):
        thesum = thesum + i
    end = time.time()
    return thesum, end-start

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_N(10000))

def anagram_solution(s1,s2):
    status = True
    if len(s1) != len(s2):
        status = False
    s2list = list(s2)
    pos1 = 0
    while pos1 < len(s1) and status:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == s2list[pos2]:
                s2list[pos2] = None
                found = True
            else:
                found = False
            pos2 = pos2 + 1
        if not found:
            status = False
        pos1 = pos1 + 1
    return status

print(anagram_solution('heart','earth'))
print(anagram_solution('python','typhon'))
print(anagram_solution('sonu','monu'))


multiples = set()
def div(n, num):
    ans = []
    for i in range(1, int(n/num)+1):
        temp = i*num
        if temp not in multiples:
            multiples.add(temp)
            ans.append(temp)
    return ans

result = []

for i in range(2, 33):
    temp = div(998,i)
    print(f'List of integers which are multiple of {i } and hence to be removed: {temp}' )

prime = list()
for i in range(2, 998):
    if i not in multiples:
        prime.append(i)

print('List of all prime numbers: ', end="")
print(prime)
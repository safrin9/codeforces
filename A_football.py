from collections import Counter
n=int(input())

x=[]
for i in range(n):
    team=input()
    x.append(team)

counter = Counter(x)

# Find the most common element
most_common_element, frequency = counter.most_common(1)[0]

print(most_common_element)

















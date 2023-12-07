
data = open("input2.txt", "r")

time = data.readline()
dist = data.readline()

time = time.split()[1:]
dist = dist.split()[1:]

time = [int(str) for str in time]
dist = [int(str) for str in dist]


scores = []



for index, t in enumerate(time):
    d = dist[index]

    sum = 0
    #assuming no races of 0 millimeters
    for i in range (1, t):
        if i * (t - i) > d:
            sum += 1
    
    scores.append(sum)

res = 1
for int in scores:
    res *= int

print(res)
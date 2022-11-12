N = int(input())
mas = list(map(int, input().split()))
count = 0
for run in range(N-1):
    for i in range (N-1):
        if mas[i]>mas[i+1]:
            count+=1
            mas[i], mas[i+1]= mas[i+1], mas[i]

print(count)

q=int(input())
for _ in range(q):
    N = int(input())
    liste = list(map(int,input().rstrip().split()))
    liste.sort()
    temp = liste[0]
    count = 1
    paralel = 0
    for elem in liste[1:]:
        if elem != temp:
            if count % 2 == 1:
                paralel = 1
                print(temp)
                break
            else:
                temp = elem
                count = 1
        else:
            count += 1
    if paralel == 0:
        print(elem)

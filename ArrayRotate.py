T = int(input())
for _ in range(T):
    N, D = map(int, input().split(" "))
    arr = [int(x) for x in input().strip().split(" ")]
    print(*(arr[D:] + arr[:D]))
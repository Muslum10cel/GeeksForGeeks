T = int(input())
for _ in range(T):
    n = int(input())
    picked_numbers = [int(x) for x in input().strip().split(" ")]
    expected_sum =  (n**2 + n) // 2
    actual_sum=sum(picked_numbers)
    print(expected_sum - actual_sum)

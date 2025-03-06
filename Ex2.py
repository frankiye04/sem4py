
N = int(input("Enter a positive integer N:"))
total_sum = 0
for number in range(1,N + 1):
    total_sum += number
    print(f"The sum of the first {N} Natural numbers is: {total_sum}")
target = int(input()) # Enter a number between 0 and 1000

sum = 0
for number in range(1, target+1):
  if number % 2 == 0:
    sum += number

print(sum)

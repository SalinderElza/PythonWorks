n = int(input())
numbers = set(range(1, n + 1))
numbers2 = numbers
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(i) for i in guess.split()}
    answer = input()
    if answer == 'YES':
        numbers2 &= guess
    else:
        numbers2 &= numbers - guess
print(' '.join([str(i) for i in sorted(numbers2)]))

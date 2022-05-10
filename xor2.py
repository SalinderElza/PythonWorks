from functools import reduce
print(
    *reduce(
        lambda x, y: map(
            lambda a, b: a ^ b, x, y
        ),
        map(
            lambda x: map(
                int, input().split()
            ),
            range(int(input()))
        )
    )
)

from math import sqrt
print(
    *filter(
        lambda i: 0 not in set(
            map(
                lambda x: i % x,
                range(2, int(sqrt(i)) + 1)
            )
        ),
        range(2, int(input()) + 1)
    )
)

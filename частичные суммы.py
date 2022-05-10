import itertools
print(
    *itertools.accumulate(
        map(
            int, input().split()
        )
    )
)

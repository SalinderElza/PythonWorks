print(
    sorted(
        map(
            int, input().split()
        ),
        key=lambda i: (i % 2 == 0, i)
    )[0]
)

from itertools import accumulate
from operator import mul
print(
    *accumulate(
        [1] + list(
            range(
                1, int(input()) + 1
            )
        ), mul
    )
)

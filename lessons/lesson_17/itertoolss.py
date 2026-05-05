import itertools
from itertools import cycle

browsers = ['Chrome', 'Firefox', 'Safari']
os = ['Windows', 'Linux', 'Mac OS']
api_version = ('v1', 'v2', 'v3')


# exhausted testing
all_combinations = itertools.product(browsers, os, api_version)

# for combination in all_combinations:
#     print(combination)

cycle_combinations = itertools.cycle(browsers)


# for item in cycle_combinations:
#     print(item)

chain_combinations = itertools.chain(browsers, api_version)

# for item in chain_combinations:
#     print(item)


unique_combinations = itertools.combinations(chain_combinations, 2)
for item in unique_combinations:
    print(item)


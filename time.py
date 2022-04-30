from time import perf_counter
from random import randrange

test_list = [randrange(0,t) for t in range(1,1000)]

start = perf_counter()
for i in range(10_000):
	a = test_list[4]
end = perf_counter()

print(f'it took {end-start:.10} seconds')

bilow = perf_counter()
for i in range(10_000):
	a = test_list.__getitem__(4)
dhamaad = perf_counter()

print('')
print(f'it took {dhamaad-bilow:.10} seconds')
print()

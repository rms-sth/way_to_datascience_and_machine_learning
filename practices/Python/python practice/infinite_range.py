def infinite_range(start):
    while True:
        yield(start)
        start += 1   

result = infinite_range(1)
for r in result:
	print(r)
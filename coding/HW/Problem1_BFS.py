lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)

print(longest)
print(middle)
print(shortest)

print(f'최대 길이: {longest:>4.0%}')        # 최대 길이: 108%
print(f'최소 길이: {shortest:>4.0%}')       # 최소 길이:  89%
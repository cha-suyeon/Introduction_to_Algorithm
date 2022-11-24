names = ['Cecilia', '남궁민수', '毛泽东']
counts = [len(n) for n in names]
print(counts)
# [7, 4, 3]


longest_name = []
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count
    
print(longest_name) # Cecilia


for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count
        
print(longest_name) # Cecilia


names.append('Rosalind')
for name, count in zip(names, counts):
    print(name)
# Cecilia
# 남궁민수
# 毛泽东


import itertools

for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')  
# Cecilia: 7
# 남궁민수: 4
# 毛泽东: 3
# Rosalind: None

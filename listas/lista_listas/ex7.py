'''
Dado o vetor nums = [3, 11, 6, 32, 15, 22, 4, 10, 5], criar uma
matriz 3x3 com os 3 maiores elementos na primeira linha, os 3
elementos intermediários na segunda linha, e os elementos
menores na terceira linha.
'''

nums = [3, 11, 6, 32, 15, 22, 4, 10, 5]
nums.sort(reverse=True)
matrix = []
for i in range(3):
    line = []
    for j in range(3):
        line.append(nums[j + i * 3])
    matrix.append(line)
print(matrix)
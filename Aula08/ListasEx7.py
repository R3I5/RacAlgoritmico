# Dado o vetor nums = [3, 11, 6, 32, 15 , 22, 4, 10 , 5], criar uma matriz 3x3 com os 3 maiores elementos na primeira linha,
# os 3 elementos intermediarios na segunda linha, e os elementos menores na terceira linha

nums = [3, 11, 6, 32, 15 , 22, 4, 10 , 5]
nums.sort(reverse=True)
print(nums)
matriz = [
    nums[:3],
    nums[3:6], 
    nums[6:]
]
for linha in matriz:
    print(linha)
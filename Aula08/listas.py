"""
Criando Listas em Python
"""
nums = []
for i in range(5):
    num = int(input(f'Digite o {i+1}° numero: '))
    nums.append(num)
for num in nums:
    print(num)
for i in range(len(nums)):
    print(nums[i])
print(nums)
print(*nums)
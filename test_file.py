total = int(input("Enter total: "))
length = int(input("Enter length: "))

base = total // length
remainder = total % length

result = []

for i in range(length):
    if i < remainder:
        result.append(base + 1)
    else:
        result.append(base)

print("\nResult:")
print(*result)

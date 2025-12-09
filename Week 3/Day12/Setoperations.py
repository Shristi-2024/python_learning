# Perform Set Operations
set1 = set(input("Enter elements for Set 1 (space separated): ").split())
set2 = set(input("Enter elements for Set 2 (space separated): ").split())

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (Set1 - Set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# From Nick Russo -->> Parallel Iteration with zip()
# Two lists can be zipped together into tuple
# If lists have unequal length then zip will truncate to the shortest one

sizes = ["small", "medium", "large"]
animals = ["frog", "wolf", "elephant"]
for size, animal in zip(sizes, animals):
    print(f"I see a {size} {animal}")
# Converting dictionary to a list of tuples

animals = {
    "small": "frog",
    "medium": "wolf",
    "large": "elephant"
}
for size, animal in animals.items():
    print(f"I see a {size} {animal}")
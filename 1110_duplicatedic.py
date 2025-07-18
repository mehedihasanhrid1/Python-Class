data = {
    'x': 10,
    'y': 20,
    'z': 10,
    'w': 30,
    'v': 20,
    'u': 40
}

unique_values = {}
for key, value in data.items():
    if value not in unique_values.values():
        unique_values[key] = value

print("Original dictionary:", data)
print("Dictionary after removing duplicates:", unique_values)
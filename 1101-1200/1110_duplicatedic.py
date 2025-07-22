data = {
    't': 20,
    'u': 10,
    'v': 20,
    'w': 10,
    'x': 30,
    'y': 20,
    'z': 40
}

unique_values = {}
for key, value in data.items():
    if value not in unique_values.values():
        unique_values[key] = value

print("Original dictionary:", data)
print("Dictionary after removing duplicates:", unique_values)
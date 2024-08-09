dict_nested = {
    "list": [1, 2, 3, [1, 2, 3]],
    "tuple": (4, 5, 6),
    "set": {7, 8, 9},
    "string": "Hello, World!",
    "boolean": True,
    "dict": {"michale": 34, "peter": 36, "alice": 37},
    "cities": {"Germany":["Berlin","Munich","hanburg"]}
}
print(dict_nested["dict"]["peter"])
print(dict_nested["list"][3][2])
print(dict_nested["cities"]["Germany"][1])
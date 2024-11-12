a_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
try:    
    value = a_dict["key5"]
except KeyError:
    value = "Key not found in the dictionary"
    
print(value)
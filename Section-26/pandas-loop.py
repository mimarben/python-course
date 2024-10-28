import pandas as pd  # Use standard alias pd instead of pnd

# Dictionary containing student data
student_dict = {  # Added space around = for PEP8
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Print dictionary items
print("\nDictionary items:")
for key, value in student_dict.items():  # Removed unnecessary parentheses
    print(f"{key}: {value}")  # More readable f-string formatting

# Create DataFrame and display it    
student_df = pd.DataFrame(student_dict)  # Better variable name
print("\nDataFrame:")
print(student_df)

# Print DataFrame columns and values
print("\nDataFrame columns and values:")
for key, value in student_df.items():
    print(f"\n{key}:")
    print(value)

# Print each student's data    
print("\nStudent records:")
for _, row in student_df.iterrows():  # Use _ for unused index variable
    print(f"Student: {row.student}, Score: {row.score}")  # More concise output


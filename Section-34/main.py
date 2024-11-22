"""
def get_file_size(file_path: str) -> int:
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        return file_size
    else:
        return 0
"""
age: int
name : str
height : float
is_human : bool
def police_check(age:int) -> bool:
    if age >18:
        can_drive= True
    else:
        can_drive= False
    return can_drive


print(police_check(9))

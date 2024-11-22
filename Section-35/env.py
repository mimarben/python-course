import os

# Set an environment variable
os.environ['API_KEY_OW'] = "86dc17895d446166ca0523db7af1356a"

API_KEY=os.environ.get('API_KEY_OW')
print(f'MY_VARIABLE: {API_KEY}')

#!in linux command line
# export API_KEY_OW="86dc17895d446166ca0523db7af1356a"

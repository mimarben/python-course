import requests

pixela_endpoint = "https://pixe.la/v1/users"
PIXLA_TOKEN= "realvalladolid_1924"
USER_NAME= "martinm"
user_params = {
    "token": PIXLA_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
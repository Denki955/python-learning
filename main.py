import requests 
response = requests.get("https://api.github.com")

print(response.status_code)
print("Learning Git on Master Branch")
print("This is my new feature")
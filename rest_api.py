import requests

# Example API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Sending a GET request
payload = {
    "userId": 1,
    "id": 1
}
response = requests.get(url, params = payload)

# Check the status code (200 means success)
if response.status_code == 200:
    data = response.json()
    print(f"Received data: {data}")
else:
    print(f"Error: {response.status_code}")

# Data to send in the request body
payload = {
    "userId": 1,
    "id": 5,
    "title": "New Post",
    "body": "This is the content of the new post.",
}

# Sending a POST request
response = requests.post(url, json=payload)

if response.status_code == 201:  # 201 Created
    print("Data created successfully:", response.json())
else:
    print(f"Error: {response.status_code}")

# Endpoint to update a specific post (e.g., post with ID 1)
url = "https://jsonplaceholder.typicode.com/posts/1"

# Updated data
updated_data = {
    "userId": 1,
    "id": 1,
    "title": "Updated Title",
    "body": "Updated content of the post."
}

# Sending a PUT request
response = requests.put(url, json=updated_data)

if response.status_code == 200:
    print("Data updated successfully:", response.json())
else:
    print(f"Error: {response.status_code}")

# Sending a GET request
payload = {
    "userId": 1,
    "id": 1
}
response = requests.get(url, params = payload)

if response.ok:  # Shortcut for checking status_code < 400
    data = response.json()
    print(f"Success: {data}")
else:
    print("Failed:", response.status_code, response.text)

# Sending a DELETE request
response = requests.delete(url)

if response.status_code == 200:
    print("Data deleted successfully.")
else:
    print(f"Error: {response.status_code}")

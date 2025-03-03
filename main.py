import requests

# Prepare the required data for the API request, including the username and API key 
# (you can get a free API key by joining: https://discord.gg/QPuWDHTnDV)
data = {
    'user': 'user',
    'apikey': 'apikey from https://exoclaim.com/'
}

# Send a POST request to the API to create a new task
response = requests.post('https://exoclaim.com/create_task.php', data=data)
print(response.text)

# How it works: Once an available user is found, a request is sent to the API with the username, 
# and the service will automatically claim it on your behalf.

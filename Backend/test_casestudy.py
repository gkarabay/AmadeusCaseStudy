#using request to access API
import requests

ENDPOINT = "https://flights-api.buraky.workers.dev"

response = requests.get(ENDPOINT)


#HTTP status test
if(200 <= response.status_code == 200): 
    print("HTTP Status:", response.status_code, " PASSED")
else:
    print("HTTP Status:", response.status_code, " FAILED")

#Response test
print(response.text)

#Header check
header = {'Content-Type': 'application/json'}

response = requests.post(ENDPOINT, header)

if(response.headers['Content-Type'] == 'application/json'):
    print("Content-Type:", response.headers['Content-Type'], " PASSED")
else:
    print("Content-Type:", response.headers['Content-Type'], " FAILED")
    


# here i imported libarary here to api requets
import requests

# here i have use api keys
Api_key = "6c4d9ebc962735b9e9f64f9e8ceaf78284a1f1ae5925136e3f05880fe95c357535b585e874437939"
Api_end_check = "https://api.abuseipdb.com/api/v2/check"
Api_end_report = "https://api.abuseipdb.com/api/v2/report"

headers = {
    "Key": "6c4d9ebc962735b9e9f64f9e8ceaf78284a1f1ae5925136e3f05880fe95c357535b585e874437939",
    "Accept": "application/json"
}

# GET request to check an IP address
ip_to_check = "8.8.8.8"
params = {
    "ipAddress": ip_to_check
}
response_get = requests.get(Api_end_check, headers=headers, params=params)
print("GET response:")
print(response_get.json())

# POST request to report an IP address
data = {
    "ip": ip_to_check,
    "categories": "18",
    "comment": "Keyed_API"
}
response_post = requests.post(Api_end_report, headers=headers, data=data)
print("POST response:")
print(response_post.json())

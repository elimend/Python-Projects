import requests

# Define the website URL
url = 'https://www.example.com'

# Send an HTTP GET request to the website and store the response
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    print(f"{url} is up and running.")
else:
    print(f"{url} is down or inaccessible.")

# Check if the website is using HTTPS
if response.url.startswith("https"):
    print(f"{url} is using HTTPS.")
else:
    print(f"{url} is not using HTTPS.")

# Check the headers of the response to see if any security-related headers are present
security_headers = ['X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection', 'Strict-Transport-Security']

for header in security_headers:
    if header in response.headers:
        print(f"{header} is present in the response headers.")
    else:
        print(f"{header} is not present in the response headers.")

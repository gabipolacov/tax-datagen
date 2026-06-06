import requests

def validate_zip(zip_code, state):
    url = f"http://api.zippopotam.us/us/{zip_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        api_state = data["places"][0]["state"]

        if  not state or state == api_state:
            return True

    else:
        return False





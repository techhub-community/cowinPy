import requests


def getStates():
    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
        response = requests.get(
            "https://cdn-api.co-vin.in/api/v2/admin/location/states",
            headers=headers)
        return response.json()
    except:
        raise Exception("cowinPy couldn't connect to cowin's server")


def getDistricts(stateId):

    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }

        apiUrl = "https://cdn-api.co-vin.in/api/v2/" + "admin/location/districts/" + str(
            stateId)
        response = requests.get(apiUrl, headers=headers)
        return response.json()

    except:

        raise Exception("cowinPy couldn't connect to cowin's server")

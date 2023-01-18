import requests

AMOUNT = 10
# CATEGORY = 31
TYPE = "boolean"
parameters = {
    "amount": AMOUNT,
    # "category": CATEGORY,
    "type": TYPE
}

response = requests.get(url = "https://opentdb.com/api.php",
                        params = parameters)
response.raise_for_status()
question_data = response.json()["results"]
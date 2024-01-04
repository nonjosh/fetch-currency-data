import requests
from google.cloud import firestore


def get_currency_data(request, context):
    # Initialize Firestore
    db = firestore.Client()

    # Extract the currency unit from the request
    request_data = request.get_json()
    currency_unit_from = request_data.get("from", "cny")
    currency_unit_to = request_data.get("from", "hkd")

    # URL to fetch data from
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{currency_unit_from}/{currency_unit_to}"

    # Send a GET request to the URL
    response = requests.get(url, timeout=5)

    # Convert the response to JSON
    data = response.json()

    # Store the data in Firestore
    doc_ref = db.collection("currencyData").document()
    doc_ref.set(data)

    return "Data fetched and stored in Firestore successfully!", 200

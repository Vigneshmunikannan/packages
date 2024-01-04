import requests

def register_customer(data):
    customer_endpoint = 'https://vigneshmunikannan.myshopify.com//admin/api/2023-10/customers.json'
    access_token = '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'
    # Customer data
    customer_data = data
    # Headers with access token
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": access_token
    }
    # Make the POST request to create the customer
    response = requests.post(customer_endpoint, json=customer_data, headers=headers)

    # Check the response
    if response.status_code == 201:
        return "Customer successfully created:", response.json()['customer']
    else:
      raise ValueError(f"Failed to create customer. Status code:", response.status_code,"Response:", response.text)
       

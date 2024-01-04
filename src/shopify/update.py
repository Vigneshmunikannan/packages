import requests

def update_customer(customer_id,updatedata):
    customer_endpoint = f'https://vigneshmunikannan.myshopify.com/admin/api/2023-10/customers/{customer_id}.json'
    access_token = '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'
    
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Shopify-Access-Token": access_token
}

    response=requests.put(customer_endpoint,json={"customer": updatedata},headers=headers)

    if response.status_code == 200:
        return "Customer successfully updated:", response.json()['customer']
    else:
        raise ValueError(f"Failed to update customer. Status code: {response.status_code}. Response: {response.text}")


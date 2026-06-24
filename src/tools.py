def get_customer(customer_id):

    return {
        "customer_id": customer_id,
        "name": "John Smith"
    }


def create_order(customer_id):

    return {
        "status": "created"
    }
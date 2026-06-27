def get_customer(customer_id):

    return {
        "status": "success",
        "customer_id": customer_id,
        "name": "John Smith",
        "email": "john@example.com"
    }


def create_order(customer_id):

    return {
        "status": "success",
        "order_id": 1001,
        "customer_id": customer_id
    }
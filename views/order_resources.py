ORDERS = [
    {
      "id": 1,
      "styleId": 3,
      "metalId": 2,
      "sizeId": 1
    },
    {
      "id": 2,
      "styleId": 1,
      "metalId": 3,
      "sizeId": 2
    }, {
      "id": 3,
      "styleId": 2,
      "metalId": 3,
      "sizeId": 4
    }, {
      "id": 4,
      "styleId": 3,
      "metalId": 2,
      "sizeId": 5
    },
  ]

def get_all_orders():
    return ORDERS
def get_single_order(id):
    requested_order = None

    for order in ORDERS:
       if order["id"] == id:
         requested_order = order
    return requested_order
def create_order(order):
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order
def delete_order(id):
    # Initial -1 value for animal index, in case one isn't found
    order_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Store the current index.
            order_index = index

    # If the animal was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)
def update_order(id, new_order):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            new_order["id"] = id
            # Found the animal. Update the value.
            ORDERS[index] = new_order
            break
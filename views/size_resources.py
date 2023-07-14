SIZES = [
    {
      "id": 1,
      "caret": 1,
      "price": 100
    },
    {
      "id": 2,
      "caret": 2,
      "price": 200
    },
    {
      "id": 3,
      "caret": 3,
      "price": 300
    },
    {
      "id": 4,
      "caret": 4,
      "price": 400
    },
    {
      "id": 5,
      "caret": 5,
      "price": 500
    }
  ]

def get_all_sizes():
    return SIZES
def get_single_size(id):
    requested_size = None

    for size in SIZES:
       if size["id"] == id:
         requested_size = size
    return requested_size
def create_size(size):
    max_id = SIZES[-1]["id"]
    new_id = max_id + 1
    size["id"] = new_id
    SIZES.append(size)
    return size
def delete_size(id):
    # Initial -1 value for animal index, in case one isn't found
    size_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, size in enumerate(SIZES):
        if size["id"] == id:
            # Found the animal. Store the current index.
            size_index = index

    # If the animal was found, use pop(int) to remove it from list
    if size_index >= 0:
        SIZES.pop(size_index)
def update_size(id, new_size):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, size in enumerate(SIZES):
        if size["id"] == id:
            new_size["id"] = id
            # Found the animal. Update the value.
            SIZES[index] = new_size
            break
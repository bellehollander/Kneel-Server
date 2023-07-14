STYLES = [
    {
      "id": 1,
      "style": "classic",
      "price": 100
    },
    {
      "id": 2,
      "style": "modern",
      "price": 200
    },
    {
      "id": 3,
      "style": "vintage",
      "price": 300
    }
  ]

def get_all_styles():
    return STYLES
def get_single_style(id):
    requested_style = None

    for style in STYLES:
       if style["id"] == id:
         requested_style = style
    return requested_style
def create_style(style):
    max_id = STYLES[-1]["id"]
    new_id = max_id + 1
    style["id"] = new_id
    STYLES.append(style)
    return style
def delete_style(id):
    # Initial -1 value for animal index, in case one isn't found
    style_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, style in enumerate(STYLES):
        if style["id"] == id:
            # Found the animal. Store the current index.
            style_index = index

    # If the animal was found, use pop(int) to remove it from list
    if style_index >= 0:
        STYLES.pop(style_index)
def update_style(id, new_style):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, style in enumerate(STYLES):
        if style["id"] == id:
            new_style["id"] = id
            # Found the animal. Update the value.
            STYLES[index] = new_style
            break
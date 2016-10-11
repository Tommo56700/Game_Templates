item_pen = {
    "id": "pen",
    
    "name": "a pen",

    "description": "A basic ballpoint pen."
}

item_handbook = {
    "id": "handbook",
    
    "name": "a student handbook",

    "description": "This student handbook explains everything. Seriously."
}

items = [item_pen, item_handbook]
item_list = [item["name"] for item in items if "name" in item]

formatted_item_list = ""

for element in item_list:
	if item_list[0] == element:
		formatted_item_list += element
	else:
		
		formatted_item_list += ", " + element

print(formatted_item_list)
import json
import os

class Item:
    def __init__(self, name, code, stock, price):
        self.name = name
        self.code = code
        self.price = price
        self.stock = stock


    def to_json(self):
        return json.dumps(self, default=vars)

    def __repr__(self):
        return self.code + ": " + self.name + " - " + str(self.price) + " - " + str(self.stock)


class Shipment:
    def __init__(self, item_code, number, date_by):
        self.item_code = item_code
        self.number = number
        self.date_by = date_by
    def to_json(self):
        return json.dumps(self, default=vars)

def item_from_json(jsons):
    itemdict = json.loads(jsons)
    item = Item(itemdict['name'], itemdict['code'], itemdict['stock'], itemdict['price'])
    return item

def shipment_from_json(jsons):
    itemdict = json.loads(jsons)
    item = Shipment(itemdict['item_code'], itemdict['number'], itemdict['date_by'])
    return item


class Database:
    def __init__(self, items_filename, shipments_filename):
        self.items_filename = items_filename
        self.shipments_filename = shipments_filename
        self._items_array_ = []
        self._shipments_array_ = []
        if os.path.isfile(items_filename):
            file_in = open(items_filename, "r")
            jsons_array = file_in.read().split("\n")
            for jsons in jsons_array:
                if jsons == '':
                    continue
                item = item_from_json(jsons)
                self._items_array_.append(item)
            file_in.close()
        if os.path.isfile(shipments_filename):
            file_in = open(shipments_filename, "r")
            jsons_array = file_in.read().split("\n")
            for jsons in jsons_array:
                if jsons == '':
                    continue
                item = shipment_from_json(jsons)
                self._shipments_array_.append(item)
            file_in.close()

    def add_item(self, item):
        self._items_array_.append(item)

    def add_shipment(self, shipment):
        self._shipments_array_.append(shipment)

    def find_item_with_code(self, code):
        for item in self._items_array_:
            if item.code == code:
                return item

    def delete_item(self, code):
        for item in self._items_array_:
            if item.code == code:
                self._items_array_.remove(item)
                return

    def delete_shipment(self, shipment_number):
        for item in self._shipments_array_:
            if item.number == shipment_number:
                self._shipments_array_.remove(item)
                return

    def all_items(self):
        return self._items_array_

    def all_shipments(self):
        return self._shipments_array_

    def save_db(self):
        #items
        jsons_array = []
        for item in self._items_array_:
            jsons = item.to_json()
            jsons_array.append(jsons)
        file_out = open(self.items_filename, "w")
        file_data = "\n".join(jsons_array)
        file_out.write(file_data)
        file_out.close()

        jsons_array = []
        for item in self._shipments_array_:
            jsons = item.to_json()
            jsons_array.append(jsons)
        file_out = open(self.shipments_filename, "w")
        file_data = "\n".join(jsons_array)
        file_out.write(file_data)
        file_out.close()



testitem = Item("Strawberry Jam", "12345", 5, 2.99)
testitem2 = Item("Terry VI", "67890", 3, 1.99)
testitem3 = Item("Hot Chocolate", "121212", 17, 3.49)
item_from_json(testitem.to_json())

database = Database("items.txt", "shipments.txt")
print(database.all_items())
database.find_item_with_code("12345").stock += 1
database.add_shipment(Shipment("12345", "7478", "30/12/2023"))
print(database.all_shipments())
# database.add_item(testitem)
# database.add_item(testitem2)
# database.add_item(testitem3)
database.save_db()
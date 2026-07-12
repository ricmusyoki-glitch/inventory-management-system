from flask import Flask, jsonify, request
from inventory import inventory

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API"
    })


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)

    return jsonify({
        "error": "Item not found"
    }), 404

@app.route("/inventory", methods=["POST"])
def add_inventory_item():
    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "name": data["name"],
        "quantity": data["quantity"],
        "price": data["price"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    data = request.get_json()

    for item in inventory:
        if item["id"] == item_id:

            if "name" in data:
                item["name"] = data["name"]

            if "quantity" in data:
                item["quantity"] = data["quantity"]

            if "price" in data:
                item["price"] = data["price"]

            return jsonify(item)

    return jsonify({
        "error": "Item not found"
    }), 404

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)

            return jsonify({
                "message": "Item deleted successfully"
            })

    return jsonify({
        "error": "Item not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)
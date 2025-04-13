from flask import Flask, render_template, request
from scraper import get_product_data
from db import init_db, insert_product, get_all_products

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        url = request.form["url"]
        data = get_product_data(url)
        if data:
            insert_product(data["title"], url, data["price"])
            message = f"Added: {data['title']} - {data['price']}"
        else:
            message = "Failed to retrieve product data."

    products = get_all_products()
    return render_template("index.html", products=products, message=message)

if __name__ == "__main__":
    app.run(debug=True)

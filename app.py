import os
from flask import Flask, render_template, request
from scraper import get_product_data
from db import init_db, insert_product, get_all_products

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    # message = ""
    if request.method == "POST":
        url = request.form["url"]
        if url:
            result = get_amazon_price(url)
            return render_template('result.html', result=result, url=url)
        return render_template('index.html')

    # products = get_all_products()
    # return render_template("/index.html", products=products, message=message)

if __name__ == "__main__":
    app.run(debug=True)

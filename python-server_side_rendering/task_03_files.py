#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_products():
    path = os.path.join(app.root_path, 'products.json')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                item['id'] = int(item['id'])
                item['price'] = float(item['price'])
            return data
    except:
        return []

def read_csv_products():
    path = os.path.join(app.root_path, 'products.csv')
    products = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except:
        return []

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source. Use ?source=json or ?source=csv")

    if source == 'json':
        all_products = read_json_products()
    else:  # csv
        all_products = read_csv_products()

    if product_id is not None:
        try:
            product_id = int(product_id)
            filtered = [p for p in all_products if p['id'] == product_id]
            if not filtered:
                return render_template('product_display.html', error="Product not found")
            return render_template('product_display.html', products=filtered)
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")

    return render_template('product_display.html', products=all_products)

@app.route('/')
def home():
    return "<h1>Welcome! Go to <a href='/products?source=json'>/products?source=json</a> or <a href='/products?source=csv&id=2'>with id</a></h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)

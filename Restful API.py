from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Connect to database
def connect_db():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    conn.close()
    
    # Convert to list of dictionaries
    result = [dict(row) for row in rows]
    return jsonify(result)

# Get product by ID
@app.route('/api/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE id = ?", (id,))
    row = cur.fetchone()
    conn.close()

    if row is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(dict(row))

# Run the app
if __name__ == '_main_':
    app.run(debug=True)
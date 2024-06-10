from flask import Flask, jsonify, send_from_directory, render_template
import os
import random

app = Flask(__name__)

# Full path to the categories folder
categories_path = '/Users/akollu/Desktop/faces/guessthecricketer/categories'

@app.route('/categories')
def get_categories():
    categories = [d for d in os.listdir(categories_path) if os.path.isdir(os.path.join(categories_path, d))]
    print(f"Categories: {categories}")
    return jsonify(categories)

@app.route('/random_image')
def get_random_image():
    categories = [d for d in os.listdir(categories_path) if os.path.isdir(os.path.join(categories_path, d))]
    random_category = random.choice(categories)
    images = os.listdir(os.path.join(categories_path, random_category))
    random_image = random.choice(images)
    image_path = f'{random_category}/{random_image}'
    print(f"Random category: {random_category}, Random image: {random_image}, Image path: {image_path}")
    return jsonify({'category': random_category, 'image': image_path})

@app.route('/categories/<path:filename>')
def serve_image(filename):
    print(f"Serving image: {filename}")
    return send_from_directory(categories_path, filename)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

#if __name__ == "__main__":
#    port = int(os.environ.get('PORT', 5000))
#    app.run(host='0.0.0.0', port=port)



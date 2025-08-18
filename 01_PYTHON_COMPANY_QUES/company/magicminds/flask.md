To create a REST API for managing a product catalog with the specified features, you can follow these steps. I'll outline the structure, key components, and provide code snippets for each part. This will include setting up a basic Flask application with SQLAlchemy for database management, asynchronous programming with `asyncio`, and Docker configuration.

### Step 1: Set Up the Project Structure

Create a directory structure like this:

```
product_catalog/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── database.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_routes.py
│
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

### Step 2: Define Dependencies

In `requirements.txt`, include:

```plaintext
Flask
Flask-SQLAlchemy
Flask-Migrate
asyncio
pytest
```

### Step 3: Create the Database Model

In `app/models.py`:

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    inventory_count = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'
```

### Step 4: Create the API Routes

In `app/routes.py`:

```python
from flask import Blueprint, request, jsonify
from .models import Product, db

api = Blueprint('api', __name__)

@api.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.id), 201

@api.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@api.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get_or_404(id)
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return jsonify(product.to_dict())

@api.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204

@api.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('q')
    results = Product.query.filter(Product.name.contains(query) | Product.description.contains(query)).all()
    return jsonify([product.to_dict() for product in results])
```

### Step 5: Initialize the Application

In `app/__init__.py`:

```python
from flask import Flask
from .database import db
from .routes import api

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
    db.init_app(app)
    app.register_blueprint(api, url_prefix='/api')
    return app
```

### Step 6: Docker Configuration

In `Dockerfile`:

```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
```

In `docker-compose.yml`:

```yaml
version: '3'
services:
  app:
    build: .
    ports:
      - "5000:5000"
```

### Step 7: Testing

In `tests/test_routes.py`:

```python
import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_product(client):
    response = client.post('/api/products', json={
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 9.99,
        'inventory_count': 100,
        'category': 'Test Category'
    })
    assert response.status_code == 201
```

### Step 8: Run the Application

Build and run your Docker container:

```bash
docker-compose up --build
```

### Step 9: Documentation

Use Swagger or Postman to document your API. Include endpoints, request/response formats, and any necessary authentication.

### Step 10: GitHub Repository

After completing your project, create a GitHub repository and push your code. Make sure to include a README file with instructions on how to set up and run your application.

### Conclusion

This setup provides a solid foundation for a REST API to manage a product catalog. You can expand upon it by adding features such as user authentication, more complex search capabilities, or real-time inventory updates using WebSockets.
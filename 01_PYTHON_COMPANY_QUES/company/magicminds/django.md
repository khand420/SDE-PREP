To create a REST API for managing a product catalog using Django, follow these steps. This will include setting up Django with Django REST Framework (DRF), defining models, creating views, and configuring Docker.

### Step 1: Set Up the Project Structure

Create a new Django project and app:

```bash
django-admin startproject product_catalog
cd product_catalog
django-admin startapp catalog
```

### Step 2: Install Dependencies

Add the following to your `requirements.txt`:

```plaintext
Django
djangorestframework
django-cors-headers
```

### Step 3: Configure Django Settings

In `product_catalog/settings.py`, add the new app and REST framework:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'catalog',
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True  # Adjust as needed
```

### Step 4: Create the Product Model

In `catalog/models.py`:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
```

### Step 5: Create Serializers

In `catalog/serializers.py`:

```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

### Step 6: Create Views

In `catalog/views.py`:

```python
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### Step 7: Set Up URLs

In `catalog/urls.py`:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

In `product_catalog/urls.py`, include the catalog URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('catalog.urls')),
]
```

### Step 8: Create Docker Configuration

In `Dockerfile`:

```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

In `docker-compose.yml`:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
```

### Step 9: Run Migrations

Run the following commands to set up the database:

```bash
docker-compose run web python manage.py migrate
```

### Step 10: Testing the API

You can use Postman or cURL to test the API endpoints:

- **Create Product**: `POST /api/products/`
- **Get Products**: `GET /api/products/`
- **Update Product**: `PUT /api/products/{id}/`
- **Delete Product**: `DELETE /api/products/{id}/`

### Step 11: Documentation

You can use tools like Swagger or DRF's built-in documentation features to document your API.

### Step 12: Push to GitHub

Create a GitHub repository and push your code. Include a README file with instructions on how to set up and run your application.

### Conclusion

This Django setup provides a robust foundation for a REST API to manage a product catalog. You can expand it further by adding features like user authentication, advanced search capabilities, and real-time inventory updates.



Here's a test case example and a README file for your Django REST API project.

### Test Cases

Create a file named `test_views.py` in the `tests` directory of your `catalog` app:

```python
# catalog/tests/test_views.py

from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTests(APITestCase):
    
    def setUp(self):
        self.product_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 9.99,
            'inventory_count': 100,
            'category': 'Test Category'
        }
        self.product = Product.objects.create(**self.product_data)

    def test_create_product(self):
        response = self.client.post('/api/products/', self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)  # 1 existing + 1 created
        self.assertEqual(Product.objects.get(id=response.data['id']).name, 'Test Product')

    def test_get_products(self):
        response = self.client.get('/api/products/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_product(self):
        updated_data = {'name': 'Updated Product'}
        response = self.client.put(f'/api/products/{self.product.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')

    def test_delete_product(self):
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
```

### README File

Create a file named `README.md` in the root of your project:

```markdown
# Product Catalog API

This is a Django REST API for managing a product catalog. It allows users to create, read, update, and delete products.

## Features

- Create a new product
- Retrieve a list of products
- Update existing products
- Delete products
- Search products by name and description

## Technologies Used

- Django
- Django REST Framework
- SQLite (default database)
- Docker

## Getting Started

### Prerequisites

- Python 3.x
- Docker (optional)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/khand420/
   cd product_catalog
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

You can run the application using Docker or directly with Django.

#### Using Docker

1. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```

2. Access the API at `http://localhost:8000/api/products/`

#### Without Docker

1. Run migrations:
   ```bash
   python manage.py migrate
   ```

2. Start the development server:
   ```bash
   python manage.py runserver
   ```

3. Access the API at `http://localhost:8000/api/products/`

### Running Tests

To run the tests, use the following command:

```bash
python manage.py test catalog
```

### API Endpoints

- **POST /api/products/**: Create a new product
- **GET /api/products/**: Retrieve a list of products
- **GET /api/products/{id}/**: Retrieve a specific product
- **PUT /api/products/{id}/**: Update a specific product
- **DELETE /api/products/{id}/**: Delete a specific product

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Conclusion

This should give you a solid foundation for testing and documenting your Django REST API. Adjust the content as needed to fit your project's specifics!
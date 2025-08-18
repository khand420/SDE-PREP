```
### Overview
The document outlines a project assignment for developing a system to process image data from CSV files. It details the requirements for asynchronous APIs, image processing, and database interactions, along with the expected input and output formats. The assignment emphasizes creating a robust architecture and thorough documentation.

### SDE 1 Assignment Backend.pdf
- **Objective:** The system aims to efficiently handle image data from CSV files, including validating, processing (compressing images), and storing the results in a database.
- **Input/Output Formats:** Clearly defined CSV formats for input and output, ensuring that processed images are linked to their respective products.
- **API Requirements:** Two main asynchronous APIs are required: an Upload API for CSV submissions and a Status API for checking processing status. A bonus feature includes implementing a webhook for post-processing notifications.
- **Low-Level Design (LLD):** The document specifies the need for a detailed technical design, including a visual diagram of the system architecture, component roles, and interactions.
- **Components:** Key components include the image processing service, webhook handling, database interaction, and API endpoints.
- **Database Schema:** A schema is needed to store product data and track processing requests, ensuring efficient data management.
- **Documentation:** Clear API specifications, descriptions of asynchronous worker functions, and a GitHub repository for project code are required, along with a Postman collection for API testing.

### Conclusion
The assignment provides a comprehensive framework for developing a backend system focused on image processing from CSV files. It emphasizes the importance of asynchronous operations, proper documentation, and a well-structured database to ensure efficiency and clarity in the development process.
```


Here's a detailed guide to creating the image processing project using Django. This will include setting up a Django project, creating models, views, and handling image processing.

### Project Structure

1. **Folder Structure**:
   ```
   image_processing_project/
   ├── image_processing/
   │   ├── migrations/
   │   ├── __init__.py
   │   ├── admin.py
   │   ├── apps.py
   │   ├── models.py
   │   ├── tests.py
   │   ├── views.py
   │   └── urls.py
   ├── uploads/
   ├── outputs/
   ├── image_processing_project/
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── manage.py
   ├── .env
   ├── requirements.txt
   └── README.md
   ```

### Step-by-Step Implementation

#### 1. Set Up Environment

```bash
mkdir image_processing_project
cd image_processing_project
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install django pandas Pillow python-dotenv
```

Create a `requirements.txt` file:

```
Django
pandas
Pillow
python-dotenv
```

#### 2. Create Django Project

```bash
django-admin startproject image_processing_project .
django-admin startapp image_processing
```

#### 3. Update Settings

In **image_processing_project/settings.py**, add the new app and configure media settings:

```python
import os
from dotenv import load_dotenv

load_dotenv()

INSTALLED_APPS = [
    ...
    'image_processing',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
```

#### 4. Create Models

In **image_processing/models.py**, define the Product model:

```python
from django.db import models

class Product(models.Model):
    serial_number = models.IntegerField()
    product_name = models.CharField(max_length=255)
    input_image_urls = models.TextField()  # Store as comma-separated URLs
    output_image_urls = models.TextField(blank=True)
    request_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='Processing')

    def __str__(self):
        return self.product_name
```

Run the following commands to create the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Create Views for Upload and Status

In **image_processing/views.py**, create the upload and status views:

```python
from django.http import JsonResponse
from django.views import View
from .models import Product
import pandas as pd
import os
import uuid
from .services import process_images

class UploadView(View):
    def post(self, request):
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file part'}, status=400)

        file = request.FILES['file']
        request_id = str(uuid.uuid4())
        file_path = os.path.join('uploads', file.name)
        
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Process the CSV file
        process_images(file_path, request_id)

        return JsonResponse({'requestId': request_id}, status=200)
```

#### 6. Implement Image Processing Logic

Create a new file **image_processing/services.py** for image processing:

```python
import pandas as pd
from PIL import Image
import os

def process_images(file_path, request_id):
    df = pd.read_csv(file_path)
    output_urls = []

    for index, row in df.iterrows():
        for url in row['Input Image Urls'].split(','):
            image_path = url.strip()  # Assuming URLs are local for simplicity
            output_image_path = os.path.join('outputs', f"output_{index}.jpg")

            # Compress the image
            with Image.open(image_path) as img:
                img = img.resize((int(img.width * 0.5), int(img.height * 0.5)))
                img.save(output_image_path, "JPEG", quality=50)

            output_urls.append(output_image_path)

    # Update the product in the database (you may want to save this data)
    # Example: Product.objects.create(...)
```

#### 7. Create URLs

In **image_processing/urls.py**, define the URL patterns:

```python
from django.urls import path
from .views import UploadView

urlpatterns = [
    path('upload/', UploadView.as_view(), name='upload'),
]
```

In **image_processing_project/urls.py**, include the app URLs:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('image_processing.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### 8. Testing

Create a `tests` directory and write unit tests for your views and processing logic.

#### 9. Documentation

Create a `README.md` file with setup instructions and usage examples. Document your APIs using Swagger or Postman.

#### 10. Deployment

Choose a platform (like Heroku, AWS, or DigitalOcean) to deploy your application.

### Conclusion

This guide provides a comprehensive approach to building the image processing project using Django. You can expand upon each section as needed, and if you have any specific questions or need further assistance, feel free to ask!
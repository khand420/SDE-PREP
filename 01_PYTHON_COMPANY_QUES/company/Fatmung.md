To create a website that meets the requirements outlined in your assignment, we'll break down the project into several key components. Below is an overview of the architecture, along with sample code snippets and a `docker-compose.yml` file.

### Project Structure

```
video_upload/
│
├── backend/
│   ├── manage.py
│   ├── video_upload/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── models.py
│   ├── videos/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   └── Dockerfile
│
├── frontend/
│   └── index.html
│
└── docker-compose.yml
```

### Backend (Django)

#### 1. **models.py**

```python
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    subtitles = models.TextField()
```

#### 2. **views.py**

```python
from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
import subprocess

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        video_instance = serializer.save()
        self.extract_subtitles(video_instance.video_file.path, video_instance)

    def extract_subtitles(self, video_path, video_instance):
        # Use ccextractor to extract subtitles
        subprocess.run(['ccextractor', video_path, '-o', 'subtitles.srt'])
        with open('subtitles.srt', 'r') as f:
            subtitles = f.read()
        video_instance.subtitles = subtitles
        video_instance.save()
```

#### 3. **serializers.py**

```python
from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
```

#### 4. **urls.py**

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet

router = DefaultRouter()
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### Docker Setup

#### 1. **Dockerfile**

```dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### 2. **docker-compose.yml**

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: video_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: ./backend
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgres://user:password@db:5432/video_db

volumes:
  postgres_data:
```

### Frontend (HTML)

#### 1. **index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Video Upload</title>
</head>
<body>
    <h1>Upload Video</h1>
    <form id="upload-form" enctype="multipart/form-data">
        <input type="file" name="video" required>
        <button type="submit">Upload</button>
    </form>
    <div id="video-list"></div>

    <script>
        document.getElementById('upload-form').onsubmit = async function (e) {
            e.preventDefault();
            const formData = new FormData(this);
            await fetch('/api/videos/', {
                method: 'POST',
                body: formData,
            });
            // Refresh video list
            fetchVideos();
        };

        async function fetchVideos() {
            const response = await fetch('/api/videos/');
            const videos = await response.json();
            const videoList = document.getElementById('video-list');
            videoList.innerHTML = '';
            videos.forEach(video => {
                const videoElement = document.createElement('div');
                videoElement.innerHTML = `<h2>${video.title}</h2><video src="${video.video_file}" controls></video>`;
                videoList.appendChild(videoElement);
            });
        }

        fetchVideos();
    </script>
</body>
</html>
```

### Final Steps

1. **Install Dependencies**: Create a `requirements.txt` file for the Django backend with the necessary packages (e.g., Django, djangorestframework, psycopg2).

2. **Run Docker**: Use `docker-compose up --build` to build and run the application.

3. **Test the Application**: Ensure the application can upload videos, extract subtitles, and display them correctly.

This structure provides a solid foundation for your project. You can further enhance the functionality based on your specific needs.
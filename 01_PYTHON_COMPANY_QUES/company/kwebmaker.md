Here's the complete code structure for your Django administrative panel assignment. I'll break down the core parts of the project:

### 1. **Django Project Setup**

Start by creating a Django project and app:
```bash
django-admin startproject admin_panel
cd admin_panel
python manage.py startapp partners
```

In `admin_panel/settings.py`, add `partners` to the `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'partners',
]
```

### 2. **Partner Model**

Create the `Partner` model inside `partners/models.py`:
```python
from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. **Authentication and Views**

In `partners/views.py`, create the views for login, dashboard, and partner management:

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Partner
from .forms import PartnerForm

# Admin Login
def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'partners/login.html', {'form': form})

# Dashboard
@login_required
def dashboard(request):
    partners_count = Partner.objects.count()
    partners = Partner.objects.all()
    return render(request, 'partners/dashboard.html', {'partners': partners, 'partners_count': partners_count})

# Partner List
@login_required
def partner_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        partners = Partner.objects.filter(name__icontains=search_query)
    else:
        partners = Partner.objects.all()
    return render(request, 'partners/partner_list.html', {'partners': partners})

# Add New Partner
@login_required
def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'partners/add_partner.html', {'form': form})

# Partner Details
@login_required
def partner_detail(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    return render(request, 'partners/partner_detail.html', {'partner': partner})

# Edit Partner
@login_required
def edit_partner(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'partners/edit_partner.html', {'form': form})
```

### 4. **Forms**

Create a form for the `Partner` model in `partners/forms.py`:

```python
from django import forms
from .models import Partner

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'contact_info']
```

### 5. **Templates**

#### Login Template (`partners/templates/partners/login.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

#### Dashboard Template (`partners/templates/partners/dashboard.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
</head>
<body>
    <h1>Admin Dashboard</h1>
    <p>Total Partners: {{ partners_count }}</p>
    <a href="{% url 'partner_list' %}">Manage Partners</a>
</body>
</html>
```

#### Partner List Template (`partners/templates/partners/partner_list.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Partner List</title>
</head>
<body>
    <h1>Partners</h1>
    <form method="get">
        <input type="text" name="search" placeholder="Search partners" value="{{ request.GET.search }}">
        <button type="submit">Search</button>
    </form>
    <ul>
        {% for partner in partners %}
        <li><a href="{% url 'partner_detail' partner.pk %}">{{ partner.name }}</a> | <a href="{% url 'edit_partner' partner.pk %}">Edit</a></li>
        {% endfor %}
    </ul>
    <a href="{% url 'add_partner' %}">Add New Partner</a>
</body>
</html>
```

#### Add Partner Template (`partners/templates/partners/add_partner.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add New Partner</title>
</head>
<body>
    <h1>Add Partner</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Add Partner</button>
    </form>
</body>
</html>
```

#### Partner Detail Template (`partners/templates/partners/partner_detail.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Partner Details</title>
</head>
<body>
    <h1>{{ partner.name }}</h1>
    <p>Contact Info: {{ partner.contact_info }}</p>
    <a href="{% url 'edit_partner' partner.pk %}">Edit</a>
</body>
</html>
```

### 6. **URLs Configuration**

In `partners/urls.py`, set up the URLs:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('partners/', views.partner_list, name='partner_list'),
    path('partners/add/', views.add_partner, name='add_partner'),
    path('partners/<int:pk>/', views.partner_detail, name='partner_detail'),
    path('partners/<int:pk>/edit/', views.edit_partner, name='edit_partner'),
]
```

In `admin_panel/urls.py`, include the app URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('partners.urls')),
]
```

### 7. **Run the Application**

1. Run the development server:
   ```bash
   python manage.py runserver
   ```

2. Visit `http://127.0.0.1:8000/login/` to access the login page and test the functionality.

### 8. **README and Setup**

In the project root, create a `README.md` file with instructions on setting up and running the project:
```md
# Django Admin Panel

## Requirements

- Python 3.x
- Django 4.x

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Apply migrations:
   ```bash
   python manage.py migrate
   ```

3. Run the server:
   ```bash
   python manage.py runserver
   ```

4. Access the application at `http://127.0.0.1:8000/`.

## Features

- Admin login and authentication
- Dashboard with system summary
- Partner management: list, add, edit, view
```

Let me know if you need further customization or clarification!
















To build the Django admin panel as described in the assignment, follow these steps:

### Step-by-Step Guide to Building a Django Admin Panel

1. **Set Up Your Django Environment**:
   - Install Django if you haven't already:
     ```bash
     pip install django
     ```
   - Create a new Django project:
     ```bash
     django-admin startproject admin_panel
     cd admin_panel
     ```
   - Create a new app for the admin functionalities:
     ```bash
     python manage.py startapp admin_app
     ```

2. **Configure Your Project**:
   - Add the new app to your project settings (`settings.py`):
     ```python
     INSTALLED_APPS = [
         ...
         'admin_app',
     ]
     ```

3. **Create Models**:
   - In `admin_app/models.py`, define the models for your partners:
     ```python
     from django.db import models

     class Partner(models.Model):
         name = models.CharField(max_length=100)
         contact_info = models.CharField(max_length=200)

         def __str__(self):
             return self.name
     ```

4. **Set Up User Authentication**:
   - Use Django’s built-in authentication system. In `admin_app/views.py`, create login views and templates:
     ```python
     from django.contrib.auth import authenticate, login
     from django.shortcuts import render, redirect

     def login_view(request):
         if request.method == 'POST':
             username = request.POST['username']
             password = request.POST['password']
             user = authenticate(request, username=username, password=password)
             if user is not None:
                 login(request, user)
                 return redirect('dashboard')
         return render(request, 'login.html')
     ```

5. **Create Templates**:
   - Create HTML templates for login, dashboard, partner listing, adding partners, and editing partners. For example, `login.html` might look like:
     ```html
     <form method="post">
         {% csrf_token %}
         <input type="text" name="username" placeholder="Username" required>
         <input type="password" name="password" placeholder="Password" required>
         <button type="submit">Login</button>
     </form>
     ```

6. **Create Views for Dashboard and Partner Management**:
   - In `admin_app/views.py`, implement views for the dashboard and partner management functionalities (listing, adding, editing):
     ```python
     from .models import Partner

     def dashboard_view(request):
         return render(request, 'index.html')

     def partner_list_view(request):
         partners = Partner.objects.all()
         return render(request, 'partner.html', {'partners': partners})

     def add_partner_view(request):
         if request.method == 'POST':
             name = request.POST['name']
             contact_info = request.POST['contact_info']
             Partner.objects.create(name=name, contact_info=contact_info)
             return redirect('partner_list')
         return render(request, 'add_new_partner.html')
     ```

7. **Set Up URLs**:
   - In `admin_app/urls.py`, define the URL patterns for your views:
     ```python
     from django.urls import path
     from .views import login_view, dashboard_view, partner_list_view, add_partner_view

     urlpatterns = [
         path('login/', login_view, name='login'),
         path('dashboard/', dashboard_view, name='dashboard'),
         path('partners/', partner_list_view, name='partner_list'),
         path('add_partner/', add_partner_view, name='add_partner'),
     ]
     ```

8. **Run Migrations**:
   - Create the database tables for your models:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

9. **Run the Development Server**:
   - Start the server to test your application:
     ```bash
     python manage.py runserver
     ```

10. **Testing and Validation**:
    - Ensure all functionalities work as expected, including user login, partner listing, adding, and editing partners.

### Conclusion
By following these steps, you will have built a basic administrative panel using Django that meets the assignment's requirements. Make sure to incorporate security best practices and validate inputs as per the guidelines.




Here’s a sample README file for your Django admin panel project:

```markdown
# Django Admin Panel

## Overview
This project is a basic administrative panel built using Django. It includes functionalities for user authentication, a dashboard, and partner management.

## Features
- **Admin Login**: Secure login for admin users with authentication.
- **Dashboard**: Overview of the system status and recent activities.
- **Partner Management**:
  - Listing of partners with search/filter functionality.
  - Add new partners with input validation.
  - Edit partner details.
  - View detailed information for individual partners.

## Requirements
- Python 3.x
- Django 3.x or later

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/khand420/admin_panel.git
   cd admin_panel
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install django
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/login/` to access the login page.

   - username admin
   - password 123

## Usage
- Log in with your admin credentials.
- Navigate through the dashboard to manage partners.

## Contributing
If you wish to contribute, please fork the repository and submit a pull request.


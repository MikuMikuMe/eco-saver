Creating a complete Django-based web application like "Eco-Saver" is a comprehensive task. Below, I will outline a simplified version of such a system with essential components and provide a basic implementation. This project may require further expansions and refinements based on specific IoT integrations and predictive analytics methods you wish to employ.

### Prerequisites
- Python 3.x
- Django
- Django REST Framework
- pandas or numpy for data processing
- A database like SQLite (default), PostgreSQL, etc.
- Required libraries for IoT devices (mocked for this example)

### Setup and Project Structure
1. **Create a Django project and application:**
   ```bash
   django-admin startproject ecosaver
   cd ecosaver
   django-admin startapp energy
   ```

2. **Directory Structure:**
   ```
   ecosaver/
       ecosaver/
           __init__.py
           settings.py
           urls.py
           wsgi.py
       energy/
           migrations/
           __init__.py
           admin.py
           apps.py
           models.py
           tests.py
           views.py
           urls.py
       manage.py
   ```

3. **Install Required Packages:**
   ```bash
   pip install django djangorestframework pandas
   ```

### Implementation

#### 1. settings.py
Add `energy` and the REST framework to the `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'energy',
]
```

#### 2. models.py
Define models to store device data and energy records:
```python
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EnergyUsage(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    energy_consumed = models.FloatField()  # kWh or similar

    class Meta:
        ordering = ['-timestamp']
```

#### 3. serializers.py
Create serializers for API endpoints:
```python
from rest_framework import serializers
from .models import Device, EnergyUsage

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class EnergyUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyUsage
        fields = '__all__'
```

#### 4. views.py
Create views to manage API requests:
```python
from rest_framework import viewsets
from .models import Device, EnergyUsage
from .serializers import DeviceSerializer, EnergyUsageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class EnergyUsageViewSet(viewsets.ModelViewSet):
    queryset = EnergyUsage.objects.all()
    serializer_class = EnergyUsageSerializer

@api_view(['GET'])
def optimize_energy(request):
    try:
        # Mocked optimization logic
        # Use pandas or numpy for real implementation logic
        optimization_message = {"status": "success", "message": "Energy optimization in progress."}
        return Response(optimization_message)
    except Exception as e:
        # Error handling
        error_message = {"status": "error", "message": str(e)}
        return Response(error_message, status=500)
```

#### 5. urls.py
Set-up the URL routing:
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'devices', views.DeviceViewSet)
router.register(r'energy-usage', views.EnergyUsageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('optimize/', views.optimize_energy),
]
```

#### 6. admin.py
Register models with the Django admin:
```python
from django.contrib import admin
from .models import Device, EnergyUsage

admin.site.register(Device)
admin.site.register(EnergyUsage)
```

### Running the Application
1. **Migrate the Database:**
   ```bash
   python manage.py migrate
   ```

2. **Create a Superuser (to access the admin site):**
   ```bash
   python manage.py createsuperuser
   ```

3. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

4. **Access the Application:**
   - Navigate to `http://127.0.0.1:8000/admin` to manage devices and energy usage.
   - API endpoints are accessible at `http://127.0.0.1:8000/devices`, `http://127.0.0.1:8000/energy-usage`, and `http://127.0.0.1:8000/optimize`.

### Note
- This is a basic starting point; real-world IoT integration would involve additional modules for communicating with devices.
- Predictive analytics using existing energy data can be implemented using libraries like scikit-learn for machine learning models.
- Error handling has been added in views, but further refinement and testing are necessary for a production environment.
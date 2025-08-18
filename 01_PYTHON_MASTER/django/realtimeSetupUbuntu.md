Setting up a real-time analytics system on Ubuntu involves several steps, including installing necessary software, configuring services, and writing code for data ingestion, processing, and visualization. Below is a step-by-step guide to help you set this up.

### Step 1: Set Up Your Environment

1. **Update Your System**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Java (for Kafka and Spark)**:
   Kafka and Spark require Java. Install OpenJDK:
   ```bash
   sudo apt install openjdk-11-jdk -y
   ```

3. **Install Python and Pip**:
   Ensure you have Python and pip installed for Django and other Python packages.
   ```bash
   sudo apt install python3 python3-pip -y
   ```

4. **Install Redis**:
   Redis will be used for caching and real-time data storage.
   ```bash
   sudo apt install redis-server -y
   ```

5. **Install PostgreSQL (optional)**:
   If you're using a relational database for your main data store, you can install PostgreSQL.
   ```bash
   sudo apt install postgresql postgresql-contrib -y
   ```

### Step 2: Install and Configure Kafka

1. **Download Kafka**:
   ```bash
   wget https://downloads.apache.org/kafka/3.5.0/kafka_2.12-3.5.0.tgz
   tar -xzf kafka_2.12-3.5.0.tgz
   cd kafka_2.12-3.5.0
   ```

2. **Start Zookeeper and Kafka**:
   Open two terminal windows or tabs. In the first terminal, start Zookeeper:
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```

   In the second terminal, start Kafka:
   ```bash
   bin/kafka-server-start.sh config/server.properties
   ```

3. **Create a Kafka Topic**:
   ```bash
   bin/kafka-topics.sh --create --topic analytics_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

### Step 3: Install and Configure Apache Spark

1. **Download and Install Spark**:
   ```bash
   wget https://downloads.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
   tar -xzf spark-3.5.0-bin-hadoop3.tgz
   cd spark-3.5.0-bin-hadoop3
   ```

2. **Start Spark**:
   ```bash
   ./bin/spark-shell
   ```

### Step 4: Set Up Django with Channels

1. **Create a Django Project**:
   ```bash
   pip install django channels channels-redis
   django-admin startproject myproject
   cd myproject
   ```

2. **Install Django and Redis Packages**:
   ```bash
   pip install django djangorestframework
   ```

3. **Configure Django Settings**:
   In `myproject/settings.py`, add channels and configure Redis as the channel layer:
   ```python
   INSTALLED_APPS = [
       ...
       'channels',
       ...
   ]

   ASGI_APPLICATION = 'myproject.asgi.application'

   CHANNEL_LAYERS = {
       'default': {
           'BACKEND': 'channels_redis.core.RedisChannelLayer',
           'CONFIG': {
               "hosts": [('127.0.0.1', 6379)],
           },
       },
   }
   ```

4. **Create ASGI Configuration**:
   Create a file named `asgi.py` in the `myproject` directory:
   ```python
   import os
   from django.core.asgi import get_asgi_application
   from channels.routing import ProtocolTypeRouter, URLRouter
   from channels.auth import AuthMiddlewareStack
   from myapp.consumers import AnalyticsConsumer  # Import your consumer

   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

   application = ProtocolTypeRouter({
       "http": get_asgi_application(),
       "websocket": AuthMiddlewareStack(
           URLRouter(
               [
                   path("ws/analytics/", AnalyticsConsumer.as_asgi()),
               ]
           )
       ),
   })
   ```

5. **Create a Consumer**:
   In your Django app (create one if you don’t have it):
   ```python
   from channels.generic.websocket import AsyncWebsocketConsumer
   import json

   class AnalyticsConsumer(AsyncWebsocketConsumer):
       async def connect(self):
           await self.accept()

       async def disconnect(self, close_code):
           pass

       async def send_analytics_update(self, data):
           await self.send(text_data=json.dumps(data))
   ```

### Step 5: Set Up Frontend for Real-Time Updates

1. **Create a Simple HTML Page**:
   Create an `index.html` file in your Django templates directory:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Real-Time Analytics</title>
   </head>
   <body>
       <h1>Real-Time Analytics Dashboard</h1>
       <div id="data"></div>
       <script>
           const socket = new WebSocket('ws://localhost:8000/ws/analytics/');

           socket.onmessage = function(event) {
               const data = JSON.parse(event.data);
               document.getElementById('data').innerHTML += '<p>' + data + '</p>';
           };
       </script>
   </body>
   </html>
   ```

### Step 6: Run Everything

1. **Run Redis**:
   Make sure Redis is running:
   ```bash
   sudo service redis-server start
   ```

2. **Run Django Development Server**:
   Open a terminal in your Django project directory and run:
   ```bash
   python manage.py runserver
   ```

3. **Run Kafka and Spark**:
   Ensure Kafka and Spark are running as described in earlier steps.

### Step 7: Testing

1. **Send Data to Kafka**:
   You can write a simple Python script to send data to your Kafka topic.

2. **Consume Data with Spark**:
   Write a Spark application that consumes data from Kafka and processes it.

3. **Open Your Dashboard**:
   Open your web browser and navigate to `http://localhost:8000/` to view the real-time analytics dashboard.

### Conclusion

This setup provides a robust foundation for real-time analytics using Ubuntu, Django, Kafka, and Spark. You can further enhance and customize the system based on your specific requirements, including advanced data processing, visualization, and scaling strategies.
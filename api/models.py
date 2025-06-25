from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # automatic date+time
    sensor_type = models.CharField(max_length=50)        # e.g., 'ldr', 'pir1'
    value = models.CharField(max_length=100)             # e.g., '980', 'ON'

    def __str__(self):
        return f"{self.timestamp} - {self.sensor_type}: {self.value}"

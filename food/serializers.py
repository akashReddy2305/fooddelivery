# from rest_framework import serializers
from models import Organization
organizations = Organization.objects.all()
print(organizations)
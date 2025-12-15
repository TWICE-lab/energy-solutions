import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.core.models import Course, Service, Project, TeamMember

# Clear existing data
Course.objects.all().delete()
Service.objects.all().delete()
Project.objects.all().delete()
TeamMember.objects.all().delete()

# Add Sample Courses
courses = [
    Course(title="Solar Energy Fundamentals", description="Learn the basics of solar energy systems and how they work.", duration=40, price=199.99),
    Course(title="Wind Power Systems", description="Comprehensive guide to wind turbines and renewable wind energy.", duration=35, price=179.99),
    Course(title="Energy Storage Solutions", description="Explore battery storage and grid-scale energy storage technologies.", duration=45, price=249.99),
]
Course.objects.bulk_create(courses)
print("Added 3 sample courses")

# Add Sample Services
services = [
    Service(name="Solar Installation", description="Professional solar panel installation for residential and commercial properties.", icon="sun", price=5000),
    Service(name="Energy Audit", description="Complete energy efficiency assessment for your property.", icon="chart", price=500),
    Service(name="Wind Turbine Setup", description="Installation and maintenance of wind turbine systems.", icon="wind", price=8000),
    Service(name="Battery Storage", description="Advanced battery storage system installation and optimization.", icon="battery", price=6000),
]
Service.objects.bulk_create(services)
print("Added 4 sample services")

# Add Sample Projects
projects = [
    Project(title="Downtown Solar Farm", description="Large-scale solar installation providing clean energy to 500+ homes.", client="City Energy Corp", completion_date="2024-06-15", featured=True),
    Project(title="Residential Wind Turbine", description="Installation of 5kW wind turbine for sustainable home energy.", client="Green Living Inc", completion_date="2024-03-20", featured=True),
    Project(title="Commercial Energy Storage", description="100kWh battery storage system for factory peak demand management.", client="Manufacturing Solutions Ltd", completion_date="2024-08-30", featured=False),
    Project(title="Grid-Scale Solar", description="25MW solar farm connected to the main power grid.", client="National Energy Authority", completion_date="2024-11-10", featured=True),
]
Project.objects.bulk_create(projects)
print("Added 4 sample projects")

# Add Sample Team Members
team = [
    TeamMember(name="John Smith", position="Solar Energy Expert", bio="20+ years experience in renewable energy systems.", email="john@energysolutions.com"),
    TeamMember(name="Sarah Johnson", position="Wind Power Specialist", bio="Expert in wind turbine design and installation.", email="sarah@energysolutions.com"),
    TeamMember(name="Mike Davis", position="Energy Engineer", bio="Electrical engineer specializing in grid integration.", email="mike@energysolutions.com"),
    TeamMember(name="Emma Wilson", position="Project Manager", bio="Manages large-scale renewable energy projects.", email="emma@energysolutions.com"),
]
TeamMember.objects.bulk_create(team)
print("Added 4 team members")

print("\nDatabase populated successfully!")
print("Visit http://localhost:8000/api/ to see your data")

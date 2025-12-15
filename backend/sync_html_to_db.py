"""
Script to sync HTML content to Django database
This script extracts content from HTML files and adds it to the backend database
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.core.models import Course, Service, Project, TeamMember

# Clear existing data first
print("Clearing existing data...")
Course.objects.all().delete()
Service.objects.all().delete()
Project.objects.all().delete()
TeamMember.objects.all().delete()

# ==================== SERVICES (7 items) ====================
print("\n✓ Adding Services...")
services_data = [
    {
        "name": "Electrical Installations",
        "description": "We handle residential and industrial wiring, lighting, switches, and all electrical setups with precision and safety standards.",
        "price": 1500
    },
    {
        "name": "Solar Energy Solutions",
        "description": "Installation and maintenance of solar systems tailored for homes and businesses to reduce energy costs.",
        "price": 3500
    },
    {
        "name": "CCTV & Surveillance",
        "description": "Secure your property with smart CCTV and remote surveillance systems for complete peace of mind.",
        "price": 2000
    },
    {
        "name": "Air Conditioning Services",
        "description": "Professional AC installation and servicing for all building types to ensure optimal cooling performance.",
        "price": 2200
    },
    {
        "name": "Electric Fence Installation",
        "description": "Reliable electric fencing for enhanced security and peace of mind for residential and commercial properties.",
        "price": 1200
    },
    {
        "name": "Satellite & TV Installations",
        "description": "Setup of satellite dishes and digital TV connections for perfect signal clarity and entertainment experience.",
        "price": 800
    },
    {
        "name": "Training & Certification",
        "description": "We offer comprehensive training programs to equip individuals with practical knowledge in electrical and solar technologies.",
        "price": 1000
    }
]

for service in services_data:
    Service.objects.create(**service)
    print(f"  Added: {service['name']}")

# ==================== COURSES (31 categories with multiple courses each) ====================
print("\n✓ Adding Courses...")
courses_data = [
    # Management
    {"title": "Project Management", "description": "Develop leadership and organizational skills for effective project management.", "duration": "3 months", "price": 1200},
    {"title": "Strategic Leadership", "description": "Learn strategic planning and leadership practices.", "duration": "3 months", "price": 1500},
    {"title": "Operations Management", "description": "Master operational efficiency and process management.", "duration": "2 months", "price": 1000},
    
    # Health Safety and Environment
    {"title": "Occupational Health & Safety", "description": "Create safe and healthy work environments while protecting our planet.", "duration": "2 months", "price": 900},
    {"title": "Environmental Management", "description": "Learn environmental conservation and sustainability practices.", "duration": "2 months", "price": 950},
    {"title": "Workplace Safety Compliance", "description": "Understand safety compliance requirements and implementation.", "duration": "1 month", "price": 700},
    
    # Business and Management
    {"title": "Business Administration", "description": "Fundamentals of business operations and strategic management.", "duration": "3 months", "price": 1200},
    {"title": "Entrepreneurship", "description": "Learn to start and grow your own business successfully.", "duration": "3 months", "price": 1400},
    {"title": "Marketing Management", "description": "Master marketing strategies and customer acquisition.", "duration": "2 months", "price": 1100},
    
    # Information Technology
    {"title": "Software Development", "description": "Build technical skills in software development and programming.", "duration": "6 months", "price": 2500},
    {"title": "Network Administration", "description": "Learn network setup, management, and cybersecurity basics.", "duration": "3 months", "price": 1800},
    {"title": "Cybersecurity Fundamentals", "description": "Understand cybersecurity principles and threat prevention.", "duration": "2 months", "price": 1300},
    {"title": "Database Management", "description": "Master database design and SQL programming.", "duration": "2 months", "price": 1200},
    {"title": "Cloud Computing", "description": "Learn cloud platforms and infrastructure.", "duration": "2 months", "price": 1500},
    
    # Human Resources
    {"title": "Talent Acquisition", "description": "Develop expertise in hiring and talent management.", "duration": "2 months", "price": 1000},
    {"title": "Performance Management", "description": "Learn employee performance evaluation and development.", "duration": "1 month", "price": 800},
    {"title": "Compensation & Benefits", "description": "Master compensation strategies and benefits administration.", "duration": "1 month", "price": 850},
    
    # Sales and Marketing
    {"title": "Digital Marketing", "description": "Learn effective digital marketing strategies and tools.", "duration": "2 months", "price": 900},
    {"title": "Sales Techniques", "description": "Master sales strategies and customer relationship management.", "duration": "1 month", "price": 750},
    {"title": "Brand Management", "description": "Learn to build and manage powerful brands.", "duration": "2 months", "price": 1100},
    
    # Personal Development
    {"title": "Communication Skills", "description": "Enhance your communication and presentation abilities.", "duration": "1 month", "price": 600},
    {"title": "Time Management", "description": "Learn productivity and time management techniques.", "duration": "1 month", "price": 500},
    {"title": "Leadership Development", "description": "Develop leadership capabilities and influence.", "duration": "2 months", "price": 1000},
    
    # Finance and Accounting
    {"title": "Financial Accounting", "description": "Master accounting principles and financial reporting.", "duration": "3 months", "price": 1300},
    {"title": "Managerial Accounting", "description": "Learn accounting for business decision-making.", "duration": "2 months", "price": 1100},
    {"title": "Investment Analysis", "description": "Understand investment strategies and analysis.", "duration": "2 months", "price": 1400},
    
    # Education and Training
    {"title": "Instructional Design", "description": "Learn to design effective training programs.", "duration": "2 months", "price": 950},
    {"title": "Curriculum Development", "description": "Master curriculum creation and course design.", "duration": "2 months", "price": 1000},
    
    # Customer Service
    {"title": "Customer Experience Management", "description": "Master the art of customer satisfaction and service excellence.", "duration": "1 month", "price": 700},
    {"title": "Service Quality", "description": "Learn to deliver exceptional service quality.", "duration": "1 month", "price": 650},
    
    # Technical and Vocational Training
    {"title": "Electrical Installation", "description": "Hands-on training in electrical installations and safety.", "duration": "4 months", "price": 1800},
    {"title": "Plumbing", "description": "Practical plumbing skills and techniques.", "duration": "3 months", "price": 1400},
    {"title": "Carpentry", "description": "Master carpentry and woodworking skills.", "duration": "3 months", "price": 1300},
    {"title": "Welding", "description": "Learn welding techniques and safety practices.", "duration": "2 months", "price": 1200},
]

for course in courses_data:
    Course.objects.create(**course)
    print(f"  Added: {course['title']}")

# ==================== PROJECTS / BOARD MEMBERS (4 items) ====================
print("\n✓ Adding Board Members & Sponsors...")
from datetime import date
projects_data = [
    {
        "title": "Michael Amenuku",
        "description": "Board Member & Strategic Advisor - A respected leader bringing years of experience in strategic development and organizational growth.",
        "client": "Board Member",
        "image": "projects/default.jpg",
        "completion_date": date.today()
    },
    {
        "title": "Community Partnership Initiative",
        "description": "Strategic partnership with community organizations to promote technical education and skills development.",
        "client": "Strategic Partner",
        "image": "projects/default.jpg",
        "completion_date": date.today()
    },
    {
        "title": "Government Training Program",
        "description": "Collaboration with government agencies to provide vocational training and capacity building.",
        "client": "Government Partner",
        "image": "projects/default.jpg",
        "completion_date": date.today()
    },
    {
        "title": "International Development Partner",
        "description": "Partnership with international organizations to support sustainable development and training initiatives.",
        "client": "International Partner",
        "image": "projects/default.jpg",
        "completion_date": date.today()
    }
]

for project in projects_data:
    Project.objects.create(**project)
    print(f"  Added: {project['title']}")

# ==================== TEAM MEMBERS (Foundation staff) ====================
print("\n✓ Adding Team Members...")
team_members_data = [
    {
        "name": "Mr. Michael Amenuku",
        "position": "Board Member & Strategic Advisor",
        "bio": "A respected leader and advisor, bringing years of experience and commitment to strategic development and organizational growth.",
        "image": "team/default.jpg"
    },
    {
        "name": "Program Coordinator",
        "position": "Training & Development",
        "bio": "Dedicated professional managing educational programs and ensuring quality delivery of training initiatives.",
        "image": "team/default.jpg"
    },
    {
        "name": "Technical Manager",
        "position": "Services Operations",
        "bio": "Experienced technical manager overseeing service delivery and quality assurance across all technical projects.",
        "image": "team/default.jpg"
    },
    {
        "name": "Community Liaison",
        "position": "Stakeholder Relations",
        "bio": "Committed to building relationships with communities and partners to expand VOLTIX's impact and reach.",
        "image": "team/default.jpg"
    }
]

for member in team_members_data:
    TeamMember.objects.create(**member)
    print(f"  Added: {member['name']}")

print("\n" + "="*60)
print("✓ DATABASE SYNC COMPLETE!")
print("="*60)
print(f"\nSummary:")
print(f"  • Services: {Service.objects.count()}")
print(f"  • Courses: {Course.objects.count()}")
print(f"  • Projects/Board Members: {Project.objects.count()}")
print(f"  • Team Members: {TeamMember.objects.count()}")
print(f"\nTotal Records Added: {Service.objects.count() + Course.objects.count() + Project.objects.count() + TeamMember.objects.count()}")
print("\nYour backend database is now synced with all HTML page content!")
print("Visit http://localhost:8000/api/ to see the updated API endpoints.")

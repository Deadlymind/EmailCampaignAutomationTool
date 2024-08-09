from django.core.management.base import BaseCommand
from dataentry.models import Company
import csv
import os
import pandas as pd

class Command(BaseCommand):
    help = "Imports data from a CSV or XLSX file into the Company model"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV or XLSX file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == '.csv':
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.create_company_record(row)
        elif file_extension in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path)
            for _, row in df.iterrows():
                self.create_company_record(row)
        else:
            self.stdout.write(self.style.ERROR('Unsupported file format. Please provide a CSV or XLSX file.'))
            return

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))

    def create_company_record(self, row):
        # Convert rating to float if it contains a comma
        rating = row.get('Rating')
        if rating and isinstance(rating, str):
            rating = rating.replace(',', '.')

        # Convert latitude and longitude to float if they contain commas
        latitude = row.get('Latitude')
        if latitude and isinstance(latitude, str):
            latitude = latitude.replace(',', '.')
        
        longitude = row.get('Longitude')
        if longitude and isinstance(longitude, str):
            longitude = longitude.replace(',', '.')

        Company.objects.create(
            title=row.get('Title'),
            address=row.get('Address'),
            category=row.get('Category'),
            located_in=row.get('Located_in'),
            pricing=row.get('Pricing'),
            website=row.get('Website'),
            email=row.get('Email'),
            phone=row.get('Phone'),
            facebook=row.get('Facebook'),
            instagram=row.get('Instagram'),
            twitter=row.get('Twitter'),
            linkedin=row.get('Linked In'),
            youtube=row.get('You Tube'),
            contact_us=row.get('Contact_US'),
            rating=float(rating) if rating else None,
            num_reviews=row.get('#_Reviews'),
            images=row.get('Images'),
            business_hours=row.get('Bussiness_Hours'),
            latitude=float(latitude) if latitude else None,
            longitude=float(longitude) if longitude else None,
            google_maps_link=row.get('Google_maps_Link'),
            google_my_maps_link=row.get('Google_My_maps_Link'),
            keyword=row.get('Keyword'),
            location=row.get('Location')
        )

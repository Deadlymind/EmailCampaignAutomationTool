from django.core.management.base import BaseCommand
from dataentry.models import Company

# Custom command to add data to the Company model

class Command(BaseCommand):
    help = 'Inserts data to the database'

    def handle(self, *args, **kwargs):
        dataset = [
            {
                'title': 'BioEnergie Bittelbronn eG',
                'address': 'Bauernfeld 1, 72401 Haigerloch, Allemagne',
                'category': 'Solutions et équipement énergétiques à Haigerloch, Allemagne',
                'located_in': '',
                'pricing': '',
                'website': '',
                'email': '',
                'phone': '+49 7474 9532180',
                'facebook': '',
                'instagram': '',
                'twitter': '',
                'linkedin': '',
                'youtube': '',
                'contact_us': '',
                'rating': 5.0,
                'num_reviews': '2 - Review(s)',
                'images': 'https://lh5.googleusercontent.com/p/AF1QipNLNNv0zOxzkWedPJdMFl_EdhSE6PoNvbGsgvJc=s1200-w1200',
                'business_hours': '',
                'latitude': 48.3790,
                'longitude': 8.76225,
                'google_maps_link': 'https://www.google.com/maps?cid=12634169362579501166',
                'google_my_maps_link': 'https://www.google.com/maps?cid=12634169362579501166',
                'keyword': '- Biomasse',
                'location': '- Baden-Württemberg'
            },
            # Add more entries here...
        ]
        
        for data in dataset:
            title = data['title']
            existing_record = Company.objects.filter(title=title).exists()

            if not existing_record:
                Company.objects.create(
                    title=data['title'],
                    address=data['address'],
                    category=data['category'],
                    located_in=data['located_in'],
                    pricing=data['pricing'],
                    website=data['website'],
                    email=data['email'],
                    phone=data['phone'],
                    facebook=data['facebook'],
                    instagram=data['instagram'],
                    twitter=data['twitter'],
                    linkedin=data['linkedin'],
                    youtube=data['youtube'],
                    contact_us=data['contact_us'],
                    rating=data['rating'],
                    num_reviews=data['num_reviews'],
                    images=data['images'],
                    business_hours=data['business_hours'],
                    latitude=data['latitude'],
                    longitude=data['longitude'],
                    google_maps_link=data['google_maps_link'],
                    google_my_maps_link=data['google_my_maps_link'],
                    keyword=data['keyword'],
                    location=data['location']
                )
            else:
                self.stdout.write(self.style.WARNING(f"Record with title '{title}' already exists in the database."))

        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))

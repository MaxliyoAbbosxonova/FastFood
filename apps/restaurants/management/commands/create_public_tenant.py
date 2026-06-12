import os
from django.core.management.base import BaseCommand
from restaurants.models import Restaurants, Domain


class Command(BaseCommand):
    help = "Create the public tenant if it doesn't exist"

    def handle(self, *args, **options):
        self.stdout.write("Creating public tenant...")

        environment = os.getenv("ENVIRONMENT", "dev")

        if environment == "prod":
            domain_name = "production-domain.com"
        elif environment == "staging":
            domain_name = "staging-domain.com"
        else:
            domain_name = "localhost"

        # ✅ 1. Public tenant yaratish (HAMMA ENV UCHUN)
        public_tenant, created = Restaurants.objects.get_or_create(
            schema_name="public",
            defaults={"name": "Public"},
        )

        if created:
            self.stdout.write(self.style.SUCCESS("Public tenant created"))
        else:
            self.stdout.write("Public tenant already exists")

        # ✅ 2. Domain yaratish / olish
        domain, domain_created = Domain.objects.get_or_create(
            domain=domain_name,
            tenant=public_tenant,
            defaults={"is_primary": True},
        )

        # ✅ 3. ensure primary
        domain.is_primary = True
        domain.save()

        self.stdout.write(
            self.style.SUCCESS(f"Domain set: {domain}")
        )
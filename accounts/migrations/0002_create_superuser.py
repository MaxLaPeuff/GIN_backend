from django.db import migrations
from django.contrib.auth.models import User

def create_superuser(apps, schema_editor):
    User.objects.create_superuser(
        username='admin',
        email='maxaraye18@gmail.com',
        password='admin'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),  # À ajuster
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]

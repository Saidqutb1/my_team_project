# Generated by Django 5.0.6 on 2024-06-05 22:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'category_products',
            },
        ),
        migrations.CreateModel(
            name='ColorProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'color_product',
            },
        ),
        migrations.CreateModel(
            name='Lather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'lather',
            },
        ),
        migrations.CreateModel(
            name='MadeCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'made_company',
            },
        ),
        migrations.CreateModel(
            name='MadeCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'made_country',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'season',
            },
        ),
        migrations.CreateModel(
            name='SizeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'size_product',
            },
        ),
        migrations.CreateModel(
            name='TypeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'type_product',
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_image/')),
                ('price', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproducts')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.colorproduct')),
                ('lather', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.lather')),
                ('made_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.madecompany')),
                ('made_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.madecountry')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.season')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sizeproduct')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.typeproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.painting')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.shoes')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]

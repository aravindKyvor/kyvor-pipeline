# Generated by Django 3.0.8 on 2022-06-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KyvorPipeline', '0006_fdareports'),
    ]

    operations = [
        migrations.CreateModel(
            name='FDA_Sheets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('GENE', models.CharField(blank=True, max_length=200, null=True)),
                ('BIOMARKER', models.CharField(blank=True, max_length=200, null=True)),
                ('VARIANT_CDS', models.CharField(blank=True, max_length=200, null=True)),
                ('THERAPY', models.TextField()),
                ('EVIDENCE_STATEMENT_1', models.TextField()),
                ('EVIDENCE_STATEMENT_2', models.TextField()),
                ('Status', models.CharField(blank=True, max_length=200, null=True)),
                ('AF_VAF', models.CharField(blank=True, max_length=200, null=True)),
                ('CANCER_TYPES', models.CharField(blank=True, max_length=800, null=True)),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2022-06-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KyvorPipeline', '0008_clinical_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='INDEL_datas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('GENE', models.CharField(blank=True, max_length=400, null=True)),
                ('AMINO_ACID_CHANGE', models.CharField(blank=True, max_length=500, null=True)),
                ('CDS', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SNV_datas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('GENE', models.CharField(blank=True, max_length=400, null=True)),
                ('AMINO_ACID_CHANGE', models.CharField(blank=True, max_length=500, null=True)),
                ('CDS', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]

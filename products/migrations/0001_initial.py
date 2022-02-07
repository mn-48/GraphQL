# Generated by Django 3.2.9 on 2022-02-07 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('picture_path', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('pack_size', models.CharField(blank=True, max_length=250, null=True)),
                ('warning_qty', models.PositiveIntegerField()),
                ('model_no', models.CharField(blank=True, max_length=250, null=True)),
                ('unit_type', models.CharField(blank=True, max_length=250, null=True)),
                ('short_qty', models.PositiveIntegerField(default=0)),
                ('box_qty', models.PositiveIntegerField(default=1)),
                ('product_type', models.CharField(choices=[('serial_No', 'serial_no'), ('Bar_Code', 'bar_code'), ('No_Bar_Code', 'no_bar_code')], max_length=20)),
                ('extra_field', models.JSONField(blank=True, default=dict, null=True)),
                ('compressor_warrenty', models.PositiveIntegerField(default=0)),
                ('compressor_warrenty_duration', models.CharField(blank=True, choices=[('YEAR', 'Year'), ('MONTH', 'Month'), ('WEEK', 'Week'), ('DAY', 'Day')], max_length=20, null=True)),
                ('panel_warrenty', models.PositiveIntegerField(default=0)),
                ('panel_warrenty_duration', models.CharField(blank=True, choices=[('YEAR', 'Year'), ('MONTH', 'Month'), ('WEEK', 'Week'), ('DAY', 'Day')], max_length=20, null=True)),
                ('motor_warrenty', models.PositiveIntegerField(default=0)),
                ('motor_warrenty_duration', models.CharField(blank=True, choices=[('YEAR', 'Year'), ('MONTH', 'Month'), ('WEEK', 'Week'), ('DAY', 'Day')], max_length=20, null=True)),
                ('spare_parts_warrenty', models.PositiveIntegerField(default=0)),
                ('spare_warrenty_duration', models.CharField(blank=True, choices=[('YEAR', 'Year'), ('MONTH', 'Month'), ('WEEK', 'Week'), ('DAY', 'Day')], max_length=20, null=True)),
                ('service_warrenty', models.PositiveIntegerField(default=0)),
                ('service_warrenty_duration', models.CharField(blank=True, choices=[('YEAR', 'Year'), ('MONTH', 'Month'), ('WEEK', 'Week'), ('DAY', 'Day')], max_length=20, null=True)),
                ('extra_warrenty', models.JSONField(blank=True, default=dict, null=True)),
                ('qrcode_image', models.ImageField(blank=True, null=True, upload_to='qrcode/')),
                ('barcode_image', models.ImageField(blank=True, null=True, upload_to='barcode/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.company')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]

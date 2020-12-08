# Generated by Django 3.1.3 on 2020-12-07 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0004_auto_20201130_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'attendance_labels',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_at', models.IntegerField()),
                ('finish_at', models.IntegerField(null=True)),
                ('total_pause', models.DurationField(null=True)),
                ('content', models.TextField(null=True)),
                ('amended_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='amended_by', to='employee.employee')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('label', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='attendance.attendancelabel')),
                ('written_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='written_by', to='employee.employee')),
            ],
            options={
                'db_table': 'attendances',
            },
        ),
    ]
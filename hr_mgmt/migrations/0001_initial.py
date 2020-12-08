# Generated by Django 3.1.2 on 2020-11-30 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0004_auto_20201130_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateField(null=True)),
                ('probation_period', models.CharField(max_length=50, null=True)),
                ('worked_since', models.DateField(null=True)),
                ('total_experience', models.CharField(max_length=50, null=True)),
                ('annual_vacation', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('promotion_date', models.DateField(null=True)),
                ('promoted_at', models.DateField(null=True)),
                ('pass_num', models.CharField(max_length=50, null=True)),
                ('etc', models.TextField(null=True)),
                ('annual_vacation_permission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='employee.employee')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'db_table': 'employee_details',
            },
        ),
    ]
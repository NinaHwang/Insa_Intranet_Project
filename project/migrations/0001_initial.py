# Generated by Django 3.1.3 on 2020-12-08 15:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=100, null=True)),
                ('is_private', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('project_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'db_table': 'project_details',
            },
        ),
        migrations.CreateModel(
            name='ProjectReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('project_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projectdetail')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'db_table': 'project_reviews',
            },
        ),
        migrations.CreateModel(
            name='ProjectParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'db_table': 'project_participants',
            },
        ),
        migrations.CreateModel(
            name='ProjectLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'db_table': 'project_likes',
            },
        ),
        migrations.CreateModel(
            name='ProjectAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('code', models.CharField(max_length=100)),
                ('project_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projectdetail')),
            ],
            options={
                'db_table': 'project_attachments',
            },
        ),
    ]

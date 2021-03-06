# Generated by Django 3.1.2 on 2020-11-24 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(choices=[('BCA', 'BCA'), ('MCA', 'MCA'), ('BBA', 'BBA'), ('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('Diploma', 'Diploma')], max_length=50)),
                ('semester', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(limit_choices_to={'is_active': True, 'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.teacher')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.teacher'),
        ),
        migrations.CreateModel(
            name='EnrollCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(choices=[('BCA', 'BCA'), ('MCA', 'MCA'), ('BBA', 'BBA'), ('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('Diploma', 'Diploma')], max_length=50)),
                ('semester', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])),
                ('enroll_date', models.DateTimeField(auto_now_add=True)),
                ('students_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.teacher'),
        ),
    ]

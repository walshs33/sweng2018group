# Generated by Django 2.0 on 2018-03-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20180130_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='additional_comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='additional_remuneration',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='annual_leave',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='commencement_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='contract_type',
            field=models.CharField(choices=[('Pe', 'Permanent'), ('SP', 'Specific Purpose'), ('FT', 'Fixed Term')], max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='discipline',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='first_increment_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='grant_source',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='home_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hours_per_week',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='increment_amount',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='is_NWA',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='post',
            name='is_new_work_group',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='post',
            name='is_permit_required',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='post',
            name='nationality',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='new_or_replacement',
            field=models.CharField(choices=[('N', 'New'), ('R', 'Replacement')], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='principal_investigator',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='project_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='qual_awarding_body',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='qual_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='school',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='termination_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='work_group_owner',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='work_group_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mister'), ('Mrs', 'Missus'), ('Ms', 'Miss'), ('Prof', 'Professor'), ('Dr', 'Doctor')], max_length=4, null=True),
        ),
    ]
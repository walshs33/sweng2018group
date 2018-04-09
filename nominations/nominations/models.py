from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30, help_text='Required')
	last_name = models.CharField(max_length=30, help_text='Required')
	email = models.EmailField(max_length=254, help_text='Required')
	public_key = models.CharField(max_length=8192)
	private_key = models.CharField(max_length=8192)
	rank_id = models.IntegerField()
	dept_id = models.IntegerField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

'''
class EncForm(models.Model):
	encdata
	dept_id
	level
	submitter
'''
class Post(models.Model):
    post_title = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    TITLE_CHOICES = (
        ('Mr','Mister'),
        ('Mrs','Missus'),
        ('Ms','Miss'),
        ('Prof','Professor'),
        ('Dr','Doctor'),
    )
    title = models.CharField(max_length=4, choices=TITLE_CHOICES, null=True)
    first_name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    home_address = models.CharField(max_length=200, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    discipline = models.CharField(max_length=1000, null=True)
    IS_NEW_CHOICES = (
        ('N', 'New'),
        ('R', 'Replacement'),
    )
    new_or_replacement = models.CharField(max_length=11, choices = IS_NEW_CHOICES, null=True)
    additional_remuneration = models.CharField(max_length=500, null=True)
    hours_per_week = models.SmallIntegerField(null=True)
    commencement_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    school = models.CharField(max_length=100, null=True)
    is_new_work_group = models.NullBooleanField()
    work_group_title = models.CharField(max_length=100, null=True)
    work_group_owner = models.CharField(max_length=100, null=True)
    qual_title = models.CharField(max_length=100, null=True)
    qual_awarding_body = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=100, null=True)
    is_permit_required = models.NullBooleanField()
    CONTRACT_CHOICES = (
        ('Pe', 'Permanent'),
        ('SP', 'Specific Purpose'),
        ('FT', 'Fixed Term'),
    )
    contract_type = models.CharField(max_length=16, choices = CONTRACT_CHOICES, null=True)
    salary = models.IntegerField(null=True)
    first_increment_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    increment_amount = models.SmallIntegerField(null=True)
    is_NWA = models.NullBooleanField()
    termination_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    project_title = models.CharField(max_length=100, null=True)
    grant_source = models.SmallIntegerField(null=True)
    principal_investigator = models.CharField(max_length=100, null=True)
    annual_leave = models.SmallIntegerField(null=True)
    additional_comments = models.TextField(null=True)


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

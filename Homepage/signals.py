from django.db.models.signals import post_delete, post_save
from django.contrib.auth.models import User
from .models import Headers,ProfessionalExperience,Education,Languages,Skills,Hobbies
def signalHeaderCreation(sender, instance, created, **kwargs):
    if created:
        User = instance
        Headers.objects.create(
            user = User.username,
            email = User.email
        )

post_save.connect(signalHeaderCreation, sender=User)

def signalProfessionalExperienceCreation(sender, instance, created, **kwargs):
    if created:
        User = instance
        ProfessionalExperience.objects.create(
            user = User.username,
        )

post_save.connect(signalProfessionalExperienceCreation, sender=User)


def signalEducationCreation(sender, instance, created, **kwargs):
    if created:
        User = instance
        Education.objects.create(
            user = User.username,
        )

post_save.connect(signalEducationCreation, sender=User)

def signalLanguageCreation(sender, instance, created, **kwargs):
    if created:
        User = instance
        Languages.objects.create(
            user = User.username,
        )

post_save.connect(signalLanguageCreation, sender=User)

def signalSkillCreation(sender, instance, created, **kwargs):
    if created:
        User = instance
        Skills.objects.create(
            user = User.username,
        )

post_save.connect(signalSkillCreation, sender=User)

def signalHobbyCreation(sender, instance, created, **kwargs):
    if created:
        User = instance
        Hobbies.objects.create(
            user = User.username,
        )

post_save.connect(signalHobbyCreation, sender=User)
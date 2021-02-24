from django.contrib import admin
from .models import Participant,ParticipantAdmin
# Register your models here.

admin.site.register(Participant,ParticipantAdmin)
from ac.models import Ticket, Tablet_info
from django import forms
from django.contrib.auth.models import User
from ac.models import UserProfile, Category
import datetime
from ac.models import *
from datetime import timedelta
class SubmitTicketForm(forms.ModelForm):
                #field for email help topic subject and message
                #category=forms.ChoiceField({% for i in Ticket%} {{i.topic_id.category}} {% endfor %})
                email=forms.EmailField(max_length=128,help_text="please enter your email address")
                ticket_id=forms.IntegerField(widget=forms.HiddenInput())
                subject=forms.CharField(max_length=100,help_text="subject")
                # days = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])
                help_topic=forms.ChoiceField(choices=[(x['category'], str(x['category'])) for x in Category.objects.values('category')],help_text="please enter the category of your problem")#Category.objects.values('category')])#the input is hidden
                for x in Category.objects.values('category'):
                                print x['category']
                message=forms.CharField(max_length=500,help_text="message")
                created_date_time=forms.DateTimeField(widget=forms.HiddenInput())
                overdue_date_time=forms.DateTimeField(widget=forms.HiddenInput())
                closed_date_time=forms.DateTimeField(widget=forms.HiddenInput())
                status=forms.IntegerField(widget=forms.HiddenInput())
                reopened_date_time=forms.DateTimeField(widget=forms.HiddenInput())
                topic_priority=forms.IntegerField(widget=forms.HiddenInput())
                duration_for_reply=forms.IntegerField(widget=forms.HiddenInput())
                #an inline class to provide additional information on the form
                
                class Meta:
                        model=Ticket#all the fields are included
                        fields=('email','subject','help_topic','message')

#class Ticket(models.Model):
# user_id=models.ForeignKey(User)
# topic_id=models.ForeignKey(Category)
# message=models.TextField()
# ticket_id=models.IntegerField()
# #file_uploads=models.FileField(upload_to='tickets/file' , blank=True)
# created_date_time=models.DateTimeField(auto_now_add=True)
# overdue_date_time=models.DateTimeField(auto_now_add=True)
# closed_date_time=models.DateTimeField(auto_now_add=True)
# status=models.IntegerField()
# reopened_date_time=models.DateTimeField(auto_now_add=True)
# topic_priority=models.IntegerField()
# duration_for_reply=models.IntegerField()
#remove this

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")
    nickname=forms.CharField(help_text="Please enter your nickname.", required=True)
    location=forms.CharField(help_text="Please enter your location.", required=True)
    tablet_id=forms.CharField(help_text="Please enter your tablet id.", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','nickname','location','tablet_id']

#class UserProfileForm(forms.ModelForm):
 # nickname=forms.CharField(help_text="Please enter your nickname.", required=True)
  # location=forms.CharField(help_text="Please enter your location.", required=True)
   # tablet_id=forms.CharField(help_text="Please enter your tablet id.", required=True)

    #class Meta:
     # model = UserProfile
      # fields = ['nickname','location','tablet_id']


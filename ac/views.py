from PIL import Image as PImage


from ac.models import *

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from ac.models import Ticket
from django.db.models import Count
from ac.forms import SubmitTicketForm
import json



def main(request):
    """Main listing."""
    tickets = Ticket.objects.all()
    return render_to_response("ac/d.html",dict(tickets=tickets), RequestContext(request))

def display(request, id):      
     """Displaying the details of the corresponding tickets"""
     threads= Ticket.objects.get(pk=id)
     return render_to_response("ac/second.html", dict(threads=threads),RequestContext(request))
    
def search(request):
 if request.method == "POST":
   Search= request.POST.get('search')
   """Searching for ticket-id"""
   tickets=Ticket.objects.filter(ticket_id__icontains=Search)
   if tickets.exists():
       #importticket=Ticket.objects.get(pk=Search)
       return render_to_response("ac/search.html",dict(tickets=tickets),RequestContext(request))
   else:
       """Searching for Topic-id"""
       tickets=Category.objects.filter(category__icontains=Search)
       if tickets.exists():
         #tickets=Ticket.objects.get(pk=tickets)
         tickets=Ticket.objects.filter(topic_id=tickets)
         return render_to_response("ac/search.html",dict(tickets=tickets),RequestContext(request))
       else:
         tickets = Ticket.objects.all()
         return render_to_response("ac/d.html",dict(tickets=tickets),RequestContext(request))
       
       
       
def graph(request):
    
     
     tickets=Ticket.objects.all()
     #theanswer = Item.objects.values('category').annotate(Count('category'))
     Countanswer = Ticket.objects.values('topic_id').annotate(Count('topic_id'))
     #category    = Category.objects.get(pk=2)
     #data = {category:Countanswer}
     #print Category
     #print Countanswer[0]["topic_id__count"]
     
     #print Countanswer
     return render_to_response("ac/graphs.html",dict(tickets=tickets),RequestContext(request))
    

def reply(request, id):
  if request.method == 'POST':
    Reply= request.POST.get('response')
    threads=Ticket.objects.get(pk=id)
    threads.reply=Reply
    threads.save()
    return render_to_response("ac/second.html",dict(threads=threads), RequestContext(request))
  

    
    
def submit(request):
                context=RequestContext(request)
                if(request.method=="POST"):
                    print request.POST
                    print "________________________\n"
                    data = request.POST.copy()
                    #data=request.POST
                    
                    print "\n"
                    print request.user.email
                    data['created_date_time']=datetime.datetime.now()
                    data['overdue_date_time']=datetime.datetime.now()
                    Date=datetime.datetime.now()
                    Enddate=Date+datetime.timedelta(days=1)
                    data['overdue_date_time']=Enddate
                    data['closed_date_time']=Enddate
                    data['status']=0 # 0 means that the ticket is still open and not yet answered
                    data['reopened_date_time']=Enddate
                    data['topic_priority']=2 # 2 is the default priority of medium
                    data['duration_for_reply']=24 #in hours
                    if request.user.is_authenticated():
                        print request.user
                        data['user_id']=request.user.email
                        #returns a user object if the user is logged in. @login_required is thus necessary
                    else:
                        return HttpResponse("you need to be a valid user to submit a ticket. click <a href=''>here</a> to go to the login page")
#let the help topic remain the same
                    #category_selected=data['help_topic']
                    #data['help_topic']=Category.objects.get(category="android")#category_selected)#get is used to get a single object
                    from django.db.models import Max
                    last_ticket=int(Ticket.objects.all().aggregate(Max('ticket_id'))['ticket_id__max'])
                    data['ticket_id']=last_ticket+1
                    #if 'submit' in data: del data['submit']
                    #if 'csrfmiddlewaretoken' in data: del data['csrfmiddlewaretoken']
                    
                    #user_form=SubmitTicketForm(data)
                    print data
                    user_form=SubmitTicketForm(data)
                    #how to validate the form for yourself
                    if user_form.is_valid():
                     print user_form.cleaned_data
                  #   user_form=Ticket.objects.set(topic_id=data['user_id'])
                     user_form.save()
                     return HttpResponse("Saved successfully")
                    #else:
                     # print data
                      # return HttpResponse("Saved unsuccessfully")
                       # print "the errors are"
                        # print user_form.errors
                else:
                     user_form=SubmitTicketForm()
                     return render_to_response(
                        'submit.html',
                        {'user_form': user_form},
                        context)
        
    

    
 
        

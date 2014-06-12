from django.conf.urls  import patterns , include , url


urlpatterns = patterns( '',
             
     url(r'^$', 'ac.views.main', name='Main'),
     url(r'^back', 'ac.views.main'),
     url(r'^display/(\d+)/$', "ac.views.display"),
     url(r'^search/$', "ac.views.search"),
     url(r'^graphs', "ac.views.graph"),
     url(r'^submit',"ac.views.submit"),
     url(r'^reply/(\d+)/$',"ac.views.reply")

)
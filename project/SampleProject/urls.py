from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$','myapp.views.startpage',name='start'),

    url(r'^login/$' ,'myapp.views.login',name='login'),
    url(r'^user/userdashboard/$', 'myapp.views.userdashboard',name='userdashboard'),
    url(r'^galery/$' ,'myapp.views.galery',name='galery'),
    url(r'^contactus/$' ,'myapp.views.contactus',name='contactus'),
    url(r'^aboutus/$' ,'myapp.views.aboutus',name='aboutus'),
    url(r'^help/$' ,'myapp.views.help',name='help'),
    url(r'^price/$' ,'myapp.views.price',name='price'),
    url(r'^edituser/([^/]+)/$', 'myapp.views.edituser',name='edituser'),
    url(r'^logout/$' ,'myapp.views.logout',name='logout'),
    ########################################################admin
    url(r'^adminpayment/$' ,'myapp.views.adminpayment',name='adminpayment'),
    url(r'^findmalek/$' ,'myapp.views.findmalek',name='findmalek'),
    url(r'^showfindedmalek/$' ,'myapp.views.showfindedmalek',name='showfindedmalek'),
    url(r'^findvahed/$' ,'myapp.views.findvahed',name='findvahed'),
    url(r'^showfindedvahed/$' ,'myapp.views.showfindedvahed',name='showfindedvahed'),
    ####################################################sabte vahed
    url(r'^sabtevahed/$', 'myapp.views.sabtevahed',name='sabtevahed'),
    url(r'^savevahed/$', 'myapp.views.savevahed',name='savevahed'),
    url(r'^showvahed/$', 'myapp.views.showvahed',name='showvahed'),
    url(r'^deletevahed/([^/]+)/$', 'myapp.views.deletevahed'),
    url(r'^editvahed/([^/]+)/$', 'myapp.views.editvahed'),
    url(r'^all/$', 'myapp.views.all',name='all'),
    #####################################################sabte malek
    url(r'^sabtemalek/$', 'myapp.views.sabtemalek',name='sabtemalek'),
    url(r'^savemalek/$', 'myapp.views.savemalek',name='savemalek'),
    url(r'^showmalek/$', 'myapp.views.showmalek',name='showmalek'),
    url(r'^deletemalek/([^/]+)/$', 'myapp.views.deletemalek'),
    url(r'^editmalek/([^/]+)/$', 'myapp.views.editmalek'),
    url(r'^allmalek/$', 'myapp.views.allmalek',name='allmalek'),
    #####################################################
    #####################################################sabte shift
    url(r'^sabtecost/$', 'myapp.views.sabtecost',name='sabtecost'),
    url(r'^savecost/$', 'myapp.views.savecost',name='savecost'),
    url(r'^showcost/$', 'myapp.views.showcost',name='showcost'),
    url(r'^deletecost/([^/]+)/$', 'myapp.views.deletecost'),
    url(r'^paycost/([^/]+)/$', 'myapp.views.paycost'),
    url(r'^editcost/([^/]+)/$', 'myapp.views.editcost'),
    url(r'^allcost/$', 'myapp.views.allcost',name='allcost'),
    #####################################################

    ######################################################
    url(r'^save/$', 'myapp.views.save',name='save'),
    url(r'^show/$', 'myapp.views.show',name='show'),
    url(r'^delete/([^/]+)/$', 'myapp.views.delete'),

    url(r'^register/$', 'myapp.views.register',name='register'),


)

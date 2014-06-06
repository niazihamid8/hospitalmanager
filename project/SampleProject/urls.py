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
                       #####################################################user pages
                       url(r'^darkhasteMorakhasi/$' ,'myapp.views.darkhasteMorakhasi',name='darkhasteMorakhasi'),
                       url(r'^savemorakhasi/$', 'myapp.views.savemorakhasi',name='savemorakhasi'),
                       url(r'^showmorakhasi/$', 'myapp.views.showmorakhasi',name='showmorakhasi'),
                       url(r'^showmorakhasiAdmin/$', 'myapp.views.showmorakhasiAdmin',name='showmorakhasiAdmin'),
                       url(r'^agree/([^/]+)/$', 'myapp.views.agree'),
                       url(r'^disagree/([^/]+)/$', 'myapp.views.disagree'),
                       ########################################################admin
                       url(r'^adminpayment/$' ,'myapp.views.adminpayment',name='adminpayment'),
                       url(r'^findpersonnel/$' ,'myapp.views.findpersonnel',name='findpersonnel'),
                       url(r'^showfindedpersonnel/$' ,'myapp.views.showfindedpersonnel',name='showfindedpersonnel'),
                       url(r'^findvahed/$' ,'myapp.views.findvahed',name='findvahed'),
                       url(r'^showfindedvahed/$' ,'myapp.views.showfindedvahed',name='showfindedvahed'),
                       ####################################################sabte vahed
                       url(r'^sabtevahed/$', 'myapp.views.sabtevahed',name='sabtevahed'),
                       url(r'^savevahed/$', 'myapp.views.savevahed',name='savevahed'),
                       url(r'^showvahed/$', 'myapp.views.showvahed',name='showvahed'),
                       url(r'^deletevahed/([^/]+)/$', 'myapp.views.deletevahed'),
                       url(r'^editvahed/([^/]+)/$', 'myapp.views.editvahed'),
                       url(r'^all/$', 'myapp.views.all',name='all'),
                       #####################################################sabte personnel
                       url(r'^sabtepersonnel/$', 'myapp.views.sabtepersonnel',name='sabtepersonnel'),
                       url(r'^savepersonnel/$', 'myapp.views.savepersonnel',name='savepersonnel'),
                       url(r'^showpersonnel/$', 'myapp.views.showpersonnel',name='showpersonnel'),
                       url(r'^deletepersonnel/([^/]+)/$', 'myapp.views.deletepersonnel'),
                       url(r'^editpersonnel/([^/]+)/$', 'myapp.views.editpersonnel'),
                       url(r'^allpersonnel/$', 'myapp.views.allpersonnel',name='allpersonnel'),
                       #####################################################
                       #####################################################sabte shift
                       url(r'^sabteshift/$', 'myapp.views.sabteshift',name='sabteshift'),
                       url(r'^savecost/$', 'myapp.views.savecost',name='savecost'),
                       url(r'^showshift/$', 'myapp.views.showcost',name='showcost'),
                       url(r'^deletecost/([^/]+)/$', 'myapp.views.deletecost'),
                       url(r'^paycost/([^/]+)/$', 'myapp.views.paycost'),
                       url(r'^editcost/([^/]+)/$', 'myapp.views.editcost'),
                       url(r'^allcost/$', 'myapp.views.allcost',name='allcost'),
                       #####################################################
                       url(r'^sabtetagheershift/$', 'myapp.views.sabtetagheershift',name='sabtetagheershift'),
                       url(r'^savetagheershift/$', 'myapp.views.savetagheershift',name='savetagheershift'),
                       url(r'^showtagheershift/$', 'myapp.views.showtagheershift',name='showtagheershift'),
                       url(r'^adminshowtagheershift/$', 'myapp.views.adminshowtagheershift',name='adminshowtagheershift'),
                       url(r'^csagree/([^/]+)/$', 'myapp.views.csagree'),
                       url(r'^csdisagree/([^/]+)/$', 'myapp.views.csdisagree'),
                       url(r'^allrequest/$', 'myapp.views.allrequest',name='allrequest'),
                       ######################################################
                       url(r'^save/$', 'myapp.views.save',name='save'),
                       url(r'^show/$', 'myapp.views.show',name='show'),
                       url(r'^delete/([^/]+)/$', 'myapp.views.delete'),

                       url(r'^register/$', 'myapp.views.register',name='register'),


                       )

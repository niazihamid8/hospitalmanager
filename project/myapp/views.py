from django.shortcuts import render
from myapp.models import member,vahed,malek,cost,user,userh
from django.template import Template
from django.http import HttpResponse, HttpResponseRedirect



################################################################kar dar class
def register(request):

      return render(request, 'user/regist.html')
def save(request):

    list2=[]
    k=request.POST.get('newuser')
    email = request.POST.get('email')
    pas=request.POST.get('pass')
    pass1 = request.POST.get('pass2')
    ac=request.POST.get('ac')


    if k=='T':
        if pas!=pass1:
            list2.append("password not match")
        if len(pas)==0:
                list2.append("pass not incorect")

        if len(list2)==0 :
            R=member(emil=request.POST.get("email"),pw=request.POST.get("pass"),
                     ac=request.POST.get("ac"))
            R.save()
            return render(request,'user/save.html')
        else :
           return render(request,'user/login.html',{'lst':list2})
    else:
        m= member.objects.filter(emil =request.POST.get('oldemail'))[0]
        m.emil=email
        m.pw=pass1
        m.ac=ac
        m.save()
        return HttpResponseRedirect("/show/")
##############################################################
def startpage(request):
    request.session['login']="false"
    return render(request, 'user/start page.html')

def login(request):
      request.session['login']="false"
      return render(request, 'user/login.html')
##########################sabte malek######################
def sabtemalek(request):
     if request.session["login"]=="true":
         return render(request, 'user/sabte malek/sabtemalek.html')
     else:
         return render(request,'user/login.html')
def savemalek(request):
 if request.session["login"]=="true":
    Msg=[]
    k=request.POST.get('newmalek')
    mellicode = request.POST.get('mellicode')
    pass1 = request.POST.get('pass1')
    fn = request.POST.get('fn')
    ln = request.POST.get('ln')
    telephon = request.POST.get('telephon')
    pelak = request.POST.get('pelak')
    startdate = request.POST.get('startdate')
    enddate = request.POST.get('enddate')
    malektype = request.POST.get('malektype')
    admin = request.POST.get('admin')
    x=vahed.objects.filter(pelak=pelak)

    if len(x)!=0:
        Msg.append("mellicode is wrong")

    if k=='T'and len(Msg)==0  :
            R=malek(mellicode=request.POST.get("mellicode"),pass1=request.POST.get("pass1"),pelak=request.POST.get("pelak"),
                    startdate=request.POST.get("startdate"),
                    enddate=request.POST.get("enddate"),fn=request.POST.get("fn"),
                    ln=request.POST.get("ln"),
                    telephon=request.POST.get("telephon"),malektype=request.POST.get("malektype"),admin=request.POST.get("admin"))
            R.save()
            return render(request,'user/sabte malek/savemalek.html')
    elif k!='T':
        m= malek.objects.filter(mellicode =request.POST.get('oldmalek'))[0]
        m.mellicode=mellicode
        m.pass1=pass1
        m.fn=fn
        m.ln=ln
        m.startdate=startdate
        m.enddate=enddate
        m.telephon=telephon
        m.pelak=pelak
        m.malektype=malektype
        m.admin=admin
        m.save()
        return HttpResponseRedirect("/showmalek/")
    else:
        return render(request,'user/sabte malek/sabtemalek.html',{'Msg':Msg})
 else:
         return render(request,'user/login.html')

def showmalek(request):
 if request.session["login"]=="true":
   Malek=malek.objects.all()

   return render(request,'user/sabte malek/showmalek.html',{'p':Malek})
 else:
         return render(request,'user/login.html')

#######################################
def deletemalek (request,mellicode):
    k = malek.objects.filter(mellicode = mellicode)
    for s in k:
     s.delete()
    return HttpResponseRedirect("/showmalek/")
def editmalek(request,mellicode):

    m=malek.objects.filter(mellicode=mellicode)
    return render(request,'user/sabte malek/sabtemalek.html',{'Malek':m[0]})
def allmalek(request):
  if request.session["login"]=="true":
      return render(request, 'user/sabte malek/all malek.html')
  else:
         return render(request,'user/login.html')
    ##################################################sabte vahed#####
def sabtevahed(request):
   if request.session["login"]=="true":
      return render(request, 'user/sabte vahed/sabtevahed.html')
   else:
         return render(request,'user/login.html')
def savevahed(request):
 if request.session["login"]=="true":
    k=request.POST.get('newvahed')
    pelak = request.POST.get('pelak')
    metraj = request.POST.get('metraj')
    telephon = request.POST.get('telephon')
    parking = request.POST.get('parking')

    if k=='T':
            R=vahed(pelak=request.POST.get("pelak"),metraj=request.POST.get("metraj"),
            telephon=request.POST.get("telephon"),parking=request.POST.get("parking"))
            R.save()
            return render(request,'user/sabte vahed/savevahed.html')
    else:
        m= vahed.objects.filter(pelak =request.POST.get('oldvahed'))[0]
        m.pelak=pelak
        m.metraj=metraj
        m.telephon=telephon
        m.parking=parking
        m.save()
        return HttpResponseRedirect("/showvahed/")
 else:
         return render(request,'user/login.html')
 #######################################
def showvahed(request):
 if request.session["login"]=="true":
   Vahed=vahed.objects.all()

   return render(request,'user/sabte vahed/showvahed.html',{'p':Vahed})
 else:
         return render(request,'user/login.html')
 ############################################
def deletevahed (request,pelak):
    k = vahed.objects.filter(pelak = pelak)
    for s in k:
     s.delete()
    return HttpResponseRedirect("/showvahed/")
def editvahed(request,pelak):

    m=vahed.objects.filter(pelak=pelak)
    return render(request,'user/sabte vahed/sabtevahed.html',{'Vahed':m[0]})
def all(request):
  if request.session["login"]=="true":
      return render(request, 'user/sabte vahed/all.html')
  else:
         return render(request, 'user/login.html')
#############################################################
##########################sabte cost######################
def sabtecost(request):
  if request.session["login"]=="true":
      return render(request, 'user/sabte cost/sabtecost.html')
  else:
         return render(request, 'user/login.html')
  #############################################
def savecost(request):
  if request.session["login"]=="true":
    Msg=[]
    k=request.POST.get('newcost')
    costn = request.POST.get('costn')
    regnum = request.POST.get('regnum')
    costfor = request.POST.get('costfor')
    special = request.POST.get('special')
    pelak = request.POST.get('pelak')
    startdate = request.POST.get('startdate')
    enddate = request.POST.get('enddate')
    if(special=="Yes"):
        x=vahed.objects.filter(pelak=pelak)
        if len(x)==0:
          Msg.append("mellicode is wrong")


    if k=='T' and len(Msg)==0:
            R=cost(regnum=request.POST.get("regnum"),costn=request.POST.get("costn"),pelak=request.POST.get("pelak"),
                    startdate=request.POST.get("startdate"),
                    enddate=request.POST.get("enddate"),costfor=request.POST.get("costfor"),
                    special=request.POST.get("special"),payed="no"
                    )
            R.save()
            return render(request,'user/sabte cost/savecost.html')
    elif k!='T':
        m= cost.objects.filter(regnum =request.POST.get('oldcost'))[0]
        m.regnum=regnum
        m.costn=costn
        m.costfor=costfor
        m.special=special
        m.startdate=startdate
        m.enddate=enddate
        m.pelak=pelak
        m.payed="no"
        m.save()
        return HttpResponseRedirect("/showcost/")
    else:
        return render(request,'user/sabte cost/sabtecost.html',{'Msg':Msg})
  else:
         return render(request, 'user/login.html')
  #############################################
def showcost(request):
 if request.session["login"]=="true":
   Cost=cost.objects.all()
   return render(request,'user/sabte cost/showcost.html',{'p':Cost})
 else:
         return render(request, 'user/login.html')
 #################################################
def deletecost (request,regnum):
    k = cost.objects.filter(regnum = regnum)
    for s in k:
     s.delete()
    return HttpResponseRedirect("/showcost/")
###############################################
def paycost (request,regnum):
    x=cost.objects.get(regnum = regnum)
    m= cost.objects.filter(regnum =regnum)[0]
    m.regnum=x.regnum
    m.costn=x.costn
    m.costfor=x.costfor
    m.special=x.special
    m.startdate=x.startdate
    m.enddate=x.enddate
    m.pelak=x.pelak
    m.payed="yes"
    m.save()
    return HttpResponseRedirect("/user/userdashboard/")
##################################################
def editcost(request,regnum):

    m=cost.objects.filter(regnum=regnum)
    return render(request,'user/sabte cost/sabtecost.html',{'Cost':m[0]})
#########################################
def allcost(request):
  if request.session["login"]=="true":
      return render(request, 'user/sabte cost/all cost.html')
  else:
         return render(request, 'user/login.html')
##########################################################################
def show(request):

   Member=member.objects.all()
   return render(request,'user/show.html',{'p':Member})
####################################################
def delete (request,email):
    k = member.objects.filter(emil = email)
    for s in k:
     s.delete()
    return HttpResponseRedirect("/show/")
###############################################
def edituser1(request,email):

    m=member.objects.filter(emil=email)
    return render(request,'user/login.html',{'Member':m[0]})
#################################################################################
###################################################################################
###################################################################################
def userdashboard(request):

  if request.session["login"]=="false":
    Msg=[]
    mellicode2 = request.POST.get('mellicode')
    pass12=request.POST.get('pass1')
    ser = malek.objects.filter(mellicode=mellicode2,pass1=pass12 )
    if len(ser)== 0:
        Msg.append("user or password is wrong")
    if len(Msg) == 0:
            m= malek.objects.get(mellicode=mellicode2 )
            adm=m.admin
            if adm=="admin":
               request.session["login"]="true"
               m= malek.objects.get(mellicode=mellicode2 )
               username=m.fn
               mellicode=m.mellicode
               request.session['mellicode'] =m.mellicode

               Cost=cost.objects.filter(payed="no")
               return render(request,'user/admin dashboard.html',{'username':username ,'mellicode':mellicode,'p':Cost,})
            elif adm=="user":
               request.session["login"]="true"
               m= malek.objects.get(mellicode=mellicode2 )
               username=m.fn
               request.session['mellicode'] =m.mellicode
               request.session['username'] =m.fn
               Cost=cost.objects.all()
               mellicode=m.mellicode
               request.session["login"]="true"

               return render(request,'user/user pages/user dashboard.html',{'username':username,'p':Cost,'mellicode':mellicode})
    else:
        return render(request, 'user/login.html',{'Msg':Msg})
  else:
      z=request.session['mellicode']
      m= malek.objects.get(mellicode=z )
      username=m.fn
      mellicode=m.mellicode
      adm=m.admin

      if adm=="admin":
          request.session["login"]="true"
          Cost=cost.objects.filter(payed="no")
          return render(request,'user/admin dashboard.html',{'username':username,'mellicode':mellicode,'p':Cost})
      else:
          Cost=cost.objects.filter(payed="no")
          request.session["login"]="true"
          return render(request,'user/user pages/user dashboard.html',{'username':username,'p':Cost,'mellicode':mellicode})




#####################################################
def edituser(request,mellicode):

    m=malek.objects.filter(mellicode=mellicode)
    return render(request,'user/user pages/edit user.html',{'Malek':m[0]})
#################################################
def logout(request):
    request.session["login"]="false"

    return render(request,'user/login.html')
################################################
def galery(request):

 return render(request,'user/user pages/galery.html')
####################################
def contactus(request):


    return render(request,'user/user pages/contactus.html')
#######################################
def aboutus(request):


    return render(request,'user/user pages/aboutus.html')
#############################
def help(request):


    return render(request,'user/user pages/help.html')
######################################################
def price(request):


    return render(request,'user/user pages/price.html')
########################################################
################################################
def adminpayment(request):
  if request.session["login"]=="true":
    Cost=cost.objects.filter(payed="no")

    return render(request,'user/admin pages/payment.html',{'p':Cost})
  else:

   return render(request,'user/login.html')
  ##############################################
def findmalek(request):
  if request.session["login"]=="true":
    return render(request,'user/admin pages/find malek.html')
  else:
   return render(request,'user/login.html')
  ##############################################
def showfindedmalek(request):
 if request.session["login"]=="true":
    fn=request.POST.get('fn')
    ln=request.POST.get('ln')
    mc=request.POST.get('mc')
    m=malek.objects.get(mellicode=mc,fn=fn,ln=ln)
    mc=m.mellicode
    fn=m.fn
    ln=m.ln
    pelak=m.pelak
    n=cost.objects.filter()
    return render(request,'user/admin pages/showfind.html',{'p':n,'mc':mc,'fn':fn,'ln':ln,'pelak':pelak,})
 else:
   return render(request,'user/login.html')
####################################################
def findvahed(request):
  if request.session["login"]=="true":
    return render(request,'user/admin pages/find vahed.html')
  else:
   return render(request,'user/login.html')
  ##############################
def showfindedvahed(request):
 if request.session["login"]=="true":
    pelak=request.POST.get('pelak')
    m=malek.objects.get(pelak=pelak)
    pelak=m.pelak
    metraj=m.metraj
    telephon=m.telephon
    parking = m.parking
    return render(request,'user/admin pages/show finded vahed.html',{'pelak':pelak,'metraj':metraj,'telephon':telephon,'parking':parking})
 else:
   return render(request,'user/login.html')

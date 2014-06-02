from django.shortcuts import render
from myapp.models import member,vahed,personnel,user,userh, shift
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
##########################sabte personnel######################
def sabtepersonnel(request):
# if request.session["login"]=="true":
    return render(request, 'user/sabte personnel/sabtepersonnel.html')
    # else:
    #     return render(request,'user/login.html')
def savepersonnel(request):
    #if request.session["login"]=="true":
        Msg=[]
        k=request.POST.get('newpersonnel')
        personnelcode = request.POST.get('personnelcode')
        mellicode = request.POST.get('mellicode')
        pass1 = request.POST.get('pass1')
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        mobile = request.POST.get('mobile')
        telephon = request.POST.get('telephon')
        semat = request.POST.get('semat')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        personneltype = request.POST.get('personneltype')
        admin = request.POST.get('admin')

        if k=='T'and len(Msg)==0  :
            R=personnel(mellicode=request.POST.get("mellicode"),personnelcode = request.POST.get('personnelcode'),pass1=request.POST.get("pass1"),
                        semat=request.POST.get("semat"),
                    startdate=request.POST.get("startdate"),
                    enddate=request.POST.get("enddate"),fn=request.POST.get("fn"),
                    ln=request.POST.get("ln"),mobile = request.POST.get('mobile'),
                    telephon=request.POST.get("telephon"),personneltype=request.POST.get("personneltype")
                ,admin=request.POST.get("admin"))
            R.save()
            return render(request,'user/sabte personnel/savepersonnel.html')
        elif k!='T':
            m= personnel.objects.filter(mellicode =request.POST.get('oldpersonnel'))[0]
            m.mellicode=mellicode
            m.personnelcode=personnelcode
            m.pass1=pass1
            m.fn=fn
            m.ln=ln
            m.startdate=startdate
            m.enddate=enddate
            m.telephon=telephon
            m.semat=semat
            m.personneltype=personneltype
            m.admin=admin
            m.save()
            return HttpResponseRedirect("/showpersonnel/")
        else:
            return render(request,'user/sabte personnel/sabtepersonnel.html',{'Msg':Msg})
   # else:
            return render(request,'user/login.html')

def showpersonnel(request):
    if request.session["login"]=="true":
        personnel=personnel.objects.all()

        return render(request,'user/sabte personnel/showpersonnel.html',{'p':personnel})
    else:
        return render(request,'user/login.html')

#######################################
def deletepersonnel (request,mellicode):
    k = personnel.objects.filter(mellicode = mellicode)
    for s in k:
        s.delete()
    return HttpResponseRedirect("/showpersonnel/")
def editpersonnel(request,mellicode):

    m=personnel.objects.filter(mellicode=mellicode)
    return render(request,'user/sabte personnel/sabtepersonnel.html',{'personnel':m[0]})
def allpersonnel(request):
    if request.session["login"]=="true":
        return render(request, 'user/sabte personnel/all personnel.html')
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
##########################sabte shift######################
def sabteshift(request):
# if request.session["login"]=="true":
    return render(request, 'user/sabte shift/sabteshift.html')
    # else:
    #        return render(request, 'user/login.html')
    #############################################
def savecost(request):
    if request.session["login"]=="true":
        Msg=[]
        k=request.POST.get('newshift')
        q=request.POST.get('newshift1')
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        post = request.POST.get('post')
        bakhsh = request.POST.get('bakhsh')

        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        if startdate=='mm/dd/yyyy':
            Msg.append("please enter your date")
        if enddate=='mm/dd/yyyy':
            Msg.append("please enter your date")
        if len(fn)==0:
            Msg.append("please enter your first name")
        if len(ln)==0:
            Msg.append("please enter your last name")
        if len(post)==0:
            Msg.append("please enter your post")
        if len(bakhsh)==0:
            Msg.append("please enter your bakhsh")

        if k=='T'and q=='T'and len(Msg)==0:
            p =shift(fn=request.POST.get("fn"),ln=request.POST.get("ln"),post=request.POST.get("post"),
                     startdate=request.POST.get("startdate"),
                     enddate=request.POST.get("enddate"),bakhsh=request.POST.get("bakhsh"))
            p.save()


            return render(request,'user/sabte shift/saveshift.html')
        elif k!='T' and q!='T':
            m= shift.objects.filter(ln =request.POST.get('oldcost'))[0]
            m.fn=fn
            m.ln=ln
            m.post=post
            m.bakhsh=bakhsh
            m.startdate=startdate
            m.enddate=enddate

            m.save()
            return HttpResponseRedirect("/showshift/")
        else:
            return render(request,'user/sabte shift/sabteshift.html',{'Msg':Msg})
    else:
        return render(request, 'user/login.html')
        #############################################
def showcost(request):
# if request.session["login"]=="true":
    Shift=shift.objects.all()
    return render(request,'user/sabte shift/showshift.html',{'p':Shift})
    # else:
    #         return render(request, 'user/login.html')
    #################################################
def deletecost (request,regnum):
    k = shift.objects.filter(regnum = regnum)
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
    return render(request,'user/sabte shift/sabteshift.html',{'Cost':m[0]})
#########################################
def allcost(request):
    if request.session["login"]=="true":
        return render(request, 'user/sabte shift/all cost.html')
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
        ser = personnel.objects.filter(mellicode=mellicode2,pass1=pass12 )
        if len(ser)== 0:
            Msg.append("user or password is wrong")
        if len(Msg) == 0:
            m= personnel.objects.get(mellicode=mellicode2 )
            adm=m.admin
            if adm=="admin":
                request.session["login"]="true"
                m= personnel.objects.get(mellicode=mellicode2 )
                username=m.fn
                mellicode=m.mellicode
                request.session['mellicode'] =m.mellicode

                Cost=shift.objects.filter(payed="no")
                return render(request,'user/admin dashboard.html',{'username':username ,'mellicode':mellicode,'p':Cost,})
            elif adm=="user":
                request.session["login"]="true"
                m= personnel.objects.get(mellicode=mellicode2 )
                username=m.fn
                request.session['mellicode'] =m.mellicode
                request.session['username'] =m.fn
                Cost=shift.objects.all()
                mellicode=m.mellicode
                request.session["login"]="true"

                return render(request,'user/user pages/user dashboard.html',{'username':username,'p':Cost,'mellicode':mellicode})
        else:
            return render(request, 'user/login.html',{'Msg':Msg})
    else:
        z=request.session['mellicode']
        m= personnel.objects.get(mellicode=z )
        username=m.fn
        mellicode=m.mellicode
        adm=m.admin

        if adm=="admin":
            request.session["login"]="true"
            Cost=shift.objects.filter(payed="no")
            return render(request,'user/admin dashboard.html',{'username':username,'mellicode':mellicode,'p':Cost})
        else:
            Cost=shift.objects.filter(payed="no")
            request.session["login"]="true"
            return render(request,'user/user pages/user dashboard.html',{'username':username,'p':Cost,'mellicode':mellicode})




#####################################################
def edituser(request,mellicode):

    m=personnel.objects.filter(mellicode=mellicode)
    return render(request,'user/user pages/edit user.html',{'personnel':m[0]})
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
def findpersonnel(request):
    if request.session["login"]=="true":
        return render(request,'user/admin pages/find personnel.html')
    else:
        return render(request,'user/login.html')
        ##############################################
def showfindedpersonnel(request):
    if request.session["login"]=="true":
        fn=request.POST.get('fn')
        ln=request.POST.get('ln')
        mc=request.POST.get('mc')
        m=personnel.objects.get(mellicode=mc,fn=fn,ln=ln)
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
        m=personnel.objects.get(pelak=pelak)
        pelak=m.pelak
        metraj=m.metraj
        telephon=m.telephon
        parking = m.parking
        return render(request,'user/admin pages/show finded vahed.html',{'pelak':pelak,'metraj':metraj,'telephon':telephon,'parking':parking})
    else:
        return render(request,'user/login.html')

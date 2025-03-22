
from .models import Student,product
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Data
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

# Dictionary to map URL patterns to template files
# TEMPLATE_MAP = {
#     "home": "index.html",
#     "dashboard_v1": "index.html",
#     "dashboard_v2": "index2.html",
#     "dashboard_v3": "index3.html",
#     "widget": "widgets.html",
#     "top_nav": "layout/top-nav.html",
#     "top_nav_sidebar": "layout/top-nav-sidebar.html",
#     "box": "layout/boxed.html",
#     "fixed_sidebar": "layout/fixed-sidebar.html",
#     "fixed_sidebar_custom": "layout/fixed-sidebar-custom.html",
#     "fixed_topnav": "layout/fixed-topnav.html",
#     "fixed_footer": "layout/fixed-footer.html",
#     "collapsed": "layout/collapsed-sidebar.html",
#     "chartjs": "charts/chartjs.html",
#     "flot": "charts/flot.html",
#     "inline": "charts/inline.html",
#     "uplot": "charts/uplot.html",
#     "generalhtml": "UI/general.html",
#     "icons": "UI/icons.html",
#     "buttonHTML": "UI/buttons.html",
#     "sliders": "UI/sliders.html",
# }
#
# # Generic view function to render templates dynamically
# def render_template(request, page):
#     template_name = TEMPLATE_MAP.get(page)
#     if template_name:
#         return render(request, template_name)
#     return HttpResponse("Page not found", status=404)

def home(request):
    return render(request,'index.html')

def stuff_home(request):
    return render(request, "Staff_templates/index.html") #user templates

def dashboard_v1(request):
    return render(request, 'index.html')  # Ensure 'index.html' exists in your templates folder

def dashboard_v2(request):
    return render(request, 'index2.html')  # Ensure 'index2.html' exists in your templates folder

def dashboard_v3(request):
    return render(request, 'index3.html')

def widget(request):
    return render(request,'widgets.html')

def top_nav(request):
    return render(request,'layout/top-nav.html')

def top_nav_sidebar(request):
    return render(request,'layout/top-nav-sidebar.html')

def box(request):
    return render(request,'layout/boxed.html')

def fixed_sidebar(request):
    return render(request,'layout/fixed-sidebar.html')

def fixed_sidebar_custom(request):
    return render(request,'layout/fixed-sidebar-custom.html')

def fixed_topnav(request):
    return  render(request,'layout/fixed-topnav.html')

def fixed_footer(request):
    return render(request,'layout/fixed-footer.html')

def collapsed(request):
    return render(request,'layout/collapsed-sidebar.html')

def chartjs(request):
    return render(request,'charts/chartjs.html')

def flot(request):
    return render(request,'charts/flot.html')

def inline(request):
    return render(request,'charts/nline.html')

def uplot(request):
    return render(request,'charts/uplot.html')

def generalhtml(request):
    return render(request,'UI/general.html')

def icons(request):
    return render(request,'UI/icons.html')

def buttonHTML(request):
    return render(request, 'UI/buttons.html')

def sliders(request):
    return render(request,'UI/sliders.html')

def model(request):
    return render(request, 'UI/modals.html')

def navbar(request):
    return render(request,'UI/navbar.html')

def timeline(request):
    return render(request,'UI/timeline.html')

def ribbon(request):
    return render(request,'UI/ribbons.html')

def genform(request):
    return render(request,'forms/general.html')

def advform(request):
    return render(request,'forms/advanced.html')

def editors(request):
    return render(request,'forms/editors.html')

def validation(request):
    return render(request,'forms/validation.html')

def simpletable(request):
    return render(request,'tables/simple.html')

def dataTa(request):
    return render(request,'tables/data.html')

def jsgrid(request):
    return render(request,'tables/jsgrid.html')

def login(request):
    return render(request,'examples/login.html')

def register(request):
    return render(request,'examples/register.html')

def calender(request):
    return  render(request,'UI/calendar.html')


def about(request):
    return  render(request,'Staff_templates/about.html')


def register(request):
    if request.method == "POST":
        name = request.POST.get('Rname')
        email = request.POST.get('Remail')
        password = request.POST.get('Rpwd')
        confirm_password = request.POST.get('RRpwd')
        usertype=request.POST.get("Rcheck")
        print(usertype)
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')


        user = Data(Full_name=name, Email=email, Password=password, Usertype= usertype if usertype == 'null' else "Employee")
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')
    return render(request, 'examples/register.html')


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        DataEmail = Data.objects.filter(Email=email).first() #quertyset

        if DataEmail:
            print(DataEmail.Email, DataEmail.Password)

            # Directly compare passwords (since they're stored in plain text)
            if password == DataEmail.Password:


                request.session['user_id'] = DataEmail.id
                request.session['email'] = DataEmail.Email # stored id and email in a session


                if DataEmail.Usertype=='Admin':
                     # messages.success(request, f"Login successful! Welcome {DataEmail.Full_name}.")
                     return redirect('dashboard_v1')  # Redirect to dashboard
                elif DataEmail.Usertype=='Employee':
                    # messages.success(request, f"Login successful! Welcome Employee {DataEmail.Full_name}.")
                    messages.success(request, f"Login successful Welcome : {DataEmail.Full_name}")
                    return redirect('Sindex')
            else:
                messages.error(request, "Invalid password")
        else:
            messages.error(request, "User not found")

    return render(request, 'examples/login.html')

# def add(request):
#     if request.method == "POST":
#         name = request.POST.get("Name")
#         email = request.POST.get("email")
#         action = request.POST.get("action")
#         Students = Student.objects.all()
#
#         if action == "add":
#
#             Student.objects.create(name=name, email=email)
#             return render(request, 'home.html', {"Students": Students})
#
#         elif action == "delete":
#             #delete from student where email={{}}
#             Student.objects.filter(email=email).delete()
#             return render(request, 'home.html', {"Students": Students})
#
#         elif action == "update":
#             #update student set={{name}} where email={{}}
#             Student.objects.filter(email=email).update(name=name)
#             return render(request, 'home.html', {"Students": Students})
#
#
#
#
# def pro(request):
#
#     if request.method == "POST":
#         P_Name = request.POST.get("P_name")
#         Quan = request.POST.get("Quan")
#         Price = request.POST.get("Price")
#         action=request.POST.get("action")
#         Product = product.objects.all()
#
#         if action == "add":
#
#             product.objects.create(p_name=P_Name,  Quantity=Quan, price=Price)
#             return render(request, 'result.html', {"products": Product})
#
#         elif action == "delete":
#             #delete from student where email={{}}
#             product.objects.filter(p_name=P_Name).delete()
#             return render(request, 'result.html', {"products": Product})
#
#         elif action == "update":
#             #update student set={{name}} where email={{}}
#             product.objects.filter(p_name=P_Name).update(price=Price)
#             return render(request, 'result.html', {"products": Product})
#
#
#
#
#

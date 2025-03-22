from django.urls import path
from . import views


urlpatterns=[
    # path('<str:page>/', views.render_template, name='render_template'),
    # path('',views.home,name='home'), # Admin templates home page or index page
    path('Staff/', views.stuff_home, name='Sindex'),

    # path('add',views.add,name='add'),
    # path('pro',views.pro,name='pro'),
    path('dashboard/v1/', views.dashboard_v1, name='dashboard_v1'),
    path('dashboard/v2/', views.dashboard_v2, name='dashboard_v2'),
    path('dashboard/v3/', views.dashboard_v3, name='dashboard_v3'),
    path('widgets/',views.widget,name='widgets'),
    path('top_nav/', views.top_nav, name='top_nav'),
    path('top_slide_nav/', views.top_nav_sidebar, name='top_slide_nav'),
    path('box/', views.box, name='box'),
    path('Fixed/slidebar/', views.fixed_sidebar, name='fixed_sidebar'),
    path('Fixed/slidebar/custom/', views.fixed_sidebar_custom, name='fixed_sidebar_custom'),
    path('Fixed/topnav/', views.fixed_topnav, name='fixed_topnav'),
    path('Fixed/footer/', views.fixed_footer, name='fixed_footer'),
    path('collapsed/', views.collapsed, name='collapsed'),
    path('chartjs/', views.chartjs, name='chartjs'),
    path('flot/', views.flot, name='flot'),
    path('inline/', views.inline, name='inline'),
    path('uplot/', views.uplot, name='uplot'),
    path('genHTML/', views.generalhtml, name='genHTML'),
    path('icons/', views.icons, name='icons'),
    path('button/', views.buttonHTML, name='buttonHTML'),
    path('slider/', views.sliders, name='slider'),
    path('model/', views.model, name='model'),
    path('navbar/', views.navbar, name='navbar'),
    path('timeline', views.timeline, name='timeline'),
    path('ribbon', views.ribbon, name='ribbon'),
    path('genform', views.genform, name='generalform'),
    path('advform', views.advform, name='advancedForm'),
    path('editor', views.editors, name='editor'),
    path('valida', views.validation, name='validation'),
    path('simpletable', views.simpletable, name='simpletable'),
    path('Datatable', views.dataTa, name='datatable'),
    path('jsgrid', views.jsgrid, name='jsgrid'),
    path('calendar/', views.calender, name='Calendar'),
    path('about/', views.about, name='Sabout'),
    # path('login/',views.login,name='login'),
    # path('register/',views.register,name='register'),
    path('register/', views.register, name='register'), # for signup
    path('', views.user_login, name='login'), # for login

]
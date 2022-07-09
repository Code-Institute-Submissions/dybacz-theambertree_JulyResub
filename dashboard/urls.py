from . import views
from django.urls import path


urlpatterns = [
    path('', views.DashboardHome.as_view(), name='dashboard_home'),
    path('tables/', views.DashboardTables.as_view(), name='dashboard_tables'),
    path('times/', views.DashboardTimes.as_view(), name='dashboard_times'),
    path('schedule/', views.DashboardSchedule.as_view(), name='dashboard_schedule'),
    path('bookings/', views.DashboardBookings.as_view(), name='dashboard_bookings'),
    path('menu/', views.DashboardBookings.as_view(), name='dashboard_menu'),
    path('messages/', views.DashboardMessages.as_view(), name='dashboard_messages'),
    path('help/', views.DashboardHelp.as_view(), name='dashboard_help'),

]
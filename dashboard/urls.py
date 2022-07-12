from . import views
from django.urls import path


urlpatterns = [
    path('', views.DashboardHome.as_view(), name='dashboard_home'),
    path('tables/', views.DashboardTables.as_view(), name='dashboard_tables'),
    path('tables/remove/<table_id>', views.DashboardTables.as_view()),
    path('tables/add/', views.DashboardTables.as_view()),
    path('tables/edit/', views.DashboardTables.as_view()),
    path('times/', views.DashboardTimes.as_view(), name='dashboard_times'),
    path('times/remove/<timeslot_id>', views.DashboardTimes.as_view()),
    path('times/add/', views.DashboardTimes.as_view()),
    path('times/edit/', views.DashboardTimes.as_view()),
    path('schedule/', views.DashboardSchedule.as_view(), name='dashboard_schedule'),
    path('schedule/remove/<bookingslot_id>', views.DashboardSchedule.as_view()),
    path('schedule/add/', views.DashboardSchedule.as_view()),
    path('schedule/edit/', views.DashboardSchedule.as_view()),
    path('bookings/', views.DashboardBookings.as_view(), name='dashboard_bookings'),
    path('bookings/cancel/<booking_id>', views.DashboardBookings.as_view()),
    path('bookings/add/', views.DashboardBookings.as_view()),
    path('bookings/edit/', views.DashboardBookings.as_view()),
    path('food/', views.DashboardFood.as_view(), name='dashboard_food'),
    path('drinks/', views.DashboardDrinks.as_view(), name='dashboard_drinks'),
    path('messages/', views.DashboardMessages.as_view(), name='dashboard_messages'),
    path('help/', views.DashboardHelp.as_view(), name='dashboard_help'),

]
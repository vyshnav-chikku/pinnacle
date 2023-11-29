from django.urls import path
from app import views

urlpatterns = [
   path('home/',views.home),
   path('',views.jobfairhome),

   path('employee/',views.employee_registration),
   path('employer/',views.employer_registration),

   path('pinnacle-employee-registration/',views.employee_registration_jobfair),
   path('pinnacle-employer-registration/',views.employer_registration_jobfair),
   



   path('admin_signup/',views.admin_signup),
   path('admin_login/',views.admin_login),
   path('logout/',views.logout),
   path('employer/',views.employer_registration),
   path('view_employee/',views.admin_view_employee),
   path('view_employer/',views.admin_view_employer),
   path('admin_index/',views.admin_index),
   path('test/',views.test),

   path('pinnacle-employee-view/',views.admin_view_employee_jobfair),
   path('pinnacle-employer-view/',views.admin_view_employer_jobfair),

   


   

   ]
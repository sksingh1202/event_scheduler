"""event_scheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

from users import views as user_views
from django.contrib.auth import views as auth_views
from tasks import views
from rest_framework.schemas import get_schema_view


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('event-scheduler/admin/', admin.site.urls),
    path('event-scheduler/',include('tasks.urls')),
    path('event-scheduler/login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('event-scheduler/logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('event-scheduler/accounts/', include('allauth.urls')),
    path('event-scheduler/profilee/',user_views.profile, name='profile'),
    path('event-scheduler/apiLogin/',user_views.create_generate_jwt, name='apilogin'),
    
    path('event-scheduler/api/task/all',views.Get_Task,name='task_list_all'),
    path('event-scheduler/api/task/<int:pk>/',views.get_task_detail,name='task_detail'),
    path('event-scheduler/api/task/new/',views.post_task_detail,name='new_task'),
    path('event-scheduler/api/task/<int:pk>/edit_few/',views.patch_task_detail,name='edit_few_task'),
    path('event-scheduler/api/task/<int:pk>/edit/',views.put_task_detail,name='edit_task'),
    path('event-scheduler/api/task/<int:pk>/delete/',views.delete_task_detail,name='delete_task'),

    path('event-scheduler/profile/',user_views.get_profile,name='profile'),
    path('event-scheduler/rsvp/all/',user_views.get_all_rsvp_tasks,name='rsvp-all'),
    path('event-scheduler/rsvp/allother/',user_views.get_all_other_tasks,name='rsvp-all-other'),
    path('event-scheduler/rsvp/allclub/<str:club_name>/',user_views.get_rsvp_club_tasks,name='rsvp-allclub'),
    path('event-scheduler/rsvp/newclub/<str:club_name>/',user_views.get_new_club_tasks,name='rsvp-newclub'),

    path('event-scheduler/rsvp/event/<int:pk>', views.rsvp_a_event, name='rsvp_a_event'),
    path('event-scheduler/unsubscribe/event/<int:pk>', views.unsub_a_event, name='unsub_a_event'),
]

urlpatterns = urlpatterns+[

   path('event-scheduler/openapi/', get_schema_view(
        title="TaskAPI",
        description="API's_FOR_TASK_CREATION"
    ), name='openapi-schema'),

    path('event-scheduler/swagger/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]

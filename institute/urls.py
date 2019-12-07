from django.conf.urls import url
from django.contrib import admin
from instituteapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.main_page),
    url(r'^home/',views.home_page),
    url(r'^contact/',views.contact_page),
    url(r'^feedback/',views.feedback_page),
    url(r'^gallary/',views.gallary_page),
    url(r'^course/',views.course_page),
    url(r'^ourteam/',views.ourteam_page),

]

from django.conf.urls import url
from Discount_Collection import views

#Template Tagging
app_name = 'Discount_Collection'

urlpatterns = [
    url(r'^table/$', views.table, name = 'table'),
    url(r'^formpage/$', views.form_name_view, name='form_name'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$',views.user_login, name='user_login'),
]


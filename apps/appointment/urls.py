from django.urls import path
from . import views

app_name = 'appointment'
urlpatterns = [
    path('', views.DoctorListView.as_view(), name='doctor_list'),
    path('primary', views.PriListView.as_view(), name='primary'),
    path('pediatric', views.PedListView.as_view(), name='pediatric'),
    path('internal', views.IntListView.as_view(), name='internal'),
    path('cardiology', views.CarListView.as_view(), name='cardiology'),
    path('neurology', views.NeuListView.as_view(), name='neurology'),
    path('ob_gy', views.OGListView.as_view(), name='ob_gy'),
    path('orthopedics', views.OrtListView.as_view(), name='orthopedics'),
    path('dermatology', views.DerListView.as_view(), name='dermatology'),
    path('<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path("search/", views.SearchView.as_view(), name="doctor_search"),
]
from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import Doctor


# all doctor list view
class DoctorListView(generic.ListView):
    template_name = 'appointment/doctor_list.html'
    queryset = Doctor.objects.all()
    paginate_by = 6


# List view
class PriListView(generic.ListView):
    template_name = 'appointment/primary_care.html'
    queryset = Doctor.objects.filter(department='primary_care')
    paginate_by = 6


# List view
class PedListView(generic.ListView):
    template_name = 'appointment/pediatrics.html'
    queryset = Doctor.objects.filter(department='pediatrics')
    paginate_by = 6


# List view
class IntListView(generic.ListView):
    template_name = 'appointment/internal_medicine.html'
    queryset = Doctor.objects.filter(department='internal_medicine')
    paginate_by = 6


# List view
class CarListView(generic.ListView):
    template_name = 'appointment/cardiology.html'
    queryset = Doctor.objects.filter(department='cardiology')
    paginate_by = 6


# List view
class NeuListView(generic.ListView):
    template_name = 'appointment/neurology.html'
    queryset = Doctor.objects.filter(department='neurology')
    paginate_by = 6


# List view
class OGListView(generic.ListView):
    template_name = 'appointment/ob_gyn.html'
    queryset = Doctor.objects.filter(department='ob_gyn')
    paginate_by = 6


# List view
class OrtListView(generic.ListView):
    template_name = 'appointment/orthopedics.html'
    queryset = Doctor.objects.filter(department='orthopedics')
    paginate_by = 6


# List view
class DerListView(generic.ListView):
    template_name = 'appointment/dermatology.html'
    queryset = Doctor.objects.filter(department='dermatology')
    paginate_by = 6

# Doctor Detail View
class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = 'appointment/doctor_detail.html'


# Search view
class SearchView(generic.ListView):
    paginate_by = 6
    template_name = 'appointment/search_result.html'

# return search Rural360 result
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Doctor.objects.filter(
                Q(name__icontains=query) | Q(specialization__icontains=query) | Q(department__icontains=query)
            )
        return object_list

# add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context





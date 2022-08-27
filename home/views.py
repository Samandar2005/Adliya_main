from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import *
from django.contrib.auth import *


# Create your views here.


def index(request):
    return render(request, "main/index.html")


class RegionListView(ListView):
    template_name = 'main/regions.html'
    context_object_name = "Regions"
    model = Region


class RegionDetailView(DetailView):
    template_name = 'malumotlar/region.html'
    model = Region

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = Department.objects.filter(
            region=self.kwargs['pk'])
        return context


class DepartmentDetailView(DetailView):
    template_name = 'malumotlar/departments.html'
    model = Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['district'] = District.objects.filter(
            department=self.kwargs['pk'])
        return context

class DistrictDetailView(DetailView):
    template_name = 'malumotlar/district.html'
    model = District

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subdepartment'] = SubDepartment.objects.filter(
            district=self.kwargs['pk'])
        return context

class SubDepartmentDetailView(DetailView):
    template_name = 'malumotlar/sub-department.html'
    model = SubDepartment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = Staff.objects.filter(
            subdepartment=self.kwargs['pk'])
        return context

class DepartmentCreateView(CreateView):
    queryset = Department.objects.all()
    template_name = 'malumotlar/departments-add.html'
    fields = "__all__"

    success_url = '/regions'


class DepartmentUpdateView(UpdateView):
    queryset = Department.objects.all()
    template_name = 'malumotlar/departments-edit.html'
    fields = "__all__"

    success_url = '/regions'


class DepartmentDeleteView(DeleteView):
    queryset = Department.objects.all()
    template_name = 'malumotlar/departments-delete.html'
    fields = "__all__"

    success_url = '/regions'


class StaffDetailView(DetailView):
    template_name = 'malumotlar/staff.html'
    model = Staff
    context_object_name = 'staff'



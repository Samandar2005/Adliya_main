from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import *
from django.contrib.auth import *
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from unicodedata import *
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def index(request):
    bks = Region.objects.all()
    context = {'regions': bks}
    return render(request, "main/index.html", context=context)





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


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="login/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login/login.html", context={"login_form": form})

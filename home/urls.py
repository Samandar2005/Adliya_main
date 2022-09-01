from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='main'),
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('region/', RegionListView.as_view(), name='region'),
    path('region/<int:pk>', RegionDetailView.as_view(), name='region-detail'),
    path('department/<int:pk>', DepartmentDetailView.as_view(),
         name='department-detail'),
    path('department/add', DepartmentCreateView.as_view(), name='department-add'),
    path('department/edit/<int:pk>',
         DepartmentUpdateView.as_view(), name='department-edit'),
    path('department/delete/<int:pk>',
         DepartmentDeleteView.as_view(), name='department-delete'),
    path('district/<int:pk>', DistrictDetailView.as_view(), name='district-detail'),
    path('subdepartment/<int:pk>', SubDepartmentDetailView.as_view(),
         name='subdepartment-detail'),
    path('staff/<int:pk>', StaffDetailView.as_view(), name='staff-detail'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.student_list),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='user-login'),
    path('logout', views.user_logout, name='user-logout'),
    path("admin_login/", views.admin_login, name="admin_login"),

    path('courses/', views.course_list, name='course-list'),
    path('courses/<int:pk>/', views.course_detail, name='course-detail'),
    path('courses/create/', views.course_create, name='course-create'),
    path('courses/update/<int:pk>/', views.course_update, name='course-update'),
    path('courses/delete/<int:pk>/', views.course_delete, name='course-delete'),

    path('students/', views.student_list, name='student-list'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
    path('students/create/', views.student_create, name='student-create'),
    path('students/update/<int:pk>/', views.student_update, name='student-update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student-delete'),

    path('faculties/', views.faculty_list, name='faculty-list'),
    path('faculties/<int:pk>/', views.faculty_detail, name='faculty-detail'),
    path('faculties/create/', views.faculty_create, name='faculty-create'),
    path('faculties/update/<int:pk>/', views.faculty_update, name='faculty-update'),
    path('faculties/delete/<int:pk>/', views.faculty_delete, name='faculty-delete'),

    path('enrollments/', views.enrollment_list, name='enrollment-list'),
    path('students/<int:student_id>/enroll/', views.enrollment_create, name='enrollment-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

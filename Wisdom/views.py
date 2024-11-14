from django.shortcuts import render, redirect
from .models import Course, Student, Faculty,Enrollment
from .forms import CourseForm, StudentForm, FacultyForm,EnrollmentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        context = {}
        n = request.POST['uname']
        p = request.POST['upass']
        cp = request.POST['ucpass']

        if n == '' or p == '' or cp == '':
            context['errmsg'] = 'Field can not be NULL'
            return render(request, 'register.html', context)
        elif len(p) < 8:
            context['errmsg'] = 'Password must be 8 characters'
            return render(request, 'register.html', context)
        elif p != cp:
            context['errmsg'] = 'Password and confirm password must be same'
            return render(request, 'register.html', context)

        else:
            try:
                u = User.objects.create(username=n, email=n)
                u.set_password(p)
                u.save()
                context['success'] = 'User created successfully'
                return render(request, 'register.html', context)
            except Exception:
                context['errmsg'] = 'User Already Exists, Please Login...!'
                return render(request, 'register.html', context)


def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        n = request.POST['uname']
        p = request.POST['upass']

        u = authenticate(username=n, password=p)

        if u is not None:

            login(request, u)
            return redirect('/students/')
        else:
            context = {'errmsg': 'Invalid UserName and Password'}
            return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/login')


def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user.is_superuser:
            login(request, user)
            return redirect('faculty-list')
        else:
            alert = True
            return render(request, "adminlogin.html", {"alert":alert})
    return render(request, "adminlogin.html")


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courselist.html', {'courses': courses})


def course_detail(request, pk):
    course = Course.objects.all().filter(pk=pk).first()
    return render(request, 'coursedetail.html', {'course': course})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course-list')
    else:
        form = CourseForm()
    return render(request, 'courseform.html', {'form': form})


def course_update(request, pk):
    course = Course.objects.all().filter(pk=pk).first()
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course-list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courseform.html', {'form': form})


def course_delete(request, pk):
    course = Course.objects.all().filter(pk=pk).first()
    if request.method == 'POST':
        course.delete()
        return redirect('course-list')
    return render(request, 'coursedelete.html', {'course': course})


# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentlist.html', {'students': students})


def student_detail(request, pk):
    student = Student.objects.all().filter(pk=pk).first()
    return render(request, 'studentdetail.html', {'student': student})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm()
    return render(request, 'studentform.html', {'form': form})


def student_update(request, pk):
    student = Student.objects.all().filter(pk=pk).first()
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'studentform.html', {'form': form})


def student_delete(request, pk):
    student = Student.objects.all().filter(pk=pk).first()
    if request.method == 'POST':
        student.delete()
        return redirect('student-list')
    return render(request, 'studentdelete.html', {'student': student})


# Faculty Views
def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'facultylist.html', {'faculties': faculties})


def faculty_detail(request, pk):
    faculty = Faculty.objects.all().filter(pk=pk).first()
    return render(request, 'facultydetail.html', {'faculty': faculty})


def faculty_create(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty-list')
    else:
        form = FacultyForm()
    return render(request, 'facultyform.html', {'form': form})


def faculty_update(request, pk):
    faculty = Faculty.objects.all().filter(pk=pk).first()
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty-list')
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'facultyform.html', {'form': form})


def faculty_delete(request, pk):
    faculty = Faculty.objects.all().filter(pk=pk).first()
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculty-list')
    return render(request, 'facultydelete.html', {'faculty': faculty})

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollmentlist.html', {'enrollments': enrollments})

def enrollment_create(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment_form.html', {'form': form})


from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import BlogSerializer


def blog_list(request):

    if request.user.is_authenticated:
        blogs = Blog.objects.all()
    else:
        blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blog_list.html', context)


def user_blog_list(request):

    if request.user.is_authenticated:
        your_blogs = Blog.objects.filter(author=request.user)
    else:
        your_blogs = []

    context = {
        'your_blogs': your_blogs,
    }

    return render(request, 'blogs/user_blog_list.html', context)


@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_list")

    else:
        form = BlogForm(current_user=request.user)

    return render(request, 'blogs/add_blog.html', {'form': form})


@login_required
def edit_blog(request, pk):

    blog = get_object_or_404(Blog, pk=pk)

    if request.user != blog.author:
        return HttpResponseForbidden("You don't have permission to edit this blog.")

    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blogs/edit_blog.html', {'form': form})


@login_required
def delete_blog(request, pk):

    blog = get_object_or_404(Blog, pk=pk)

    if request.user != blog.author:
        return HttpResponseForbidden("You don't have permission to delete this blog.")

    blog = Blog.objects.get(pk=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('blog_list')

    return render(request, 'blogs/delete_blog.html', {'blog': blog})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_login(request):
    error_message = None

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a different page after login
                return redirect('blog_list')
            else:
                error_message = "Invalid username or password. Please try again."
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('blog_list')


# api views.


@api_view(['GET'])
def all_blogs_api(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


# user specific blogs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@login_required
def user_blogs_api(request):
    blogs = Blog.objects.filter(author=request.user)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow anyone to login
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'User logged in successfully.'}, status=200)
    else:
        return Response({'error': 'Invalid username or password.'}, status=401)


@api_view(['POST'])
# Allow only authenticated users to logout
@login_required
@permission_classes([IsAuthenticated])
def logout_api(request):
    logout(request)
    return Response({'message': 'User logged out successfully.'}, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Allow only authenticated users
def current_user_api(request):
    user_data = {
        'is_authenticated': True,
        'username': request.user.username,
    }
    return Response(user_data)


User = get_user_model()


@api_view(['POST'])
def signup_api(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            try:
                user = User.objects.create_user(
                    username=username, password=password)
                login(request, user)
                return Response({'message': 'User registered and logged in successfully.'})
            except:
                return Response({'message': 'User registration failed.'}, status=400)

    return Response({'message': 'Invalid data provided.'}, status=400)

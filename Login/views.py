# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from . import models
from Login.models import Restaurant_name,Rate,User,Review,Comment
from .forms import RestForm

# Create your views here.


def index(request):
    rest_list = models.Restaurant_name.objects.all()
    return render(request, 'Login/index.html', {"rest_list": rest_list})

def category(request, category):
    rest_list = Restaurant_name.objects.filter(category=category)
    return render(request, 'Login/index.html', {"rest_list": rest_list})


def details(request, rest_id):
    rest = get_object_or_404(Restaurant_name, pk=rest_id)
    reviewList = Review.objects.filter(restId=rest_id)
    return render(request, 'Login/details.html', {"rest": rest, "reviewList": reviewList})


def rate(request, rest_id):
    if request.session.get('is_login'):
        rest = get_object_or_404(Restaurant_name, pk=rest_id)
        user = get_object_or_404(User, pk=request.session['userid'])
        reviewList = Review.objects.filter(restId=rest_id)

        if request.method == 'POST':
            rate = request.POST.get('your_rate')
            review = request.POST.get('your_review')
            new_rate = models.Rate()
            new_review = models.Review()
            new_rate.restid = rest
            new_rate.userid = user
            new_rate.rate = rate
            new_review.restId = rest
            new_review.ownerUserId = user
            new_review.content = review
            new_rate.save()
            new_review.save()
            restList = Rate.objects.filter(restid=rest.Rest_id)
            sum = 0.0
            count = 0
            for restObj in restList:
                sum += restObj.rate
                count += 1
            rest.ave_rate = round(sum / count, 3)
            rest.save()
            return render(request, 'Login/details.html', {"rest": rest, "reviewList": reviewList})
        return render(request, 'Login/rate.html', {"rest": rest})
    else:
        return render(request, 'Login/login.html')


def comment(request, rest_id, review_id):
    rest = get_object_or_404(Restaurant_name, pk=rest_id)
    reviewObj = get_object_or_404(Review, pk=review_id)
    commentList = Comment.objects.filter(review=reviewObj)
    if request.method == "POST":
        c = request.POST.get('c')
        new_comment=models.Comment()
        new_comment.review = reviewObj
        new_comment.content = c
        new_comment.commentUserName = reviewObj.ownerUserId.username
        new_comment.save()
        return render(request, 'Login/comment.html', {'rest': rest, 'reviewObj': reviewObj, 'commentList': commentList})
    return render(request, 'Login/comment.html', {'rest': rest, 'reviewObj':reviewObj ,'commentList': commentList})


def login(request):
    if request.session.get('is_login',None):
        return redirect("/index/")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = ""
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['username'] = user.username
                    request.session['userid'] = user.user_id
                    return redirect("/index/")
                else:
                    message = "Password is incorrent"
            except:
                message = "User doesn't exist"
        return render(request, 'Login/login.html', {"message": message})
    return render(request, 'Login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # Can't register user when you have logged in
        return redirect("/index/")
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        message = ""
        if password1 and password2:
            if password1 != password2:
                message = "The password entered twice is different"
                return render(request, 'Login/register.html', locals())
            else:
                username_exist = models.User.objects.filter(username=username)
                if username_exist:
                    message = "Username has registered"
                    return render(request, 'Login/register.html', locals())
                new_user = models.User()
                new_user.username = username
                new_user.password = password1
                new_user.save()
                return redirect('/login')
    return render(request, 'Login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")

def new(request):
    return render(request, 'Login/newrest.html')

def add(request):
    if request.method == "POST":
        new_rest = Restaurant_name(
            img=request.FILES.get('img'),
            Rest_name = request.POST.get('restname'),
            address = request.POST.get('address'),
            category = request.POST.get('category')
        )
        new_rest.save()
        return redirect('/index')

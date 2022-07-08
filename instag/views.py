from django.shortcuts import render,redirect
from django.db.models import Count
from django.contrib.auth.models import User
from .models import Post,Like,Comment,Profile
from .forms import postForm
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your views here.

@login_required(login_url='/')
def index(request):
    di = {}
    lc = {}
    pf = Profile.objects.get(user=request.user)
    fg = Profile.objects.get(user=request.user).follows.all()
    posts = Post.objects.filter(author__in=fg)
    for post in posts:
        lo = [i.likedby for i in Like.objects.filter(post=post)]
        lc['likes'] = lo
        lc['comments'] = list(Comment.objects.filter(post=post))
        di[post] = lc
        lo = []
        lc = {}
    context = {
        'pf' : pf,
        'di' : di
    }
    
    return render(request,'index.html',context)
    
@login_required(login_url='/')
def profile(request):
    di = {}
    lc = {}
    us = request.user
    pf = Profile.objects.get(user=request.user)
    self = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author=pf)
    for post in posts:
        lo = [i.likedby for i in Like.objects.filter(post=post)]
        lc['likes'] = lo
        lc['comments'] = list(Comment.objects.filter(post=post))
        di[post] = lc
        lo = []
        lc = {}
    fs = Profile.objects.get(user=request.user).followed_by.all()
    fg = Profile.objects.get(user=request.user).follows.all()
    btn = 'Edit Profile'
    context = {
        'self' : self,
        'us' : us,
        'fs' : fs,
        'fg' : fg,
        'pf' : pf,
        'posts' : posts,
        'btn' : btn,
        'di' : di
    }
    return render(request,'profile.html',context)


def search(request):
    di = {}
    lc = {}
    search = request.GET['profile']
    us = User.objects.get(username=search)
    pf = Profile.objects.get(user=us)
    self = Profile.objects.get(user=request.user)
    self_pf = Profile.objects.get(user=request.user)
    fs = Profile.objects.get(user=us).followed_by.all()
    fg = Profile.objects.get(user=us).follows.all()
    posts = Post.objects.filter(author=pf)
    for post in posts:
        lo = [i.likedby for i in Like.objects.filter(post=post)]
        lc['likes'] = lo
        lc['comments'] = list(Comment.objects.filter(post=post))
        di[post] = lc
        lo = []
        lc = {}
    if search == request.user.username:
        btn = 'Edit Profile'
    else:
        if Profile.objects.filter(user=request.user,follows=pf):
            btn = 'Following'
        else:
            btn = 'Follow'
        
    context = {
        'is_searched' : True, 
        'us' : us,
        'fs' : fs,
        'fg' : fg,
        'pf' : pf,
        'self' : self,
        'self_pf' : self_pf,
        'posts' : posts,
        'btn' : btn,
        'di' : di
    }

    
    return render(request,'profile.html',context)

def authorprofile(request,author):
    di = {}
    lc = {}
    us = User.objects.get(username=author)
    pf = Profile.objects.get(user=us)
    self = Profile.objects.get(user=request.user)
    fs = Profile.objects.get(user=us).followed_by.all()
    fg = Profile.objects.get(user=us).follows.all()
    posts = Post.objects.filter(author=pf)
    for post in posts:
        lo = [i.likedby for i in Like.objects.filter(post=post)]
        lc['likes'] = lo
        lc['comments'] = list(Comment.objects.filter(post=post))
        di[post] = lc
        lo = []
        lc = {}
    if author == request.user.username:
        btn = 'Edit Profile'
    else:
        if Profile.objects.filter(user=request.user,follows=pf):
            btn = 'Following'
        else:
            btn = 'Follow'
        
        
    context = {
        'us' : us,
        'fs' : fs,
        'fg' : fg,
        'pf' : pf,
        'self' : self,
        'posts' : posts,
        'btn' : btn,
        'di' : di
    }

    
    return render(request,'profile.html',context)

def updatelikes(request):
    action = request.GET.get('action',None)
    post_id = request.GET.get('post',None)
    post = Post.objects.get(id=post_id)
    pf = Profile.objects.get(user=request.user)
    if action == 'liked':
        Like.objects.create(post=post,likedby=pf)
    else:
        Like.objects.get(post=post,likedby=pf).delete()
    likes = Like.objects.filter(post=post).count()
    di = {
        'pf' : pf.id,
        'likes' : likes
    }
    return JsonResponse(di)

def followupdate(request):
    action = request.GET.get('action',None)
    to = request.GET.get('to',None)
    us = User.objects.get(username=to)
    to = Profile.objects.get(user=us)
    by = Profile.objects.get(user=request.user)
    
    if action == 'Follow':
        by.follows.add(to)
        btn = 'Following'
    else:
        by.follows.remove(to)
        btn = 'Follow'
    
    followers = Profile.objects.get(user=us).followed_by.all().count() 
    di = {
        'by' : by.id,
        'button' : btn, 
        'followers' : followers
    }
    return JsonResponse(di)

def comments(request):
    post_id = request.GET.get('id',None)
    comment = request.GET.get('comment',None)
    post = Post.objects.get(id=post_id)
    pf = Profile.objects.get(user=request.user)
    obj = Comment.objects.create(post=post,commentby=pf,comments=comment)
    comments = Comment.objects.filter(post=post).count()
    di = {
        'comments' : comments,
        'id' : obj.id
    }
    return JsonResponse(di)

def changepass(request):
    message = ''
    old = request.POST['oldpass']
    new = request.POST['newpass']
    user = User.objects.get(username=request.user)
    if user.check_password(old):
        if old != new:
            user.set_password(new)
            user.save()  
            message = 'Password changed successfully'
            msgclass = 'alert-success'
        else:
            message = 'Old password cannot be your new password'
            msgclass = 'alert-danger'
    else:
        message = 'Incorrect old password'
        msgclass = 'alert-danger'
    di = {
        'message' : message,
        'msgclass' : msgclass
    }
    return JsonResponse(di)

def editprofile(request):
    user = request.user
    user.username = request.POST['username']
    user.save()
    profile = Profile.objects.get(user=request.user)
    profile.full_name = request.POST['fullname']
    profile.bio = request.POST['bio']
    profile.save()
    return redirect('profile')

def newpost(request):
    user = Profile.objects.get(user=request.user)
    author = Post.objects.all()
    author.create(author=user,img=request.FILES['mypost'],caption=request.POST['caption'])
    return redirect('profile')

def dp(request):
    user = Profile.objects.get(user=request.user)
    img = Image.open(request.FILES['mydp'])
    width = img.size[0]
    height = img.size[1]
    if width > height:
        diff = width - height
        off = diff/2
        resize = (off,0,width-off,height)
    elif height > width:
        diff = height - width
        off = diff/2
        resize = (0,off,width,height-off)
    else:
        user.dp = request.FILES['mydp']
        user.save()
        img.close()
        return redirect('profile')

    final = img.crop(resize)
    blob =  BytesIO()
    final.save(blob,format='JPEG')
    user.dp.save('dp.jpg',File(blob)) 
    user.save()
    img.close()
    return redirect('profile')

def suggestions(request):
    users = User.objects.filter(is_superuser=False,is_staff=False).only('username')
    name = [user.username for user in users]
    di = {'name' : name}
    return JsonResponse(di)

def deletepost(request,id):
    Post.objects.get(id=id).delete()
    return redirect('profile')

def editpost(request,postid):
    post = Post.objects.get(id=postid) 
    post.caption = request.GET['caption']
    post.save()
    return redirect('profile')

def unfollow(request,author):
    Profile.objects.get(user=request.user).follows.remove(author)
    return redirect('index')

def deletecomment(request,comment):
    Comment.objects.get(id=comment).delete()
    return redirect(request.META['HTTP_REFERER'])
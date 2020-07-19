from django.urls import path
from . import views


urlpatterns=[
   
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('suggestions/',views.suggestions,name='suggestions'),
    path('search/',views.search,name='search'),
    path('update_likes/',views.updatelikes,name='updatelikes'),
    path('follow_update/',views.followupdate,name='followupdate'),
    path('comments/',views.comments,name='comments'),
    path('change_pass/',views.changepass,name='changepass'),
    path('edit_profile/',views.editprofile,name='editprofile'),
    path('dp/',views.dp,name='dp'),
    path('new_post/',views.newpost,name='newpost'),
    path('delete_comment/<comment>',views.deletecomment,name='deletecomment'),
    path('author_profile/<author>',views.authorprofile,name='authorprofile'),
    path('unfollow/<author>',views.unfollow,name='unfollow'),
    path('delete_post/<id>',views.deletepost,name='deletepost'),
    path('edit_post/<postid>',views.editpost,name='editpost')

]


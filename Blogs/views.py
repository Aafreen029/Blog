from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category
from django.contrib import messages 
from django.core.paginator import Paginator


# Create your views here.

def HomeView(request):
    if request.user.is_authenticated:
        allposts=Post.objects.all()
    else:
        allposts=Post.objects.filter(is_published=True)
    paginator = Paginator(allposts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'page_obj': page_obj}
    return render(request,'index.html',context)

def add_post(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    categories=Category.objects.all()
    user = request.user
    if request.method == 'POST':
        title=request.POST['title']
        category_id=request.POST['category_id']
        content=request.POST['content']
        thumbnail=request.FILES['thumbnail']
        published=request.POST['published']

        if published=="on":
            published=True
        else:
            published=False
        print(published)

        category_obj=Category.objects.filter(id=category_id).first()
        Post.objects.create(title=title,category=category_obj,content=content,thumbnail=thumbnail,created_by=user,is_published=published)
        messages.success(request,"Form Submitted Successfully")
        return redirect('/')
    else:
        return render(request,'blog/add_post.html',{'categories':categories})
    
def blog_post(request,title):
    try:
        blog=Post.objects.filter(title=title).first()
        recent_posts = Post.objects.filter(is_published=True).order_by('-created_by')[:3]
        context={'Post': blog,'recent_posts': recent_posts}
        return render(request,'blog/blog_post.html',context)
    except Post.DoesNotExist:
        return HttpResponse("post not found")
   
def edit_post(request, Post_id):
    posts = get_object_or_404(Post,id=Post_id)
    print(posts.title)
    
    if request.method == 'POST':
        title=request.POST.get("title")
        content=request.POST.get("content")
        thumbnail=request.FILES.get("thumbnail")
        published=request.POST.get("published")
        if published=="on":
            published=True
        else:
            published=False

        print(published)
        
        try:
            posts.title=title
            posts.content=content
            posts.thumbnail=thumbnail
            posts.is_published=published
           
            posts.save()
            messages.success(request,"Update successfully")
            return redirect('/')
        
        except Exception as e:
            messages.error(request,"Error updating Post",str(e))

    context={'Post':posts,'user':request.user}
    return render(request, 'blog/edit_post.html',context)

def delete_post(request, Post_id):
    posts = get_object_or_404(Post,id=Post_id)
    posts.delete()
    messages.success(request,"deleted successfully")
    return redirect('/')









          


   


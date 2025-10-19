from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import blogPost,comments
from django.contrib.auth.decorators import login_required

# Create your views here.


def index (request):
    post = blogPost.objects.all()
    context = {"post":post}

    return render(request,"index.html",context)


@login_required
def add(request):
    
    if request.method == "POST":
        user = request.user
        name = request.POST.get("name")
        description = request.POST.get("description")
        
        p = blogPost.objects.create(
            title=name,
            des=description,
            user=user,
        )
        
    elif request.method == "GET":
        print(request.POST)
    
    context = {}
    return render(request,"add.html",context)




def detail(request,pk):
    post = get_object_or_404(blogPost,pk=pk)
    comment = comments.objects.filter(postoa=post)
    if request.method == "POST":
       name =  request.POST.get("name")
       email =  request.POST.get("email",None)
       address =  request.POST.get("address","")
       city =  request.POST.get("city")
       state =  request.POST.get("state")
       zipcode =  request.POST.get("zipcode")
       hide_name =  request.POST.get("hide_name")
       hide_name =  True if hide_name else False
       text =  request.POST.get("text")
       comments.objects.create(
           name=name,
           email = email,
           adrees = address,
           city = city,
           ostan = state,
           zipcode = zipcode,
           hideusers = hide_name,
           comment = text,
           postoa = post,
       )
       if hide_name:
          hide_name=True
       else:
          hide_name = False
    context = {"post":post,"comments":comment}
    return render(request, 'detail.html',context)

# def custom_404(request):
#     return render(request, '404.html')

def recent(request):
 
    post = blogPost.objects.all().order_by("-date_create")
    post = post[:5]
    context = {"post":post}
    return render(request,"index.html",context)
        



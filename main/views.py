from django.shortcuts import redirect, render, HttpResponse
from .models import Movie,Dojos,Ninjas
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)


def add(request):
    title = request.POST['title']
    release = request.POST['date']
    duration = request.POST['duration']
    description = request.POST['description']

    new_movie = Movie.objects.create(title = title, description = description, release_date = release, duration = duration)
    print(new_movie)
    return redirect("/")

def delete(request,num):
    id_m = num
    bring_movie = Movie.objects.get(id = id_m)
    bring_movie.delete()
    return redirect("/")

def edit(request,num):
    bring_movie = Movie.objects.get(id = num)
    return render(request,'form.html')

def index2(request):
    ninjas = Ninjas.objects.all()
    dojos = Dojos.objects.all()
    context = {
        'ninjas': ninjas,
        'dojos': dojos
    }
    return render(request,'index2.html',context)

def add2(request):
    first_name = request.POST['name']
    last_name = request.POST['last']
    dojo_id = request.POST['dojo']
    dojo = Dojos.objects.get(id=dojo_id)
    new_ninja= Ninjas.objects.create(firs_name=first_name, last_name=last_name, dojo = dojo)
    print(new_ninja)
    return redirect('home/')
    
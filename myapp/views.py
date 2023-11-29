from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Project
from .forms import CreateNew,EditProjectForm

# Create your views here.
def index(request):
    return render(request,"Index.html")

def hello(request):
    return HttpResponse('<h2>Hola mundo</h2>')

def projects(request):
    projects = list(Project.objects.values())
    return render(request,'projects.html',{'projects':projects})

def create_task(request):
    if request.method == 'GET':
        return render(request,'create.html',{'form':CreateNew() })
    else:
        Project.objects.create(name=request.POST['name'],pais=request.POST['pais'],
        nodos=request.POST['nodos'],num_cores=request.POST['num_cores'],ram=request.POST['ram'],almacenamiento=request.POST['almacenamiento'],teraFlops=request.POST['teraFlops'],SO=request.POST['SO'])
        return redirect('/')
    
def delete(request, id_comp):
    print(f"ID a eliminar: {id_comp}")
    comp = Project.objects.get(pk=id_comp)
    comp.delete()
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {'projects': projects, 'mensaje': 'Eliminado'})

# def pestaña_editar(request):
#     return render(request,'edicion.html')


def editar(request, id_comp):
    comp = get_object_or_404(Project, pk=id_comp)
    
    if request.method == 'POST':
        form = EditProjectForm(request.POST, instance=comp, prefix=str(comp.id))
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditProjectForm(instance=comp, prefix=str(comp.id))

    projects = list(Project.objects.values())
    return render(request, 'projects.html', {'projects': projects, 'form': form, 'mensaje': 'Editado'})

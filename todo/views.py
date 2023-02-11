from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def index(request):
    
    if (request.method == "POST"):
        # form = TodoForm(request.POST)
        # print(form)
        # print(request.POST.get("title"))
        Todo.objects.create(
            title=request.POST.get("title"),
            details = request.POST.get("details")
            )
        return HttpResponseRedirect("/todo/")
        
    if (request.method == "GET"):
        todos = Todo.objects.all()
        form = TodoForm()
        return render(request, "index.html", {"todos": todos, "form": form})
        
        
def destroy(request, id):
    Todo.object.delete(id)
    return HttpResponseRedirect("/todo/")
        


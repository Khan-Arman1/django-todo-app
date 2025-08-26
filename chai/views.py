from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm, UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# # Create your views here.
# def chaihome(request):
#     return render(request, 'index.html')


def todolist(request):
    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'todo_list.html', {'form':form, 'todos':todos})

@login_required
def todo_add(request):
    if request.method == "POST":
        forms = TodoForm(request.POST)
        if forms.is_valid():
            todo = forms.save(commit=False)
            todo.user = request.user
            forms.save(commit=True)
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html',{'form':form})

@login_required
def todoedit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        # print(form.instance)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            form.save(commit=True)
            return redirect('todo_list', permanent=True)
    else:
        form = TodoForm(instance=todo)
        return render(request, 'add_todo.html', {'form':form})

def deletetodo(request, todo_id):
        todo = get_object_or_404(Todo, pk=todo_id)
    # if request.method == "POST": # yaha toh hum form se data le rahe hai
        todo.delete()            
        return redirect('todo_list')
    # else:
        # return render(request, 'delete_todo.html', {'todo':todo})

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html',{'form':form})

def search(request):
    if request.method == "POST":
        todo = Todo.objects.filter(user = request.user)
        query = request.POST.get('q')
        if todo and query:
            todos = todo.filter(Q(todo_name__icontains=query) | Q(todo_text__icontains=query))
            return render(request, 'search.html',{'todos':todos, 'query':query})
        else:
            todos = Todo.objects.all()
            return render(request, 'search.html',{'todos':todos, 'query':query})

    return redirect('todo_list')
    #     todo= Todo.objects.all()
    #     if search:
    #         data = todo.filter(text__icontains=query)
    #         return render(request, 'search.html', {'data':data})
    #     else:
    #         todo = Todo.objects.all()
    #         return render(request, 'search.html', {'data':todo})
    # else:
    #     return redirect('todo_list')

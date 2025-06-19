from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from home.models import Task
# Create your views here.


def home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(
            title=title,
            description=desc
        )
        ins.save()
        return redirect('/?success=1')

    success = request.GET.get('success') == '1'
    return render(request, 'home.html', {'success': success})


def showList(request):
    tasks = Task.objects.all()
    return render(request, 'showList.html', {'tasks': tasks})


def delete_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        task.delete()
    return redirect('showList')

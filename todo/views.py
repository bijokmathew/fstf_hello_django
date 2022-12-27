from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .form import Form_item


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_todo_list(request):
    if request.method == "POST":
        form = Form_item(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")
    form = Form_item()
    context = {
        'form': form
    }
    return render(request, 'todo/todo_list_add.html', context)


def edit_todo_list(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = Form_item(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")
    elif request.method == "GET":
        form = Form_item(instance=item)
        context = {
            'form': form
        }
        return render(request, 'todo/todo_list_edit.html', context)


def toggle_todo_list(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect("get_todo_list")


def delete_todo_list(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect("get_todo_list")
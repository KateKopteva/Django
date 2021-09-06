"""Дана форма с тремя текстовыми полями. Вернуть пользователю
максимальное по длине значение поля. Пример: введены abc, abcdef, ab -
пользователю вернется abcdef."""
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def get_max_word(request):
    if request.method =='GET':
        return render(request, 'task_18_1.html')
    if request.method =='POST':
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')
        name3 = request.POST.get('name3')
        return HttpResponse(f'{max(len(name1), len(name2), len(name3))}')

def get_data(request):
    if request.method =='GET':
        return render(request, 'task_18_2.html')
    if request.method =='POST':
        name = request.POST.get('name')
        date_object = datetime.datetime.strptime(name, '%Y-%m-%d')
        if date_object.month == 1 and date_object.day == 1:
            return HttpResponse(f'С Новым {date_object.year} годом!')
        else:
            return HttpResponse(f'{date_object.date()}')
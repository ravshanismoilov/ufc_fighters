from django.shortcuts import render
from django.views import View
from .models import Category, Fighter


def get_home(request):
    return render(request, 'index.html')


class CategoryFighters(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'fighter/category_fighters.html', context=context)


class CategoryDetailFighter(View):
    def get(self, request, pk):
        fighters = Fighter.objects.filter(category=pk)
        categoryname = Category.objects.get(pk=pk)
        context = {
            'fighters': fighters,
            'categoryname': categoryname
        }
        return render(request, 'fighter/fighters.html', context=context)


class FighterDetail(View):
    def get(self, request, pk):
        fighter = Fighter.objects.get(pk=pk)
        division = Category.objects.filter(pk=pk)
        context = {
            'fighter': fighter,
            'division': division
        }
        return render(request, 'fighter_detail.html', context=context)
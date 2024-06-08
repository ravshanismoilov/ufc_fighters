from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Fighter
from .forms import CreateFighterForm


def get_home(request):
    return render(request, 'index.html')


class CategoryFighters(View):
    def get(self, request):
        categories = Category.objects.all().order_by('-id')
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
        return render(request, 'fighter/fighter_detail.html', context=context)


class CreateFighter(View):
    def get(self, request):
        create_form = CreateFighterForm()
        context = {
            'create_form': create_form
        }
        return render(request, 'fighter/add_fighter.html', context=context)

    def post(self, request):
        create_form = CreateFighterForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('category-fighter')
        context = {
            'create_form': create_form
        }
        return render(request, 'fighter/add_fighter.html', context=context)
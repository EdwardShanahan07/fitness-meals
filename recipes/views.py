from django.shortcuts import render
from django.views import generic
from .models import Recipe


class Index(generic.ListView):
    """
        Render home page and display 
        the 3 most recently created recipes
    """
    """
        Code used is taken from Code Institute Blog Walkthrough porject
        'I Think Therefore I Blog'
    https://github.com/Code-Institute-Solutions/Django3blog/tree/master/
    12_final_deployment
    """

    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

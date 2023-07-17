from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
from .forms import CommentForm


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


class RecipeList(generic.ListView):
    """
        Render all shared recipes
    """
    """
        Code used is taken from Code Institute Blog Walkthrough porject
        'I Think Therefore I Blog'
    https://github.com/Code-Institute-Solutions/Django3blog/tree/master/
    12_final_deployment
    """

    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes_list.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False

        ingredients_list = recipe.ingredients.split("\n")
        methods_list = recipe.method.split("\n")

        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "ingredients_list": ingredients_list,
                "methods_list": methods_list,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

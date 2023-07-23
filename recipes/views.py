from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm, RecipeForm

class RecipeDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    template_name = 'recipe_delete.html'
    model = Recipe

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def get_success_url(self):
        return reverse('recipes_list')  

    def post(self, request, *args, **kwargs):
        recipe = self.get_object()
        recipe.delete()
        messages.success(self.request, "Recipe deleted successfully!")  
        return redirect(self.get_success_url())

class RecipeCreate(LoginRequiredMixin, generic.CreateView):
    """ 
        Create Recipe View.
        Checks if the form is valid.
        If the recipe is created successfully the user will be redirect 
        to the recipe view page.
    """
    
    template_name = "recipe_create.html"
    model = Recipe
    form_class = RecipeForm
    success_url = '<slug:slug>/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Recipe Created Successfully!")
        return response
    
    def get_success_url(self):
        return reverse("recipe_detail", kwargs={'slug': self.object.slug})
    
    
class RecipeEdit(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    template_name = 'recipe_edit.html'
    model = Recipe
    form_class = RecipeForm
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    def get_success_url(self):
        messages.success(self.request, "Recipe Updated Successfully!")
        return reverse("recipe_detail", kwargs={'slug': self.object.slug})
        


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
        queryset = Recipe.objects.filter(status__in=[0, 1])
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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )
        
    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False

        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
            
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = recipe
            comment.save()
        else: 
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )
        
        
class RecipeLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))

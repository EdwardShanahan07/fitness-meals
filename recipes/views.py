from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm, RecipeForm

class RecipeCreate(LoginRequiredMixin, generic.CreateView):
    """ Create Recipe View """
    
    template_name = "recipe_create.html"
    model = Recipe
    form_class = RecipeForm
    success_url = '<slug:slug>/'
    
    # Checks if the form is valid
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Recipe Created Successfully!")
        return response
    
    # If created successfully the user will redirect to the recipe detail page.
    def get_success_url(self):
        return reverse("recipe_detail", kwargs={'slug': self.object.slug})
    
    # If form is invaild message error will appear
    def form_invalid(self, form):
        messages.error(self.request, "Error creating the recipe. Please check the form.")
        return super().form_invalid(form)
    
class RecipeDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """ Delete Recipe View """
    template_name = 'recipe_delete.html'
    model = Recipe

    # Check if the user owns the recipe
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    # If deleted successfully they will be redirected to the recipes page
    def get_success_url(self):
        return reverse('recipes_list')  

    # Delete Recipe and display success message
    def post(self, request, *args, **kwargs):
        recipe = self.get_object()
        recipe.delete()
        messages.success(self.request, "Recipe deleted successfully!")  
        return redirect(self.get_success_url())

class RecipeEdit(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    template_name = 'recipe_edit.html'
    model = Recipe
    form_class = RecipeForm
    
    # Check if the user owns the recipe
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    # A success message will display if edited successfully
    def get_success_url(self):
        messages.success(self.request, "Recipe Updated Successfully!")
        return reverse("recipe_detail", kwargs={'slug': self.object.slug})

class UserProfile(LoginRequiredMixin, generic.ListView):
    """ User Profile View """
    model = Recipe
    template_name = 'user_profile.html'
    context_object_name = 'user_recipes'
    
    # Gets logged in user
    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)
    
    # Filters users shared and frafted recipes
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['recipes_public'] = context['user_recipes'].filter(status=1)
        context['recipes_draft'] = context['user_recipes'].filter(status=0)
        return context


class Index(generic.ListView):
    """
        Render home page and display the 3 most recently created recipes
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class RecipeList(generic.ListView):
    """Render all users shared recipes"""

    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes_list.html'
    paginate_by = 6


class RecipeDetail(View):
    """ Recipe Detail View """
    
    # Get recipe and comments
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status__in=[0, 1])
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        
        # Splits ingredients and method by escape key
        ingredients_list = recipe.ingredients.split("\n")
        methods_list = recipe.method.split("\n")

        # Checks if the user has liked the recipe
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
        
        
    # Post comment form and render comments 
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
    """ Recipe Like View """
    
    # Post like form 
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
    

def custom_404(request, exception):
    """ Render 404 page """
    return render(request, "404.html")
from .models import Comment, Recipe
from django import forms
from django.utils.text import slugify

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
        
class RecipeForm(forms.ModelForm):
    """ 
    Recipe form class 
    Uses a save method to save the recipe title as the slug
    """
    class Meta:
        model = Recipe
        fields = (
            'title',
            'description',
            'image',
            'category',
            'prep_time',
            'cook_time',
            'servings',
            'calories',
            'carbs',
            'protein',
            'fats',
            'ingredients',
            'method',
            'status',
        )
        
        labels = {
            'title': 'Recipe Title',
            'description': 'Description',
            'image': 'Recipe Image',
            'category': 'Meal Type',
            'prep_time': 'Preparation Time',
            'cook_time': 'Cook Time',
            'servings': 'Servings',
            'calories': 'Calories',
            'carbs': 'Carbs',
            'protein': 'Protein',
            'fats': 'Fats',
            'ingredients': 'Recipe Ingredients',
            'method': 'Method',
            'status': 'Status'
        }
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)  
        if commit:
            instance.save()
        return instance
        

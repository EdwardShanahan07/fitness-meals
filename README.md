# Fitness Meals

## Content

- [UX](#ux)
  - [Project Description](#project-description)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [ERD Database](#erd-database)
    - [Wireframes](#wireframes)
- [Tests](#tests)
  - [Bugs](#bugs)
    - [Solved Bugs](#solved-bugs)
- [Deployment](#deployment)
  - [Database](#database)
  - [Cloudinary](#cloudinary)
  - [Heroku](#heroku)
  - [IDE](#ide)
- [Credits](#credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)

## UX

### Project Description

Fitness Meals is an application that lets users share healthy recipes. Registered users can create and share recipes and engage with other members by liking and commenting on their recipes. Unregistered users will only be able to view recipes but need to register to use the full features of the application. Fitness Meals is built with the Django Python framework using the Agile methodology to plan the project.

### Project Goals

1. Create a user-friendly application with a visually pleasing design
2. Make sure the website is fully responsive to fit all screen sizes
3. View a list of member's shared recipes on a pagination pages
4. Implement user registration and login so authentic users can create and share their recipes and also like and comment on other member's recipes
5. Deploy the application making sure the site has excellent performance and accessibility

### User Stories

- As a User, I can view the home page so that I can learn about the application
- As a User, I can register an account so that I can create and share my recipes
- As a User, I can log in so that I can use the application's full functionality
- As a user, I can log out so that I can keep my account secure
- As a User, I can create a new recipe so that I can share it with others
- As a User, I can edit recipes so that I can change recipe details
- As a User, I can delete my recipes so that I can remove the recipe from the application
- As a User, I can view recipes so that I can view members' recipes
- As a User, I can view recipes so that I can see the recipe's full details
- As a User, I can comment on members' recipes so that I ask questions about the recipe
- As a User, I can like or unlike recipes so that I can support the other members

## Design

### ERD Database

![](./readme-assets/imgs/erd-database.jpeg)

### Wireframes

<details>
  <summary>Home Page</summary>
  
  ![](./readme-assets/imgs/home.jpg)
</details>

<details>
  <summary>Recipes Page</summary>
  
  ![](./readme-assets/imgs/recipes.jpg)
</details>

<details>
  <summary>Recipe Detail Page</summary>
  
  ![](./readme-assets/imgs/recipe-details.jpg)
</details>

<details>
  <summary>Sign Up Page</summary>
  
  ![](./readme-assets/imgs/register.jpg)
</details>

<details>
  <summary>Login Page</summary>
  
  ![](./readme-assets/imgs/login.jpg)
</details>

<details>
  <summary>Create Recipe Page</summary>
  
  ![](./readme-assets/imgs/create-recipe.jpg)
</details>

<details>
  <summary>Edit Recipe Page</summary>
  
  ![](./readme-assets/imgs/edit-recipe.jpg)
</details>

## Tests

### Bugs

#### Solved Bugs

| Bug                                                                                 | Error Message   | Solution                                                                            |
| ----------------------------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------- |
| When deploying the project to Heroku, I got an error when viewing the uploaded site | Disallowed Host | In settings.py I changed the value of ALLOWED_HOSTS to my right Heroku project URL. |

## Deployment

### Database

1. Register or log in to [ElephantSQL](https://www.elephantsql.com/)
2. At the home page click the "Create New Instance" button
3. Name your database (fitness_meals)
4. Select the free plan "Tiny Turtle"
5. Click the "Select Region" Button
6. Select your "data centre"
7. Click the "Review" Button
8. Click the "Create Instance" button
9. Click into the new instance, and copy the database URL (You need this URL for Heroku Variable later)

### Cloudinary

1. Register or log in to [Cloudinary](https://cloudinary.com/)
2. Open the dashboard tab
3. Copy API Environment Variable (When pasting the variable make sure to remove "CLOUDINARY_URL=" at the start of the varibale)

### Heroku

1. Register or log in to [Heroku](https://www.heroku.com/)
2. Click the "New" button and select "Create new app"
3. Name your app name
4. Select your region
5. Open the settings tab, and click the "Reval Config Vars"
6. Add DATABASE_URL to Config Vars and use your database url as the value
7. Add SECRET_KEY to Config Vars and use your secret key
8. Add CLOUDINARY_URL to Config Vars and use your Cloudinary API Environment Variable
9. Select the Deploy tab, choose GitHub as your deployment method
10. Search for the project repo and connect
11. Deploy from the main branch to publish

## IDE

1. Create an env.py file
2. Import the os module, add DATABASE_URL and paste the database key

```
import os

os.es.environ["DATABASE_URL"] = "DATABASE URL"
```

3. Add your Django secret key to the env.py file, and cut the SECRET_KEY from
   the settings.py file (If the SECRET_KEY doesn't exist create your own)

```
os.es.environ["SECRET_KEY"] = "SECRET KEY"
```

4. Add your CLOUDINARY variable, copy your Cloudinary API Variable key from the website

```
os.es.environ["CLOUDINARY_URL"] = "CLODINARY API KEY"
```

## Credits

### Code Used

- Project code is based on Code Institue Walkthrough project, "I Think Therefor I Blog".
  [Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment)

### Content

- Recipes content is from [MyProtein](https://www.myprotein.ie/blog/recipe/healthy-breakfast-burrito/)

### Media

- Images gathered from [Pexels](https://www.pexels.com/)

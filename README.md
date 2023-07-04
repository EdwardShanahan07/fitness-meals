# Fitness Meals

## Content

- [UX](#ux)
  - [Project Description](#project-description)
  - [Project Goals](#project-goals)
- [Deployment](#deployment)
  - [Database](#database)
  - [Cloudinary](#cloudinary)
  - [Heroku](#heroku)
  - [IDE](#ide)

## UX

### Project Description

Fitness Meals is an application that lets users share healthy recipes. Registered users can create and share recipes and engage with other members by liking and commenting on their recipes. Unregistered users will only be able to view recipes but need to register to use the full features of the application. Fitness Meals is built with the Django Python framework using the Agile methodology to plan the project.

### Project Goals

1. Create a user-friendly application with a visually pleasing design
2. Make sure the website is fully responsive to fit all screen sizes
3. View a list of member's shared recipes on a pagination pages
4. Implement user registration and login so authentic users can create and share their recipes and also like and comment on other member's recipes
5. Deploy the application making sure the site has excellent performance and accessibility

## Deployment

### Database

1. Register or log in to [ElephantSQL](https://www.elephantsql.com/)
2. At the home page click the "Create New Instance" button
3. Name your database (fitnessmeals)
4. Select free plan "Tiny Turtle"
5. Click "Select Region" Button
6. Select your "data center"
7. Click the "Review" Button
8. Click the "Create Instance" button
9. Click into the new instance, and copy the database url (You need this url for Heroku Variable later)

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
6. Add DATABASE_URL to Config Vars and use your datbase url as the value
7. Add SECRET_KEY to Config Vars and use your secret key
8. Add CLOUDINARY_URL to Config Vars and use your Cloudinary API Environment Variable
9. Select the Deploy tab, choose GitHub as your deployment method
10. Search for the project repo and connect
11. Deploy from the main branch to publish

## IDE

1. Create env.py file
2. Import the os module, add DATABASE_URL and paste the database key

```
import os

os.es.environ["DATABASE_URL"] = "DATABASE URL"
```

3. Add your Django secret key to env.py file, cut the SECRET_KEY from
   the settings.py file (If the SECRET_KEY doesn't exist create your own)

```
os.es.environ["SECRET_KEY"] = "SECRET KEY"
```

4. Add your CLOUDINARY variable, copy your Cloudinary API Variable key from the website

```
os.es.environ["CLOUDINARY_URL"] = "CLODINARY API KEY"
```

# Milestone Project 3 - Code Institute Full Stack Developer Course

## BAKE IT!

### Introduction

A website that is used for accessing and sharing baking recipes. Baking is quite popular at the moment with the great British Bake off and people seem to be passing time in lockdown by rediscovering baking. 

The site owners goal is to share and collect recipes and to advertise cooking equipment.

I have decided to advertise the brand ‘Pyrex’. They are a well-established brand and are known for their hard wearing well-designed products that can be found in most kitchens. https://www.pyrexuk.com/collections/bakeware

The main priorities for the site are accessing recipes, sharing recipes and advertising bakeware.

## UX
 
I wanted to produce a simple easy to use website where people can easily share and view baking recipes. As there are lots of different images on the recipe cards I decided to keep the background simple and went for a simple gingham style as to give the feel of a country kitchen table cloth. I selected a teal theme as it is one of my favorite colours and I think it fits with the style I am aiming for.

I chose to use the materialize framework to produce the site. I liked the fonts and the simple / clean feel.  This allowed me to focus my attention on the database schema and the back end code.

Looking at the Pyrex bakeware products I decided that I would link 1 product to each of the baking categories. i.e. 'Cupcake baking tray' to 'cupcakes and muffins' category. This also makes it easier for the Admin to add and alter products and categories in one form making the Admin user experience simple, straightforward and quick. After gathering my thoughts and initial ideas I started to develop a list of user stories.

### User Stories:
I have determined that there are 3 types of user:
1.	New Visitor:

    A non-member visiting the site for the first time. 

2.	A Member

    Likes to browse the site. Looks for the recently added recipes and Likes to share their recipes.

3.	Site Owner / Admin
	
    Can add recipes and update and delete any recipes added to the site. Updates recipe categories. Updates Advertisements. 

There will be user stories for each user type and there will also be user stories that are applicable to all users. Such as UX i.e. recipe contents and layout.  Imagery etc… In these instances, I shall refer to them as a ‘User’.

1.	As a new visitor I want to understand the purpose of the site
2.	As a new visitor I want to browse baking recipes.
3.	As a new visitor I want to learn how to become a member.
4.	As a new visitor I want the Member sign up process to be simple.
5.	As a member I want to share one of my recipes.
6.	As a member I want to see what new recipes have been added recently.
7.  As a member I want to be able to update and delete recipes that I have previously added.
8.	As an Admin I want to be able to create, update and delete the baking recipe categories.
9.	As an Admin I want to be able to update and delete recipes on the site. 
10.	As an Admin I want to be able to modify the links to the bake ware ads.
11. As a user I want to be able to view recipes based on the recipe category.
12.	As a user I want to be able to see the name of a recipe. E.g. Chocoholics Muffins
13.	As a user I want to see the description of a recipe. E.g. Delicious chocolate muffins with white and milk chocolate chips and chocolate topping.
14.	As a user I would like to see the preparation and cooking time for each recipe.
15.	As a user I want to see the level of skill required to complete each recipe.
16.	As a user I want to see the ingredients required for the recipe.
17.	As a user I want to see the instructions on how to complete the recipe.
18.	As a user I want to see an image on the recipe page.
19.	As a user I want to see links to good quality bake ware to allow me to improve my baking.
20.	As a user I want the site to be fun to look at.
21.	As a user I want the site to be easy to navigate.

After determining the user stories I put together some basic wireframes.   

Click here for [Wireframes](./docs/MS3Wireframes.pdf).

I then spent time working out how to structure the data needed. 

I decided I required 3 collections in my database. 
1. members - I wanted this to be simple as I have limited experience in security issues with passwords and email addresses etc.. So I decided to just use a username and password. The collection also takes a users member_type. This is always member. I manually changed one user to be an Admin.

2. recipe_category - This includes the category name. i.e. Cupcakes and the product information that will be advertised when this recipe category is included in a recipe. 

3. recipes - This includes all the information for the recipe, Name, description, pre and cook times

Click here for [Database Schema](./docs/MS3Wireframes.pdf).



## Features

### Homepage: index.html
-   Description on the homepage to allow new visitors to quickly understand the purpose of the site.
-   Link to a Sign up page that allows new visitors to be easily become members.
-   Button link to Log In page so members can log in
-   Button link to All recipes to allow all users to access all the recipes from one click from the Homepage. 
-   Display the latest recipes that have been added so that returning visitors can quickly see and any new exciting recipes.

### Sign Up Page:
-   Simple Sign up procedure. Using only a Username and password. i.e. limiting personal data and encourage people to sign up.
-   Link to log in page if you realise you are an existing user.
*********************************************
In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
*************************************************
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
************************************
- Add a filter to allow recipes to be filtered by skill level.
- Add a link to 'Bake its favorite Pyrex products' and a page that lists them all using the ad data populated in the categories database. 
- Add feature to Admin Tools: allow Admins to change other users member_type to Admin. 

## Technologies Used

HTML, CSS, JS, PYTHON - FLASK, MONGO DB, MATERIALIZE 1.0

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

Click here for [Database Schema](./docs/manual_testing.pdf).

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content

To work out how to do a simple log in I came across this tutorial on youtube.com  https://www.youtube.com/watch?v=vVx1737auSE I used this to base my sign up and log in functionality. https://github.com/PrettyPrinted/mongodb-user-login

For the 'Add recipe' page it was necessary to dynamically add form fields. I wasn't sure how to achieve this and a google search led me to this page:  http://www.randomsnippets.com/2008/02/21/how-to-dynamically-add-form-elements-via-javascript/ This code achieved what I wanted and is included in my main.js file.

### Media

https://www.pyrexuk.com/collections/bakeware


### Acknowledgements

- I received inspiration for this project from X

### Acknowledgements

During development I used online resources to help with issues I came across:

https://www.w3schools.com/
https://stackoverflow.com/

My Mentor briefly talked me thought unit testing and i found this: https://code-maven.com/slides/python-programming/flask-testing  and this https://blogthetech.com/testing-flask-applications-using-unittest-in-python/#Routing_Tests and from this I managed to put together some basic python route tests.

I would also like to thank my Mentor: Ignatius Ukwuoma for the support.









## Attributes
#Youtube reference: https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc

The import things to understand here are:

1. For every particular section of your app you must create a different app which is called the django way. Each app will have its own url, views and templates folders.
2. Displaying data as an html is called render
3. Models:
   -Models in python are class which represent table in database.
   -Each model maps to a single table in a database.

   IMG: model2.png
![](refImages/model2.jpg)

4. Every time we make a model or make any change to our model then the two important steps are
      - python manage.py makemigrations
      - python manage.py migrate
   and then we are good to go.

5. To create super user command is
      - python manage.py createsuperuser
   then you are good to login.

6. To show our other applications in the admin area we need to edit the admin area of that particular application.

7. To show the data that we stored in out database in this case in articles:
   # here 'articles' is  a dictonary of articles
   # to pass anything in a html we need to send it thorough a dictonarty variable
   # the name is not necessarily articles it can be anything. (ref views.py in articles)

8. In the html:
   {% code %} to write python code but not output any data
   {{ code }} to output any data

9.  Previously what we did that for every html page we were coding the same
   header and footer repeatedly so if in any point of time there is a need to change
   content or style of the header then it will be hell of a job to do. So instead
   of that we will create a base_layout.html in the template folder of the main project
   directory and rest of other views will inherit for it.

   lets do it!!

10. This was the original content of base_layout
<!-- {% extends 'base_layout.html' %}
{% block content %}
   <h1>Welcome to the home page.</h1>
   <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
{% endblock %} -->

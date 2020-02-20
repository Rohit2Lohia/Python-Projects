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

7. 

# Bookmarking website
> Share any image you find on the internet with your friend

## Requirements
* Python 3
* Redis 4

## Installation

Navigate to a new folder using your command prompt and type :

`git clone https://github.com/AbdellaouiSofiane/Bookmark.git`

Navigate to the project directory (make sure to activate your virtual enviroment) and type :

`python -m pip install -r requirements.txt`

Launch the developpement server :

`python manage.py runserver`

Visite http://127.0.0.1:8000/ in your browser.

Note : This project make use of Redis, make sure you have a redis server up and running. Check settings for config issues.

## Screenshots

![image](https://user-images.githubusercontent.com/62038668/116131614-e4607d00-a6cc-11eb-804d-6529091836d7.png)

![image](https://user-images.githubusercontent.com/62038668/116131735-0e19a400-a6cd-11eb-9eed-4e6fc8cd9ba8.png)

![image](https://user-images.githubusercontent.com/62038668/116131883-33a6ad80-a6cd-11eb-83a0-09781ec2e858.png)

![image](https://user-images.githubusercontent.com/62038668/116132051-618bf200-a6cd-11eb-8d90-7a4689731cf3.png)


## Features

* Bookmark an image from any website.
* Like/Unlike any image.
* Follow/Unfollow people.
* See the activity stream of people you follow.
* Create/Edit you profile.


## Tech Stack / Built With

1. [Django](https://docs.djangoproject.com/en/3.1/) - The Python framework
2. [Material Design for Bootstrap 5 ](https://mdbootstrap.com/) - A CSS theme
3. [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) - A django 3rd party package
4. [easy_thumbnails](https://easy-thumbnails.readthedocs.io/en/latest/) - A django 3rd party package



## Authors

Sofiane Abdellaoui - abdellaoui.sofiane.esb@gmail.com

## Credits

This project was inspired by chapter 4 to 6 from the book :

Django 3 By Example - Build powerful and reliable Python web applications from scratch (author Antonio Melé)




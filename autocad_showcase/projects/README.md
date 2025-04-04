initialized the project
added rest framework, rest_framework.authtoken, the project to settings.py installed apps
created the models to create the databsse of the project
in models.py:
1. created a model named project
2. has fields for the title, owner, description of the project, 2 fields for the images
3. imported the built in User in django 
created a serializer for the project and User models 
in serializers.py:
1. made 2 classes one for the user and one for the project
make the migrations to create the database
created the view endpoints for project serializers
in views.py:
1. imported generics, permissions from rest_framework
2. make 2 classes to perform the CRUD operations

added 3 classes login logout register to handle the authentication for the client
added 1 class for registration in serializer 
added the path for the projects in projects/urls
added the paths of the projects to autocad_showcase/urls.py
add security steps in settings.py
in settings.py:
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000 (1 year)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
last steps configured the settings.py to be ready for deployment

from django.contrib import admin
from django.urls import path
#from articles import models
import articles
from articles import views

"""urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name = 'archive'),
    path('article/<int:article_id>', views.get_article, name='get_article'),  
]

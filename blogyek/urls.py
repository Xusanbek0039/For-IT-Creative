
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('pages.urls')),
    path('post/', include('posts.urls')),
    path('accounts/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('darslik/', include('blog.urls')),
    path('quiz/', include('exam.onlinexam.urls')),
    path('studentclick', include('exam.student.urls')),
    path('teacherclick', include('exam.teacher.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
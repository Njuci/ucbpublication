from django.urls import path


from .views import getfichier,get_fichierUploader,uploandingCsvfile,MyView

urlpatterns = [
    path('get/', getfichier),
    path('getFic/<str:id>',get_fichierUploader),
    path('uploadfile',uploandingCsvfile.as_view()),
    path('up',MyView.as_view())
]

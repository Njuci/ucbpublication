from django.urls import path


from .views import getfichier,get_fichierUploader,uploandingCsvfile,MyView,Email_envoie

urlpatterns = [
    path('get/', getfichier),
    path('getFic/<str:id>',get_fichierUploader),
    path('uploadfile',uploandingCsvfile.as_view()),
    path('email/<str:email>',Email_envoie,name='email_envoie'),
    path('up',MyView.as_view())
]

from django.urls import path


from .views import getfichier,get_fichierUploader,uploandingCsvfile,MyView,Email_envoie,Email_envoie3

urlpatterns = [
    path('get/', getfichier),
    path('getFic/<str:id>',get_fichierUploader),
    path('uploadfile',uploandingCsvfile.as_view()),
    path('email',Email_envoie.as_view(),name='email_envoie'),
    path('emailk',Email_envoie3.as_view(),name='email_envoie3'),
    path('up',MyView.as_view())
]

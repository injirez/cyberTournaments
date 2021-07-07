from django.urls import path
from . import views

urlpatterns = [
    path('', views.DotaListView.as_view()),
    path('siteName/<str:siteName>/', views.DotaListViewSiteName.as_view()),
    path('status/<str:status>/', views.DotaListViewStatus.as_view()),
    path('updatePart/', views.AddParticipant.as_view())
]

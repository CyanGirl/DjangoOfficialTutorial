from django.urls import path

# importing the view to bind it
from . import views

app_name = "polls"
urlpatterns = [
    # binding the home " with index view and naming it
    # look for generic we are giving it a formatted name
    path("", views.IndexView.as_view(), name="index"),
    # sending the question id with the request URL
    # angle brackets matches a pattern
    path("<int:pk>/", views.DetailsView.as_view(), name="details"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/votes/", views.votes, name="votes"),
]

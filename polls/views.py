from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

from django.utils import timezone

from .models import Question, Choices

# Create your views here.
# this takes a request from the client and response back something


class IndexView(generic.ListView):
    # specifiying the path of template html
    template_name = "polls/index.html"
    # setting the context name
    context_object_name = "latest_list"

    def get_queryset(self):
        # this is where the list is generated

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailsView(generic.DetailView):
    # use this model
    model = Question
    template_name = "polls/details.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def votes(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        # getting the choice selected from the client side POST method request object
        selected_choice = question.choices_set.get(pk=request.POST['choices'])

    except (KeyError):
        return render(request, "polls/details.html", {"question": question, "error_message": "You didn't select a valid choice!"})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # redirect prevents the form being submitted over and over
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

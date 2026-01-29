from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,UpdateView,View,GenericViewError
from .models import Question,Choice
from .forms import ChoiceForm
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class ListQuestionView(ListView):
    template_name = 'polls/questions_list.html'
    context_object_name = 'top_5_latest_question_list'
    queryset = Question.objects.order_by('-pub_date')[:6]


class DetailQuestionView(DetailView):
    model = Question
    template_name = 'polls/question_detail.html'

class ResultQuestionView(DetailView):
    model = Question
    template_name = 'polls/question_results.html'

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = super().get_context_data(**kwargs)
        context["choices"] = self.object.choice_set.order_by('-votes')
        return context

class VoteQuestionView(View):

    def post(self, request, *args, **kwargs):
        question_object = get_object_or_404(Question,pk=self.kwargs.get('pk'))
        choice = request.POST.get('choice')
        choice_object=get_object_or_404(Choice,pk=choice,question=question_object.pk)
        choice_object.votes += 1
        choice_object.save()
        return redirect("polls:results",pk=question_object.pk)
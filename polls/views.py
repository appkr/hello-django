from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Alternative, Question


def index(request):
    questions = Question.objects.all().order_by('-created_at')[:5]
    return render(request, 'polls/index.html', {'questions': questions})


def show(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/show.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_alternative = question.alternative_set.get(pk=request.POST['alternative'])
    except (KeyError, Alternative.DoesNotExist):
        return render(request, 'polls/show.html', {
            'question': question,
            'error_message': 'Select one!'
        })
    else:
        selected_alternative.vote_count += 1
        selected_alternative.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

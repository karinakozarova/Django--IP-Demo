from django.shortcuts import render
from .models import Score
from .forms import ScoreForm


def list_scores(request):
    score = Score.objects.all()
    return render(request, 'list_scores.html', {'scores': score})


def new_score(request):
    form = ScoreForm(request.POST or None)
    print("OPaa")
    if request.POST:
        print("POST")
        if form.is_valid():
            # if we're creating data
            print("HERE")
            form.save()

    return render(request, 'new_score.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Question, UserAnswer, Score
from django.views.generic import DeleteView

#@login_required
def home_view(request):
    return render(request, 'quiz/home.html')

#@login_required
def quiz_view(request):
    if request.method == "POST":
        user = request.user
        user_answers = {}

        for key, value in request.POST.items():
            if key.startswith("question"):
                question_id = int(key[len("question"):])
                selected_option = int(value)
                user_answers[question_id] = selected_option

        questions = Question.objects.all()
        score = 0

        for question in questions:
            selected_option = user_answers.get(question.id, None)
            if selected_option != None:
                user_answer = UserAnswer(user=user, question=question, selected_option=selected_option)
                user_answer.save()
                if user_answer.is_correct():
                    try:
                        score = Score.objects.get(user=user)
                    except Score.DoesNotExist:
                # If the user does not have a score record, create one
                        score = Score(user=user, score=0)
                    score.score += 1
                    score.save()

        messages.success(request, f'あなたのスコアは: {score}/{len(questions)}')
        return redirect('quiz:result')

    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'quiz/quiz.html', context)

#@login_required
def result_view(request):
    user = request.user
    user_answers = UserAnswer.objects.filter(user=user).order_by('-id')[:5]
    try:
        score = Score.objects.filter(user=user).first()
    except:
        score = 0
    context = {
        'user_answers': user_answers,
        'score': score,
        'question_length': Question.objects.all().count(),
    }
    return render(request, 'quiz/result.html', context)



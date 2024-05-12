from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def profile(request, id):
    response = f"You're looking at the results of question {id}."
    context = {'response': response}
    return render(request, 'profile.html', context)


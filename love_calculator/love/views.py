from django.shortcuts import render
from django.http import JsonResponse
from .forms import LoveForm
def calculate_love(request):
    if request.method == 'POST':
        form = LoveForm(request.POST)
        if form.is_valid():
            percentage = form.cleaned_data['percentage']

            # envoyer le percentage comme un objet js pour le traitement AJAX 

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'percentage': percentage})
            return render(request, 'love/love.html', {'form': form, 'percentage': percentage})
        # si le formulaire envoyé n'est pas valide 
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Formulaire invalide'}, status=400)
    
    #Si la requete n'est pas post
    else:
        form = LoveForm()
        return render(request, 'love/love.html', {'form': form})

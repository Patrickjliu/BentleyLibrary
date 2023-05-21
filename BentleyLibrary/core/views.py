from django.shortcuts import render
from .models import BookInventory
from django.db.models import Q

def search_results(request):
    query = request.GET.get('q')  # Update parameter name to 'q'
    if query:
        results = BookInventory.objects.filter(
            Q(title__icontains=query) |
            Q(publisher__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        results = []
    print("Query:", query)
    print("Results:", results)
    return render(request, 'search_results.html', {'results': results, 'query': query})


def index(request):
    # Your view logic goes here
    return render(request, 'core/index.html')
from django.shortcuts import render
from .models import Bookinventory
from django.db.models import Q

from .models import Bookinventory

def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Bookinventory.objects.filter(
            Q(title__icontains=query) |
            Q(publisher__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        results = Bookinventory.objects.all()

    context = {
        'results': results,
        'query': query
    }
    return render(request, 'search_results.html', context)



# def search_results(request):
    
#     books = Bookinventory.objects.all()
#     context = {
#         'books' : books
#     }
#     return render(request, 'search_results.html', context)
#     # query = request.GET.get('q')  # Update parameter name to 'q'
#     # if query:
#     #     results = BookInventory.objects.filter(
#     #         Q(title__icontains=query) |
#     #         Q(publisher__icontains=query) |
#     #         Q(author__icontains=query) |
#     #         Q(description__icontains=query)
#     #     )
#     # else:
#     #     results = []
#     # print("Query:", query)
#     # print("Results:", results)
#     # return render(request, 'search_results.html', {'results': results, 'query': query})


def index(request):
    # Your view logic goes here
    return render(request, 'core/index.html')
from django.shortcuts import render
from .models import Bookinventory, Log
from django.db.models import Q

def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Bookinventory.objects.filter(
            Q(title__icontains=query) |
            Q(publisher__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        )
        book_ids = results.values_list('id', flat=True)
        borrowed_books = Log.objects.filter(book_id__in=book_ids, returned_date__isnull=True)
        borrower_emails = borrowed_books.values_list('borrower_email', flat=True)
    else:
        results = Bookinventory.objects.all()
        borrowed_books = []
        borrower_emails = []

    context = {
        'results': results,
        'query': query,
        'borrowed_books': borrowed_books,
        'borrower_emails': borrower_emails
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
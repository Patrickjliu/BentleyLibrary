from django.shortcuts import render, get_object_or_404
from .models import Bookinventory, Log
from django.db.models import Q

def resource_view(request):
    classes = [
        {
            'name': 'MWH',
            'resources': [
                {
                    'title': 'Citing: Chicago Style',
                    'url': 'https://www.loc.gov/programs/teachers/getting-started-with-primary-sources/citing/chicago/',
                },
                # Add more resources for Class 1
            ],
        },
        {
            'name': 'History Seminar: Colonialism',
            'resources': [
                {
                    'title': 'Citing: Chicago Style',
                    'url': 'https://www.loc.gov/programs/teachers/getting-started-with-primary-sources/citing/chicago/',
                },
                # Add more resources for Class 2
            ],
        },
        # Add more classes as needed
    ]

    return render(request, 'resource.html', {'classes': classes})


def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Bookinventory.objects.filter(
            Q(title__icontains=query) |
            Q(publisher__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query) |
            Q(isbn__icontains=query)
        )
        book_ids = results.values_list('id', flat=True)
        borrowed_books = Log.objects.filter(book_id__in=book_ids, returned_date__isnull=True)
        borrower_emails = borrowed_books.values_list('borrower_email', flat=True)
        borrowed_book_ids = borrowed_books.values_list('book_id', flat=True)  # Get the borrowed book IDs
    else:
        results = Bookinventory.objects.all()
        borrowed_books = []
        borrower_emails = []
        borrowed_book_ids = []

    context = {
        'results': results,
        'query': query,
        'borrowed_books': borrowed_books,
        'borrower_emails': borrower_emails,
        'borrowed_book_ids': borrowed_book_ids  # Include the borrowed book IDs in the context
    }

    return render(request, 'search_results.html', context)

def book_page(request, book_id):
    book = get_object_or_404(Bookinventory, id=book_id)
    borrowed_books = Log.objects.filter(book_id=book_id, returned_date__isnull=True)
    borrower_emails = borrowed_books.values_list('borrower_email', flat=True)
    borrowed_book_ids = borrowed_books.values_list('book_id', flat=True)  # Get the borrowed book IDs

    context = {
        'book': book,
        'borrowed_books': borrowed_books,
        'borrower_emails': borrower_emails,
        'borrowed_book_ids': borrowed_book_ids
    }
    return render(request, 'book_page.html', context)


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
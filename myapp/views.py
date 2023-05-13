from django.shortcuts import render
from .models import BookInventory

def book_inventory(request):
    books = BookInventory.objects.all()
    return render(request, 'book_inventory.html', {'books': books})


def my_view(request):
    # Call your main() function here
    result = main()

    # Pass the result to your template
    context = {'result': result}
    return render(request, 'my_template.html', context)
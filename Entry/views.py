from django.shortcuts import render_to_response, get_object_or_404

from entry.models import Entry, Category


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'entries': Entry.objects.all()[:10]
    })

def view_entry(request, slug):
    return render_to_response('view_entry.html', {
        'entry': get_object_or_404(Entry, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'entries': Entry.objects.filter(category=category)[:5]
    })
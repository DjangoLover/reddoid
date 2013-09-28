from django.http import HttpResponse


def load_source(request):
    """
    Loads some source.
    """
    html = "test"
    return HttpResponse(html)

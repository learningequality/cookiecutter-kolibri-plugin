from __future__ import absolute_import, print_function, unicode_literals
from django.http import HttpResponse

def PluginTemplateView(request):
    return HttpResponse(status=204)

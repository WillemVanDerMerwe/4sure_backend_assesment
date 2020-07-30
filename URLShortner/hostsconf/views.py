from django.http import HttpResponseRedirect
from django.conf import settings

DEFAULT_REDIRECT_URL = getattr(settings,"DEFAULT_REDIRECT_URL","https://www.hello4sure.com")

def wildcard_redirect(request,path=None):
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL +"/"+ path
    return HttpResponseRedirect(new_url)
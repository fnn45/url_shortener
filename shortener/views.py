from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from analytics.models import ClickEvent
from shortener.forms import CheckoutForm, AdjustmentForm
from shortener.models import UrlDetails
from .utils import is_exist_url, get_description_text_from_html, initialize_url


def create_short_url(request):
    form = CheckoutForm()
    if request.method == "POST":
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session = request.session
        form    = CheckoutForm(request.POST)
        if form.is_valid():
            url                     = form.cleaned_data.get('url')
            parsed_html             = is_exist_url(url)
            if not parsed_html:
                return HttpResponse(status=204)
            protocol                = 'https' if request.is_secure() else 'http'
            domain                  = request.META['HTTP_HOST']
            shortcode               = initialize_url(UrlDetails, protocol, domain)
            description_text        = get_description_text_from_html(parsed_html)
            obj, created            = UrlDetails.objects.get_or_create(
                                            url=url,
                                            defaults = {
                                                'description_text': description_text
                                                ,'shortcode': shortcode
                                                }
                                            )
            session['url']          = url
            session['short_url']    = obj.get_short_url()
            session['description']  = obj.description_text
            session['timestamp']    = str(obj.timestamp)
            session['is_url_exist'] = created
            try:
                 session['count']   = obj.clickevent.count
            except:
                 session['count'] = 0
            return HttpResponseRedirect('/')
    return render(request, 'shortener/home.html', locals())

def update_short_url(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    session = request.session
    if request.method == 'POST':
        adj_form = AdjustmentForm(request.POST)
        if adj_form.is_valid():
            protocol    = 'https' if request.is_secure() else 'http'
            domain      = request.META['HTTP_HOST']
            shortcode   = session['short_url'] = initialize_url(UrlDetails, protocol, domain, adj_form.cleaned_data['shortcode'])
            description = session['description'] = adj_form.cleaned_data['description_text']
            session['timestamp']  = str(adj_form.cleaned_data['timestamp'])
            obj, created = UrlDetails.objects.update_or_create(
                url = session['url'], defaults = {
                    'shortcode'         : shortcode
                    ,'description_text' : description
                    ,'timestamp'        : adj_form.cleaned_data['timestamp']
                })
            ClickEvent.objects.create_event(obj, adj_form.cleaned_data['count'])
            session['count'] = adj_form.cleaned_data['count']
            return HttpResponse(status=200)
        return HttpResponse(list(adj_form.errors.get('__all__')), status=203)
    if request.method == 'DELETE':
        session.modified = True
        if session['url']:
            UrlDetails.objects.filter(url=session['url']).delete()
            try:
                for k in ['url', 'short_url', 'description', 'timestamp', 'count', 'is_url_exist']:
                    del request.session[k]
            except: pass
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)

def redirect_to_source_url(request):
    obj = get_object_or_404(UrlDetails, shortcode=request.build_absolute_uri())
    count = ClickEvent.objects.create_event(obj)
    request.session['count'] = count
    return HttpResponseRedirect(obj.url)



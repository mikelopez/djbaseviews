from django.shortcuts import render
from django import http
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils import simplejson as json

# Create your views here.

from django.views.generic import DetailView, ListView, UpdateView,\
                                 TemplateView, CreateView, View

class BaseView(View):
    """
    Base view for View classes
    """
    def get_object(self, obj, key, val):
        """
        Get an object by key/value
        """
        f = {key: value}
        try:
            return obj.objects.get(**f)
        except obj.DoesNotExist:
            return None

    def submit_form(self, form, **kwargs):
        """
        Submit the form and set any additional data
        to the object.
        """
        if form.is_valid():
            # check for save arg
            if kwargs.get('save_arg'):
                 obj = form.save(kwargs.get('save_arg'))
            else:
                obj = form.save()
            if kwargs.get('data'):
                for k, v in kwargs.get('data').items():
                    setattr(obj, k, v)
                obj.save()
            return form, obj
        else:
            return form, False


class PostViewBase(BaseView):
    """
    Handles POST requests only.
    """
    def get(self, request):
        return Http404

    def post(self, request):
        pass


def create_form(data, form_class, instance):
    """
    When POSTING a form, it checks for instance,
    and if its found, it creates the form class instance
    with that object and edits it."""
    if instance:
        form = form_class(instance=instance)
        if data:
            form = form_class(data, instance=instance)
    else:
        form = form_class()
        if data:
            form = form_class(data)
    return form


class UpdateInstanceView(UpdateView):
    """
    Update an instance view base
    """
    def form_valid(self, form):
        self.object = form.save(commit=False)
        clean = form.cleaned_data
        for k, v in clean.items():
            setattr(self.object, k, v)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
# Create your views here.

from django.views.generic import DetailView, ListView, TemplateView, CreateView, View

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


class PostViewBase(BaseView)
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

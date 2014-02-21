Readme for djbaseviews
------------------------------

``from APP-NAME import *``

Sample usage
=============


The following sample illustrates how to create a basic view class and instantiate a
form that will create a new object if instance is None. If instance is provided, it will edit the current object with the fields from the form.


.. code-block:: python

	from forms import FormClass

	class SomeView(ViewBase):
		def post(self, request):
			instance = self.get_object(ModelClass, pk, 123)
			form = create_form(request.POST, FormClass, instance)
			# optionally pass additional data to set to the object after saving
			additional_data = {'somekey': 'somevalue'}
			# returns the form, and the object created/edited
			form, obj = self.submit_form(form, data=additional_settings)
			if obj:
				return HttpResponseRedirect(reverse('some_successful_url'))




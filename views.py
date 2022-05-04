from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.http import Http404
from .models import ComingSoonNotice
from .forms import ComingSoonForm

# Create your views here.
class ComingSoonSignUp(CreateView):
	form_class = ComingSoonForm
	template_name = "comingsoon/index.html"
	# success_url = reverse_lazy("comingsoon:signup-success")

	def form_valid(self, form):
		if form.is_valid():
			obj = form.save()
		# obj = super(ComingSoonSignUp, self).form_valid(form)
		return render(self.request, self.template_name, context={"sent_mail": True})

class ComingSoonSuccess(DetailView):
	model = ComingSoonNotice
	template_name = "comingsoon/index.html"
	extra_context = {"success_page":True}
	slug_field= 'verification_link'

	def get_object(self, queryset=None):
		try:
			obj = super(ComingSoonSuccess, self).get_object(queryset)
			if obj and not obj.verified:
				print("obj is", obj)
				obj.verified = True
				obj = obj.save()
				obj.send_verification_complete_mail()
			return obj
		except:
			raise Http404()
	# def get_extra_context(self, request, *args, **kwargs):
	# 	slug = kwargs.pop("slug", None)
	# 	if slug:

def test_email():
	c = ComingSoonNotice.objects.get(id=1)
	c.send_verification_email()

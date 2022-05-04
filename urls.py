from django.urls import path
from django.views.generic.base import TemplateView
from .views import ComingSoonSignUp, ComingSoonSuccess

app_name = "comingsoon"
urlpatterns = [
    path('', TemplateView.as_view(template_name = "comingsoon/index.html")),
    path('comingsoon-signup/', ComingSoonSignUp.as_view(template_name = "comingsoon/index.html"), name="signup"),
    path('comingsoon-signup/verify/<slug:slug>/', ComingSoonSuccess
.as_view(), name="verify-signup",)
]
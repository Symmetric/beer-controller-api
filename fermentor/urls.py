from django.conf.urls import patterns, url
from fermentor.views import TargetTemperatureViewSet, MeasuredTemperatureViewSet

urlpatterns = patterns(
    '',
    url(r'^temperature/targets$', TargetTemperatureViewSet.as_view()),
    url(r'^temperature/measurements$', MeasuredTemperatureViewSet.as_view()),
)

from django.conf.urls import url
from . import views

# important inorder to use namespaces in urls
app_name = 'polls'

urlpatterns = [
	#localhost:8000/polls/
	url(r'^$', views.index, name="index"),
	url(r'^str/$', views.getString, name="getString"),
	url(r'^json/$', views.getJson, name="getString"),
	# #localhost:8000/polls/1
	# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# #localhost:8000/polls/1/results
	# url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
	# #localhost:8000/polls/1/vote
	# url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
]
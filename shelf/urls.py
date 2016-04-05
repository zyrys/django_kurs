from django.conf.urls import patterns, include, url

from shelf.views import AuthorLiestView, AuthorDetailView

urlpatterns = patterns('',
                       url(r'^authors/$', AuthorLiestView.as_view(), name='author-list'),
                       url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
)

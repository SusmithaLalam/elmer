from django.conf.urls import url

from .views import (ActiveThreadsList, BoardListCreateAPIView, BoardRetrieveUpdateDestroyAPIView,
                    CommentCreateAPIView, CommentListAPIView,
                    GetSubscribedBoards, StarSubjectView,
                    SubjectListCreateAPIView, SubjectRetrieveUpdateDestroyAPIView, SubscribeBoardView,
                    TrendingBoardsList)

urlpatterns = [
    url(r'^subjects/$', SubjectListCreateAPIView.as_view(), name='list_or_create_subjects'),
    url(r'^subjects/active_threads/$', ActiveThreadsList.as_view(), name='active_threads'),
    url(r'^subjects/star/$', StarSubjectView.as_view(), name='star_subject'),
    url(r'^subjects/(?P<slug>[-\w]+)/$', SubjectRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_or_update_or_destroy_subjects'),

    url(r'^boards/$', BoardListCreateAPIView.as_view(), name='list_or_create_boards'),
    url(r'^boards/subscribe/$', SubscribeBoardView.as_view(), name='subscribe_boards'),
    url(r'^boards/trending/$', TrendingBoardsList.as_view(), name='boards_trending'),
    url(r'^boards/user_subscribed/$', GetSubscribedBoards.as_view(), name='boards_users'),
    url(r'^boards/(?P<slug>[-\w]+)/$', BoardRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_or_update_or_destroy_boards'),

    url(r'^comments/create/$', CommentCreateAPIView.as_view(), name='comments_create'),
    url(r'^comments/(?P<slug>[-\w]+)/$', CommentListAPIView.as_view(), name='comments_list'),
]

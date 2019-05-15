"""Defines URL patterns for learning_logs."""

from django.urls import path

from learning_logs import views

urlpatterns = [
    # home page
    path("", views.index, name="index"),

    # show all topics
    path("topics/", views.topics, name="topics"),

    # detail page for a single topic
    path("topics/<int:topic_id>/", views.topic, name="topic"),

    # page for adding a new topic
    path("new_topic/", views.new_topic, name="new_topic"),

    # page for editing an entry
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]

from django.shortcuts import render
from django.db import transaction
from .utils import reduce_user_balance, publish_post


# @transaction.atomic
# def publish_blog_post(post_id, user_id, scope_value):
#     reduce_user_balance(user_id, scope_value)
#     publish_post()


def publish_blog_post(post_id, user_id, scope_value):
    with transaction.atomic():
        reduce_user_balance(user_id, scope_value)
        publish_post()

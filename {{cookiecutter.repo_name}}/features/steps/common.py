import time

from behave import *
from django.core.urlresolvers import reverse
from django.test import Client,TestCase
from mytest.users.models import User

#use_step_matcher("re")


@given('I am on the "{page}" page')
@when('I visit the "{page}" page')
@then('I should be on the "{page}" page')
def step_impl(context, page):
    """
    :param page: url name to be reversed
    :type context: behave.runner.Context
    """
    resp = context.test.client.get(reverse(page))
    assert resp.status_code == 200

    context.browser.get(context.base_url + reverse(page))




@then('I should see "{text}"')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """

    assert(text in context.browser.page_source)


@when('I fill in "{field}" with "{data}"')
def step_impl(context, field, data):
    """
    :type context: behave.runner.Context
    :type field: the field to be selected by the name attr
    :type data: the data to be entered into the field
    """

    # if data set to NA then field should be empty
    if data == "N/A":
        return

    input_field = context.browser.find_element_by_name(field)
    input_field.send_keys(data)



@step('I click "{link_name}"')
def step_impl(context, link_name):
    """
    :type context: behave.runner.Context
    """
    link = context.browser.find_element_by_name(link_name)
    link.click()



@given('A user exists with username "{username}" email "{email}"')
def step_impl(context, username, email):
    """
    :type context: behave.runner.Context
    :type username
    :type email: email address of user
    """
    User.objects._create_user(username,email,"testpass")
    assert User.objects.count() == 1


@step("I should be sent an email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    from django.core import mail

    assert(len(mail.outbox) == 1)


@step('I check the "{name}" box')
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    """
    box = context.browser.find_element_by_name(name)
    box.click()

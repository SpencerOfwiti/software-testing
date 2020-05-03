import pytest
from ..people import format_data_for_display, format_data_for_excel


@pytest.fixture
def example_people_data():
	return [
		{
			'given_name': 'Spencer',
			'family_name': 'Ofwiti',
			'title': 'Software Engineer'
		},
		{
			'given_name': 'Herman',
			'family_name': 'Muyanga',
			'title': 'Project Manager'
		}
	]


def test_format_data_for_display(example_people_data):
	assert format_data_for_display(example_people_data) == [
		'Spencer Ofwiti: Software Engineer',
		'Herman Muyanga: Project Manager'
	]


def test_format_data_for_excel(example_people_data):
	assert format_data_for_excel(example_people_data) == """given,family,title
Spencer,Ofwiti,Software Engineer
Herman,Muyanga,Project Manager
"""

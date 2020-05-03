def format_data_for_display(people):
	display = []
	for person in people:
		name = person['given_name']
		surname = person['family_name']
		title = person['title']
		report = f'{name} {surname}: {title}'
		display.append(report)
	return display


def format_data_for_excel(people):
	docstring = ''
	display = ['given,family,title\n']
	for person in people:
		name = person['given_name']
		surname = person['family_name']
		title = person['title']
		report = f'{name},{surname},{title}\n'
		display.append(report)
	for item in display:
		docstring += item
	return docstring

def is_palindrome(text):
	text = text.lower().strip('?')
	text = text.replace(' ', '')
	reverse = ''.join(reversed(text))
	if reverse == text:
		return True
	return False

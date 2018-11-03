# Codes for message display and logging

CODES_REQUEST_SUCCESS = {
	'CONNECT_SUCCESSFUL': "A connection was successfully made."
}

CODES_REQUEST_ERROR = {
	'INPUT_TOO_LONG': "Input too long. Please provide an input of %s or less characters.",
	'EMPTY_INPUT': "Please provide some input to proceed.",
	'INCORRECT_INPUT': "Please provide some valid input.",
	'INCORRECT_CSRF_TOKEN': "Please clear cookies and cache, then try again.",
	'INVALID_CHAR': "Please use valid characters for the input.",
	'INVALID_INPUT': "Please provide some valid input for %s.",
	'INVALID_CAPTCHA': "Please properly fill the reCaptcha.",
	'NO_CONNECTION': "Internet not connected.",
	'INVALID_ENDPOINT': "Please provide a valid endpoint",
	'NOT_FOUND':"Not found. Perhaps, it went missing."
}

CODES_PLATFORM_SUCCESS = {
	'DB_DATA_FOUND': "Successfully found data in our database.",
	'DB_DATA_DELETED':"Successfully deleted data in our database."
}

CODES_PLATFORM_ERROR = {
	'DB_UNKNOWN': "There was some error with our database.",
	'DB_CANNOT_CONNECT': "Couldn't connect to the database.",
	'FILE_SIZE_BIG': "File is too large.",
	'FILE_ERROR': "There was an error with the file.",
	'DB_DATA_NOT_FOUND': "Couldn't find the data in our database."
}

# Success and Error Codes
REQUEST = {
	'SUCCESS': CODES_REQUEST_SUCCESS,
	'ERROR': CODES_REQUEST_ERROR
}

PLATFORM = {
	'SUCCESS': CODES_PLATFORM_SUCCESS,
	'ERROR': CODES_PLATFORM_ERROR
}

UNKNOWN = "Oops! Something went wrong."
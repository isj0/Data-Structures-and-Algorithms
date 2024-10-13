def status_code_meaning(number):
    if number == 200:
        return "OK"
    elif number == 301:
        return "Moved Permanently"
    elif number == 401:
        return "Unauthorized"
    elif number == 404:
        return "Not Found"
    elif number == 500:
        return "Internal Server Error"

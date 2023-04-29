
class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        print( f'The user: {request.user.username} has made a request to: {request.path}, description {request.POST.get("description")}')

        return response


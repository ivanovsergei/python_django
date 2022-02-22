import time


class PauseNReqMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.N = 0

    def __call__(self, request):
        self.N += 1
        if self.N % 2 == 0:
            time.sleep(2)

        response = self.get_response(request)
        return response

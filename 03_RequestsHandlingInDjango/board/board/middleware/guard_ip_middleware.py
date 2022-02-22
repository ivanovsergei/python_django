from django.core.exceptions import PermissionDenied
from time import time


class GuardIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count_req = 0
        self.count_sec = 0
        self.first_time = 0
        self.last_time = 0

    def __call__(self, request):
        dict_ips = dict()

        ip = request.META.get('REMOTE_ADDR')
        self.count_req += 1
        if self.count_req == 1:
            self.first_time = time()
        self.last_time = time()
        dict_ips[ip] = [self.count_req, self.first_time, self.last_time]
        self.count_sec = int(self.last_time - self.first_time)
        # print(self.count_req, self.count_sec)
        if self.count_req > 3 and self.count_sec < 9:
            raise PermissionDenied
        if self.count_sec > 15:
            self.count_req = 0
            self.count_sec = 0
            self.first_time = time()

        response = self.get_response(request)
        return response

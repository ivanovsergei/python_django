import os.path
import time


class InfoRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        remote_ip = request.META.get('REMOTE_ADDR')
        req_method = request.META.get('REQUEST_METHOD')
        path_info = request.META.get('PATH_INFO')
        date_time = time.asctime()

        with open(os.path.join(os.path.abspath('board/logs'), 'request_info.txt'), 'a') as file:
            file.write(f'{date_time}, {remote_ip},{path_info}, {req_method}\n')

        response = self.get_response(request)
        return response

from django.utils.deprecation import MiddlewareMixin


class MenuStateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print("Session before:", request.session.get('menu_state'))
        response = self.get_response(request)
        # print("Session after:", request.session.get('menu_state'))
        return response




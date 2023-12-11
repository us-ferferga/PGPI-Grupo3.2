class AddHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Max-Age'] = '600'
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Expose-Headers'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        response['Access-Control-Allow-Methods'] = '*'
        response['Access-Control-Allow-Credentials'] = 'True'

        return response
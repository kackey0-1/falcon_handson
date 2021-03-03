class ExampleMiddleware(object):

    def process_request(self, req, resp):
        print('process_request')
        print(req)
        print(resp)

    def process_resource(self, req, resp, resource, param):
        print('process_resource')
        print(req)
        print(resp)
        print(resource)
        print(param)

    def process_response(self, req, resp, resource, param):
        print('process_response')
        print(req)
        print(resp)
        print(resource)

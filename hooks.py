
def before_resource(req, resp, resource, params):
    print('hook: before_resource')
    print(req)
    print(resp)
    print(resource)
    print(params)


def after_resource(req, resp, resource):
    print('hook: after_resource')
    print(req)
    print(resp)
    print(resource)

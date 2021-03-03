import json
import falcon
import hooks
import middleware


class RootResource(object):
    def on_get(self, req, resp):
        msg = {
            "message": "Welcome to the Falcon"
        }
        resp.body = json.dumps(msg)


@falcon.before(hooks.before_resource)
@falcon.after(hooks.after_resource)
class ParamsResource(object):
    def on_get(self, req, resp):
        params = req.params
        resp.body = json.dumps(params)


app = falcon.API()
app.add_route('/', RootResource())
app.add_route('/params', ParamsResource())
# app = falcon.API(middleware=[middleware.ExampleMiddleware()])

if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()

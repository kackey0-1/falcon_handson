import falcon
import json
from hooks import hooks


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


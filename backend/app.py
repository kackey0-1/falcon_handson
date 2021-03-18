import falcon
from .images import ImagesResource

api = application = falcon.API()
api.add_route('/images', ImagesResource())

# from api.sample import RootResource, ParamsResource
# app.add_route('/', RootResource())
# app.add_route('/params', ParamsResource())
# app = falcon.API(middleware=[middleware.ExampleMiddleware()])


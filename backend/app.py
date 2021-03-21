import falcon
from mongoengine import connect
from .api import BookResource, ImageResource

connect(db='local',
        username="root",
        password="example",
        host='localhost',
        port=27017,
        authentication_mechanism='SCRAM-SHA-1',
        authentication_source='admin'
        )
api = application = falcon.API()
images = ImageResource()
books = BookResource()
api.add_route('/images', images)
api.add_route('/book/{book_id}', books)
api.add_route('/books/', books)

# api.add_route('')
# from api.sample import RootResource, ParamsResource
# app.add_route('/', RootResource())
# app.add_route('/params', ParamsResource())
# app = falcon.API(middleware=[middleware.ExampleMiddleware()])


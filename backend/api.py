from typing import ByteString
import json
import falcon
from .models import Book


class ImageResource(object):

    def on_get(self, req, resp):
        doc = {
            'images': [{'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'}]}
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200


class BookResource(object):

    def on_get(self, req: falcon.Request, resp: falcon.Request, book_id: ByteString):
        """
        :param req: A request object
        :param resp: A response object
        :param book_id: book_id received in http path to query book object
        :return:
        """
        # Query book collection to get a record with id = book_id
        book_obj = Book.objects.get(id=book_id)
        # It will set response body as a json object of book fields.
        resp.body = json.dumps({'author':book_obj.author,'name':book_obj.name,'isbn':book_obj.isbn})
        # Finally return 200 response on success
        resp.status = falcon.HTTP_200

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        """
        :param req: A request object
        :param resp: A response object
        :return:
        """
        # req.media will deserialize json object
        book_data = req.media
        # passing book_data to create method. It will create a database document in book collection.
        book_obj = Book.objects.create(**book_data)
        resp.body = json.dumps({'book_id': str(book_obj.id), 'message': 'book successfully created'})
        resp.status = falcon.HTTP_200

    def on_put(self, req: falcon.Request, resp: falcon.Response, book_id: ByteString):
        """
        :param req: A request object
        :param resp: A response object
        :return:
        """
        book_data = req.media
        book_obj = Book.objects.get(id=book_id)
        book_obj.update(author=book_data.get('author') if book_data.get('author') else book_obj.author,
                        name=book_data.get('name') if book_data.get('name') else book_obj.name,
                        isbn=book_data.get('isbn') if book_data.get('isbn') else book_obj.isbn,)
        resp.body = json.dumps({'book_id': str(book_obj.id), 'message': 'book successfully updated'})
        resp.status = falcon.HTTP_204






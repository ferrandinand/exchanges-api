from flask import Blueprint

from object.api import ObjectAPI

object_app = Blueprint('object_app', __name__)

object_view = ObjectAPI.as_view('object_api')
object_app.add_url_rule('/objects/', defaults={'object_id': None},
view_func=object_view, methods=['GET',])
object_app.add_url_rule('/objects/', view_func=object_view, methods=['POST',])
object_app.add_url_rule('/objects/<object_id>', view_func=object_view,
methods=['GET', 'PUT', 'DELETE',])
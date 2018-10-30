from flask.views import MethodView
from flask import jsonify, request, abort


class ObjectAPI(MethodView):

    objects = [
        {"id": 1, "name": u"oven","links": [{"rel": "self","href":"/objects/1"}]},
        {"id": 2, "name": u"beer","links": [{"rel": "self","href":"/objects/2"}]},
        {"id": 3, "name": u"clock","links": [{"rel": "self","href":"/objects/3"}]}
    ]

    def get(self,object_id):
        if object_id:
            return jsonify({"object":self.objects[int(object_id) - 1]})
        else:
            return jsonify({"object":self.objects})

    def post(self):
        if not request.json or not 'name' in request.json:
            abort(400)
        object = {
            "id": len(self.objects) + 1,
            "name": request.json["name"],
            "links": [{"rel": "self","href":"/objects/" + str(len(self.objects) + 1)}]
        }
        self.objects.append(object)
        return jsonify({'object':object},201)

    def put(self, object_id):
        if not request.json or not 'name' in request.json:
            abort(400)
        object = self.objects[int(object_id) -1]
        object["name"] = request.json["name"]
        return jsonify({'object': object}),200
    def delete(self, object_id):
        del self.objects[int(object_id) - 1]
        return jsonify({}), 204
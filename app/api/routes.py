from traceback import print_tb

from flask import jsonify

from app.api import bp
from app.models import Resource, Language


@bp.route('/resources', methods=['GET'])
def resources():
    return get_resources()


@bp.route('/languages', methods=['GET'])
def languages():
    return get_languages()


def get_resources():
    resources = {}
    try:
        resources = Resource.query.all()

    except Exception as e:
        print_tb(e.__traceback__)
        print(e)

    finally:
        return jsonify([single_resource.serialize for single_resource in resources])


def get_languages():
    try:
        languages = Language.query.all()

    except Exception as e:
        print_tb(e.__traceback__)
        print(e)
        languages = {}
    finally:
        return jsonify([single_resource.serialize for single_resource in resources])

from flask import Blueprint
import logging
from flask import current_app, request

from tasks.algorithms import fibonacci_algo, ackermann_algo, factorial_algo

api_blueprint = Blueprint('api', __name__)

logger = logging.getLogger('lara.api')


@api_blueprint.route('/ping')
@api_blueprint.route('/')
def ping():
    return {"message": "pong"}, 200


@api_blueprint.route('/fibonacci')
def fibonacci():
    n = request.args.get("n", None)
    if n is None:
        return {"status": "failed", "algo": "fibonacci", "result": "Bad input"}, 400

    try:
        n = int(n)
        result = fibonacci_algo(n)
        return {"status": "success", "algo": "fibonacci", "result": result}, 200
    except ValueError as e:
        return {"status": "failed", "algo": "fibonacci", "result": str(e)}, 400


@api_blueprint.route('/factorial')
def factorial():
    n = request.args.get("n", None)
    if n is None:
        return {"status": "failed", "algo": "factorial", "result": "Bad input"}, 400

    try:
        n = int(n)
        result = factorial_algo(n)
        return {"status": "success", "algo": "factorial", 'result': result}, 200
    except ValueError as e:
        return {"status": "failed", "algo": "factorial", "result": str(e)}, 400


@api_blueprint.route('/ackermann')
def ackermann():
    m = request.args.get("m", None)
    n = request.args.get("n", None)

    if (n is None) or (m is None):
        return {"status": "failed", "algo": "ackermann", "ackermann": "Bad input"}, 400

    try:
        m = int(m)
        n = int(n)
        result = ackermann_algo(m, n)
        return {"status": "success", "algo": "ackermann", 'result': result}, 200
    except ValueError as e:
        return {"status": "failed", "algo": "ackermann", "result": str(e)}, 400



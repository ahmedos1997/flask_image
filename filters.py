from flask import Blueprint

bp = Blueprint('filters', __name__, url_prefix='/filters')

@bp.route('/blur', methods=['POST'])
def blur():
    pass

@bp.route('/constract', methods=['POST'])
def constract():
    pass

@bp.route('/brightness', methods=['POST'])
def brightness():
    pass
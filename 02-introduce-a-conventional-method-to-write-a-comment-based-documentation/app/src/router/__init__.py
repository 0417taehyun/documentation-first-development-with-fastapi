from flask import Blueprint

from src.router import book


router = Blueprint(name="router", import_name=__name__)
router.register_blueprint(blueprint=book.router)

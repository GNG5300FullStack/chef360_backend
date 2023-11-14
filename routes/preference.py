from flask import Blueprint
from services.preferenceService import getPreference,addPreference
from services.openaiService import getRecipe
preference_bp = Blueprint('preference', __name__)


preference_bp.route('/getPreference', methods=['GET'])(getPreference)
preference_bp.route('/addPreference', methods=['POST'])(addPreference)

preference_bp.route('/testOpenai', methods=['POST'])(getRecipe)

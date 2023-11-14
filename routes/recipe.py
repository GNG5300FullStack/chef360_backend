from flask import Blueprint
from services.recipeService import recipePromptGeneration


recipe_bp = Blueprint('recipe_bp', __name__)

recipe_bp.route('/recipePrompt', methods=['POST'])(recipePromptGeneration)
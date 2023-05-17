from flask import Blueprint, render_template

random_puzzle_bp = Blueprint('random_puzzle_bp', __name__, 
                             static_folder = 'static', static_url_path = 'assets',
                             template_folder = 'templates')

@random_puzzle_bp.route('/')
def start_rp():
    return render_template('random_puzzle.html')
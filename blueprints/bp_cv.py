from flask import Blueprint, jsonify
from static.cv_data import cv_data

bp = Blueprint('api', __name__)

# @bp.route('/personal', methods=["GET"])
# def get_personal():
#     personal_data = cv_data.get("Personal", None)
#     return jsonify(personal_data)

"""
    Used a more explicit form to emphasize exception handling + custom error message and code
"""


@bp.route('/personal', methods=["GET"])
def get_personal():
    """
    This endpoint returns the personal data from the cv_data.py file.
    If the key 'Personal' is not found in the cv_data dictionary, it returns a custom error message and a 404 status
    code.
    """
    try:
        personal_data = cv_data["Personal"]
        return jsonify(personal_data)
    except KeyError:
        return jsonify(error="KeyError: Personal data not found"), 404


@bp.route('/competencies', methods=["GET"])
def get_competencies():
    """
    This endpoint returns the core competencies from the cv_data.py file.
    If the key 'Core Competencies' is not found in the cv_data dictionary, it returns a custom error message and a 404
    status code.
    """
    try:
        competencies = cv_data["Core Competencies"]
        return jsonify(competencies)
    except KeyError:
        return jsonify(error="KeyError: Core Competencies not found"), 404


@bp.route('/experience', methods=["GET"])
def get_experience():
    """
    This endpoint returns the professional experience from the cv_data.py file.
    If the key 'Professional Experience' is not found in the cv_data dictionary, it returns a custom error message and
    a 404 status code.
    """
    try:
        experience = cv_data["Professional Experience"]
        return jsonify(experience)
    except KeyError:
        return jsonify(error="KeyError: Professional Experience not found"), 404


@bp.route('/projects', methods=["GET"])
def get_projects():
    """
    This endpoint returns the personal projects from the cv_data.py file.
    If the key 'Personal Projects' is not found in the cv_data dictionary, it returns a custom error message and a 404
    status code.
"""

    try:
        projects = cv_data["Personal Projects"]
        return jsonify(projects)
    except KeyError:
        return jsonify(error="KeyError: Personal Projects not found"), 404


@bp.route('/education', methods=["GET"])
def get_education():
    """
    This endpoint returns the education data from the cv_data.py file.
    If the key 'Education' is not found in the cv_data dictionary, it returns a custom error message and a 404 status
    code.
    """
    try:
        education = cv_data["Education"]
        return jsonify(education)
    except KeyError:
        return jsonify(error="KeyError: Education not found"), 404

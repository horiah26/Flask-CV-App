import logging
from typing import Dict, List


def process_data(cv_data: Dict) -> str:
    """
    Processes data from a CV and returns a formatted string.

    Parameters:
    cv_data : dict
    A dictionary with CV data in a specific format, see static/cv_data.py for details.

    Returns:
    complete_cv : str
    A formatted string with all the data from the CV.
    """
    header = "====================================  CV IN FLASK  ===================================="
    if not cv_data:
        raise ValueError("No CV found or CV is empty")
    personal = process_personal(cv_data)
    competencies = process_competencies(cv_data)
    experience = process_experience(cv_data)
    personal_projects = process_projects(cv_data)
    education = process_education(cv_data)
    complete_cv = "\n{}\n\n{}{}{}{}{}".format(header, personal, competencies, experience, personal_projects, education)
    return complete_cv


def process_personal(cv_data: Dict) -> str:
    """
    This function receives a dictionary 'cv_data' and extracts the 'Personal' information from it.
    It then gets the personal information values and join them into a single string and formats them to have a bullet
    point before each line.
    Finally, the function returns the "section_personal" string.

    Parameters:
    cv_data : dict
    A dict containing the CV data.

    Returns:
    section_personal : str
    A string containing the personal info.
    """
    personal = validate_input(cv_data, "Personal")
    if not personal:
        return ""
    try:
        personal_values_list = list(personal.values())
        personal_values = ' | '.join(personal_values_list)
        section_personal = "{} \n{}\n\n".format("-------------------- Personal info --------------------",
                                                personal_values)
    except Exception as e:
        logging.error(f"Error joining personal values: {e}")
        return ""
    return section_personal


def process_competencies(cv_data: Dict) -> str:
    """
    This function receives a dictionary 'cv_data' and extracts the 'Core Competencies' from it.
    It checks that all competencies are strings
    If the key exists and is not None, it joins the list of competencies into a single string, separated by " | ".
    It then formats that string as "Core Competencies" followed by the list of competencies.
    Finally, it returns the formatted "section_competencies" string.

    Parameters:
    cv_data : dict
    A dict containing the CV data.

    Returns:
    section_competencies : str
    A string containing the core competencies.
    """
    competencies = validate_input(cv_data, "Core Competencies")
    if not are_all_strings(competencies):
        logging.error(f"Not all competencies are strings")
        return ""
    try:
        competencies = ' | '.join(competencies)
    except Exception as e:
        logging.error(f"Error joining competencies list: {e}")
        return ""

    section_competencies = f"-------------------- Core Competencies -------------------- \n{competencies}\n"
    return section_competencies


def process_experience(cv_data: Dict) -> str:
    """
    This function receives a dictionary 'cv_data' and extracts the 'Professional Experience' from it.
    It then iterates through the list of experiences, extracting the company name, job title, date, and job description
    for each experience.
    If a job description exists, it is formatted to have a bullet point before each line.
    The function then creates a string for each experience by combining the company name, job title, date, and job
    description, and appending that to a larger string called "all_experience".
    Finally, the function returns the "section_experience" string.

    Parameters:
    cv_data : dict
    A dict containing the CV data.

    Returns:
    all_experience : str
    A string containing all the professional experiences.
    """
    all_experience, section_experience = "", ""
    experiences = validate_input(cv_data, "Professional Experience")
    for experience in experiences:
        company = experience.get('company_name', None)
        job_title = experience.get('job_title', None)
        date = experience.get('date', None)
        job_description = experience.get('job description', None)

        if not company:
            logging.error("No company found in experience, skipping")
            continue
        if not job_title:
            logging.error("No job title found in experience, skipping")
            continue
        if not date:
            logging.error("No date found in experience, skipping")
            continue

        if job_description:
            job_description = '\n - '.join(job_description)
            job_description = '- {}'.format(job_description)
        experience_at_company = f'\n{company} | {job_title} \n{date} \n {job_description}\n'
        all_experience += experience_at_company
        section_experience = "\n{} {}".format("-------------------- Professional Experience --------------------",
                                              all_experience)
    return section_experience


def process_projects(cv_data: Dict) -> str:
    """
    This function receives a dictionary 'cv_data' and extracts the 'Personal Projects' from it.
    It then iterates through the list of projects, extracting the name, description, and skills for each project.
    If a skills exist, it is formatted to have a bullet point before each line.
    The function then creates a string for each project by combining the name, description and skills, and appending
    that to a larger string called "all_projects".
    Finally, the function returns the "section_projects" string.

    Parameters:
    cv_data : dict
    A dict containing the CV data.

    Returns:
    section_projects : str
    A string containing formatted projects.
    """
    all_projects, section_projects = "", ""
    projects = validate_input(cv_data, "Personal Projects")
    if not projects:
        return all_projects
    for project in projects:
        name = project.get('name', None)
        description = project.get('description', None)
        skills = project.get('skills', None)
        if not are_all_strings(skills):
            logging.error(f"Not all skills are strings")
            continue
        if not name:
            logging.error(f"Missing project name: {name}")
            continue
        if not description:
            logging.error(f"Missing project description: {description}")
            continue
        try:
            if skills:
                skills = " | ".join(skills)
                project_str = f'\n{name} \n- {description}\n- {skills}\n'
            else:
                project_str = f'\n{name} \n- {description}\n'
        except Exception as e:
            logging.error(f"Error joining project skills: {e}")
            continue
        all_projects += project_str
        section_projects = "\n{} {}".format("--------------------Personal Projects--------------------", all_projects)
    return section_projects


def process_education(cv_data: Dict) -> str:
    """
    This function receives a dictionary 'cv_data' and extracts the 'Education' from it.
    It then iterates through the list of education, extracting the institution name, description, date, and skills for
    each.
    If skills exists, it is formatted to have a bullet point before each line.
    The function then creates a string for each experience by combining the company name, name, description, date, and
    skills, and appending that to a larger string called "all_experience". Finally, the function returns the
    "section_education" string.

    Parameters:
    cv_data : dict
    A dict containing the CV data.

    Returns:
    section_education : str
    A string containing formatted education.
    """
    all_education, section_education = "", ""
    educations = validate_input(cv_data, "Education")
    if not educations:
        return all_education
    for education in educations:
        name = education.get('institution_name', None)
        description = education.get('description', None)
        date = education.get('date', None)
        skills = education.get('skills', None)
        if not are_all_strings(skills):
            logging.error("Not all education skills are strings")
            continue
        if not name:
            logging.error(f"Missing education name: {name}")
            continue
        if not description:
            logging.error(f"Missing education description: {description}")
            continue
        if not date:
            logging.error(f"Missing education date: {date}")
            continue
        try:
            if skills:
                skills = " | ".join(skills)
                education_str = f'\n{name}\n{date} \n- {description}\n- {skills}\n'
            else:
                education_str = f'\n{name}\n{date}  \n- {description}\n'
        except Exception as e:
            logging.error(f"Error joining education skills: {e}")
            continue
        all_education += education_str

        section_education = "\n{} {}".format("-------------------- Education --------------------", all_education)
    return section_education


def validate_input(data: Dict, key: str):
    """
    This function receives a dictionary 'data' and a key, it checks if the input is a dictionary,
    if the key exist in the dictionary and if the value of that key is not None and not empty
    if any of these checks fails it will log an error message and return an empty string.

    Parameters:
    data : dict
    A dict containing the data.
    key : str
    The key that needs to be checked in the data.

    Returns:
    data[key]: any
    The value of the key if the input is valid, otherwise an empty string.
    """
    if not isinstance(data, dict):
        logging.error("Input is not a dictionary.")
        return ""

    if key not in data:
        logging.error(f"{key} key not found in input.")
        return ""
    key_value = data.get(key, None)
    if not key_value:
        logging.error(f"No {key} found, skipping.")
        return ""
    if key_value is None:
        logging.error(f"{key} value is None.")
        return ""
    return key_value


def are_all_strings(elements: List[str]) -> bool:
    """
    Checks if all elements of a list are strings

    Parameters:
    elements (List[str]): A list containing str

    Returns:
    bool: True if all elements are strings or there are no elements, False otherwise.
    """
    if not elements:
        return True
    for element in elements:
        if not isinstance(element, str):
            return False
    return True

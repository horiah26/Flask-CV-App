from flask import Flask
from blueprints import bp_cv
from static.cv_data import cv_data
from services.process_cv_data import process_data
import click

app = Flask(__name__)
app.register_blueprint(bp_cv.bp)


@click.command(name="print_cv")
def print_cv():
    """
    This command is used to print the CV data in a formatted string.
    It checks if the cv_data variable is empty or None, and raises a ValueError if it is.
    It processes the data using the process_data function from services.process_cv_data and then prints the result.
    """
    if not cv_data:
        raise ValueError("No CV found or CV is empty")
    processed_data = process_data(cv_data)
    click.echo(processed_data)
    print("New branch")


app.cli.add_command(print_cv)

if __name__ == '__main__':
    app.run()

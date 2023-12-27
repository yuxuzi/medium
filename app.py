import json
import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import SubmitField

load_dotenv()  # load environment variables from .env file

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["UPLOAD_FOLDER"] = "./medium"  # set the upload folder to ./markdown
token = os.getenv("TOKEN")
url = os.getenv("URL")



class UploadForm(FlaskForm):
    submit = SubmitField("Upload")


@app.route("/", methods=["GET", "POST"])
def upload_file():
    form = UploadForm()
    files = [
        file for file in os.listdir(app.config["UPLOAD_FOLDER"]) if file.endswith(".md")
    ]

    # get a list of all files in the directory
    message = ""
    if form.validate_on_submit():
        filename = request.form.get("file")  # get the selected file
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        with open(filepath, "r") as file:
            content = file.read()

            first_line = content.split("\n", 1)[0].strip()
            if first_line.startswith("#"):
                title = first_line[1:].strip()
            else:
                raise ValueError("Your first line should be the title of the post")

        data = {
            "title": title,
            "contentFormat": "markdown",
            "content": content,
            "tags": ["python","data science"],
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",  # replace 'token' with your actual token
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 201:
            message = "File uploaded and posted successfully. ✅"
        else:


       
            message = f"An error occurred. ❌\n{response.text}"
           

    return render_template(
        "upload.html", form=form, files=files, message=message
    )  # pass the list of files to the template


if __name__ == "__main__":
    app.run(debug=True)

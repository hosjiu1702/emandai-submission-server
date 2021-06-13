from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from app.config import submission_folder


app = Flask(__name__)


@app.get("/index")
def get_index_page():
    return render_template("index.html")


@app.post("/")
@app.get("/")
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        file_name = uploaded_file.filename
        if filename != "":
            save_path = os.path.join(submission_folder, filename)
            uploaded_file.save(save_path)
        return redirect(url_for("get_index_page"))
    return render_template("submit.html")


if __name__ == '__main__':
    app.run(debug=True)

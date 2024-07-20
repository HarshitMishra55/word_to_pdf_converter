import os
from flask import Flask, render_template, request, send_file, redirect, url_for
from word_to_pdf_converter.convert import convert_to_pdf
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    if "word_file" not in request.files:
        return "No file part"

    word_file = request.files["word_file"]

    if word_file.filename == "":
        return "No selected file"

    pdf_buffer = convert_to_pdf(word_file)
    pdf_buffer.seek(0)  # Reset buffer position to start

    pdf_path = os.path.join(UPLOAD_FOLDER, "converted.pdf")
    with open(pdf_path, "wb") as f:
        f.write(pdf_buffer.read())

    return redirect(url_for("download_pdf"))


@app.route("/download")
def download_pdf():
    pdf_path = os.path.join(UPLOAD_FOLDER, "converted.pdf")
    return send_file(pdf_path, as_attachment=True, download_name="converted.pdf")


if __name__ == "__main__":
    app.run(debug=True)

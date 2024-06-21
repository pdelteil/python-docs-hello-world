from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    html_content = """
    <!DOCTYPE html>
    <html>

    <body>
      
        <!-- Takeover by pdelteil -->
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=True)

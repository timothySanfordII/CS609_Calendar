// V added test.py file updated file.....
from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Flask HTML Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
            text-align: center;
        }
        header {
            background-color: #4CAF50;
            padding: 10px;
            color: white;
            font-size: 24px;
        }
        main {
            padding: 20px;
        }
        footer {
            background-color: #ddd;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        Welcome to My Flask App
    </header>
    <main>
        <h1>Hello, World!</h1>
        <p>This is a simple HTML page served using Flask.</p>
    </main>
    <footer>
        &copy; 2024 Your Name
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)

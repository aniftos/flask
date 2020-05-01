from flaskblog import create_app

app = create_app() #used config.py configuration as a defult if you dont pass anything


if __name__ == "__main__":
    app.run(debug=True)
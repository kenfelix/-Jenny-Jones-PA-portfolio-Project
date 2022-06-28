from app import app
# from flask_ngrok import run_with_ngrok as ngrok


# ngrok(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)


    
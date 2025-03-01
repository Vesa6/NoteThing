import { useState } from "react";

function AuthForm({ isLogin }) {
  const [formValues, setFormValues] = useState({
    username: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormValues({ ...formValues, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    //Converts json to form-encoded data for FastAPI
    const formData = new URLSearchParams();
    formData.append("username", formValues.username);
    formData.append("password", formValues.password);

    const endpoint = isLogin ? "/auth/login" : "/auth/register";

    try {
      const response = await fetch(`http://127.0.0.1:8000${endpoint}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",  //FastAPI needs this type instead of JSON
        },
        body: formData,
      });

      const data = await response.json();
      console.log("Server Response:", data);

      if (response.ok) {
        if (isLogin) {
          localStorage.setItem("token", data.access_token);
          alert("Login successful!");
        } else {
          alert("Registration successful! You can now log in.");
        }
      } else {
        alert(`Error: ${data.detail}`);
      }
    } catch (error) {
      console.error("Error during authentication:", error);
      alert("An error occurred. Please try again.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input
        type="text"
        name="username"
        placeholder="Username"
        value={formValues.username}
        onChange={handleChange}
        className="w-full p-2 border rounded"
        required
      />
      <input
        type="password"
        name="password"
        placeholder="Password"
        value={formValues.password}
        onChange={handleChange}
        className="w-full p-2 border rounded"
        required
      />
      <button type="submit" className="w-full p-2 bg-blue-500 text-white rounded">
        {isLogin ? "Login" : "Register"}
      </button>
    </form>
  );
}

export default AuthForm;

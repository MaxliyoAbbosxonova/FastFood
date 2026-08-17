const toggle = document.getElementById("toggle");
const toggleIcon = document.getElementById("toggleIcon");
const password = document.getElementById("password");
const errorBox = document.getElementById("errorBox");
const errorMsg = document.getElementById("errorMsg");

toggle.onclick = () => {
  const isPass = password.type === "password";
  password.type = isPass ? "text" : "password";
  toggleIcon.className = isPass ? "ti ti-eye-off" : "ti ti-eye";
};

document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  errorBox.style.display = "none";
  const phone = document.getElementById("phone").value;
  const passwordVal = password.value;
  const btn = e.target.querySelector(".btn-login");
  btn.innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> Yuklanmoqda...';
  btn.disabled = true;
  try {
    const res = await fetch("/c_admin/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ phone, password: passwordVal })
    });
    const data = await res.json();
    if (!res.ok) {
      errorMsg.textContent = data.detail || "Login xato";
      errorBox.style.display = "flex";
    } else {
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
      window.location.href = "base/";
    }
  } catch (err) {
    errorMsg.textContent = "Server xatosi";
    errorBox.style.display = "flex";
  }
  btn.innerHTML = '<i class="ti ti-login"></i> Kirish';
  btn.disabled = false;
});
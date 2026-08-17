// Sidebar
const sidebar = document.querySelector(".sidebar");
const sidebarToggle = document.querySelector(".sidebar-toggle");

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("collapsed");
});

// Main content va page title
const mainContent = document.getElementById("main-content");
const pageTitle = document.getElementById("page-title");

// Sidebar menu
document.querySelectorAll(".menu-link").forEach(item => {
    item.addEventListener("click", async function (e) {
        e.preventDefault();

        // Navbar title
        pageTitle.innerText = this.dataset.title;

        // Qaysi sahifa yuklanishi
        const page = this.dataset.page;

        try {
            const response = await fetch(`/custom_admin/${page}/`);
            if (!response.ok) {
                throw new Error("Sahifa topilmadi!");
            }

            const html = await response.text();

            mainContent.innerHTML = html;
            loadCards();

        } catch (error) {
            mainContent.innerHTML = `
                <div style="padding:20px;color:red;">
                    ${error.message}
                </div>
            `;
        }
    });
});

// Dark mode (sizdagi kod)
const navbar = document.querySelector(".main-wrapper");
const iconDark = document.querySelector(".icon-btn");

iconDark.addEventListener("click", () => {
    navbar.classList.toggle("collapsed");
});

async function loadCards() {
    try {
        const response = await fetch("/custom_admin/cards/");

        console.log("Status:", response.status);

        if (!response.ok) {
            throw new Error("Ma'lumotlarni olib bo'lmadi.");
        }

        const data = await response.json();

        console.log("Data:", data);

        document.getElementById("total-orders").textContent = data.total_orders;
        document.getElementById("total-res").textContent = data.total_res;
        document.getElementById("total-orders-today").textContent = data.total_orders_today;
        document.getElementById("avg-time").textContent = data.avg_time;

        document.getElementById("total-revenue").textContent =
            new Intl.NumberFormat("uz-UZ").format(data.total_revenue);
        document.getElementById("today-revenue").textContent =
            new Intl.NumberFormat("uz-UZ").format(data.today_revenue);
        document.getElementById("avg-revenue").textContent =
            new Intl.NumberFormat("uz-UZ").format(data.avg_revenue);
    } catch (err) {
        console.error(err);
    }
}

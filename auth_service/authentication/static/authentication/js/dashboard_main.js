// dashboard_main.js — exclusivo para dashboard.html (Página Principal)

const token = localStorage.getItem("access_token");
if (!token) window.location.href = "/login/";

document.addEventListener("DOMContentLoaded", () => {
  aplicarPermissoes();
  atualizarDashboard("dia");

  document.querySelectorAll(".filtro-periodo").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".filtro-periodo").forEach(b => {
        b.classList.remove("bg-blue-600", "text-white");
        b.classList.add("bg-gray-100", "text-gray-800");
      });

      btn.classList.remove("bg-gray-100", "text-gray-800");
      btn.classList.add("bg-blue-600", "text-white");

      const periodo = btn.dataset.periodo;
      atualizarDashboard(periodo);
    });
  });
});

function aplicarPermissoes() {
  const perfil = localStorage.getItem("user_type");
  document.querySelectorAll(".btn-permissao-restrita").forEach(btn => {
    if (perfil === "admin" || perfil === "secretaria") {
      btn.classList.remove("hidden");
      btn.disabled = false;
    } else {
      btn.classList.add("hidden");
      btn.disabled = true;
    }
  });

  const aprovacaoLink = document.getElementById("admin-aprovacao-link");
  if (perfil === "admin" && aprovacaoLink) {
    aprovacaoLink.classList.remove("hidden");
    aprovacaoLink.addEventListener("click", function(e) {
      e.preventDefault();
      carregarAprovacaoUsuarios();
    });
  }
}

function atualizarDashboard(periodo) {
  // Simulação de dados dinâmicos por período
  const dados = {
    dia:     { atendimentos: 5, pacientes: 12, consultas: 8, meta: "35%" },
    semana:  { atendimentos: 27, pacientes: 45, consultas: 36, meta: "70%" },
    mes:     { atendimentos: 110, pacientes: 165, consultas: 142, meta: "82%" },
    ano:     { atendimentos: 820, pacientes: 1110, consultas: 960, meta: "90%" },
  };

  const info = dados[periodo] || dados["dia"];
  document.getElementById("atendimentos").innerText = info.atendimentos;
  document.getElementById("pacientes").innerText = info.pacientes;
  document.getElementById("consultas").innerText = info.consultas;
  document.getElementById("meta").innerText = info.meta;
}

function logout() {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  localStorage.removeItem("username");
  localStorage.removeItem("user_type");
  window.location.href = "/login/";
}

function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("sidebar-collapsed");
}

function voltarDashboard() {
  window.location.href = "/dashboard/";
}

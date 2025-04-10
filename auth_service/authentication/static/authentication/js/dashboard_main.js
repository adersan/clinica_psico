const token = localStorage.getItem("access_token");
if (!token) window.location.href = "/login/";

const username = localStorage.getItem("username") || "Usuário";
document.getElementById("user-name").innerText = `Bem-vindo, ${username}!`;

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
      carregarAprovacaoUsuarios();  // função definida em carregar_aprovacao.js
    });
  }
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

function carregarConteudo(url) {
  fetch(url)
    .then(res => {
      if (!res.ok) throw new Error("Erro ao carregar página");
      return res.text();
    })
    .then(html => {
      const container = document.getElementById("conteudo-principal");

      // Cria um container temporário
      const temp = document.createElement("div");
      temp.innerHTML = html;

      // Extrai os scripts antes de injetar o HTML
      const scripts = temp.querySelectorAll("script");
      scripts.forEach(script => script.remove());

      // Injeta o conteúdo HTML no container
      container.innerHTML = temp.innerHTML;

      // Injeta scripts dinamicamente (resolve seu problema!)
      scripts.forEach(oldScript => {
        const newScript = document.createElement("script");

        if (oldScript.src) {
          newScript.src = oldScript.src;
        } else {
          newScript.textContent = oldScript.textContent;
        }

        // Garante execução imediata
        document.body.appendChild(newScript);
      });

      // Esconde título principal e recolhe o menu
      document.getElementById("sidebar").classList.add("sidebar-collapsed");
      document.getElementById("titulo-painel").classList.add("hidden-title");
    })
    .catch(() => {
      document.getElementById("conteudo-principal").innerHTML = `
        <div class="bg-red-100 text-red-800 p-4 rounded">
          Ocorreu um erro ao carregar esta página.
        </div>
      `;
    });
}

function voltarDashboard() {
  const dashboardBackup = document.getElementById("dashboard-conteudo");
  if (dashboardBackup) {
    document.getElementById("conteudo-principal").innerHTML = dashboardBackup.outerHTML;
  }
  document.getElementById("sidebar").classList.remove("sidebar-collapsed");
  document.getElementById("titulo-painel").classList.remove("hidden-title");

  aplicarPermissoes();
}

document.addEventListener("DOMContentLoaded", () => {
  aplicarPermissoes();
});
document.addEventListener("DOMContentLoaded", () => {
  carregarPacientes();

  document.getElementById("form-novo-paciente").addEventListener("submit", async (e) => {
    e.preventDefault();
    const dados = coletarDadosNovoPaciente();

    if (!validarPaciente(dados)) return;

    const sucesso = await enviarRequisicao("http://127.0.0.1:8001/api/pacientes/", "POST", dados);
    if (sucesso) {
      fecharModalNovoPaciente();
      carregarPacientes();
    }
  });
});

let pacientesCache = [];

function coletarDadosNovoPaciente() {
  return {
    nome: document.getElementById("novo-nome").value.trim(),
    cpf: document.getElementById("novo-cpf").value.trim(),
    email: document.getElementById("novo-email").value.trim(),
    telefone: document.getElementById("novo-telefone").value.trim(),
  };
}

function validarPaciente(dados) {
  if (!dados.nome || !dados.cpf) {
    mostrarToast("Preencha todos os campos obrigatórios", "red");
    return false;
  }
  return true;
}

async function enviarRequisicao(url, metodo, corpo) {
  try {
    const res = await fetch(url, {
      method: metodo,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(corpo)
    });

    if (res.ok) {
      mostrarToast("Operação realizada com sucesso", "green");
      return true;
    } else {
      const erro = await res.json();
      mostrarToast(erro.detail || "Erro na operação", "red");
    }
  } catch (err) {
    mostrarToast("Erro de conexão com servidor", "red");
  }
  return false;
}

function mostrarToast(mensagem, cor) {
  const toast = document.getElementById("toast");
  toast.textContent = mensagem;
  toast.className = `fixed top-4 right-4 bg-${cor}-500 text-white px-4 py-2 rounded shadow-lg z-50`;
  toast.classList.remove("hidden");

  setTimeout(() => {
    toast.classList.add("hidden");
  }, 3000);
}

function carregarPacientes() {
  fetch("http://127.0.0.1:8001/api/pacientes/")
    .then(res => res.json())
    .then(data => {
      pacientesCache = data;
      const tbody = document.getElementById("pacientes-tbody");
      tbody.innerHTML = "";
      data.forEach(p => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td class="border px-4 py-2">${p.nome}</td>
          <td class="border px-4 py-2">${p.cpf}</td>
          <td class="border px-4 py-2">${p.telefone}</td>
          <td class="border px-4 py-2">${p.email}</td>
          <td class="border px-4 py-2 space-x-2">
            <button class="bg-blue-600 text-white px-2 py-1 rounded" onclick="abrirModalEditar(${p.id})">Editar</button>
            <button class="bg-red-600 text-white px-2 py-1 rounded" onclick="abrirModalExcluir(${p.id})">Excluir</button>
          </td>`;
        tbody.appendChild(row);
      });
    });
}

function abrirModalNovoPaciente() {
  document.getElementById("modal_novo_paciente").classList.remove("hidden");
}

function fecharModalNovoPaciente() {
  document.getElementById("modal_novo_paciente").classList.add("hidden");
}

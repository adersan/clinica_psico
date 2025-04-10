document.addEventListener("DOMContentLoaded", () => {
  carregarPacientes();

  document.getElementById("form-novo-paciente").addEventListener("submit", salvarNovoPaciente);
  document.getElementById("form-editar-paciente").addEventListener("submit", salvarEdicaoPaciente);
  document.getElementById("btn-excluir-paciente").addEventListener("click", excluirPacienteConfirmado);
});

let pacientesCache = [];

async function carregarPacientes() {
  try {
    const response = await fetch("http://127.0.0.1:8001/api/pacientes/");
    const data = await response.json();
    pacientesCache = data;

    const tbody = document.getElementById("pacientes-tbody");
    tbody.innerHTML = "";

    data.forEach(paciente => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td class="border px-4 py-2">${paciente.nome}</td>
        <td class="border px-4 py-2">${paciente.cpf}</td>
        <td class="border px-4 py-2">${paciente.telefone}</td>
        <td class="border px-4 py-2">${paciente.email}</td>
        <td class="border px-4 py-2 space-x-2">
          <button class="bg-blue-600 text-white px-2 py-1 rounded" onclick="abrirModalEditar(${paciente.id})">Editar</button>
          <button class="bg-red-600 text-white px-2 py-1 rounded" onclick="abrirModalExcluir(${paciente.id})">Excluir</button>
        </td>
      `;
      tbody.appendChild(row);
    });
  } catch (err) {
    alert("Erro ao carregar pacientes.");
  }
}

function abrirModalNovoPaciente() {
    const modal = document.getElementById('modal_novo_paciente');
    if (modal) modal.classList.remove('hidden');
}


function fecharModalNovoPaciente() {
  document.getElementById("modal_novo_paciente").classList.add("hidden");
}

function abrirModalEditar(id) {
  const paciente = pacientesCache.find(p => p.id === id);
  if (!paciente) return;

  document.getElementById("edit-id").value = paciente.id;
  document.getElementById("edit-nome").value = paciente.nome;
  document.getElementById("edit-cpf").value = paciente.cpf;
  document.getElementById("edit-email").value = paciente.email;
  document.getElementById("edit-telefone").value = paciente.telefone;

  document.getElementById("modal_editar_paciente").classList.remove("hidden");
}

function fecharModalEditarPaciente() {
  document.getElementById("modal_editar_paciente").classList.add("hidden");
}

function abrirModalExcluir(id) {
  document.getElementById("excluir-id").value = id;
  document.getElementById("modal_excluir_paciente").classList.remove("hidden");
}

function fecharModalExcluirPaciente() {
  document.getElementById("modal_excluir_paciente").classList.add("hidden");
}

async function salvarNovoPaciente(e) {
  e.preventDefault();
  const dados = {
    nome: document.getElementById("novo-nome").value,
    cpf: document.getElementById("novo-cpf").value,
    email: document.getElementById("novo-email").value,
    telefone: document.getElementById("novo-telefone").value,
  };

  try {
    const response = await fetch("http://127.0.0.1:8001/api/pacientes/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados)
    });

    if (response.ok) {
      fecharModalNovoPaciente();
      carregarPacientes();
    }
  } catch {
    alert("Erro ao salvar paciente.");
  }
}

async function salvarEdicaoPaciente(e) {
  e.preventDefault();
  const id = document.getElementById("edit-id").value;
  const dados = {
    nome: document.getElementById("edit-nome").value,
    cpf: document.getElementById("edit-cpf").value,
    email: document.getElementById("edit-email").value,
    telefone: document.getElementById("edit-telefone").value,
  };

  try {
    const response = await fetch(`http://127.0.0.1:8001/api/pacientes/${id}/`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados)
    });

    if (response.ok) {
      fecharModalEditarPaciente();
      carregarPacientes();
    }
  } catch {
    alert("Erro ao atualizar paciente.");
  }
}

async function excluirPacienteConfirmado() {
  const id = document.getElementById("excluir-id").value;
  try {
    const response = await fetch(`http://127.0.0.1:8001/api/pacientes/${id}/`, {
      method: "DELETE"
    });

    if (response.ok) {
      fecharModalExcluirPaciente();
      carregarPacientes();
    }
  } catch {
    alert("Erro ao excluir paciente.");
  }
}

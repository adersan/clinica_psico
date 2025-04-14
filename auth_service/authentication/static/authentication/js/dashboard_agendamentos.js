document.addEventListener("DOMContentLoaded", () => {

  // Botão para abrir modal de nova consulta
  document.getElementById("btn-nova-consulta")?.addEventListener("click", abrirModalNovaConsulta);

  // Submissões dos formulários
  document.getElementById("form-nova-consulta")?.addEventListener("submit", salvarNovaConsulta);
  document.getElementById("form-editar-consulta")?.addEventListener("submit", salvarConsultaEditada);
  document.getElementById("btn-excluir-consulta")?.addEventListener("click", excluirConsultaSelecionada);
});

function perfilRestrito() {
  const perfil = localStorage.getItem("user_type");
  return perfil !== "admin" && perfil !== "secretaria";
}

function abrirModalNovaConsulta() {
  if (perfilRestrito()) {
    alert("Você não tem permissão para criar consultas.");
    return;
  }
  document.getElementById("modal_nova_consulta").classList.remove("hidden");
}

function fecharModalNovaConsulta() {
  document.getElementById("modal_nova_consulta").classList.add("hidden");
}

function fecharModalEditarConsulta() {
  document.getElementById("modal_editar_consulta").classList.add("hidden");
}

function obterDadosFormulario(prefixo) {
  return {
    paciente: document.getElementById(`${prefixo}paciente`)?.value,
    profissional: document.getElementById(`${prefixo}profissional`)?.value,
    data: document.getElementById(`${prefixo}data`)?.value,
    hora: document.getElementById(`${prefixo}hora`)?.value,
    status: document.getElementById(`${prefixo}status`)?.value,
    observacoes: document.getElementById(`${prefixo}observacoes`)?.value,
  };
}

function validarCamposObrigatorios(dados) {
  for (const [campo, valor] of Object.entries(dados)) {
    if (!valor) {
      alert(`O campo "${campo}" é obrigatório.`);
      return false;
    }
  }
  return true;
}

async function salvarNovaConsulta(e) {
  e.preventDefault();
  if (perfilRestrito()) {
    alert("Você não tem permissão para criar consultas.");
    return;
  }

  const dados = obterDadosFormulario("");
  if (!validarCamposObrigatorios(dados)) return;

  try {
    const res = await fetch("http://127.0.0.1:8001/api/consultas/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados),
    });

    if (res.ok) {
      alert("Consulta criada com sucesso!");
      fecharModalNovaConsulta();
      if (typeof carregarCalendario === "function") carregarCalendario();
    } else {
      const erro = await res.json();
      alert("Erro: " + (erro.detail || "Não foi possível salvar a consulta."));
    }
  } catch (err) {
    alert("Erro de conexão com o servidor.");
  }
}

async function salvarConsultaEditada(e) {
  e.preventDefault();
  if (perfilRestrito()) {
    alert("Você não tem permissão para editar consultas.");
    return;
  }

  const id = document.getElementById("edit-id")?.value;
  const dados = obterDadosFormulario("edit-");
  if (!validarCamposObrigatorios(dados)) return;

  try {
    const res = await fetch(`http://127.0.0.1:8001/api/consultas/${id}/`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados),
    });

    if (res.ok) {
      alert("Consulta atualizada com sucesso!");
      fecharModalEditarConsulta();
      if (typeof carregarCalendario === "function") carregarCalendario();
    } else {
      const erro = await res.json();
      alert("Erro: " + (erro.detail || "Erro ao atualizar."));
    }
  } catch (err) {
    alert("Erro ao conectar com o servidor.");
  }
}

async function excluirConsultaSelecionada() {
  if (perfilRestrito()) {
    alert("Você não tem permissão para excluir consultas.");
    return;
  }

  const id = document.getElementById("edit-id")?.value;

  try {
    const res = await fetch(`http://127.0.0.1:8001/api/consultas/${id}/`, {
      method: "DELETE",
    });

    if (res.ok) {
      alert("Consulta excluída com sucesso!");
      fecharModalEditarConsulta();
      if (typeof carregarCalendario === "function") carregarCalendario();
    } else {
      const erro = await res.json();
      alert("Erro: " + (erro.detail || "Erro ao excluir."));
    }
  } catch (err) {
    alert("Erro ao excluir consulta.");
  }
}

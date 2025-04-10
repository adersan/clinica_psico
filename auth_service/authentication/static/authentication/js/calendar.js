
let calendar;
let consultasCache = [];

function inicializarCalendario() {
  const calendarEl = document.getElementById('calendar');
  if (!calendarEl) return;

  calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    locale: 'pt-br',
    height: 'auto',
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    events: [],
    eventClick: function (info) {
      const evento = info.event;
      const consulta = consultasCache.find(c => `${c.data}T${c.hora}` === evento.startStr);
      if (consulta) {
        const detalhes = `
          <p><strong>Paciente:</strong> ${consulta.paciente}</p>
          <p><strong>Profissional:</strong> ${consulta.profissional}</p>
          <p><strong>Tipo:</strong> ${consulta.tipo_consulta}</p>
          <p><strong>Participantes:</strong> ${consulta.participantes || 'N/A'}</p>
          <p><strong>Data:</strong> ${consulta.data}</p>
          <p><strong>Hora:</strong> ${consulta.hora}</p>
          <p><strong>Status:</strong> ${consulta.status}</p>
          <p><strong>Observações:</strong> ${consulta.observacoes || 'N/A'}</p>
        `;
        document.getElementById('detalhesConsulta').innerHTML = detalhes;
        document.getElementById('modalDetalhes').classList.remove('hidden');

        // Preencher modal de edição
        document.getElementById('edit-id').value = consulta.id;
        document.getElementById('edit-paciente').value = consulta.paciente;
        document.getElementById('edit-profissional').value = consulta.profissional;
        document.getElementById('edit-tipo-consulta').value = consulta.tipo_consulta;
        document.getElementById('edit-participantes').value = consulta.participantes;
        document.getElementById('edit-data').value = consulta.data;
        document.getElementById('edit-hora').value = consulta.hora;
        document.getElementById('edit-status').value = consulta.status;
        document.getElementById('edit-observacoes').value = consulta.observacoes;
      }
    }
  });
  calendar.render();
}

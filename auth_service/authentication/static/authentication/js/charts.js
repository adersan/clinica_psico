
let graficoStatus;
let graficoDias;

function atualizarGraficos(consultas) {
  if (!document.getElementById('graficoStatus')) return;

  if (graficoStatus) graficoStatus.destroy();
  if (graficoDias) graficoDias.destroy();

  const statusCount = {};
  const diaCount = {};

  consultas.forEach(c => {
    statusCount[c.status] = (statusCount[c.status] || 0) + 1;
    diaCount[c.data] = (diaCount[c.data] || 0) + 1;
  });

  graficoStatus = new Chart(document.getElementById('graficoStatus'), {
    type: 'pie',
    data: {
      labels: Object.keys(statusCount),
      datasets: [{
        label: 'Consultas por status',
        data: Object.values(statusCount),
        backgroundColor: ['#facc15', '#22d3ee', '#34d399', '#f87171']
      }]
    }
  });

  graficoDias = new Chart(document.getElementById('graficoDias'), {
    type: 'bar',
    data: {
      labels: Object.keys(diaCount),
      datasets: [{
        label: 'Consultas por dia',
        data: Object.values(diaCount),
        backgroundColor: '#3b82f6'
      }]
    }
  });
}

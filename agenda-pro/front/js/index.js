async function getAgendamentos() {
  const response = await fetch("http://127.0.0.1:8000/agendamentos");
  const agendamentos = await response.json();
  return agendamentos.agendamentos;
}

async function populateTable() {
  const agendamentos = await getAgendamentos();
  const tbody = document.querySelector("table tbody");

  agendamentos.forEach((agendamento) => {
    const tr = document.createElement("tr");
    tr.setAttribute("data-id", agendamento.id);

    const th = document.createElement("th");
    th.scope = "row";
    th.textContent = agendamento.id;
    tr.appendChild(th);

    const tdCliente = document.createElement("td");
    tdCliente.textContent = agendamento.cliente_nome;
    tr.appendChild(tdCliente);

    const tdServico = document.createElement("td");
    tdServico.textContent = agendamento.servico_nome;
    tr.appendChild(tdServico);

    const tdData = document.createElement("td");
    tdData.textContent = agendamento.data_atendimento ?? "N/A";
    tr.appendChild(tdData);

    const tdRetorno = document.createElement("td");
    tdRetorno.textContent = agendamento.retorno ?? "N/A";
    tr.appendChild(tdRetorno);

    const tdStatus = document.createElement("td");
    tdStatus.textContent = agendamento.status;
    tr.appendChild(tdStatus);

    const tdAcoes = document.createElement("td");
    tdAcoes.style = "display: flex; gap: 6px;";

    const btnEditar = document.createElement("a");
    btnEditar.href = "./edicao.html";
    btnEditar.className = "btn btn-primary";
    btnEditar.textContent = "Editar";
    btnEditar.onclick = () => editarAgendamento(agendamento.id);
    tdAcoes.appendChild(btnEditar);

    const btnApagar = document.createElement("button");
    btnApagar.className = "btn btn-danger";
    btnApagar.textContent = "Apagar";
    btnApagar.onclick = () => apagarAgendamento(agendamento.id);
    tdAcoes.appendChild(btnApagar);

    tr.appendChild(tdAcoes);

    tbody.appendChild(tr);
  });
}

function editarAgendamento(id) {
  localStorage.setItem("agendamentoId", id);
}

async function apagarAgendamento(id) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/agendamento/${id}`, {
      method: "DELETE",
    });

    if (response.ok) {
      document.querySelector(`tr[data-id='${id}']`).remove();
    } else {
      console.error(`Erro ao apagar agendamento ${id}`);
    }
  } catch (error) {
    console.error(`Erro ao apagar agendamento ${id}:`, error);
  }
}

populateTable();

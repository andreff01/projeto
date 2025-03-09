// async function getClientes() {
//   const response = await fetch("http://127.0.0.1:8000/clientes");
//   const clientes = await response.json();
//   return clientes.clientes;
// }

// async function getServicos() {
//   const response = await fetch("http://127.0.0.1:8000/servicos");
//   const servicos = await response.json();
//   return servicos.servicos;
// }

// async function getAgendamento(id) {
//   const response = await fetch(`http://127.0.0.1:8000/agendamento/${id}`);
//   const agendamento = await response.json();
//   return agendamento.agendamento;
// }

// async function atualizarAgendamento(id, data) {
//   const response = await fetch(`http://127.0.0.1:8000/agendamento/${id}`, {
//     method: "PUT",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(data),
//   });
//   return response.json();
// }

// async function main() {
//   const agendamentoId = localStorage.getItem("agendamentoId");
//   if (!agendamentoId) {
//     console.error("Nenhum ID de agendamento encontrado no localStorage");
//     return;
//   }

//   const agendamento = await getAgendamento(agendamentoId);
//   const clientes = await getClientes();
//   const servicos = await getServicos();

//   const selectClientes = document.getElementById("select-clientes");
//   const selectServicos = document.getElementById("select-servicos");

//   clientes.forEach((cliente) => {
//     const option = document.createElement("option");
//     option.textContent = cliente.nome + " - " + cliente.cpf_cnpj;
//     option.value = cliente.cpf_cnpj;
//     selectClientes.appendChild(option);
//   });

//   servicos.forEach((servico) => {
//     const option = document.createElement("option");
//     option.textContent = servico.tipo_servico;
//     option.value = servico.id;
//     selectServicos.appendChild(option);
//   });

//   selectClientes.value = agendamento.cliente_cpf_cnpj;
//   selectServicos.value = agendamento.servico_id;
//   document.getElementById("data-atendimento").value =
//     agendamento.data_atendimento;
//   document.getElementById("data-retorno").value = agendamento.retorno;
//   document.getElementById("valor").value = agendamento.valor;
//   document.getElementById("status").value = agendamento.status;
//   document.getElementById("observacoes").value = agendamento.observacoes;
// }

// document.addEventListener("DOMContentLoaded", main);

async function getClientes() {
  const response = await fetch("http://127.0.0.1:8000/clientes");
  const clientes = await response.json();
  return clientes.clientes;
}

async function getServicos() {
  const response = await fetch("http://127.0.0.1:8000/servicos");
  const servicos = await response.json();
  return servicos.servicos;
}

async function getAgendamento(id) {
  const response = await fetch(`http://127.0.0.1:8000/agendamento/${id}`);
  const agendamento = await response.json();
  return agendamento.agendamento;
}

async function atualizarAgendamento(id, data) {
  const response = await fetch(`http://127.0.0.1:8000/agendamento/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
}

async function main() {
  const agendamentoId = localStorage.getItem("agendamentoId");
  if (!agendamentoId) {
    console.error("Nenhum ID de agendamento encontrado no localStorage");
    return;
  }

  const agendamento = await getAgendamento(agendamentoId);
  const clientes = await getClientes();
  const servicos = await getServicos();

  const selectClientes = document.getElementById("select-clientes");
  const selectServicos = document.getElementById("select-servicos");

  clientes.forEach((cliente) => {
    const option = document.createElement("option");
    option.textContent = cliente.nome + " - " + cliente.cpf_cnpj;
    option.value = cliente.cpf_cnpj;
    selectClientes.appendChild(option);
  });

  servicos.forEach((servico) => {
    const option = document.createElement("option");
    option.textContent = servico.tipo_servico;
    option.value = servico.id;
    selectServicos.appendChild(option);
  });

  selectClientes.value = agendamento.cliente_cpf_cnpj;
  selectServicos.value = agendamento.servico_id;
  document.getElementById("data-atendimento").value =
    agendamento.data_atendimento;
  document.getElementById("data-retorno").value = agendamento.retorno;
  document.getElementById("valor").value = agendamento.valor;
  document.getElementById("status").value = agendamento.status;
  document.getElementById("status").textContent = agendamento.status;
  document.getElementById("observacoes").value = agendamento.observacoes;

  document
    .getElementById("form-agendamento")
    .addEventListener("submit", async (event) => {
      event.preventDefault();

      const agendamentoAtualizado = {
        status: document.getElementById("status").value,
        cliente_cpf_cnpj: selectClientes.value,
        servico_id: selectServicos.value,
        data_atendimento: document.getElementById("data-atendimento").value,
        retorno: document.getElementById("data-retorno").value,
        valor: document.getElementById("valor").value,
        observacoes: document.getElementById("observacoes").value,
      };

      console.log(agendamentoAtualizado);
      const result = await atualizarAgendamento(
        agendamentoId,
        agendamentoAtualizado
      );

      if (result.message) {
        console.log(result.message);
        alert("Agendamento atualizado com sucesso!");
        window.location.href = "./index.html";
      } else {
        alert("Erro ao atualizar agendamento.");
      }
    });
}

document.addEventListener("DOMContentLoaded", main);

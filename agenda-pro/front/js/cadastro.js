async function getAgendamentos() {
  const response = await fetch("http://127.0.0.1:8000/agendamentos");
  const agendamentos = await response.json();
  return agendamentos.agendamentos;
}

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

async function main() {
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
}

main();

document.querySelector("form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const clienteCpfCnpj = document.getElementById("select-clientes").value;
  const servicoId = document.getElementById("select-servicos").value;
  const dataAtendimento = document.getElementById("data-atendimento").value;
  const dataRetorno = document.getElementById("data-retorno").value;
  const valor = document.getElementById("valor").value;
  const status = document.getElementById("status").value;
  const observacoes = document.getElementById("observacoes").value;

  const agendamento = {
    cliente_cpf_cnpj: clienteCpfCnpj,
    servico_id: servicoId,
    data_atendimento: dataAtendimento || null,
    retorno: dataRetorno || null,
    valor: valor,
    status: status,
    observacoes: observacoes || null,
  };

  const response = await fetch("http://127.0.0.1:8000/agendamento", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(agendamento),
  });

  if (response.ok) {
    alert("Agendamento criado com sucesso!");
  } else {
    alert("Erro ao criar agendamento.");
  }
});

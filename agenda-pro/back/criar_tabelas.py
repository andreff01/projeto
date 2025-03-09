import asyncpg
import asyncio

user="postgres"
password="sql"
database="agendateste"
host="localhost"


async def criar_banco_de_dados():
    conn = await asyncpg.connect(user=user, password=password, database="postgres", host=host)
    await conn.execute(f"CREATE DATABASE {database}")
    await conn.close()


async def criar_schemas():
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)

    await conn.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            cpf_cnpj VARCHAR(18) PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            telefone VARCHAR(20) NOT NULL,
            email VARCHAR(100) UNIQUE,
            endereco TEXT,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    await conn.execute('''
        CREATE TABLE IF NOT EXISTS servicos (
            id SERIAL PRIMARY KEY,
            tipo_servico VARCHAR(100) NOT NULL,
            descricao VARCHAR(255) NOT NULL,
            valor DECIMAL(10,2) NOT NULL
        );
    ''')

    await conn.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id SERIAL PRIMARY KEY,
            cliente_cpf_cnpj VARCHAR(18) NOT NULL,
            servico_id INT NOT NULL,
            data_atendimento TIMESTAMP NULL,
            retorno TIMESTAMP NULL,
            valor DECIMAL(10,2) NOT NULL,
            status VARCHAR(20) DEFAULT 'Disponível',
            observacoes TEXT,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cliente_cpf_cnpj) REFERENCES clientes(cpf_cnpj) ON DELETE CASCADE,
            FOREIGN KEY (servico_id) REFERENCES servicos(id) ON DELETE CASCADE
        );
    ''')

    await conn.execute('''
        INSERT INTO clientes (cpf_cnpj, nome, telefone, email, endereco)
        VALUES
        ('12345678901', 'João Silva', '11987654321', 'joao.silva@example.com', 'Rua das Flores, 123'),
        ('23456789012', 'Maria Oliveira', '21987654321', 'maria.oliveira@example.com', 'Avenida Brasil, 456'),
        ('34567890123', 'Carlos Pereira', '31987654321', 'carlos.pereira@example.com', 'Praça da Sé, 789'),
        ('45678901234', 'Ana Souza', '41987654321', 'ana.souza@example.com', 'Rua das Palmeiras, 101'),
        ('56789012345', 'Pedro Santos', '51987654321', 'pedro.santos@example.com', 'Avenida Paulista, 202'),
        ('67890123456', 'Lucas Lima', '61987654321', 'lucas.lima@example.com', 'Rua das Acácias, 303'),
        ('78901234567', 'Mariana Costa', '71987654321', 'mariana.costa@example.com', 'Avenida Atlântica, 404'),
        ('89012345678', 'Fernanda Almeida', '81987654321', 'fernanda.almeida@example.com', 'Rua das Hortênsias, 505'),
        ('90123456789', 'Ricardo Gomes', '91987654321', 'ricardo.gomes@example.com', 'Praça da Liberdade, 606'),
        ('01234567890', 'Juliana Ferreira', '21987654322', 'juliana.ferreira@example.com', 'Avenida Central, 707');
    ''')

    await conn.execute('''
        INSERT INTO servicos (tipo_servico, descricao, valor)
        VALUES 
        ('Corte de Cabelo', 'Corte de cabelo masculino ou feminino', 50.00),
        ('Manicure', 'Serviço de manicure completo', 30.00),
        ('Massagem Relaxante', 'Sessão de massagem relaxante de 1 hora', 100.00),
        ('Pedicure', 'Serviço de pedicure completo', 35.00),
        ('Depilação', 'Serviço de depilação a laser', 150.00),
        ('Limpeza de Pele', 'Sessão de limpeza de pele profunda', 80.00),
        ('Maquiagem', 'Serviço de maquiagem para eventos', 120.00),
        ('Design de Sobrancelhas', 'Design e modelagem de sobrancelhas', 40.00),
        ('Tratamento Capilar', 'Tratamento de hidratação capilar', 90.00),
        ('Escova Progressiva', 'Alisamento capilar com escova progressiva', 200.00);
    ''')

    await conn.close()

if __name__ == "__main__":
    asyncio.run(criar_banco_de_dados())
    asyncio.run(criar_schemas())

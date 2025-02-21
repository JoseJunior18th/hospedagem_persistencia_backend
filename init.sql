CREATE TABLE IF NOT EXISTS (
    id SERIAL PRIMARY KEY,
    categoria VARCHAR(255),
    classificacao VARCHAR(255),
    descricao VARCHAR(255),
    horas VARCHAR(10),
    horas_aproveitadas VARCHAR(10)
)
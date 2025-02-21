CREATE TABLE IF NOT EXISTS activities (
    id SERIAL PRIMARY KEY,
    categoria VARCHAR(255),
    classificacao VARCHAR(255),
    descricao VARCHAR(255),
    horas VARCHAR(10),
    horas_aproveitadas VARCHAR(10)
);

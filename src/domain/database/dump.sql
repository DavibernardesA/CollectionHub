CREATE DATABASE collectionhub;                                       -- Nome do banco de dados

CREATE TABLE users (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),      -- ID único para identificar cada usuário
    name            VARCHAR(100) NOT NULL,                           -- Nome do usuário
    email           VARCHAR(255) UNIQUE NOT NULL,                    -- Email do usuário, único e obrigatório
    password        TEXT         NOT NULL,                           -- Senha do usuário
    account_type    VARCHAR(20)  NOT NULL,                           -- Tipo de conta: "admin" ou "user"
    created_at      TIMESTAMP    DEFAULT  NOT NULL,                  -- Data de criação
    updated_at      TIMESTAMP    DEFAULT  NOT NULL                   -- Data de atualização

);
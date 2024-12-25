-- Habilitar extensão para UUID
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Criar tabela `users`
CREATE TABLE users (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),      -- ID único para identificar cada usuário
    name            VARCHAR(100) NOT NULL,                           -- Nome do usuário
    email           VARCHAR(255) UNIQUE NOT NULL,                    -- Email do usuário, único e obrigatório
    password        TEXT NOT NULL,                                   -- Senha do usuário
    account_type    VARCHAR(20) NOT NULL,                            -- Tipo de conta: "admin" ou "user"
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,    -- Data de criação
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL     -- Data de atualização
);

-- Criar tabela `collections`
CREATE TABLE collections (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),      -- ID único para identificar cada coleção
    name              VARCHAR(255) NOT NULL,                           -- Nome da coleção
    item_count        INTEGER NOT NULL,                               -- Contagem de itens na coleção
    custom_attributes JSONB NOT NULL,                                  -- Atributos personalizados, armazenados em formato JSON
    likes             INTEGER NOT NULL DEFAULT 0,                      -- Número de curtidas
    favorites         INTEGER NOT NULL DEFAULT 0,                      -- Número de favoritos
    followers         INTEGER NOT NULL DEFAULT 0,                      -- Número de seguidores
    status            VARCHAR(20) NOT NULL,                            -- Status da coleção
    created_by        TEXT NOT NULL,                                   -- ID do usuário que criou a coleção
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,    -- Data de criação
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,    -- Data de última atualização
    deleted_at        TIMESTAMP,                                      -- Data de deleção (se aplicável)
    errors            JSONB NOT NULL DEFAULT '[]'::JSONB               -- Erros registrados (se houver)
);
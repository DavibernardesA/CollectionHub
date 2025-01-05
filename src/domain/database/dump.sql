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
    item_count        INTEGER NOT NULL,                                -- Contagem de itens na coleção
    custom_attributes JSONB NOT NULL DEFAULT '[]'::JSONB,              -- Atributos personalizados, armazenados em formato JSON
    likes             INTEGER NOT NULL DEFAULT 0,                      -- Número de curtidas
    favorites         INTEGER NOT NULL DEFAULT 0,                      -- Número de favoritos
    followers         INTEGER NOT NULL DEFAULT 0,                      -- Número de seguidores
    status            VARCHAR(20) NOT NULL,                            -- Status da coleção
    created_by        TEXT NOT NULL,                                   -- ID do usuário que criou a coleção
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,    -- Data de criação
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,    -- Data de última atualização
    deleted_at        TIMESTAMP,                                       -- Data de deleção (se aplicável)
    errors            JSONB NOT NULL DEFAULT '[]'::JSONB               -- Erros registrados (se houver)
);

-- Criar tabela `locks`
CREATE TABLE locks (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),      -- ID único para identificar cada bloqueio
    collection_id     UUID NOT NULL                                    -- ID da coleção bloqueada
);

-- Criar tabela `flf_collections`
CREATE TABLE flf_collections (
    account_id        TEXT NOT NULL,                                    -- ID do usuário que realizou uma ação
    action            TEXT NOT NULL,                                    -- Ação do usuário
    collection_id     TEXT NOT NULL                                    -- ID da coleção que recebeu a ação
);

-- Criar tabela `flf_items`
CREATE TABLE flf_items (
    account_id        TEXT NOT NULL,                                    -- ID do usuário que realizou uma ação
    action            TEXT NOT NULL,                                    -- Ação do usuário
    item_id           TEXT NOT NULL                                    -- ID do item que recebeu a ação
);

-- Criar tabela `items`
CREATE TABLE items (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),      -- ID único para identificar cada item
    collection_id     UUID NOT NULL,                                   -- ID da coleção a qual o item pertence
    attributes        JSONB NOT NULL,                                  -- Atributos do item, armazenados em formato JSON
    likes             INTEGER NOT NULL DEFAULT 0,                      -- Número de curtidas
    views             INTEGER NOT NULL DEFAULT 0,                      -- Número de visualizações
    visibility        BOOLEAN NOT NULL DEFAULT true,                   -- Visibilidade do item
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,    -- Data de criação
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL     -- Data de última atualização
);
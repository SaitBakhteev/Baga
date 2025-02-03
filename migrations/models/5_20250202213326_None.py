from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "gym" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "info" TEXT NOT NULL,
    "show_location" TEXT
);
CREATE TABLE IF NOT EXISTS "event" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "training_type" VARCHAR(64) NOT NULL,
    "date" DATE NOT NULL,
    "begin" TIMETZ NOT NULL,
    "end" TIMETZ NOT NULL,
    "participants_count" INT NOT NULL  DEFAULT 18,
    "gym_id" INT NOT NULL REFERENCES "gym" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "tg_id" BIGINT NOT NULL,
    "tg_username" VARCHAR(64),
    "tg_name" VARCHAR(64),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "admin_permissions" BOOL NOT NULL  DEFAULT False
);
CREATE TABLE IF NOT EXISTS "EventUser" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "paid_check" VARCHAR(4),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "payment_confirmed" BOOL,
    "event_id" INT NOT NULL REFERENCES "event" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """

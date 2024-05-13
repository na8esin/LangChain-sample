CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> dfebef2f0749

CREATE TABLE products (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(50) NOT NULL, 
    description VARCHAR(200), 
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('dfebef2f0749');


CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    domain VARCHAR(100)
);

INSERT INTO employees (name, domain)
VALUES
('spk', 'DevOps'),
('siva', 'Backend'),
('Manoj', 'Frontend');

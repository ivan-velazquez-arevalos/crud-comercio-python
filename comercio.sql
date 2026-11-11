CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    ciudad VARCHAR(50),
    fecha_alta DATE DEFAULT CURRENT_DATE
);

CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(12,2) NOT NULL,
    stock INTEGER DEFAULT 0
);

CREATE TABLE pedidos (
    id_pedido SERIAL PRIMARY KEY,
    id_cliente INTEGER REFERENCES clientes (id_cliente),
    id_producto INTEGER REFERENCES productos (id_producto),
    cantidad INTEGER NOT NULL,
    fecha DATE DEFAULT CURRENT_DATE
);

SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
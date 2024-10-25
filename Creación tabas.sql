USE desarrollo;

CREATE TABLE ordenes (
    idOrden INT AUTO_INCREMENT PRIMARY KEY,
    idCliente INT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    estado ENUM('pendiente', 'completada', 'cancelada') NOT NULL,
    fechaOrden TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE compras (
    idCompra INT AUTO_INCREMENT PRIMARY KEY,
    idOrden INT NOT NULL,
    idProducto INT NOT NULL,
    cantidad INT NOT NULL,
    precioUnitario DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) AS (cantidad * precioUnitario),
    fechaCompra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (idOrden) REFERENCES ordenes(idOrden)
);

CREATE TABLE ventas (
    idVenta INT AUTO_INCREMENT PRIMARY KEY,
    idOrden INT NOT NULL,
    idProducto INT NOT NULL,
    cantidad INT NOT NULL,
    precioUnitario DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) AS (cantidad * precioUnitario),
    fechaVenta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (idOrden) REFERENCES ordenes(idOrden)
);


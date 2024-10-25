USE desarrollo;

INSERT INTO ordenes (idCliente, total, estado) 
VALUES 
(1, 50.00, 'pendiente'),
(2, 75.50, 'completada'),
(3, 120.00, 'cancelada'),
(4, 85.75, 'pendiente');


INSERT INTO compras (idOrden, idProducto, cantidad, precioUnitario) 
VALUES 
(1, 101, 2, 25.00),
(2, 102, 1, 75.50),
(2, 103, 3, 15.00),
(3, 101, 4, 30.00),
(4, 104, 1, 85.75);


INSERT INTO ventas (idOrden, idProducto, cantidad, precioUnitario) 
VALUES 
(2, 102, 1, 75.50),
(2, 103, 3, 15.00),
(4, 104, 1, 85.75);

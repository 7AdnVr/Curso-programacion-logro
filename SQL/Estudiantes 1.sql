CREATE TABLE estudiantes (
    cedula INT PRIMARY KEY,
    nombre VARCHAR(50),
    segundo_nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo VARCHAR(100),
    edad INT,
    pelicula_favorita VARCHAR(100)
);

INSERT INTO Estudiantes (cedula, nombre, segundo_nombre, apellido, correo, edad, pelicula_favorita) 
VALUES
(31096641 , 'Jose', 'Angel', 'Franco', 'josefranber2609@gmail.com', 21, 'Rey leon'),
(32577415, 'Javier', 'Medina', 'Alejandro', 'javiermedina@gmail.com', 17, 'Thor'),
(33104854, 'Alan', 'Hernandez', 'David', 'alan.hernandez3310@gmail.com', 17, 'Spiderman: a través del multiverso'),
(31989067, 'Adrian', 'Jesus', 'Vera', 'abokase4706@gmail.com', 20, 'Avengers: End Game');

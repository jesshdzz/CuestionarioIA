drop table if exists alumnos;
drop table if exists profesores;
drop table if exists cuestionarios;
drop table if exists preguntas;
drop table if exists respuestas;

CREATE TABLE alumnos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    contrasena VARCHAR(255),
    grupo VARCHAR(20),
    grado INT,
    calificacion_total FLOAT

);

CREATE TABLE profesores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    contrasena VARCHAR(255)
);

CREATE TABLE cuestionarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    profesor_id INT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (profesor_id) REFERENCES profesores(id)
);

CREATE TABLE preguntas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cuestionario_id INT,
    tipo ENUM('opcion_multiple', 'abierta'),
    contenido TEXT,
    opciones JSON, -- Solo para opción múltiple
    respuesta_correcta TEXT,
    FOREIGN KEY (cuestionario_id) REFERENCES cuestionarios(id)
);

CREATE TABLE respuestas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pregunta_id INT,
    alumno_id INT,
    respuesta TEXT,
    calificacion FLOAT,
    FOREIGN KEY (pregunta_id) REFERENCES preguntas(id),
    FOREIGN KEY (alumno_id) REFERENCES alumnos(id)
);

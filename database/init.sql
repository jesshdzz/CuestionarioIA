drop table if exists Alumno;
drop table if exists Profesor;
drop table if exists Cuestionario;
drop table if exists Pregunta;
drop table if exists Respuesta;

CREATE TABLE Alumno (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    contrasena VARCHAR(255),
    grupo VARCHAR(20),
    grado INT,
    calificacion_total FLOAT

);

CREATE TABLE Profesor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    contrasena VARCHAR(255)
);

CREATE TABLE Cuestionario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    profesor_id INT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (profesor_id) REFERENCES profesor(id)
);

CREATE TABLE Pregunta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cuestionario_id INT,
    tipo ENUM('opcion_multiple', 'abierta'),
    contenido TEXT,
    opciones JSON, -- Solo para opción múltiple
    respuesta_correcta TEXT,
    FOREIGN KEY (cuestionario_id) REFERENCES cuestionario(id)
);

CREATE TABLE Respuesta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pregunta_id INT,
    alumno_id INT,
    respuesta TEXT,
    calificacion FLOAT,
    FOREIGN KEY (pregunta_id) REFERENCES pregunta(id),
    FOREIGN KEY (alumno_id) REFERENCES alumno(id)
);

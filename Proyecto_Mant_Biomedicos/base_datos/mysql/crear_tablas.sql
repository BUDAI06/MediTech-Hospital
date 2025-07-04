CREATE DATABASE IF NOT EXISTS PF_Informatica1;
USE PF_Informatica1;

CREATE TABLE usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol ENUM('Administrador','Ingeniero','Tecnico') NOT NULL
);

CREATE TABLE tecnicos (
    tecnico_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100),
    cedula_profesional VARCHAR(30),
    contacto VARCHAR(100)
);

CREATE TABLE equipos (
    equipo_id VARCHAR(20) PRIMARY KEY,
    nombre_equipo VARCHAR(100) NOT NULL,
    tipo VARCHAR(50),
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ubicacion VARCHAR(100),
    fecha_ingreso DATE,
    estado_actual VARCHAR(50)
);

CREATE TABLE mantenimientos (
    mmto_id INT AUTO_INCREMENT PRIMARY KEY,
    equipo_id VARCHAR(20),
    tecnico_id INT,
    tipo_mmto ENUM('Preventivo','Correctivo'),
    fecha_mmto DATE,
    duracion_mmto INT,
    observaciones TEXT,
    FOREIGN KEY (equipo_id) REFERENCES equipos(equipo_id),
    FOREIGN KEY (tecnico_id) REFERENCES tecnicos(tecnico_id)
);

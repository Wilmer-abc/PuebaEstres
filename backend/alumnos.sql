-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-02-2025 a las 04:51:07
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ingenieria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `id` int(11) NOT NULL,
  `carnet1` varchar(4) NOT NULL,
  `carnet2` varchar(3) NOT NULL,
  `carnet3` varchar(4) NOT NULL,
  `PrimerNombre` varchar(50) NOT NULL,
  `SegundoNombre` varchar(50) DEFAULT NULL,
  `primerApellido` varchar(50) NOT NULL,
  `segundoApellido` varchar(50) DEFAULT NULL,
  `Telefono` varchar(15) DEFAULT NULL,
  `CorreoElectronico` varchar(100) DEFAULT NULL,
  `Pagado` enum('Sí','No') NOT NULL,
  `FechaNacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`id`, `carnet1`, `carnet2`, `carnet3`, `PrimerNombre`, `SegundoNombre`, `primerApellido`, `segundoApellido`, `Telefono`, `CorreoElectronico`, `Pagado`, `FechaNacimiento`) VALUES
(3, '1490', '21', '1456', 'edvin ', 'evaraldo', 'de leon ', 'say', '90123456', 'edvin1@gmail.com', 'Sí', '2003-08-10'),
(4, '1490', '21', '1414', 'josue', 'david', 'lopez', 'lopez', '12345612', 'lopez@gmail.com', 'No', '1998-09-01'),
(5, '1490', '21', '1412', 'dany', 'francisco', 'sacaxol', 'aj', '90781234', 'dany12@gmail.com', 'No', '2001-11-11'),
(7, '1490', '20', '0123', 'pablo', 'emilio', 'escobar', 'peralta', '77889900', 'escobar10@gmail.com', 'Sí', '1998-05-10'),
(8, '1490', '24', '1214', 'sandra', 'paola', 'canastujo', 'menchu', '77110021', 'sandra00@gmail.com', 'Sí', '2003-12-15'),
(9, '1490', '21', '1477', 'Wilmer', 'Admidael', 'Batz', 'Chaclan', '19181716', 'wilmer1@gmail.com', 'No', '2001-04-15');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-01-2021 a las 17:18:43
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `searchflix`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recomendar`
--

CREATE TABLE `recomendar` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `poster` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `rating` float(2,1) NOT NULL,
  `genero` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `duracion` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `trama` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `director` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `escritor` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `recomendar`
--

INSERT INTO `recomendar` (`id`, `titulo`, `poster`, `rating`, `genero`, `duracion`, `trama`, `director`, `escritor`) VALUES
(111161, 'The Shawshank Redemption (1994)', 'https://image.tmdb.org/t/p/w342/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg', 9.3, 'Drama', '2h 22m', 'Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne c', 'Frank Darabont', 'Stephen King'),
(167260, 'The Lord of the Rings: The Return of the King (2003)', 'https://image.tmdb.org/t/p/w342/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg', 8.9, 'Action, Adventure, Drama, Fantasy', '3h 21m', 'Aragorn is revealed as the heir to the ancient kings as he, Gandalf and the other members of the broken fellowship struggle to save Gondor from Sauron\'s forces. Meanwhile, Frodo and Sam take the ring closer to the heart of Mordor, the dark lord\'s realm.', 'Peter Jackson', 'J.R.R. Tolkien'),
(468569, 'The Dark Knight (2008)', 'https://image.tmdb.org/t/p/w342/qJ2tW6WMUDux911r6m7haRef0WH.jpg', 9.0, 'Action, Crime, Drama, Thriller', '2h 32m', 'Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they so', 'Christopher Nolan', 'Jonathan Nolan');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitadas`
--

CREATE TABLE `visitadas` (
  `id` int(11) NOT NULL,
  `long_titulo` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `titulo` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `rating` float(2,1) NOT NULL,
  `generos` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `duracion` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `director` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `escritor` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `trama` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `cover` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `visitadas`
--

INSERT INTO `visitadas` (`id`, `long_titulo`, `titulo`, `rating`, `generos`, `duracion`, `director`, `escritor`, `trama`, `cover`) VALUES
(71562, 'The Godfather: Part II (1974)', 'The Godfather: Part II', 9.0, 'Crime, Drama', '3h 22m', 'Francis Ford Coppola', 'Francis Ford Coppola', 'In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York. In the 1950s, Michael Corleone attempts to expand the family business into Las Vegas, Hollywood and Cuba.', 'https://image.tmdb.org/t/p/w342/hek3koDUyRQk7FIhPXsa6mT2Zc3.jpg'),
(468569, 'The Dark Knight (2008)', 'The Dark Knight', 9.0, 'Action, Crime, Drama, Thriller', '2h 32m', 'Christopher Nolan', 'Jonathan Nolan', 'Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.', 'https://image.tmdb.org/t/p/w342/qJ2tW6WMUDux911r6m7haRef0WH.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `recomendar`
--
ALTER TABLE `recomendar`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

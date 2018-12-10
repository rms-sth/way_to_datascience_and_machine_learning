-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2018 at 08:50 AM
-- Server version: 10.1.33-MariaDB
-- PHP Version: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ktmlist-official`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `gender` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `contact` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `facebook_url` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `twitter_url` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `linkedin_url` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `google_url` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `verifyToken` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '0',
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `image`, `email`, `password`, `gender`, `address`, `username`, `contact`, `facebook_url`, `twitter_url`, `linkedin_url`, `google_url`, `verifyToken`, `status`, `remember_token`, `created_at`, `updated_at`) VALUES
(1, 'Manish Basnyat', NULL, 'manishbasnyat182@gmail.com', '$2y$10$k6UbClXDSy6oYuxxzpWR6uG5lwPcLk9kv3CNyWE7WXYWMMvYO5r6.', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '6683', 1, 'sxoIOW7q3DhZC14fu2dIWK5ObWxoy4mN2Au49ZYfrFw8ha13uBJFkhI0gC05', '2018-11-20 01:46:17', '2018-11-20 01:46:17'),
(2, 'Seeder2 Sapkota', NULL, 'seeder2sapkota@gmail.com', '$2y$10$YXIRGFplgA4NGsEg5/F2Qu/GDIlUBZ9DVIU0pkgv2PZp2XIsCBXXa', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3453', 1, 'qqkjvgJPiG0kTZfnH6qBTWTIdXXCKPmF6ayQTOjwPtNPx3Q19uW9kSnGDza3', '2018-11-20 01:46:18', '2018-11-20 01:46:18'),
(3, 'Seeder2 Singh', NULL, 'seeder3singh@gmail.com', '$2y$10$2cDsOcjx5K/pjfVeGrokeeKaf7LekvfXJyopXdEVPNWyGB9ugMZXW', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3540', 1, NULL, '2018-11-20 01:46:18', '2018-11-20 01:46:18');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customers_email_unique` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

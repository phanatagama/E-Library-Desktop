-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2021 at 04:51 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `judul` varchar(100) NOT NULL,
  `pengarang` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL,
  `tahun` year(4) NOT NULL,
  `rak` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `judul`, `pengarang`, `penerbit`, `tahun`, `rak`) VALUES
(2, 'Dilan 1998', 'Joko Widodo', 'PT. Gramedia', 2018, 1),
(4, 'Komik One Piece', 'Eichiiro Oda', 'Shueisha', 1998, 5),
(5, 'Harry Potter', 'J.K. Rowling', 'Warner Bross', 2005, 1),
(7, 'Cerita Rakyat', 'David', 'PT. Gadgetin', 2016, 2),
(8, 'Secangkir Kopi', 'Uut Dwisetya', 'Jawa Pos', 2017, 1),
(9, '7 Keajaiban Rezeki', 'Ippho Santosa', 'Gramedia', 2010, 3),
(13, 'Belajar Pemrograman', 'Aga', 'univ', 2020, 4),
(16, 'Matematika', 'Rizal', 'Pahlevi', 2010, 5),
(19, 'naruto', 'masashi kisimoto', 'shueisha', 2002, 21),
(20, 'buku baru', 'asd', 'ddda', 0000, 2),
(21, 'Menuai Benih Padi', 'Rano Karno', 'Solo Book', 2014, 4);

-- --------------------------------------------------------

--
-- Table structure for table `borrow`
--

CREATE TABLE `borrow` (
  `id` int(11) NOT NULL,
  `id_buku` int(11) NOT NULL,
  `id_students` int(11) NOT NULL,
  `id_staff` int(11) NOT NULL,
  `tanggal_pinjam` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `borrow`
--

INSERT INTO `borrow` (`id`, `id_buku`, `id_students`, `id_staff`, `tanggal_pinjam`) VALUES
(88, 7, 2, 1, '2021-05-27'),
(89, 7, 1, 1, '2021-05-27');

--
-- Triggers `borrow`
--
DELIMITER $$
CREATE TRIGGER `inserttriwayatpeminjaman` AFTER INSERT ON `borrow` FOR EACH ROW INSERT INTO riwayatpeminjaman SET
id_buku=NEW.id_buku, id_students=NEW.id_students, id_staff=NEW.id_staff, tanggal_pinjam=NEW.tanggal_pinjam,
id_borrow=NEW.id
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `pengembalian`
--

CREATE TABLE `pengembalian` (
  `id` int(11) NOT NULL,
  `id_borrow` int(11) NOT NULL,
  `tanggal_kembali` date NOT NULL,
  `denda` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengembalian`
--

INSERT INTO `pengembalian` (`id`, `id_borrow`, `tanggal_kembali`, `denda`) VALUES
(1, 40, '2021-05-25', 0),
(2, 41, '2021-05-25', 0),
(3, 58, '2021-05-27', 0),
(4, 60, '2021-05-27', 0),
(5, 59, '2021-05-27', 0),
(6, 61, '2021-05-27', 0),
(7, 62, '2021-05-27', 0),
(8, 64, '2021-05-27', 0),
(9, 63, '2021-05-27', 0),
(10, 65, '2021-05-27', 0),
(11, 66, '2021-05-27', 0),
(12, 67, '2021-05-27', 0),
(13, 68, '2021-05-27', 0),
(14, 69, '2021-05-27', 0),
(15, 70, '2021-05-27', 0),
(16, 71, '2021-05-27', 0),
(17, 72, '2021-05-27', 0),
(18, 73, '2021-05-27', 0),
(21, 76, '2021-05-27', 0),
(22, 77, '2021-05-27', 0),
(23, 78, '2021-05-27', 0),
(24, 79, '2021-05-27', 0),
(25, 80, '2021-05-27', 0),
(26, 81, '2021-05-27', 0),
(27, 82, '2021-05-27', 0),
(28, 84, '2021-05-27', 0),
(29, 85, '2021-05-27', 0),
(30, 86, '2021-05-27', 0),
(31, 87, '2021-05-27', 0),
(32, 83, '2021-05-27', 0);

-- --------------------------------------------------------

--
-- Table structure for table `riwayatpeminjaman`
--

CREATE TABLE `riwayatpeminjaman` (
  `id` int(11) NOT NULL,
  `id_borrow` int(11) NOT NULL,
  `id_buku` int(11) NOT NULL,
  `id_students` int(11) NOT NULL,
  `id_staff` int(11) NOT NULL,
  `tanggal_pinjam` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `riwayatpeminjaman`
--

INSERT INTO `riwayatpeminjaman` (`id`, `id_borrow`, `id_buku`, `id_students`, `id_staff`, `tanggal_pinjam`) VALUES
(14, 0, 9, 2, 1, '2020-12-27'),
(15, 0, 4, 1, 1, '2020-12-27'),
(16, 0, 10, 1, 1, '2020-12-27'),
(17, 0, 13, 1, 1, '2020-12-30'),
(18, 0, 13, 1, 1, '2021-01-02'),
(19, 0, 2, 2, 1, '2021-01-02'),
(20, 40, 9, 1, 1, '2021-05-25'),
(21, 41, 13, 2, 1, '2021-05-25'),
(22, 58, 5, 2, 1, '2021-05-27'),
(23, 59, 4, 1, 1, '2021-05-27'),
(24, 60, 2, 2, 1, '2021-05-27'),
(25, 61, 8, 2, 1, '2021-05-27'),
(26, 62, 2, 1, 1, '2021-05-27'),
(27, 63, 13, 2, 1, '2021-05-27'),
(28, 64, 7, 1, 1, '2021-05-27'),
(29, 65, 2, 1, 1, '2021-05-27'),
(30, 66, 8, 2, 1, '2021-05-27'),
(31, 67, 13, 1, 1, '2021-05-27'),
(32, 68, 7, 2, 1, '2021-05-27'),
(33, 69, 2, 1, 1, '2021-05-27'),
(34, 70, 7, 2, 1, '2021-05-27'),
(35, 71, 8, 1, 1, '2021-05-27'),
(36, 72, 13, 2, 2, '2021-05-27'),
(37, 73, 13, 2, 1, '2021-05-27'),
(38, 74, 2, 1, 1, '2021-05-27'),
(39, 75, 7, 2, 2, '2021-05-27'),
(40, 76, 2, 1, 1, '2021-05-27'),
(41, 77, 7, 2, 1, '2021-05-27'),
(42, 78, 13, 1, 1, '2021-05-27'),
(43, 79, 7, 2, 1, '2021-05-27'),
(44, 80, 13, 1, 2, '2021-05-27'),
(45, 81, 13, 1, 2, '2021-05-27'),
(46, 82, 4, 2, 1, '2021-05-27'),
(47, 83, 4, 1, 2, '2021-05-27'),
(48, 84, 13, 2, 2, '2021-05-27'),
(49, 85, 13, 2, 1, '2021-05-27'),
(50, 86, 8, 2, 2, '2021-05-27'),
(51, 87, 7, 2, 1, '2021-05-27'),
(52, 88, 7, 2, 1, '2021-05-27'),
(53, 89, 7, 1, 1, '2021-05-27');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `nip` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `pass` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id`, `nama`, `nip`, `email`, `contact`, `alamat`, `pass`) VALUES
(1, 'Hendra', '232456', 'hendra@gmail.com', '081523499778', 'Jl. Jawa 7 - Jember', 'abc12345'),
(2, 'Joko', '1981050219980502', 'joko@yahoo.com', '083847317655', 'Jalan Tunggul Ametung, Sobo - Brawijaya , Banyuwangi', 'jokowi');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `nim` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `alamat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `nama`, `nim`, `email`, `contact`, `alamat`) VALUES
(1, 'Afif Nurrudin', '192410102039', 'afif.nrd@gmail.com', '087755657123', 'Jl. Kalimantan 10 - Jember'),
(2, 'Ade Londok', '172410101009', 'ade.londok@gmail.com', '083847317655', 'Jl. Sukorambi No. 7');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `borrow`
--
ALTER TABLE `borrow`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_buku` (`id_buku`),
  ADD KEY `id_staff` (`id_staff`),
  ADD KEY `id_students` (`id_students`) USING BTREE;

--
-- Indexes for table `pengembalian`
--
ALTER TABLE `pengembalian`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `riwayatpeminjaman`
--
ALTER TABLE `riwayatpeminjaman`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `borrow`
--
ALTER TABLE `borrow`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=90;

--
-- AUTO_INCREMENT for table `pengembalian`
--
ALTER TABLE `pengembalian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `riwayatpeminjaman`
--
ALTER TABLE `riwayatpeminjaman`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `borrow`
--
ALTER TABLE `borrow`
  ADD CONSTRAINT `borrow_ibfk_1` FOREIGN KEY (`id_buku`) REFERENCES `books` (`id`),
  ADD CONSTRAINT `borrow_ibfk_2` FOREIGN KEY (`id_students`) REFERENCES `students` (`id`),
  ADD CONSTRAINT `borrow_ibfk_3` FOREIGN KEY (`id_staff`) REFERENCES `staff` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

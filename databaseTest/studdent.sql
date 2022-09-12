-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2022 at 03:16 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Student_ID` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Course` varchar(50) NOT NULL,
  `Year` varchar(50) NOT NULL,
  `Semester` varchar(50) NOT NULL,
  `Division` varchar(50) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `DOB` varchar(50) NOT NULL,
  `Mobile_No` decimal(50,0) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Roll_No` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Teacher_Name` varchar(50) NOT NULL,
  `PhotoSample` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Student_ID`, `Name`, `Department`, `Course`, `Year`, `Semester`, `Division`, `Gender`, `DOB`, `Mobile_No`, `Address`, `Roll_No`, `Email`, `Teacher_Name`, `PhotoSample`) VALUES
('1', 'M Sajan', 'CS', 'MLP', '2019', 'Project Level', 'Evening', 'Male', '2002-07-17', '3030302783', 'Hyderabad', '2k19/MLP/1', 'sajan@gmail.com', 'Kashif', 'Yes'),
('2', 'Kashif', 'CS', 'MLP', '2019', 'Project Level', 'Morning', 'Male', '1995-07-12', '3124532102', 'kotri', '2k19/MLP/2', 'kashif@gmail.com', 'Imtain Ali', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Student_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

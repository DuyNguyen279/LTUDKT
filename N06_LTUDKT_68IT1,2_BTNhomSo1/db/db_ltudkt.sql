-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: lttkud
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `inservicestudent`
--

DROP TABLE IF EXISTS `inservicestudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inservicestudent` (
  `student_id` varchar(45) COLLATE utf8mb3_bin NOT NULL,
  `scores` float DEFAULT '0',
  `job` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  CONSTRAINT `fk_inservice` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inservicestudent`
--

LOCK TABLES `inservicestudent` WRITE;
/*!40000 ALTER TABLE `inservicestudent` DISABLE KEYS */;
INSERT INTO `inservicestudent` VALUES ('SV2',7.5,'Giáo viên THCS'),('SV4',8,'Kỹ sư Hóa học');
/*!40000 ALTER TABLE `inservicestudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regularstudent`
--

DROP TABLE IF EXISTS `regularstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regularstudent` (
  `student_id` varchar(45) COLLATE utf8mb3_bin NOT NULL,
  `gpa` float DEFAULT '0',
  `credit` int DEFAULT '15',
  PRIMARY KEY (`student_id`),
  CONSTRAINT `fk_regulars` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regularstudent`
--

LOCK TABLES `regularstudent` WRITE;
/*!40000 ALTER TABLE `regularstudent` DISABLE KEYS */;
INSERT INTO `regularstudent` VALUES ('SV1',15,0),('SV3',3.8,110),('SV5',2.9,75);
/*!40000 ALTER TABLE `regularstudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` varchar(45) COLLATE utf8mb3_bin NOT NULL,
  `name` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `department` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `type` varchar(45) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('SV1','Nguyễn Việt Anh','2001-04-17','Computer Science','Regular'),('SV2','Trần Thị Bình','2006-11-22','Mathematics','InService'),('SV3','Lê Văn Cường','2001-02-10','Physics','Regular'),('SV4','Phạm Thị Dung','1998-08-30','Chemistry','InService'),('SV5','Hoàng Văn Đông','2000-12-05','Biology','Regular');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-09 19:34:08

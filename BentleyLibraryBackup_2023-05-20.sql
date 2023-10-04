-- MySQL dump 10.13  Distrib 8.0.32, for macos12.6 (arm64)
--
-- Host: localhost    Database: BentleyLibrary
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookinventory`
--

DROP TABLE IF EXISTS `bookinventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookinventory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `isbn` varchar(13) NOT NULL,
  `published_date` date NOT NULL,
  `publisher` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `available_quantity` int NOT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookinventory`
--

LOCK TABLES `bookinventory` WRITE;
/*!40000 ALTER TABLE `bookinventory` DISABLE KEYS */;
INSERT INTO `bookinventory` VALUES (1,'The Great Gatsby','F. Scott Fitzgerald','9780743273565','2004-09-30','Simon and Schuster',1,0,'A young man newly rich tries to recapture the past and win back his former love, despite the fact that she has married.'),(2,'The Great Gatsby','F. Scott Fitzgerald','9780743273565','2004-09-30','Simon and Schuster',1,1,'A young man newly rich tries to recapture the past and win back his former love, despite the fact that she has married.'),(3,'Novos Contextos De Introdução Á Psicologia','Apolenário Portugal','0123456789','1900-01-01','Olsi Jazexhi',1,1,'Caro estudante de Psicologia, você tem em suas mãos um material que servirá como referência para a disciplina de Introdução à Psicologia Geral. Nesta obra cientifica trouxe os conteúdos que fazem parte da disciplina Psicologia Geral de forma clara e objectiva,com uma linguagem coloquial; entendendo, no entanto, que, estamos tratando de uma ciência que possui suas especificidades e, por isso, pode ser complexa, e exigirá uma leitura mais atenta. Não temos a pretensão de esgotar o assunto com os conteúdos neste livro, eles funcionarão como uma iniciação a sua investigação. E, para tanto, além dos conteúdos que vamos fornecer, estaremos indicando para uma bibliografia além de sites da web. Na maior parte das unidades você encontrará, em primeiro lugar, uma exposição mais geral da teoria, em seguida os teóricos relacionados a ela e seus principais pressupostos. Na parte final, haverá uma correlação com aspectos práticos relacionados à disciplina. Os conteúdos que compõem cada unidade foram elaborados levando em conta os conceitos e características epistemológicas mais importantes para a Psicologia. Como se trata da disciplina de Introdução à Psicologia Geral, este livro é uma introdução ao estudo de Psicologia. Por isso, aborda aspectos relevantes para um conhecimento da Psicologia Científica, sem privilegiar essa ou aquela teoria.');
/*!40000 ALTER TABLE `bookinventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `publisher` varchar(255) NOT NULL,
  `publication_date` date NOT NULL,
  `isbn` varchar(13) NOT NULL,
  `borrower_first_name` varchar(255) NOT NULL,
  `borrower_last_name` varchar(255) NOT NULL,
  `borrower_email` varchar(255) NOT NULL,
  `borrowed_date` date NOT NULL,
  `borrowed_time` time NOT NULL,
  `returned_date` date DEFAULT NULL,
  `returned_time` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_log_bookinventory` (`book_id`),
  CONSTRAINT `fk_book_id` FOREIGN KEY (`book_id`) REFERENCES `bookinventory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES (5,3,'Novos Contextos De Introdução Á Psicologia','Apolenário Portugal','Olsi Jazexhi','1900-01-01','0123456789','name','lastname','email','2023-05-20','11:18:54',NULL,NULL),(6,3,'Novos Contextos De Introdução Á Psicologia','Apolenário Portugal','Olsi Jazexhi','1900-01-01','0123456789','name','lastname','email','2023-05-20','11:19:45',NULL,NULL),(19,3,'Novos Contextos De Introdução Á Psicologia','Apolenário Portugal','Olsi Jazexhi','1900-01-01','0123456789','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','11:59:02',NULL,NULL),(20,3,'Novos Contextos De Introdução Á Psicologia','Apolenário Portugal','Olsi Jazexhi','1900-01-01','0123456789','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','12:06:32',NULL,NULL),(21,1,'The Great Gatsby','F. Scott Fitzgerald','Simon and Schuster','2004-09-30','9780743273565','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','12:06:54',NULL,NULL),(23,1,'The Great Gatsby','F. Scott Fitzgerald','Simon and Schuster','2004-09-30','9780743273565','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','12:27:19',NULL,NULL),(24,1,'The Great Gatsby','F. Scott Fitzgerald','Simon and Schuster','2004-09-30','9780743273565','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','13:22:00',NULL,NULL),(25,1,'The Great Gatsby','F. Scott Fitzgerald','Simon and Schuster','2004-09-30','9780743273565','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','13:40:15',NULL,NULL),(26,1,'The Great Gatsby','F. Scott Fitzgerald','Simon and Schuster','2004-09-30','9780743273565','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','13:41:37',NULL,NULL),(27,1,'The Great Gatsby','F. Scott Fitzgerald','Simon and Schuster','2004-09-30','9780743273565','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','13:45:19',NULL,NULL),(28,1,'The Great Gatsby','F. Scott Fitzgerald','Simon and Schuster','2004-09-30','9780743273565','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','13:49:29','2023-05-20','13:50:07'),(29,1,'The Great Gatsby','F. Scott Fitzgerald','Simon and Schuster','2004-09-30','9780743273565','Pat','Liu','pliu25@bentleyschool.org','2023-05-20','14:08:27',NULL,NULL);
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-20 16:16:47

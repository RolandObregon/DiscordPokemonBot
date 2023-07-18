
--
-- Host:    Database: 
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario` (
  `user_id` bigint NOT NULL,
  `cantidades` varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pokemon`
--

DROP TABLE IF EXISTS `pokemon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokemon` (
  `id` int NOT NULL,
  `nombre` varchar(18) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rareza` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokemon`
--

LOCK TABLES `pokemon` WRITE;
/*!40000 ALTER TABLE `pokemon` DISABLE KEYS */;
INSERT INTO `pokemon` VALUES (1,'Bulbasaur',1),(2,'Ivysaur',1),(3,'Venusaur',1),(4,'Charmander',1),(5,'Charmeleon',1),(6,'Charizard',2),(7,'Squirtle',1),(8,'Wartortle',1),(9,'Blastoise',2),(10,'Caterpie',1),(11,'Metapod',1),(12,'Butterfree',2),(13,'Weedle',1),(14,'Kakuna',1),(15,'Beedrill',2),(16,'Pidgey',1),(17,'Pidgeotto',1),(18,'Pidgeot',2),(19,'Rattata',1),(20,'Raticate',1),(21,'Spearow',1),(22,'Fearow',1),(23,'Ekans',1),(24,'Arbok',1),(25,'Pikachu',1),(26,'Raichu',2),(27,'Sandshrew',1),(28,'Sandslash',1),(29,'Nidoran♀',1),(30,'Nidorina',1),(31,'Nidoqueen',2),(32,'Nidoran♂',1),(33,'Nidorino',1),(34,'Nidoking',2),(35,'Clefairy',2),(36,'Clefable',3),(37,'Vulpix',2),(38,'Ninetales',3),(39,'Jigglypuff',2),(40,'Wigglytuff',3),(41,'Zubat',1),(42,'Golbat',2),(43,'Oddish',1),(44,'Gloom',1),(45,'Vileplume',2),(46,'Paras',1),(47,'Parasect',1),(48,'Venonat',1),(49,'Venomoth',2),(50,'Diglett',1),(51,'Dugtrio',2),(52,'Meowth',1),(53,'Persian',2),(54,'Psyduck',1),(55,'Golduck',2),(56,'Mankey',1),(57,'Primeape',2),(58,'Growlithe',1),(59,'Arcanine',2),(60,'Poliwag',1),(61,'Poliwhirl',1),(62,'Poliwrath',2),(63,'Abra',2),(64,'Kadabra',2),(65,'Alakazam',3),(66,'Machop',1),(67,'Machoke',1),(68,'Machamp',2),(69,'Bellsprout',1),(70,'Weepinbell',1),(71,'Victreebel',2),(72,'Tentacool',1),(73,'Tentacruel',2),(74,'Geodude',1),(75,'Graveler',1),(76,'Golem',2),(77,'Ponyta',1),(78,'Rapidash',2),(79,'Slowpoke',1),(80,'Slowbro',2),(81,'Magnemite',1),(82,'Magneton',2),(83,'Farfetch\'d',2),(84,'Doduo',1),(85,'Dodrio',2),(86,'Seel',1),(87,'Dewgong',2),(88,'Grimer',1),(89,'Muk',2),(90,'Shellder',1),(91,'Cloyster',2),(92,'Gastly',1),(93,'Haunter',1),(94,'Gengar',2),(95,'Onix',1),(96,'Drowzee',1),(97,'Hypno',2),(98,'Krabby',1),(99,'Kingler',2),(100,'Voltorb',1),(101,'Electrode',2),(102,'Exeggcute',1),(103,'Exeggutor',2),(104,'Cubone',1),(105,'Marowak',2),(106,'Hitmonlee',3),(107,'Hitmonchan',3),(108,'Lickitung',2),(109,'Koffing',1),(110,'Weezing',2),(111,'Rhyhorn',1),(112,'Rhydon',2),(113,'Chansey',4),(114,'Tangela',2),(115,'Kangaskhan',3),(116,'Horsea',1),(117,'Seadra',2),(118,'Goldeen',1),(119,'Seaking',2),(120,'Staryu',2),(121,'Starmie',3),(122,'Mr. Mime',3),(123,'Scyther',3),(124,'Jynx',3),(125,'Electabuzz',3),(126,'Magmar',3),(127,'Pinsir',3),(128,'Tauros',3),(129,'Magikarp',1),(130,'Gyarados',2),(131,'Lapras',3),(132,'Ditto',4),(133,'Eevee',2),(134,'Vaporeon',3),(135,'Jolteon',3),(136,'Flareon',3),(137,'Porygon',3),(138,'Omanyte',3),(139,'Omastar',3),(140,'Kabuto',3),(141,'Kabutops',3),(142,'Aerodactyl',3),(143,'Snorlax',4),(144,'Articuno',6),(145,'Zapdos',6),(146,'Moltres',6),(147,'Dratini',4),(148,'Dragonair',4),(149,'Dragonite',5),(150,'Mewtwo',6),(151,'Mew',6);
/*!40000 ALTER TABLE `pokemon` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;


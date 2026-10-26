-- 科政明数据库表结构（MySQL 8.0）
CREATE DATABASE IF NOT EXISTS tech_policy DEFAULT CHARSET utf8mb4;
USE tech_policy;

CREATE TABLE `user` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `openid` varchar(50) NOT NULL,
  `prefer` text,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `policy` (
  `pid` int NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `title_link` varchar(255) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `department` varchar(255) DEFAULT NULL,
  `datetime` varchar(255) DEFAULT NULL,
  `txt` text,
  `type` varchar(255) DEFAULT NULL,
  `cnt_type` varchar(255) DEFAULT NULL,
  `docx_link` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `abstract` text,
  `tfidf` text,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `record` (
  `uid` int NOT NULL,
  `pid` int NOT NULL,
  `time` timestamp NULL DEFAULT NULL,
  `count` int DEFAULT NULL,
  PRIMARY KEY (`uid`,`pid`),
  KEY `pid` (`pid`),
  CONSTRAINT `record_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`),
  CONSTRAINT `record_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `policy` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `star` (
  `uid` int NOT NULL,
  `pid` int NOT NULL,
  `time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`uid`,`pid`),
  KEY `pid` (`pid`),
  CONSTRAINT `star_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`),
  CONSTRAINT `star_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `policy` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `push` (
  `uid` int NOT NULL,
  `pid` int NOT NULL,
  `time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`uid`,`pid`),
  KEY `pid` (`pid`),
  CONSTRAINT `push_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`),
  CONSTRAINT `push_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `policy` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

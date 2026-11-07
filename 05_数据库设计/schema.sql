-- 科政明数据库表结构（MySQL 8.0）
CREATE DATABASE IF NOT EXISTS tech_policy DEFAULT CHARSET utf8mb4;
USE tech_policy;

-- 用户表：通过 openid 关联小程序用户，prefer 保存偏好信息。
CREATE TABLE `user` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `openid` varchar(50) NOT NULL,
  `prefer` text,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 政策主表：集中保存政策元数据、正文、摘要及关键词结果。
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

-- 浏览记录：uid 与 pid 构成联合主键，每名用户对每篇政策保留一条记录。
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

-- 收藏关系表：联合主键避免同一用户重复收藏同一政策。
CREATE TABLE `star` (
  `uid` int NOT NULL,
  `pid` int NOT NULL,
  `time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`uid`,`pid`),
  KEY `pid` (`pid`),
  CONSTRAINT `star_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`),
  CONSTRAINT `star_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `policy` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 推送关系表：记录用户与政策的关联及相应时间。
CREATE TABLE `push` (
  `uid` int NOT NULL,
  `pid` int NOT NULL,
  `time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`uid`,`pid`),
  KEY `pid` (`pid`),
  CONSTRAINT `push_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`),
  CONSTRAINT `push_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `policy` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

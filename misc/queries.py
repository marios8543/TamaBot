queries=["""
CREATE TABLE IF NOT EXISTS `pets` (
  `name` varchar(765) COLLATE utf8_bin DEFAULT NULL,
  `gender` tinyint(4) DEFAULT NULL COMMENT '0: male 1: female',
  `owner` varchar(765) COLLATE utf8_bin DEFAULT NULL,
  `cycle` int(5) DEFAULT NULL COMMENT '1: Baby 2:Child 3:Teen 4:Adult 5:Senior',
  `hunger` int(50) DEFAULT NULL,
  `happy` int(50) DEFAULT NULL,
  `discipline` int(50) DEFAULT NULL,
  `weight` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
"""
,"""
CREATE TABLE IF NOT EXISTS `users` (
  `id` varchar(765) COLLATE utf8_bin DEFAULT NULL,
  `birthday` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `registration_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `credit` bigint(20) DEFAULT NULL,
  `items` text COLLATE utf8_bin
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
"""]
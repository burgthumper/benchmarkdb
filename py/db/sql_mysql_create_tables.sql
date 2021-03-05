CREATE TABLE `restaurant` (
  `restaurant_id` varchar(6) NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `province` varchar(2) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `country` varchar(3) DEFAULT NULL,
  `latitude` decimal(8,6) DEFAULT NULL,
  `longitude` decimal(9,6) DEFAULT NULL,
  `mdb` varchar(200) DEFAULT NULL,
  `dbd` varchar(200) DEFAULT NULL,
  `rvp` varchar(200) DEFAULT NULL,
  `rmm` varchar(200) DEFAULT NULL,
  `mos` varchar(200) DEFAULT NULL,
  `mrt` varchar(200) DEFAULT NULL,
  `dma` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `daily_coupon_redemptions_per_restaurant` (
  `summary_date` date NOT NULL,
  `coupon_id` int(11) NOT NULL,
  `restaurant_id` varchar(6) NOT NULL,
  `redemption_count` int(11) DEFAULT '0',
  PRIMARY KEY (`summary_date`,`coupon_id`,`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
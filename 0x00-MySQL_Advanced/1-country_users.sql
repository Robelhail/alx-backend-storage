-- Creates a table users
-- country, enum of countries: US, CO and TN, never null (default=US)
-- If table exists, script will not fail
-- Drop table `users` if it exists
DROP TABLE IF EXISTS `users`;
-- Create table `users` if it does not exists
CREATE TABLE IF NOT EXISTS `users`(
       `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
       `email` VARCHAR(255) UNIQUE NOT NULL,
       `name` VARCHAR(255),
       `country` ENUM('US','CO','TN') NOT NULL DEFAULT 'US'
);

-- Create user if not exists user_0d_1 in MySQL Server
-- User should have all privileges on MySQL Server
-- Set the password for user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

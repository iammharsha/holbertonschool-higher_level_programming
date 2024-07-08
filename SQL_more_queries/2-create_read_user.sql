-- Create if doesn't exist both database hbtn_0d_2 and user user_0d_2
-- User should only have select privilege in database hbtn_0d_2
-- User password should be set
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.hbtn_0d_2 TO 'user_0d_2'@'localhost';

use ELearningPlatform;

-- Creating Users
-- Create Project Manager
CREATE USER 'project_manager_pratik'@'localhost' IDENTIFIED BY 'Darade@123';
GRANT SELECT, INSERT, UPDATE, DELETE ON ELearningPlatform.* TO 'project_manager_pratik'@'localhost';
FLUSH PRIVILEGES;

alter user 'project_manager_pratik'@'localhost' identified by 'Darade@123' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 1;

-- Create Database Admin
CREATE USER 'db_admin_ishan'@'localhost' IDENTIFIED BY 'Prabhune@123';
GRANT ALL PRIVILEGES ON ELearningPlatform.* TO 'db_admin_ishan'@'localhost';
FLUSH PRIVILEGES;

alter user 'db_admin_ishan'@'localhost' identified by 'Prabhune@123' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 1;

-- Create Database Manager
CREATE USER 'db_manager_harshal'@'localhost' IDENTIFIED BY 'Sawant@123';
GRANT SELECT, INSERT, UPDATE, DELETE ON ELearningPlatform.* TO 'db_manager_harshal'@'localhost';
FLUSH PRIVILEGES;

alter user 'db_manager_harshal'@'localhost' identified by 'Sawant@123' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 1;

-- Create Database Designer
CREATE USER 'db_designer_raj'@'localhost' IDENTIFIED BY 'Dedhia@123';
GRANT SELECT, INSERT ON ELearningPlatform.* TO 'db_manager_harshal'@'localhost';
FLUSH PRIVILEGES;

alter user 'db_designer_raj'@'localhost' identified by 'Dedhia@123' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 1;

-- Create Database Designer
CREATE USER 'db_designer_aniket'@'localhost' IDENTIFIED BY 'Singh@123';
GRANT SELECT, INSERT ON ELearningPlatform.* TO 'db_designer_aniket'@'localhost';
FLUSH PRIVILEGES;

alter user 'db_designer_aniket'@'localhost' identified by 'Singh@123' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 1;

SELECT user FROM mysql.user;


-- Create database
-- Coder: Noelia
CREATE DATABASE "PFJobTrends"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Argentina.1252'
    LC_CTYPE = 'Spanish_Argentina.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Conect to db
\c "PFJobTrends";


-- Create table developer
CREATE TABLE developer (
    id_dev INTEGER PRIMARY KEY,
    Age VARCHAR(50),
    Gender VARCHAR(50),
    Sexuality VARCHAR(50),
    Ethnicity VARCHAR(50),
    EdLevel VARCHAR(50),
	SurveyYear INTEGER,
    id_job INTEGER,
    id_exp INTEGER
);

-- Create table job
CREATE TABLE job (
    id_job INTEGER PRIMARY KEY,
    CompanySize VARCHAR(50),
    Country VARCHAR(50),
    Employment VARCHAR(50),    
    Currency VARCHAR(50),
    CurrencySymbol VARCHAR(20),
    Salary FLOAT,
    SalaryFreq VARCHAR(50),
    DollarizedSalary FLOAT
);


-- Create table experience
CREATE TABLE experience (
    id_exp INTEGER PRIMARY KEY,
    YearsCode VARCHAR(50),
    YearsCodePro VARCHAR(50),
    OperatingSystem VARCHAR(50)
);

-- Create table language (unique languages)
CREATE TABLE language(
    id_lang INTEGER PRIMARY KEY,
    language VARCHAR(50)
);

-- Create table database (unique databases)
CREATE TABLE "database"(
    id_db INTEGER PRIMARY KEY,
    database VARCHAR(50)
);

-- Create table framework (unique framework)
CREATE TABLE framework(
    id_framework INTEGER PRIMARY KEY,
    framework VARCHAR(50)
);

-- Create table platform (unique platform)
CREATE TABLE platform (
    id_platform INTEGER PRIMARY KEY,
    platform VARCHAR(50)
);

-- Create table dev_type (unique dev_type)
CREATE TABLE dev_type(
    id_dev_type	FLOAT PRIMARY KEY,
    dev_type VARCHAR(50)
);



-- Create table exp-lang
CREATE TABLE exp_lang(
    id_exp_lang INTEGER PRIMARY KEY,
    id_exp INTEGER,
    id_lang INTEGER
);

-- Create table exp-db
CREATE TABLE exp_db(
    id_exp_db INTEGER PRIMARY KEY,
    id_exp INTEGER,
    id_database INTEGER
);

-- Create table exp-framework
CREATE TABLE exp_framework(
    id_exp_framework INTEGER PRIMARY KEY,
    id_exp INTEGER,
    id_framework INTEGER
);

-- Create table exp-platform
CREATE TABLE exp_platform(
    id_exp_platform INTEGER PRIMARY KEY,
    id_exp INTEGER,
    id_platform INTEGER
);


CREATE TABLE job_devtype(
    id_job_devtype INTEGER PRIMARY KEY,
    id_job INTEGER,
    id_dev_type FLOAT
);

-- ***********************************************************************
-- ADD FOREIGN KEYS
ALTER TABLE developer
ADD FOREIGN KEY (id_job) REFERENCES job (id_job); 

ALTER TABLE developer
ADD FOREIGN KEY (id_exp) REFERENCES experience (id_exp); 

ALTER TABLE exp_lang
ADD FOREIGN KEY (id_exp) REFERENCES experience (id_exp),
ADD FOREIGN KEY (id_lang) REFERENCES language (id_lang);

ALTER TABLE exp_db
ADD FOREIGN KEY (id_exp) REFERENCES experience (id_exp),
ADD FOREIGN KEY (id_database) REFERENCES "database" (id_db);

ALTER TABLE exp_framework
ADD FOREIGN KEY (id_exp) REFERENCES experience (id_exp),
ADD FOREIGN KEY (id_framework) REFERENCES framework (id_framework);

ALTER TABLE exp_platform
ADD FOREIGN KEY (id_exp) REFERENCES experience (id_exp),
ADD FOREIGN KEY (id_platform) REFERENCES platform (id_platform);

ALTER TABLE job_devtype
ADD FOREIGN KEY (id_job) REFERENCES job(id_job),
ADD FOREIGN KEy (id_dev_type) REFERENCES dev_type(id_dev_type);

-- Hacer esto que sigue desde psql y no desde PGADMIN

\copy "language" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/language.csv' delimiter ',' CSV HEADER;
\copy "database" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/database.csv' delimiter ',' CSV HEADER;
\copy "framework" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/framework.csv' delimiter ',' CSV HEADER;
\copy "platform" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/platform.csv' delimiter ',' CSV HEADER;
\copy "dev_type" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/devtype.csv' delimiter ',' CSV HEADER;


-- Error operating system  --> varchar(50) is not enough
ALTER TABLE experience
ALTER COLUMN OperatingSystem TYPE VARCHAR(100);
\copy "experience" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/experience.csv' delimiter ',' CSV HEADER;

-- Error DevType(Position) --> varchar(150) is not enough
-- Error Employment --> varchar(50) is not enough
ALTER TABLE job
ALTER COLUMN "DevType(Position)" TYPE VARCHAR(1500);

ALTER TABLE job
ALTER COLUMN Employment TYPE VARCHAR(300);
\copy "job" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/job.csv' delimiter ',' CSV HEADER;


-- Due to Nan, id_lang is not integer rather float
ALTER TABLE language
ALTER COLUMN id_lang TYPE FLOAT;

ALTER TABLE exp_lang
ALTER COLUMN id_lang TYPE FLOAT;
\copy "exp_lang" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/exp_lang.csv' delimiter ',' CSV HEADER;


-- Due to Nan, id_database is not integer rather float
ALTER TABLE "database"
ALTER COLUMN id_db TYPE FLOAT;

ALTER TABLE exp_db
ALTER COLUMN id_database TYPE FLOAT;
\copy "exp_db" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/exp_db.csv' delimiter ',' CSV HEADER;

-- Due to Nan, id_framework is not integer rather float
ALTER TABLE "framework"
ALTER COLUMN id_framework TYPE FLOAT;

ALTER TABLE exp_framework
ALTER COLUMN id_framework TYPE FLOAT;
\copy "exp_framework" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/exp_framework.csv' delimiter ',' CSV HEADER;


-- Due to Nan, id_plaform is not integer rather float
ALTER TABLE "platform"
ALTER COLUMN id_platform TYPE FLOAT;

ALTER TABLE exp_platform
ALTER COLUMN id_platform TYPE FLOAT;
\copy "exp_platform" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/exp_platform.csv' delimiter ',' CSV HEADER;


\copy "job_devtype" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/job_devtype.csv' delimiter ',' CSV HEADER;

-- Error edLevel --> vachar(50) is not enough
ALTER TABLE developer
ALTER COLUMN edLevel TYPE VARCHAR(100);

-- Error Gender --> vachar(50) is not enough
ALTER TABLE developer
ALTER COLUMN Gender TYPE VARCHAR(100);

-- Error Ethnicity --> vachar(50) is not enough
ALTER TABLE developer
ALTER COLUMN Ethnicity TYPE VARCHAR(500);

-- Error Sexuality --> vachar(50) is not enough
ALTER TABLE developer
ALTER COLUMN Sexuality TYPE VARCHAR(200);

\copy "developer" FROM 'C:/Users/kuens/Documents/.Pandas/.Henry/Data/PF/PF_TENDENCIAS_MERCADO_LABORAL/data/final_tables/developer.csv' delimiter ',' CSV HEADER;

-- Use some queries

-- Get all languages for developers of 2018 survey, and job
select d.id_dev, l.language, j.Country, j.DollarizedSalary
from developer d inner join experience e on d.id_exp=e.id_exp
inner join exp_lang el on e.id_exp=el.id_exp
inner join language l on el.id_lang=l.id_lang
inner join job j on d.id_job = j.id_job
where d.SurveyYear=2018
limit 40;
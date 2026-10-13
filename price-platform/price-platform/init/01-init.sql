-- بيشتغل مرة واحدة بس عند إنشاء الـ volume لأول مرة
CREATE USER airflow WITH PASSWORD 'airflow123';
CREATE DATABASE airflow OWNER airflow;

-- الـ serving layer اللي Power BI هيتوصل بيه
CREATE DATABASE serving OWNER admin;

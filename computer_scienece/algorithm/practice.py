import pymysql

conn = pymysql.connect(
    host='localhost', user='root', password="12345678",
    charset='utf8', db='test'
)
cursor = conn.cursor()

sql = "select * from olist_customers_dataset"
cursor.execute(sql)
print(cursor.fetchone())

# sql = "select * from student_tb;"
# sql = """
# CREATE TABLE covid19_country (
#   countrycode                 VARCHAR(10) NOT NULL,
#   countryname                 VARCHAR(80) NOT NULL,
#   continent                   VARCHAR(50),
#   population                  int,
#   population_density          int,
#   median_age                  int,
#   aged_65_older               int,
#   aged_70_older               int,
#   hospital_beds_per_thousand  int,
#   PRIMARY KEY (countrycode)
# );
# """


# sql을 실행한다. 반환 값은 결과 값의 길이를 반환한다.
# cursor.execute(sql)

# sql = "select * from covid19_country"

# 실행된 query 결과를 반환한다.
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)

conn.commit()
conn.close()
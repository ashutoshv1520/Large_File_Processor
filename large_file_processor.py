import pymysql
import sys

class Processor:

    def __init__(self, db_name="product", table_name="product_data", db_user="root", db_password="iamgroot", db_host="localhost"):
        self.db_name = db_name
        self.table_name = table_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host

    def connect(self):
        try:
            self.con = pymysql.connect(host=self.db_host,
                                    user=self.db_user,
                                    password=self.db_password,
                                    autocommit=True,
                                    local_infile=1,
                                    database=self.db_name)
            print('Connected to DB: {}'.format(self.db_host))
        except Exception as e:
            print('Error: {}'.format(str(e)))
            sys.exit(1)

        

    def disconnect(self):
        try:
            self.con.close()
            print('Disconnected from DB')
        except Exception as e:
            print('Error: {}'.format(str(e)))
            sys.exit(1)



    def create_table_from_csv(self, file_name="products.csv"):
        '''
        This function load a csv file to MySQL table.
        '''
        try:
            cursor = self.con.cursor()
            cursor.execute('DROP TABLE IF EXISTS '+self.db_name+'.'+self.table_name+';')
            cursor.execute('CREATE TABLE '+self.db_name+'.'+self.table_name+'(name varchar(255),sku varchar(255),description varchar(255));')
            print("Table Created.")
            load_sql = "LOAD DATA LOCAL INFILE 'data/"+file_name+"' INTO TABLE "+self.db_name+'.'+self.table_name+"\
 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';"
            cursor.execute(load_sql)
            cursor.execute("DELETE FROM "+self.db_name+"."+self.table_name+" WHERE name='name' and sku='sku' and description='description';")
            print('Succuessfully loaded the table from csv.')
        except Exception as e:
            print('Error: {}'.format(str(e)))
            sys.exit(1)

    def insert_data_according_sku(self,name,sku,description):
        try:
            cursor = self.con.cursor()
            cursor.execute("INSERT INTO "+self.db_name+"."+self.table_name+" (name, sku, description) VALUES ('"+name+"', '"+sku+"', '"+description+"');")
            print("1 row(s) affected")
        except Exception as e:
            print('Error: {}'.format(str(e)))
            sys.exit(1)

    def update_data_according_sku(self,name,sku,description):
        try:
            cursor = self.con.cursor()
            cursor.execute("UPDATE "+self.db_name+"."+self.table_name+" SET name = '"+name+"', description = '"+description+"' WHERE sku = '"+sku+"';")
            print("1 row(s) affected")
        except Exception as e:
            print('Error: {}'.format(str(e)))
            sys.exit(1)

    def create_aggregated_table(self,agg_table_name):
        try:
            cursor = self.con.cursor()
            cursor.execute("create table "+self.db_name+"."+agg_table_name+"(name varchar(100), no_of_products INT); ")
            cursor.execute("insert into "+agg_table_name+" select name , count(sku) from "+self.db_name+"."+self.table_name+" group by name;")
            print("Aggregated table with names and number of products created.")
        except Exception as e:
            print('Error: {}'.format(str(e)))
            sys.exit(1)
    
    def update_table_from_csv(self, file_name="products.csv"):
        '''
        This function load a csv file and update data to MySQL table.
        '''
        try:
            cursor = self.con.cursor()
            load_sql = "LOAD DATA LOCAL INFILE 'data/"+file_name+"' INTO TABLE "+self.db_name+'.'+self.table_name+"\
 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n';"
            cursor.execute(load_sql)
            cursor.execute("DELETE FROM "+self.db_name+"."+self.table_name+" WHERE name='name' and sku='sku' and description='description';")
            print('Succuessfully updated the table from csv.')
        except Exception as e:
            print('Error: {}'.format(str(e)))
            sys.exit(1)
        


def main():
    obj=Processor()
    flag=1
    while(flag==1):
        print("Select appropriate option:")
        print('''1. insert_csv_data (table,data-feeding)
2. insert data on basis of sku
3. update data on basis of sku 
4. create aggregated table  
5. update data 
6. connect to database 
7. disconnect.''')
        print("press 0 if you wish to exit\n")
        inp=int(input())
        if inp==0:
            flag=0
        elif inp==1:
            file=input("Enter file name: ")
            obj.create_table_from_csv(file)
        elif inp==2:
            name=input("Enter name: ")
            sku=input("Enter sku: ")
            description=input("Enter description: ")
            obj.insert_data_according_sku(name,sku,description)
        elif inp==3:
            name=input("Enter name: ")
            sku=input("Enter sku: ")
            description=input("Enter description: ")
            obj.update_data_according_sku(name,sku,description)
        elif inp==4:
            agg_table_name=input("Enter new table name: ")
            obj.create_aggregated_table(agg_table_name)
        elif inp==5:
            file=input("Enter file name: ")
            obj.update_table_from_csv(file)
        elif inp==6:
            obj.connect()
        elif inp==7:
            obj.disconnect()
        print("Do you wish to continue? 0/1")
        flag=int(input())

        

if __name__ == "__main__":
    main()





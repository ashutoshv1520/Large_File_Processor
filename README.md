# Large_File_Processor
Submission for assignment of Data Engineer Role at Postman.

## Steps to run code:
1. Install MySQL 
https://dev.mysql.com/downloads/installer/
2. Install Python 3.7
https://www.python.org/downloads/
3. Install pymysql using: ```pip install pymysql``` 
4. Run large_file_processor.py using:
```python large_file_processor.py``` in cmd

## Details of table and schema:
Note: *table and schema would be created automatically whem you will run code*.
1. Table:

### products_data
It has three columns **name**, **sku** and **description** with 500000 rows.
 
![alt text](product_data_table.png "Logo Title Text 1")

### aggregated_data
It has two columns **name** and **no_of_products**.

![alt text](aggregated_data_table.png "Logo Title Text 1")

## What is done from Points to achieve

1. Your code should follow concept of OOPS. `(done)`

2. Support for regular non-blocking parallel ingestion of the given file into a table. Consider thinking about the scale of what should happen if the file is to be processed in 2 mins. `(done)`
*For this we have used ```LOAD DATA``` which directly feeds csv data to mysql rather than ```INSERT INTO```

3. Support for updating existing products in the table based on `sku` as the primary key. (Yes, we know about the kind of data in the file. You need to find a workaround for it). `(done)`

4. All product details are to be ingested into a single table. `(done)`

5. An aggregated table on above rows with `name` and `no. of products` as the columns. `(done)`

## What is not done from Points to achieve

Point 3 from above was not clear but still we have created functionality to add data to table on basis of `sku`.

## What would you improve if given more days

If given more days i would have added more funtionalities, provided an user interface for better interaction and must have dockerised the code.

# Crawling Data Teks pada Website (Scrapy).

Website URL :  http://www.disney.id/

##### Tools :

- Python 2.7

- Library Scrapy

- Command Prompt

  

##### Langkah - langkah Crawling Data Teks pada Website :

1. Install library Scrapy menggunakan pip dengan perintah :

   ```
   pip install scrapy
   
   ```

2. Buatlah Project baru dengan perintah :

   ```
   scrapy startproject projectname
   ```

   

3. Buatlah File Spider baru dengan perintah :

   ```
   scrapy genspider example example.com
   ```

   **genspider** merupakan perintah untuk membuat file baru, nama file dapat disesuaikan dengan kebutuhan. **example.com** dapat anda ganti dengan alamat website yang akan di crawling. 

   Dalam crawling website disney ini digunakan perintah :

   ```
   scrapy genspider crawling www.disney.id
   ```

   **crawling** merupakan nama file spider yang dibuat. File akan tersimpan dalam format .py pada direktori.

   

4. Buka file python (**crawling.py**) yang telah dibuat, edit class parse pada file untuk mengambil data teks pada web.

   ```
   def parse(self, response):
           titles = response.css('.title p ::text').extract()
           for item in zip(titles):
           scraped_info = {
               'title' : item[0]
           }
           yield scraped_info
   ```

          
               
   Pada variabel **titles**, berisi script untuk mengambil data menggunakan class css pada website.

   

5. Jalankan program **crawling.py** pada command prompt dengan perintah :

   ```
   scrapy runspider crawling.py
   ```

   

6. Setelah crawling data selesai, export data hasil ke format CSV atau Excel dengan perintah :

   ```
   scrapy crawl crawling.py -o disney.csv -t csv
   ```

   

7. Export data pada file CSV ke dalam database.


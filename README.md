# invent-system
A system to organize &amp; optimize inventory for wholesale &amp; ECommerce businesses.

## About 
I wanted to create a system for my father so that he can organize tens of thousands of products in the shop in a systematic manner wherein whatever product he looks for, he can find it, track it. And at the same time, I wanted the system I create to integrate with existing accounting and data management applications like MS Excel and Tally ERP.

## How to Use
- Use `pip install -r requirements.txt` to install all the necessary dependencies.
- Then run the main file by `python main_with_excel.py`
- Type the data separated by "-"
Example: OM-NC-NTH-8009-R1
In this, OM becomes name of supplier, NC-NTH-8009 is the SKU Code of product that can be mapped while R1 is the location of the product/product box in the shop.
- You have to just type these codes and the barcodes alongwith inventory sheet will be generated automatically 

## How did I create it?
- I first explored the different kinds of naming conventions in wholesale markets, ECom outlets (yes, those outlets that actually deliver the material when an order gets placed by the app like Amazon or Flipkart). 
- Then I studied, different supply chains and courier services so that I could understand how SKUs get mapped, products get listed and what will be the best way to access them.
- I then visited different websites where I could create a barcode with number + ASCII letters and at the end <link>https://barcode.tec-it.com/en/</link> used this website. This website provided a link for the barcode generated and also a data header that can be customized to create the barcode. 
- For this I used the `requests` module to access the website. Then added a status check. If the `status_code` is not 200, the script execution ends.

More documentation coming soon, stay tuned :)

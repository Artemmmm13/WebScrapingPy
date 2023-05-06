# WebScrapingPy

To run the script stored in the 'spider_artfed.py' it is mandatory to:
    - Install scrapy (either using pip (pip install Scrapy) or if you have Conda (conda install -c conda-forge scrapy))
    - Configure your spider, in my case i did: scrapy genspider spider_artfed (here goes URL of the website to be parsed)
    - The last step to run the script you have to type in command line: 'scrapy runspider spider_artfed.py -o parsed_data.json'
    Where the 'spider_artfed.py' is the name of the script itself and 'parsed_data.json' is the JSON file you are going 
    to store the data from website.
    - Additionally, it would be reasonable to change header for the one suitable for your machine

To run the script stored in the 'soup_artfed.py' you simply have to run it in your IDE, press 'shift+f10' in case of PyCharm
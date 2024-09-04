from bs4 import BeautifulSoup
import requests
import sys

# Set the default encoding to UTF-8 for stdout
sys.stdout.reconfigure(encoding='utf-8')

# Open the file to write the output
with open('ProcDna_data.txt', 'w', encoding='utf-8') as f:
    # Fetching data from URLs
    Analytics = requests.get('https://www.procdna.com/analytics').text
    Technolgy = requests.get('https://www.procdna.com/technology').text
    Data_Science = requests.get('https://www.procdna.com/dataScience').text
    Case_study = requests.get('https://www.procdna.com/case_studies').text
    Articles = requests.get('https://www.procdna.com/articles').text
    News = requests.get('https://www.procdna.com/news').text    

    # Parsing the HTML content
    soup_an = BeautifulSoup(Analytics, 'lxml')
    soup_te = BeautifulSoup(Technolgy, 'lxml')
    soup_ds = BeautifulSoup(Data_Science, 'lxml')
    soup_cs = BeautifulSoup(Case_study, 'lxml')
    soup_ar = BeautifulSoup(Articles, 'lxml')
    soup_ne = BeautifulSoup(News, 'lxml')

    # Finding relevant elements
    An_all = soup_an.find_all('div', class_="flex flex-col justify-center gap-8")
    Te_all = soup_te.find_all('div', class_="flex flex-col justify-center gap-8")
    Ds_all = soup_ds.find_all('div', class_="flex flex-col justify-center gap-8")
    Cs_all = soup_cs.find_all('div', class_='h-96 my-20 flex flex-col items-start rounded-lg w-80')
    Ar_all = soup_ar.find_all('a', class_='group flex flex-col gap-2')
    Ne_all = soup_ne.find_all('div', class_='flex flex-col w-2/3 gap-4')

    f.write('''
        SOLUTIONS BY ProcDNA
        
    ''')

    f.write('''
        
    -----Analytics-----
        
    ''')
    for An in An_all:
        head = An.find('div', class_='text-4xl font-semibold text-blue-70').text
        description = An.find('div', class_='text-[#575757] text-lg font-medium').text
        f.write(f'Heading --> {head}\n')
        f.write(f'Description --> {description}\n')
        f.write('\n')

    f.write('''
        
    -----Technology-----
        
    ''')
    for Te in Te_all:
        hea_div = Te.find('div', class_='text-4xl font-semibold text-blue-70')
        if hea_div:
            hea = hea_div.text
            descriptio = Te.find('div', class_='text-[#575757] text-lg font-medium').text
            f.write(f'Heading --> {hea}\n')
            f.write(f'Description --> {descriptio}\n')
            f.write('\n')
        else:
            f.write("Heading not found for this item\n")

    f.write('''
        
    -----Data Science-----
        
    ''')
    for Ds in Ds_all:
        head = Ds.find('div', class_='text-4xl font-semibold text-blue-70').text
        description = Ds.find('div', class_='text-[#575757] text-lg font-medium').text
        f.write(f'Heading --> {head}\n')
        f.write(f'Description --> {description}\n')
        f.write('\n')

    f.write('''
        
        RESOURCES BY ProcDNA
        
        ''')

    f.write('''
        
    -----Case Study-----
        
    ''')
    for Cs in Cs_all:
        head_div = Cs.find('div', class_='absolute text-sm w-full h-12 text-white flex items-center justify-center bottom-0 bg-rectangle-overlay')
        number_div = Cs.find('div', class_='text-left text-lg font-semibold py-3 pt-9 text-blue-90')
        description_div = Cs.find('div', class_='text-left pb-4 font-semibold text-blue-90 text-2xl hover:text-yellow-90')
        
        head = head_div.text if head_div else "No heading"
        number = number_div.text if number_div else "No serial number"
        description = description_div.text if description_div else "No description"
        
        f.write(f'Heading --> {head}\n')
        f.write(f'Serial No. --> {number}\n')
        f.write(f'Description --> {description}\n')
        f.write('\n')

    f.write('''
        
    -----Articles-----
        
    ''')
    for Ar in Ar_all:
        head = Ar.find('div', class_='text-2xl text-[#072970] font-semibold group-hover:text-yellow-90').text
        description = Ar.find('div', class_='group-hover:text-yellow-90').text
        f.write(f'Heading --> {head}\n')
        f.write(f'Description --> {description}\n')
        f.write('\n')

    f.write('''
        
    -----News-----
        
    ''')
    for Ne in Ne_all:
        time_location_div = Ne.find('div', class_='flex items-center gap-1 text-gray-600 text-md')
        news_div = Ne.find('div', class_='text-2xl font-semibold')
        description_div = Ne.find('div', class_='text-base text-gray-600')
        
        time_location = time_location_div.text if time_location_div else "No time and location"
        news = news_div.text if news_div else "No news"
        description = description_div.text if description_div else "No description"
        
        f.write(f'Time and Location --> {time_location}\n')
        f.write(f'News --> {news}\n')
        f.write(f'Description --> {description}\n')
        f.write('\n')

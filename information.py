import base64


def adanient():
    file_path = "static/adanient.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")

        info = "Adani Enterprises Limited (AEL) is an Indian multinational publicly-listed holding company and a part of Adani Group. It is headquartered in Ahmedabad and primarily involved in mining and trading of coal and iron ore. Through its various subsidiaries, it also has business interests in airport operations, edible oils, road, rail and water infrastructure, data centers, and solar manufacturing, among others."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def adanisez():
    file_path = "static/adanisez.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")

        info = "Adani Ports and Special Economic Zone Limited is an Indian multinational port operator and logistics company, based in Ahmedabad, India. A subsidiary of Adani Group, APSEZ is India's largest private port operator with a network of 12 ports and terminals, including India's first deep water Transshipment Port Vizhinjam International Seaport Thiruvananthapuram and India's first port-based SEZ at Mundra."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def apollo():
    file_path = "static/apollo.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Apollo Hospitals Enterprise Limited is an Indian multinational healthcare group headquartered in Chennai. It is the largest hospital chain in India, with a network of 71 owned and managed hospitals. Along with the eponymous hospital chain, the company also operates pharmacies, primary care and diagnostic centres, telehealth clinics, and digital healthcare services among others through its subsidiaries. The company was founded by Prathap C. Reddy in 1983 as the first corporate healthcare provider in India. Several of Apollo's hospitals have been among the first in India to receive international healthcare accreditation by the America-based Joint Commission International as well as NABH accreditation."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def asian():
    file_path = "static/asian.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Asian Paints Ltd is an Indian multinational paint company, headquartered in Mumbai, Maharashtra, India. The company is engaged in the business of manufacturing, selling and distribution of paints, coatings, products related to home décor, bath fittings and providing related services. Asian Paints is India's largest paints company by market share. It is the holding company of Berger International. The company's manufacturing operations encompass 15 countries of the world including India, with considerable presence in the Indian subcontinent and the Middle East."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def axis():
    file_path = "static/axis.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Axis Bank Limited, formerly known as UTI Bank, is an Indian banking and financial services company headquartered in Mumbai, Maharashtra. It is India's third largest private sector bank by assets and Fourth largest by Market capitalisation. It sells financial services to large and mid-size companies, SMEs and retail businesses. As of 30 June 2016, 30.81% shares are owned by the promoters and the promoter group. The remaining 69.19% shares are owned by mutual funds, FIIs, banks, insurance companies, corporate bodies and individual investors. "
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def bajaj():
    file_path = "static/bajaj.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Bajaj Auto Limited is an Indian multinational automotive manufacturing company based in Pune. It manufactures motorcycles, scooters and auto rickshaws. Bajaj Auto is a part of the Bajaj Group. It was founded by Jamnalal Bajaj in Rajasthan in the 1940s. Bajaj Auto is the world's third-largest manufacturer of motorcycles and the second-largest in India. It is the world's largest three-wheeler manufacturer. In December 2020, Bajaj Auto crossed a market capitalisation of ₹1 trillion, making it the world's most valuable two-wheeler company."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def bajajfinance():
    file_path = "static/bajajfinance.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Bajaj Finance Limited is an Indian non-banking financial company headquartered in Pune. It is one of the leading non-banking financial companies of India with a customer base of 73 million and holds assets under management worth ₹270,050 crore. As per the 2023 list of NBFCs issued by the Reserve Bank of India, Bajaj Finance Limited holds the second position in the upper layer based on scale-based regulation guidelines."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def bajajfin():
    file_path = "static/bajajfin.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Bajaj Finserv Limited is an Indian non-banking financial services company headquartered in Pune. It is focused on lending, asset management, wealth management and insurance."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def bpl():
    file_path = "static/bpl.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Bharat Petroleum Corporation Limited is an Indian public sector undertaking under the ownership of the Ministry of Petroleum and Natural Gas, Government of India. It operates three refineries in Bina, Kochi and Mumbai. BPCL is India's second-largest government-owned downstream oil producer, whose operations are overseen by the Ministry of Petroleum and Natural Gas. BPCL was ranked 309th on the Fortune list of the world's biggest PSUs in 2020, and 792nd on Forbes's Global 2000 list in 2021."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def airtel():
    file_path = "static/airtel.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Bharti Airtel Limited, commonly known as Airtel, is an Indian multinational telecommunications services company based in New Delhi. It operates in 18 countries across South Asia and Africa, as well as the Channel Islands. Currently, Airtel provides 5G, 4G and LTE Advanced services throughout India. Currently offered services include fixed-line broadband, and voice services depending upon the country of operation. Airtel had also rolled out its Voice over LTE technology across all Indian telecom circles. It is the second largest mobile network operator in India and the second largest mobile network operator in the world. Airtel was named India's 2nd most valuable brand in the first ever Brandz ranking by Millward Brown and WPP plc. Airtel is credited with pioneering the strategic management of outsourcing all of its business operations except marketing, sales and finance and building the 'minutes factory' model of low cost and high volumes. The strategy has since been adopted by several operators. Airtel's equipment is provided and maintained by Ericsson, Huawei, and Nokia Networks whereas IT support is provided by Amdocs."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def brit():
    file_path = "static/britannia.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Britannia Industries Limited is an Indian multinational food products company, which sells biscuits, breads and dairy products. Founded in 1892, it is one of India's oldest existing companies and currently part of the Wadia Group headed by Nusli Wadia. As of 2023, about 80% of its revenues came from biscuit products. Beginning with the circumstances of its takeover by the Wadia Group in the early 1990s, the company has been mired in several controversies connected to its management, but it continues to hold a large market share."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def cipla():
    file_path = "static/cipla.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Cipla Limited is an Indian multinational pharmaceutical company, headquartered in Mumbai. Cipla primarily develops medication to treat respiratory disease, cardiovascular disease, arthritis, diabetes, depression, and other medical conditions. Cipla has 47 manufacturing locations across the world and sells its products in 86 countries. It is the third largest drug producer in India."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def coal_india():
    file_path = "static/coal_india.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Coal India Limited is an Indian central public sector undertaking under the ownership of the Ministry of Coal, Government of India. It is headquartered at Kolkata. It is the largest government-owned-coal-producer in the world. It is also the ninth largest employer in India with nearly 272,000 employees. The PSU contributes around 82% to the total coal production in India. It produced 554.14 million tonnes of raw coal in 2016–17, an increase from its earlier production of 494.24 million tonnes of coal during FY 2014–15 and earned revenues of ₹95,435 crore from sale of coal in the same financial year. In April 2011, CIL was conferred the Maharatna status by the Government of India, making it one of the seven with that status. As of 14 October 2015, CIL is a PSU owned by the Central Government of India which controls its operations through the Ministry of Coal. As of 14 October 2015, CIL's market capitalisation stood at ₹2.11 lakh crore making it India's 8th most valuable company. CIL ranks 8th among the top 20 firms responsible for a third of all global carbon emissions."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def divi():
    file_path = "static/divis.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Divi's Laboratories Limited is an Indian multinational pharmaceutical company and producer of active pharmaceutical ingredients and intermediates, headquartered in Hyderabad. The company manufactures and custom synthesizes generic APIs, intermediates. The company also manufactures and supplies nutraceutical ingredients through its subsidiary, Divi's Nutraceuticals. Divi's Laboratories is India's fourth largest publicly listed pharmaceutical company by market capitalization."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def reddy():
    file_path = "static/reddy.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Dr. Reddy's Laboratories is an Indian multinational pharmaceutical company based in Hyderabad. The company was founded by Kallam Anji Reddy, who previously worked in the mentor institute Indian Drugs and Pharmaceuticals Limited. Dr. Reddy manufactures and markets a wide range of pharmaceuticals in India and overseas. The company produces over 190 medications, 60 active pharmaceutical ingredients for drug manufacture, diagnostic kits, critical care, and biotechnology. Dr. Reddy's began as a supplier to Indian drug manufacturers, but it soon started exporting to other less-regulated markets that had the advantage of not having to spend time and money on a manufacturing plant that would gain approval from a drug licensing body such as the U.S. Food and Drug Administration. By the early 1990s, the expanded scale and profitability from these unregulated markets enabled the company to begin focusing on getting approval from drug regulators for their formulations and bulk drug manufacturing plants – in more-developed economies. This allowed their movement into regulated markets such as the US and Europe. "
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def eicher():
    file_path = "static/eicher.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Eicher Motors Limited is an Indian multinational automotive company that manufactures motorcycles and commercial vehicles, headquartered in New Delhi. Eicher is the parent company of Royal Enfield, a manufacturer of middleweight motorcycles."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def grasim():
    file_path = "static/grasim.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Grasim Industries Limited is an Indian manufacturing company based in Mumbai. Since its inception in 1947 as a textile manufacturer, Grasim has diversified into textile raw materials like viscose staple fiber and viscose filament yarn, chemicals and insulators, along with cement and financial services through its subsidiaries UltraTech Cement and Aditya Birla Capital respectively. The company is a part of the Aditya Birla Group."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def hcl():
    file_path = "static/hcl.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "HCL Technologies Limited, d/b/a HCLTech, is an Indian multinational information technology consulting company headquartered in Noida. The founder of HCLTech is Shiv Nadar. It was spun out in 1991 when HCL entered into the software services business. The company has offices in 52 countries and over 225,944 employees."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def hdfc():
    file_path = "static/hdfc.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "HDFC Bank Limited is an Indian banking and financial services company headquartered in Mumbai. It is India's largest private sector bank by assets and the world's fifth-largest bank by market capitalization as of August 2023, following its takeover of parent company HDFC. The Reserve Bank of India has identified the HDFC Bank, State Bank of India, and ICICI Bank as Domestic Systemically Important Banks, which are often referred to as banks that are “too big to fail”. The bank was incorporated in August 1994 after its erstwhile parent HDFC received an 'in principle' approval from the RBI to set up a bank in the private sector, as part of its liberalization of the Indian banking industry, and commenced operations in January 1995. With a market capitalization of $140 billion, HDFC Bank is the third-largest company on Indian stock exchanges. It is also the sixteenth largest employer in India with nearly 1.73 lakh employees."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def hdfclife():
    file_path = "static/hdfclife.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "HDFC Life Insurance Company Limited is a long-term life insurance provider headquartered in Mumbai, offering individual and group insurance services and it was incorporated on 14 August 2000."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def hero():
    file_path = "static/hero.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Hero MotoCorp Limited is an Indian multinational motorcycle and scooter manufacturer headquartered in Delhi. It is one of the world's largest two-wheeler manufacturer and has a market share of about 46% in the Indian two-wheeler industry. As of 27 May 2021, the market capitalization of the company was ₹59,600 crore"
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def hindalco():
    file_path = "static/hindalco.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Hindalco Industries Limited an Indian aluminium and copper manufacturing company, is a subsidiary of the Aditya Birla Group. Its headquarters are at Mumbai, Maharashtra, India. The company is listed in the Forbes Global 2000 at 661st rank. Its market capitalisation by the end of November 2023 was US$15.6 billion."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def unilever():
    file_path = "static/unilever.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Hindustan Unilever Limited is a British-owned Indian Final good company headquartered in Mumbai. It is a subsidiary of the British company Unilever. Its products include foods, beverages, cleaning agents, personal care products, water purifiers and other fast-moving consumer goods. HUL was established in 1931 as Hindustan Vanaspati Manufacturing Co. Following a merger of constituent groups in 1956, it was renamed Hindustan Lever Limited. The company was renamed again in June 2007 as Hindustan Unilever Limited. Hindustan Unilever has been at the helm of a lot of controversies, such as dumping highly toxic mercury-contaminated waste in regular dumps, contaminating the land and water of Kodaikanal. The British company also faced major flak for an advertising campaign attacking the Hindu pilgrimage site at Kumbh Mela, calling it a place where old people get abandoned, a move that was termed racist and insensitive. As of 2019, Hindustan Unilever's portfolio had more than 50 product brands in 14 categories. The company has 21,000 employees and recorded sales of ₹34,619 crores in FY2017–18."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def icici():
    file_path = "static/icici.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "ICICI Bank Limited is an Indian multinational bank and financial services company headquartered in Mumbai with registered office in Vadodara. It offers a wide range of banking and financial services for corporate and retail customers through a variety of delivery channels and specialized subsidiaries in the areas of investment banking, life, non-life insurance, venture capital and asset management. This development finance institution has a network of 5,900 branches and 16,650 ATMs across India and has a presence in 17 countries. The bank has subsidiaries in the United Kingdom and Canada; branches in United States, Singapore, Bahrain, Hong Kong, Qatar, Oman, Dubai International Finance Centre, China and South Africa; as well as representative offices in United Arab Emirates, Bangladesh, Malaysia and Indonesia. The company's UK subsidiary has also established branches in Belgium and Germany. The Reserve Bank of India has identified the State Bank of India, HDFC Bank, and ICICI Bank as Domestic Systemically Important Banks, which are often referred to as banks that are too big to fail"
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def itc():
    file_path = "static/itc.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "ITC Limited is an Indian conglomerate company headquartered in Kolkata. ITC has a diversified presence across industries such as FMCG, hotels, software, packaging, paperboards, specialty papers and agribusiness. The company has 13 businesses in 5 segments. It exports its products in 90 countries. Its products are available in 6 million retail outlets. On 17 April 2023, its market cap crossed the milestone of ₹500,000 crore for the first time in company's history, followed by crossing the ₹600,000 crore mark on 20 July 2023 and becoming the biggest FMCG Company in India passing the Hindustan Unilever's market cap the very next day. It employs 36,500 people at more than 60 locations across India."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def indusind():
    file_path = "static/indusind.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "IndusInd Bank Limited is an Indian financial services headquartered in Mumbai. IndusInd Bank was inaugurated in April 1994 by then Union Finance Minister Manmohan Singh."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def infosys():
    file_path = "static/infosys.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Infosys Limited is an Indian multinational information technology company that provides business consulting, information technology and outsourcing services. The company was founded in Pune and is headquartered in Bangalore. Infosys is the second-largest Indian IT company, after Tata Consultancy Services, by 2020 revenue figures. On 24 August 2021, Infosys became the fourth Indian company to reach US$100 billion in market capitalization. It is one of the top Big Tech companies."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def jsw():
    file_path = "static/jsw.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "JSW Steel Limited is an Indian multinational steel producer based in Mumbai and is a flagship company of the JSW Group. After the merger of Bhushan Power & Steel, Ispat Steel and Jindal Vijayanagar Steel Limited, JSW Steel became India's second largest private sector steel company."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def kotak():
    file_path = "static/kotak.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Kotak Mahindra Bank Limited is an Indian banking and financial services company headquartered in Mumbai. It offers banking products and financial services for corporate and retail customers in the areas of personal finance, investment banking, life insurance, and wealth management. It is India's third largest private sector bank by market capitalisation after HDFC Bank and ICICI Bank. As of 31 March 2023, the bank has a national footprint of 1,780 branches and 2,963 ATMs."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def lti():
    file_path = "static/ltimind.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "LTIMindtree Limited is an Indian multinational information technology services and consulting company based in Mumbai. A subsidiary of Larsen & Toubro, the company was incorporated in 1996 and employs more than 82,000 people. It is one of the top Big Tech companies."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def lt():
    file_path = "static/lt.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Larsen & Toubro Limited, abbreviated as L&T, is an Indian multinational conglomerate, with interests in engineering, construction, manufacturing, technology, information technology, military and financial services. It is headquartered in Chennai. L&T was founded in 1938 in Bombay by Danish engineers Henning Holck-Larsen and Søren Kristian Toubro. As at March 31, 2022, the L&T Group comprises 93 subsidiaries, 5 associate companies, 27 joint ventures and 35 jointly held operations, operating across basic and heavy engineering, construction, realty, manufacturing of capital goods, information technology, and financial services. On October 1, 2023, Shri. S N Subrahmanyan took charge as Chairman and Managing Director of L&T."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def maruti():
    file_path = "static/maruti.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Maruti Suzuki India Limited is the Indian subsidiary of Japanese automaker Suzuki Motor Corporation. As of September 2022, the company had a leading market share of 42 percent in the Indian passenger car market."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def ntpc():
    file_path = "static/ntpc.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "NTPC Limited, formerly known as National Thermal Power Corporation, is an Indian central Public Sector Undertaking under the ownership of the Ministry of Power and the Government of India, who is engaged in the generation of electricity and other activities. The headquarters of the PSU are situated at New Delhi"
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def nestle():
    file_path = "static/nestle.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Nestlé India Limited is the Indian subsidiary of Nestlé which is a Swiss multinational company. The company is headquartered in Gurgaon, Haryana. The company's products include food, beverages, chocolate, and confectioneries. The company was incorporated on 28 March 1959 and was promoted by Nestle Alimentana S.A. via a subsidiary, Nestle Holdings Ltd. As of 2020, the parent company Nestlé owns 62.76% of Nestlé India. The company has 9 production facilities in various locations across India."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def ongc():
    file_path = "static/ongc.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "The Oil and Natural Gas Corporation Limited is an Indian central public sector undertaking under the ownership of Ministry of Petroleum and Natural Gas, Government of India. The company is headquartered in New Delhi. ONGC was founded on 14 August 1956 by the Government of India. It is the largest government-owned-oil and gas explorer and producer in the country and produces around 70 percent of India's domestic production of crude oil and around 84 percent of natural gas. In November 2010, the Government of India conferred the Maharatna status to ONGC. In a survey by the Government of India for fiscal year 2019–20, it was ranked as the largest profit making Central Public Sector Undertaking in India. It is ranked 5th among the Top 250 Global Energy Companies by Platts. ONGC is involved in exploring for and exploiting hydrocarbons in 26 sedimentary basins of India, and owns and operates over 11,000 kilometers of pipelines in the country. Its international subsidiary ONGC Videsh currently has projects in 15 countries. ONGC has discovered 7 out of the 8 producing Indian Basins, adding over 7.15 billion tonnes of In-place Oil & Gas volume of hydrocarbons in Indian basins."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def powergrid():
    file_path = "static/powergrid.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Power Grid Corporation of India Limited is an Indian central public sector undertaking under the ownership of the Ministry of Power, Government of India. It is engaged mainly in transmission of bulk power across different states of India. It is headquartered in Gurugram. Power Grid transmits about 50% of the total power generated in India on its transmission network."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def reliance():
    file_path = "static/reliance.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Reliance Industries Limited is an Indian multinational conglomerate headquartered in Mumbai. Its businesses include energy, petrochemicals, natural gas, retail, telecommunications, mass media, and textiles. Reliance is the largest public company in India by market capitalisation and revenue, and the 100th largest company worldwide. It is India's largest private tax payer and largest exporter, accounting for 7% of India's total merchandise exports. The company has relatively little free cash flow and high corporate debt"
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def sbilife():
    file_path = "static/sbin.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "SBI Life Insurance Company Limited is an Indian life insurance company which was started as a joint venture between State Bank of India and French financial institution BNP Paribas Cardif. SBI has a 55.50% stake in the company and BNP Paribas Cardif owns a 0.22% stake. Other investors are Value Line Pte. Ltd. and MacRitchie Investments Pte. Ltd., holding a 1.95% stake each while the remaining 12% is free float stake with public investors.It has Assets under management worth ₹352,422 crore and a Gross Written Premium of ₹67,320 crore as of March 2023. SBI Life has an authorized capital of ₹20 billion and a paid up capital of ₹10 billion. In 2007, CRISIL Limited, a subsidiary of global rating agency Standard & Poor's, gave the company a AAA/Stable/P1+ rating."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def sbi():
    file_path = "static/sbi.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "State Bank of India is an Indian multinational public sector bank and financial services statutory body headquartered in Mumbai, Maharashtra. SBI is the 48th largest bank in the world by total assets and ranked 221st in the Fortune Global 500 list of the world's biggest corporations of 2020, being the only Indian bank on the list. It is a public sector bank and the largest bank in India with a 23% market share by assets and a 25% share of the total loan and deposits market. It is also the tenth largest employer in India with nearly 250,000 employees. On 14 September 2022, State Bank of India became the third lender and seventh Indian company to cross the ₹ 5-trillion market capitalisation on the Indian stock exchanges for the first time. The bank descends from the Bank of Calcutta, founded in 1806 via the Imperial Bank of India, making it the oldest commercial bank in the Indian subcontinent. The Bank of Madras merged into the other two presidency banks in British India, the Bank of Calcutta and the Bank of Bombay, to form the Imperial Bank of India, which in turn became the State Bank of India in 1955."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def sun():
    file_path = "static/sun.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Sun Pharmaceutical Industries Limited is an Indian multinational pharmaceutical company headquartered in Mumbai, that manufactures and sells pharmaceutical formulations and active pharmaceutical ingredients in more than 100 countries across the globe. It is the largest pharmaceutical company in India and the fourth largest specialty generic pharmaceutical company in the world. The products cater to a vast range of therapeutic segments covering psychiatry, anti-infectives, neurology, cardiology, diabetology, gastroenterology, ophthalmology, nephrology, urology, dermatology, gynaecology, respiratory, oncology, dental and nutritionals. Its active pharmaceutical products include baricitinib, brivaracetam, and dapaglifozin."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def tcs():
    file_path = "static/tcs.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Tata Consultancy Services Limited is an Indian multinational information technology services and consulting company headquartered in Mumbai. It is a part of the Tata Group and operates in 150 locations across 46 countries. In September 2023, it was reported that TCS had over 616,000 employees worldwide. TCS is the second-largest Indian company by market capitalization, the most valuable IT service brands worldwide, and the top Big Tech company. As of June 2023, it was the world's second-largest user of U.S. H-1B visas. As of 2021, it was ranked seventh on the Fortune India 500 list. In September 2021, TCS recorded a market capitalization of US$200 billion, making it the first Indian IT tech company to do so. In 2016–2017, parent company Tata Sons owned 72.05% of TCS and more than 70% of Tata Sons' dividends were generated by TCS."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def tcp():
    file_path = "static/tataconsumer.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Tata Consumer Products is an Indian fast-moving consumer goods company and a part of the Tata Group. Its registered office is located in Kolkata while its corporate headquarters is in Mumbai. It is the world's second-largest manufacturer and distributor of tea and a major producer of coffee. Formerly known as Tata Global Beverages Limited, Tata Consumer Products was formed when the consumer products business of Tata Chemicals merged with Tata Global Beverages in February 2020. The company now operates in the food and beverages industry, with ~56% of their revenue coming from India while the rest is from their international businesses. After the merger, the company controls Indian and international brands like Tata Salt, Tata Tea, Tetley, Eight O'Clock Coffee, Good Earth Tea, Tata Sampann and Tata Starbucks. Tata Tea is the biggest-selling tea brand in India. Tetley is the biggest-selling tea brand in Canada and the second-biggest-selling in the United Kingdom and the United States."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def tm():
    file_path = "static/tatamotors.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Tata Motors Limited is an Indian Multinational automotive company, headquartered in Mumbai and part of the Tata Group. The company produces cars, trucks, vans, and busses. Subsidiaries include British Jaguar Land Rover and South Korean Tata Daewoo. Tata Motors has a joint ventures with Hitachi and Stellantis, which makes vehicle parts for Fiat Chrysler and Tata-branded vehicles. On 12 October 2021, private equity firm TPG invested $1 billion in Tata Motors' electric vehicle subsidiary. Tata Motors has auto manufacturing and vehicle plants in Jamshedpur, Pantnagar, Lucknow, Sanand, Dharwad, and Pune in India, as well as in Argentina, South Africa, the United Kingdom, and Thailand. It has research and development centres in Pune, Jamshedpur, Lucknow, Dharwad, India and South Korea, the United Kingdom, and Spain. Tata Motors is listed on the BSE, where it is a constituent of the BSE SENSEX index, the National Stock Exchange of India, and the New York Stock Exchange. The company is ranked 265th on the Fortune Global 500 list of the world's biggest corporations as of 2019. On 17 January 2017, Natarajan Chandrasekaran was appointed chairman of the company Tata Group."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def tatasteel():
    file_path = "static/tatasteel.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Tata Steel Limited is an Indian multinational steel-making company, based in Jamshedpur, Jharkhand and headquartered in Mumbai, Maharashtra. It is a part of the Tata Group. Formerly known as Tata Iron and Steel Company Limited, Tata Steel is among the largest steel producing companies in the world, with an annual crude steel capacity of 35 million tonnes. It is one of the world's most geographically diversified steel producers, with operations and commercial presence across the world. The group recorded a consolidated turnover of US$31 billion in the financial year ending 31 March 2023. It is the largest steel company in India with an annual capacity of 21.6 million tonnes after Steel Authority of India Ltd. Tata Steel, SAIL, and Jindal Steel and Power, are the only three Indian steel companies that have captive iron-ore mines, which gives the three companies price advantages. Tata Steel operates in 26 countries with key operations in India, the Netherlands, and the United Kingdom, and employs around 80,500 people. Its largest plant is located in Jamshedpur, Jharkhand. In 2007, Tata Steel acquired the UK-based steel maker Corus."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def techmahindra():
    file_path = "static/techmahindra.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Tech Mahindra is an Indian multinational information technology services and consulting company. Part of the Mahindra Group, the company is headquartered in Pune and has its registered office in Mumbai. Tech Mahindra has over 146,000 employees across 90 countries. The company was ranked #5 in India's IT firms and overall No. 47 on Fortune India 500 list for 2019. On 25 June 2013, Tech Mahindra announced the completion of a merger with Mahindra Satyam. Tech Mahindra is one of the top Big Tech companies. Tech Mahindra has 1,262 active clients as of June 2022."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def titan():
    file_path = "static/titan.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Titan Company Limited is an Indian company that mainly manufactures luxury fashion accessories such as jewellery, watches and eyewear. Part of the Tata Group and started as a joint venture with the TIDCO, the company has its corporate headquarters in Electronic City, Bangalore, and registered office in Hosur, Tamil Nadu. Titan Company commenced operations in 1984 under the name Titan Watches Limited. In 1994, Titan diversified into jewellery with Tanishq and subsequently into eyewear with Titan Eyeplus. In 2005, it launched its youth fashion accessories brand Fastrack. The company is the largest branded jewellery maker in India, with more than 80% of its total revenues coming from the jewellery segment. As of 2022, Titan has a 6% market share in India's jewellery market. As of 2019, it is also the fifth-largest watch manufacturer in the world."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def upl():
    file_path = "static/upl.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "UPL Limited, formerly United Phosphorus Limited, is an Indian multinational company that manufactures and markets agrochemicals, industrial chemicals, chemical intermediates, and specialty chemicals, and also offers pesticides. Headquartered in Mumbai, Maharashtra, the company engages in both agro and non-agro activities. The agro-business is the company's primary source of revenue and includes the manufacture and marketing of conventional agrochemical products, seeds, and other agricultural-related products. The non-agro segment includes manufacturing and marketing industrial chemicals and other nonagricultural products such as fungicides, herbicides, insecticides, plant growth regulators, rodenticides, industrial & specialty chemicals, and nutrifeeds. UPL products are sold in 150+ countries. United Phosphorus Limited was established on 29 May 1969. The company changed its name to UPL Limited in October 2013. On 20 July 2018, UPL signed a US$4.2 billion agreement with Platform Specialty Products Corporation to acquire control of Arysta LifeScience Inc."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def ultratech():
    file_path = "static/ultratech.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "UltraTech Cement Limited is an Indian multinational cement company based in Mumbai. It is the largest manufacturer of grey cement, ready-mix concrete and white cement in India and 5th largest around the globe with an installed capacity of 133 million tonnes per annum and 105.71 million tonnes per annum sales volume."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def wipro():
    file_path = "static/wipro.png"
    try:
        with open(file_path, "rb") as file:
            png_data = file.read()
            png_base64 = base64.b64encode(png_data).decode("utf-8")
        info = "Wipro is an Indian multinational corporation that provides information technology, consultant and business process services. It is one of the leading Big Tech companies. Wipro's capabilities range across cloud computing, computer security, digital transformation, artificial intelligence, robotics, data analytics, and other technology consulting services to customers in 167 countries."
        return png_base64, info
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def stock_name_info(stock_name):
    if stock_name == "Adani Enterprises Ltd":
        return adanient()

    if stock_name == "Adani Ports and Special Economic Zone Ld":
        return adanisez()

    if stock_name == "Apollo Hospitals Enterprise Limited":
        return apollo()

    if stock_name == "Asian Paints Ltd":
        return asian()

    if stock_name == "Axis Bank Ltd":
        return axis()

    if stock_name == "Bajaj Auto Ltd":
        return bajaj()

    if stock_name == "Bajaj Finance Ltd":
        return bajajfinance()

    if stock_name == "Bajaj Finserv Ltd":
        return bajajfin()

    if stock_name == "Bharat Petroleum Corporation Ltd":
        return bpl()

    if stock_name == "Bharti Airtel Ltd":
        return airtel()

    if stock_name == "Britannia Industries Ltd":
        return brit()

    if stock_name == "Cipla Ltd":
        return cipla()

    if stock_name == "Coal India Ltd":
        return coal_india()

    if stock_name == "Divi's Laboratories Ltd":
        return divi()

    if stock_name == "Dr Reddy's Laboratories Ltd":
        return reddy()

    if stock_name == "Eicher Motors Ltd":
        return eicher()

    if stock_name == "Grasim Industries Ltd":
        return grasim()

    if stock_name == "HCL Technologies Ltd":
        return hcl()

    if stock_name == "HDFC Bank Ltd":
        return hdfc()

    if stock_name == "HDFC Life Insurance Company Ltd":
        return hdfclife()

    if stock_name == "Hero MotoCorp Ltd":
        return hero()

    if stock_name == "Hindalco Industries Ltd":
        return hindalco()

    if stock_name == "Hindustan Unilever Ltd":
        return unilever()

    if stock_name == "ICICI Bank Ltd":
        return icici()

    if stock_name == "ITC Ltd":
        return itc()

    if stock_name == "Indusind Bank Ltd":
        return indusind()

    if stock_name == "Infosys Ltd":
        return infosys()

    if stock_name == "JSW Steel Limited":
        return jsw()

    if stock_name == "Kotak Mahindra Bank Ltd Fully Paid Ord. Shrs":
        return kotak()

    if stock_name == "LTIMindtree Ltd":
        return lti()

    if stock_name == "Larsen and Toubro Ltd":
        return lt()

    if stock_name == "Maruti Suzuki India Ltd":
        return maruti()

    if stock_name == "NTPC Ltd":
        return ntpc()

    if stock_name == "Nestle India Limited":
        return nestle()

    if stock_name == "Oil and Natural Gas Corporation Ltd":
        return ongc()

    if stock_name == "Power Grid Corporation of India Ltd":
        return powergrid()

    if stock_name == "Reliance Industries Ltd":
        return reliance()

    if stock_name == "Sbi Life Insurance Company Ltd":
        return sbilife()

    if stock_name == "State Bank of India":
        return sbi()

    if stock_name == "Sun Pharmaceutical Industries Ltd":
        return sun()

    if stock_name == "Tata Consultancy Services Ltd":
        return tcs()

    if stock_name == "Tata Consumer Products Ltd":
        return tcp()

    if stock_name == "Tata Motors Ltd Fully Paid Ord. Shrs":
        return tm()

    if stock_name == "Tata Steel Ltd":
        return tatasteel()

    if stock_name == "Tech Mahindra Ltd":
        return techmahindra()

    if stock_name == "Titan Company Ltd":
        return titan()

    if stock_name == "UPL Ltd":
        return upl()

    if stock_name == "UltraTech Cement Ltd":
        return ultratech()

    if stock_name == "Wipro Ltd":
        return wipro()

# Scrape US Justice


All files from US Justice and Archive that contain "China" and one of these keywords:

US Justice: https://www.justice.gov/news

Archive: https://www.justice.gov/archives/doj-archive (this have connections to local websites(ex: Arizona Justice; California Justice) with the files) -> more than 50 differents layouts

"intellectual property theft"
"trade secrets"
"patent infrigement"
"trademark"
"copyright"
"trade secrets"
"economic espionage"
"industrial espionage"
"cyberattack"
"cybercrime"


- Data inside folder "data"
- scrape_by_keywords.py (step 1)
- scrap_text_website_after2009.ipynb (step 3/4) - us justice website
- scrap_text_archive.ipynb (step 3/4) - archive website 
- classification_by_year.py (step 6)

Process extraction by steps:

1 - Scrap title + link (which contains keywords)

2 - Search one by one with the link previosly scrapped

3 - Extract text and date from webpage

4 - Create pdf and insert in correct year named folder

If date/text can't be extracted in step 3, download all page to pdf file and:

5 - Read pdf into text 

6 - Search with regex for the first appearance of year "re.compile('|'.join('years'))" - years is a list of all years from 1994 to 2020

7 - Move to correct folder (year named folder)

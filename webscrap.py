import requests
from bs4 import BeautifulSoup

def get_data():

  link = "https://boards.greenhouse.io/embed/job_board?for=coursera"

  res = requests.get(link)

  soup = BeautifulSoup(res.text , "html.parser")
  
  divs = soup.findAll(class_= 'opening')    

  jobs = []

  for div in divs:

      data = {}

      data["Job description"] = div.find("a").text

      data["job link"] = div.find("a" , href=True)['href']

      data["Location"] = div.find("span").text

      jobs.append(data)
    
  return jobs

    
jobs = get_data()

print(jobs)

"""

output:

[{'Job description': 'Content Strategy Manager, Computer Science & Technology',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4645401004',
  'Location': 'United States'},
 {'Job description': 'Engineering Manager',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4614435004',
  'Location': 'Bulgaria'},
 {'Job description': 'Senior Software Engineer, Back End',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4710854004',
  'Location': 'Bulgaria'},
 {'Job description': 'Sr Software Engineer - Application Architecture',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4606915004',
  'Location': 'Canada'},
 {'Job description': 'Equity Accountant',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4703409004',
  'Location': 'United States'},
 {'Job description': 'Senior Data Scientist, Analytics',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4660113004',
  'Location': 'Canada'},
 {'Job description': ' Senior Data Scientist - Insight',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4659828004',
  'Location': 'Canada'},
 {'Job description': 'Senior Machine Learning Scientist - Search',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4674413004',
  'Location': 'United States'},
 {'Job description': 'Staff Machine Learning Engineer',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4668328004',
  'Location': 'Canada'},
 {'Job description': 'Staff Machine Learning Scientist - Recommendation',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4612922004',
  'Location': 'United States'},
 {'Job description': 'Enterprise Account Executive - Public Sector',
  'job link': 'https://about.coursera.org/careers/jobs?gh_jid=4687783004',
  'Location': 'United States'}]

"""

#feel free to run the code on google-colab

#https://colab.research.google.com/drive/1bcpl5b5CAdqC_goHmKic2n23vmCSDU1T?usp=sharing
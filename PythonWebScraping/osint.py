from bs4 import BeautifulSoup
import requests
import os, os.path, csv
import pandas as pd

listingurl = "http://www.espn.com/college-sports/football/recruiting/databaseresults/_/sportid/24/class/2006/sort/school/starsfilter/GT/ratingfilter/GT/statuscommit/Commitments/statusuncommit/Uncommited"
df_list = pd.read_html(listingurl)
df_list[0].to_csv("footballers.csv")

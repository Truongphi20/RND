import requests
from lxml import etree
import pandas as pd
import plotly.express as px

def YearCount(terme):
	ncbi_url = 'https://pubmed.ncbi.nlm.nih.gov/'
	payload = {
		'term': terme,
		'size':50
	}

	handle = requests.get(ncbi_url, params=payload)

	text = handle.text
	# print(text)

	html_file = etree.HTML(text)

	xpath_years = '//*[@id="timeline-table"]/tbody/tr/td[1]/text()'
	xpath_count = '//*[@id="timeline-table"]/tbody/tr/td[2]/text()'

	years = list(map(lambda x: x.strip(),html_file.xpath(xpath_years)))
	# print(years)

	counts = list(map(lambda x: int(x.strip()),html_file.xpath(xpath_count)))
	# print(counts)

	table = pd.DataFrame(zip(years, counts), columns=["Year", "Count"])
	# print(table)
	return table

def Xticks(Years):
	minyear = Years[0]
	# print(minyear)

	xtich = [year for year in Years if (int(year) - int(minyear))%5 == 0]
	# print(xtich)
	return xtich

def PrintPlotYear(table):

	fig = px.bar(table, x='Year', y='Count')
	return fig



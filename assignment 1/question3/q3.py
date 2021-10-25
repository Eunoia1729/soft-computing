"""## Question 3: Scrap Hotel Data

The below code is for India and can be extended to other countries by adding an outer loop given in the last part. The below codes takes several minutes to run.
"""
import requests
import pandas as pd  
from bs4 import BeautifulSoup

hotelname_list = []
city_list = []
countries_list = []
rating_list = []
prince_list = []
Amenities_list = []
HotelDescription_list = []
Review1_list = []
Review2_list = []

hotel_name = ""
city_name = ""
country_name = ""
ratingl = ""
pricel = ""
amenities = ""
descriptionl = ""
review1l = ""
review2l = ""

url = 'https://www.goibibo.com/destinations/all-states-in-india/'
data = requests.get(url)
html = data.text
soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', {'class' : 'col-md-4 col-sm-4 col-xs-12 filtr-item posrel'})
state_urls = []
state_names = []
for card in cards :
	for a in card.find_all('a', href=True):
		if a.text.rstrip():
			state_urls.append(a['href'])
			state_names.append(a.text.rstrip())
length = len(state_urls)
for i in range(length):
  url = state_urls[i]
  country_name = 'India'
  data = requests.get(url)
  html = data.text
  soup = BeautifulSoup(html, 'html.parser')
  places_to_visit = soup.find('div', {'class' : 'place-to-visit-container'})
  if(places_to_visit):
    card = places_to_visit.find('div', {'class' : 'col-md-12'})
    city_urls = {}
    for a in card.find_all('a', href=True):
      if a['href']:
        list = a['href'].split('/')
        city_urls[list[4]] = 'https://www.goibibo.com/hotels/hotels-in-' + list[4] + '-ct/'

    for city in city_urls:
      print(f'Extracting for city : {city}')
      city_name = city
      url = city_urls[city]
      response = requests.get(url)
      data = BeautifulSoup(response.text, 'html.parser')
      cards_price_data = data.find_all('p', attrs={'class', 'HotelCardstyles__CurrentPrice-sc-1s80tyk-27 czKsrL'})
      cards_url_data = data.find_all('div', attrs={'class', 'HotelCardstyles__HotelNameWrapperDiv-sc-1s80tyk-11 hiiHjq'})
      hotel_price = {}
      hotel_url = {}
      for i in range(0, len(cards_price_data)):
        hotel_price[cards_url_data[i].text.rstrip()] = cards_price_data[i].text.rstrip()
        hotel_url[cards_url_data[i].text.rstrip()] = 'https://www.goibibo.com' + cards_url_data[i].find('a', href = True)['href']
      for i in range(0, len(cards_price_data)):
        url = hotel_url[cards_url_data[i].text.rstrip()]
        data = requests.get(url)
        html = data.text
        hotel_name = cards_url_data[i].text.rstrip()
        pricel = hotel_price[cards_url_data[i].text.rstrip()]
        # print('Extracting for hotel : ' + cards_url_data[i].text.rstrip())
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', { 'id': 'root' })
        description = div.find('section', {'class' : 'HotelDetailsMain__HotelDetailsContainer-sc-2p7gdu-0 kpmitu'})
        descriptiont = description.find('span', {'itemprop' : 'streetAddress'})
        if descriptiont:
          address = descriptiont.text.rstrip().replace(' View on Map', '')
        descriptionl = address

        rating = 'Rating not found'
        ratingdata = description.find('span', {'itemprop' : 'ratingValue'}) #contains rating
        if ratingdata:
          rating = ratingdata.text.rstrip()
        ratingl = rating

        review1 = 'Review not found'
        review2 = 'Review not found'
        reviews = div.find_all('span', {'class' : 'UserReviewstyles__UserReviewTextStyle-sc-1y05l7z-4 dTkBBw'})
        
        if(len(reviews) > 1):
          review1 = reviews[0].text.rstrip()
        if(len(reviews) > 3):
          review2 = reviews[3].text.rstrip()
        review1l = review1
        review2l = review2

        amenities_list = []  #contains all the amenities.
        amenitiesdiv = div.find('div', {'class' : 'Amenitiesstyles__AmenitiesListBlock-sc-10opy4a-4 cMbIgg'})
        if amenitiesdiv:
          for amenity in amenitiesdiv.find_all('span', {'class':'Amenitiesstyles__AmenityItemText-sc-10opy4a-8 iwRmcg'}) :
            if amenity:
              amenities_list.append(amenity.text.rstrip())
            else:
              amenities_list.append('Amenity Not Found')
        amenities = amenities_list
        hotelname_list.append(hotel_name)
        city_list.append(city_name)
        countries_list.append(country_name)
        rating_list.append(ratingl)
        prince_list.append(pricel)
        Amenities_list.append(amenities)
        HotelDescription_list.append(descriptionl)
        Review1_list.append(review1l)
        Review2_list.append(review2l)
      
      print(f'Extracted {len(cards_price_data)} hotels at {city} successfully')
dict = {'Hotel_Name': hotelname_list, 'City_Name': city_list, 'country_name': countries_list,
				'Rating' : rating_list, 'Price/Night' : prince_list, 'Amenities' : Amenities_list,
				'Description' : HotelDescription_list, 'Review1' : Review1_list, 'Review2' : Review2_list}
df = pd.DataFrame(dict)
df.to_csv('hotels.csv')

"""To extract for all the countries, we need to use the below code in the outer loop"""

hotelname_list = []
city_list = []
countries_list = []
rating_list = []
prince_list = []
Amenities_list = []
HotelDescription_list = []
Review1_list = []
Review2_list = []

hotel_name = ""
city_name = ""
country_name = ""
ratingl = ""
pricel = ""
amenities = ""
descriptionl = ""
review1l = ""
review2l = ""

url = 'https://www.goibibo.com/destinations/intl/all-countries/'
data = requests.get(url)
html = data.text
soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', {'class' : 'col-md-4 col-sm-4 col-xs-12 filtr-item posrel'})
country_urls = []
country_names = []
for card in cards :
  for a in card.find_all('a', href=True):
    if a['href']:
      country_urls.append(a['href'])
      country_names.append(a.text.rstrip())
length = len(country_urls)
for i in range(length):
  url = country_urls[i]
  country_name = country_names[i]
  data = requests.get(url)
  html = data.text
  soup = BeautifulSoup(html, 'html.parser')
  places_to_visit = soup.find('div', {'class' : 'place-to-visit-container'})
  if(places_to_visit):
    card = places_to_visit.find('div', {'class' : 'col-md-12'})
    city_urls = {}
    for a in card.find_all('a', href=True):
      if a['href']:
        list = a['href'].split('/')
        city_urls[list[3]] = 'https://www.goibibo.com/hotels/intl-hotels-in-' + list[3] + '-ct/'
  print(country_name)
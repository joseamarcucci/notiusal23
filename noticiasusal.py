import streamlit as st
st.set_page_config(
page_title="Estadísticas Noticias USAL",
page_icon="https://webinars.usal.edu.ar/sites/default/files/favicon.ico",
layout="wide",
initial_sidebar_state="expanded",)
import argparse  
import smtplib




import ssl
import altair as alt
from altair import *
import streamlit.components.v1 as components
import requests
import re
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as url
import gspread
import pandas as pd

import os 
import IPython

import os
import re

import folium
import pandas as pd
import socket
import socks
import base64
from decouple import Config, RepositoryEnv
from PIL import Image
from io import BytesIO
import ftplib
from ftplib import FTP
from bs4 import BeautifulSoup
import requests
from oauth2client.service_account import ServiceAccountCredentials
urllib.request.urlretrieve('https://entendiste.ar/mail/service_account.json',"service_account.json")
from gspread import authorize
from decouple import Config, RepositoryEnv
DOTENV_FILE = 'jamis.env'
env_config = Config(RepositoryEnv(DOTENV_FILE))
ruta='/es'
ids = env_config.get('idsheet')
plani = env_config.get('plani')
userID = env_config.get('userID')
password = env_config.get('password')
api = env_config.get('api')
secret = env_config.get('secret')

scopes = ["https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/drive"] 
cred = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scopes)
from googleapiclient.discovery import build
import argparse
import streamlit as st
import streamlit.components.v1 as components
from apiclient.discovery import build
import httplib2
import re
import numpy as np
from oauth2client import client
from oauth2client import file
from oauth2client import tools
import urllib.request
import urllib.request as url
import argparse
import plotly.express as px
import pandas as pd
import urllib.request
import urllib.request as url
from gspread import authorize
from decouple import Config, RepositoryEnv
DOTENV_FILE = 'jamis.env'
env_config = Config(RepositoryEnv(DOTENV_FILE))
ids = env_config.get('idsheet')
plani = env_config.get('plani')
from apiclient.discovery import build 
from oauth2client.service_account import ServiceAccountCredentials
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Oswald" rel="stylesheet"><style>.css-tsy3mu,.streamlit-expanderHeader{font-size:18px;font-family: Oswald;}.st-f8, .st-b7 ,.st-fd ,.st-fe ,.st-ff ,.st-fg ,.st-fh,.st-fi,.st-fj, .st-fk,.css-1lcbmhc, .st-bv{font-family: Oswald;}.css-1ekf893 {margin-bottom: -1rem;font-family: Oswald;}.css-1v0mbdj {margin-top: -60px;}body{font-family: "Oswald", Arial, sans-serif;}</style>', unsafe_allow_html=True)
import datetime
from datetime import date
st.session_state['key'] = 0
st.session_state['key1'] = 0
st.session_state['key2'] = 0
st.session_state['key33'] = 109403
today = date.today()
today=today.strftime('%d/%m/%Y')
#st.sidebar.markdown('<img style=" margin-top: -70px;width:80%;" src="https://noticias.usal.edu.ar/sites/default/files/logon_1.jpg" />', unsafe_allow_html=True)

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly',"https://www.googleapis.com/auth/spreadsheets"]
DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
urllib.request.urlretrieve('https://entendiste.ar/mail/service_account.json',"service_account.json")                  
credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", SCOPES)
CLIENT_SECRETS_PATH = 'client_secret_analytics.json'
url_kwargs = {
    'view_id': 201209640,  # Can be obtained from here: https://ga-dev-tools.appspot.com/account-explorer/
    'get_args': 'metrics=rt:activeusers',  # https://developers.google.com/analytics/devguides/reporting/realtime/v3/reference/data/realtime/get
  'get_devi':'dimensions=rt:deviceCategory'
}
credentials2 = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scopes=['https://www.googleapis.com/auth/analytics.readonly'])
session = requests.Session()
session.headers= {'Authorization': 'Bearer ' + credentials2.get_access_token().access_token}
response = session.get('https://www.googleapis.com/analytics/v3/data/realtime?ids=ga:{view_id}&{get_args}'.format(**url_kwargs))
response.raise_for_status()
response2 = session.get('https://www.googleapis.com/analytics/v3/data/realtime?ids=ga:{view_id}&{get_args}&{get_devi}'.format(**url_kwargs))
response2.raise_for_status()
x = response.json()
x2 = response2.json()

#df0 = pd.DataFrame(x['rows'])
#vivo=df0.iat[0,0]
 

#df = pd.DataFrame(x2['rows'])

#vivod=df.iat[1,1]
#vivom=df.iat[0,1]
col1, col2,col3,col4,col5 = st.beta_columns([1,1,1,1,1])
#vivod=df.iat[1,1]
#vivom=df.iat[0,1]
col3.image("https://noticias.usal.edu.ar/sites/default/files/inline-images/logo1_0.png")

st.markdown('<div style="text-align:center; border-bottom:3px double #008357;border-top:1px solid #008357;font-family: Oswald; margin-top:-10px;font-size:20px;">NOTICIAS USAL</div><div style="text-align:center; font-size:18px;border-bottom:1px solid #008357;font-family: Oswald"><b>ESTADÍSTICAS DESDE EL 15/3/2019 AL '+today+'</b></div>', unsafe_allow_html=True)
arriba=st.empty()

#st.sidebar.markdown('<div style="text-align:center; border-bottom:3px double #008357;border-top:1px solid #008357;font-family: Oswald; margin-top:-10px;font-size:20px;">NOTICIAS USAL</div><br>', unsafe_allow_html=True)
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Oswald" rel="stylesheet"><style>.css-tsy3mu,.streamlit-expanderHeader{font-size:18px;font-family: Oswald;}.st-f8, .st-b7 ,.st-fd ,.st-fe ,.st-ff ,.st-fg ,.st-fh,.st-fi,.st-fj, .st-fk,.css-1lcbmhc, .st-bv{font-family: Oswald;}.css-1ekf893 {margin-bottom: -1rem;font-family: Oswald;}.css-1v0mbdj {margin-top: -60px;}body{font-family: "Oswald", Arial, sans-serif;}</style>', unsafe_allow_html=True)
#st.markdown('<div style="text-align:left; font-size:18px;border-bottom:1px solid #008357;font-family: Oswald"><b>ESTADÍSTICAS DESDE EL 15/3/2019 AL '+today+'</b></div>', unsafe_allow_html=True)
#st.sidebar.markdown('<div style="text-align:center; ;font-family: Oswald; margin-top:-10px;font-size:18px;">En este momento:</div>', unsafe_allow_html=True)
#st.sidebar.markdown('<div style="text-align:center; ;font-family: Oswald; margin-top:-10px;font-size:24px;color:#e65100;"> '+vivo+' </div>', unsafe_allow_html=True)
#st.sidebar.markdown('<div style="text-align:center; border-bottom:3px double #008357;font-family: Oswald; margin-top:-10px;font-size:16px;">usuarios activos en el sitio</div>', unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
       
footer {visibility: hidden;}
#header {visibility: hidden;}

.css-4zfol6{display:none;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown("""
<style>
.css-zx8yrj {
    padding: 0.2rem 0.4rem;
    z-index: 101;
    opacity: 1;
    font-family: Oswald;
text-align: left;
    transition: opacity 300ms ease 0s;
    border: 0px;
    color: rgb(38, 39, 48);
}
.css-4ux067 {
    width: 1514px;
    margin: 0px 0px 1rem;
    text-align: center;
}
.css-nlntq9 {
    font-family: Oswald;
    text-transform: uppercase;
    font-weight: bold;
 
}
.css-y37zgl {
    font-size: 1rem;
    font-family: Oswald;
    text-align: center;
    padding: 0.5rem;
    line-height: 1.3;
}
.css-165ax5l {
    width: 100%;
    margin-bottom: 1rem;
    color: rgb(49, 51, 63);
    border-collapse: collapse;
    border: 0;
    /* border: 1px solid rgba(49, 51, 63, 0.1); */
}
.css-nlntq9{
 font-family: Oswald;
}
.st-by, .st-cd , .st-ce , .st-ae , .st-af , .st-ag , .st-ah , .st-ai , .st-aj {
   font-family: Oswald;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>


.css-glyadz {
    font-size: 1rem;
    color: rgb(38, 39, 48);
    margin-bottom: 0.4rem;
    height: 1.5rem;
    vertical-align: middle;
    display: flex;
    flex-direction: row;
    -webkit-box-align: center;
    align-items: center;
}.css-7uy1ct {
    width: 1200px;
    margin: 0px 0px 1rem;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
make_map_responsive= """
     <style>
     [title~="st.iframe"] { width: 100%}
     </style>
    """
st.markdown(make_map_responsive, unsafe_allow_html=True)
#display_code = st.sidebar.radio("Mostrar", ( "Totales x país","Por número","Búsqueda"))
def total():
  st.markdown("""
  <style>
  table td:nth-child(1) {
      display: none
  }
  table th:nth-child(1) {
      display: none
  }


  </style>
  """, unsafe_allow_html=True)
  VIEW_ID = '201209640'#'201209640'
  ruta='es/'
  
  date = datetime.date(2019, 3, 15)
  date2 = date.today()
  
  col1, col2,col3,col4,col5 = st.beta_columns([1,1,1,1,1])
  #import pycountry

  #countries = pd.DataFrame()
  #data = [[country.name] for country in pycountry.countries]
  DEFAULT='Seleccionar'
  def selectbox_with_default(text, values, default=DEFAULT, sidebar=False):
    func = st.selectbox #if sidebar else st.selectbox
    return func(text, np.insert(np.array(values, object), 0, default))
  
  #idioma=col3.select_slider("", ["Español", "Inglés"])

  container=st.empty()

  def initialize_analyticsreporting():
      parser = argparse.ArgumentParser(
          formatter_class=argparse.RawDescriptionHelpFormatter,
          parents=[tools.argparser])
      flags = parser.parse_args([])
      credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", SCOPES)
      if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, flags)
      http = credentials.authorize(http=httplib2.Http())
      analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)
      return analytics
  def checker(txt):
    try:
        float(txt)
        return False
    except:
        return True 


  def get_report5(analytics):
    return analytics.reports().batchGet(
      body=
      {"reportRequests":[{"viewId": VIEW_ID,'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],"metrics":[{"expression": "ga:pageviews"}],

          "dimensions": [{"name": "ga:country"}],

                    'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ],
        }
       ]
          }
        ]
          }] }
          ).execute() 

  def print_responsepais(response):
           
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)
            #fig = px.bar(df, x = "ga:country", y = "ga:pageviews")
            #col1.plotly_chart(fig, use_container_width=True)
            df=df.sort_values(by=['ga:pageviews'],ascending=False) 
            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
            
            df.columns =['País','Visitas']
            #st.table(df)
            values = df['País'].tolist()
            pais=st.selectbox('Paises desde los cuales hubo visitas:', values)
            
            st.session_state['key'] = pais
          except ValueError as ve:
                      st.warning('No hay visitas') 
          #st.table(df )
          return df
  def print_responsepaisolo(response):
           
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)
            df=df[~df["ga:country"].str.contains('(not set)')]
            #fig = px.bar(df, x = "ga:country", y = "ga:pageviews")
            #col1.plotly_chart(fig, use_container_width=True)
            df=df.sort_values(by=['ga:pageviews'],ascending=False) 
            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
            
            df.columns =['País','Visitas']
           
            
            st.session_state['key'] = pais
          except ValueError as ve:
                      st.warning('No hay visitas') 
          st.table(df )
          return df
  analytics = initialize_analyticsreporting()
  response = get_report5(analytics) #get the response from the API

  print_responsepais(response)



  #countries = pd.DataFrame(data, columns=['name'])
  
  
    
  pais=st.session_state.key#selectbox_with_default('País:',countries)
          
  def get_report20(analytics):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
            
              'metrics': [
          {
              'expression': 'ga:pageviews'
          }
       ]

          ,

                'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()
  def get_report0(analytics):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
            'dimensions':[{'name':'ga:date'}],         
            
             'metrics': [
          {
              'expression': 'ga:pageviews'
          }],
            'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ],              "dimensionName": "ga:country",
              "operator": "EXACT",
              "expressions": [pais]
        }
       ]
          }
        ]
          }]
        }
    ).execute()




  def get_report3(analytics):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
             'metrics': [{'expression': 'ga:pageviews'}],
                       'metrics': [
          {
              'expression': 'ga:pageviews'
          }],
           "dimensions": [
              {"name": "ga:deviceCategory"}
          ],
            'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()
  def get_reportdispo(analytics):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
             'metrics': [{'expression': 'ga:pageviews'}],
                       'metrics': [
          {
              'expression': 'ga:pageviews'
          }],
           "dimensions": [
              {"name": "ga:deviceCategory"}
          ],
            'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ],              "dimensionName": "ga:country",
              "operator": "EXACT",
              "expressions": [pais]
        }
       ]
          }
        ]
          }]
        }
    ).execute()


  def get_report55(analytics):
    return analytics.reports().batchGet(
      body=
      {"reportRequests":[{"viewId": VIEW_ID,'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],"metrics":[{"expression": "ga:pageviews"}],

          "dimensions": [{"name": "ga:country"},{"name": "ga:city"}],

                    'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         
         "expressions": [
          ruta
         ],              "dimensionName": "ga:country",
              "operator": "EXACT",
              "expressions": [pais]
         
        }

       ]
          }
        ]
          }] }
          ).execute()
  def get_report555(analytics):
    return analytics.reports().batchGet(
      body=
      {"reportRequests":[{"viewId": VIEW_ID,'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],"metrics":[{"expression": "ga:pageviews"}],

          "dimensions": [{"name": "ga:country"}],

                    'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         
         "expressions": [
          ruta
         ],              "dimensionName": "ga:country",
              "operator": "EXACT",
              "expressions": [pais]
         
        }

       ]
          }
        ]
          }] }
          ).execute()

  def get_reportcity555(analytics):
                      return analytics.reports().batchGet(body={
                      'reportRequests': [{
                          'viewId': VIEW_ID,
                          'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                       
                                     'metrics': [
          {
              'expression': 'ga:pageviews'
          }],
                        "dimensions": [{"name": "ga:country"},{"name": "ga:city"},
                              {"name": "ga:longitude"},
                              {"name": "ga:latitude"}
                          ],            'dimensionFilterClauses': [
                              {
                              'filters':[
                          {
                          "operator": "PARTIAL",
                          "dimensionName": "ga:pagePath",
                          "expressions": [
                            ruta
                          ],    "dimensionName": "ga:country",
              "operator": "EXACT",

            "expressions": [pais]    
         
        

                          }
                        ]
                            }
                          ]
                            }]
                          
                    }).execute()  
  def get_reportcity(analytics):
                      return analytics.reports().batchGet(body={
                      'reportRequests': [{
                          'viewId': VIEW_ID,
                          'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                       
                                     'metrics': [
          {
              'expression': 'ga:pageviews'
          }],
                        "dimensions": [
                              {"name": "ga:longitude"},
                              {"name": "ga:latitude"}
                          ],            'dimensionFilterClauses': [
                              {
                              'filters':[
                          {
                          "operator": "PARTIAL",
                          "dimensionName": "ga:pagePath",
                          "expressions": [
                            ruta
                          ]
                          }
                        ]
                            }
                          ]
                            }]
                          
                    }).execute()  
  def print_responsebar(response):
      #col1, col2 = st.beta_columns([1,1])  
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)

      df = pd.DataFrame(list)
      fig = px.pie(df, names = "ga:deviceCategory", values = "ga:pageviews")
      st.plotly_chart(fig, use_container_width=True)

      #col1.dataframe(df.assign(hack='').set_index('hack'),  height=600)
      df = pd.DataFrame(list)
      df.columns =['Dispositivo','Visitas']

      #col1.table(df)
      return df

  def print_responsed(response):
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)

            
            df=df.sort_values(by=['ga:date'],ascending=False) 
            df['ga:date'] = pd.to_datetime(df['ga:date']).dt.strftime('%d-%m-%y')



            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)

            df.columns =['','visitas']
            
            df['%']=df['visitas']/df['visitas'].sum()
            st.table(df)
          except ValueError as ve:
                      st.warning('No hay visitas')    
          return df
  

  def print_responsepais55(response):
           
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)
            df=df[~df["ga:city"].str.contains('(not set)')]
            #fig = px.bar(df, x = "ga:country", y = "ga:pageviews")
            #col1.plotly_chart(fig, use_container_width=True)
            df=df.sort_values(by=['ga:pageviews'],ascending=False)
            df02 = pd.DataFrame(df, columns=['ga:city','ga:pageviews']) 
            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
            #df.query('ga:country' == 'Argentina' , inplace = True)
            #values = df['ga:country'].tolist()
            #st.selectbox('Seleccionar pais', df02)
            
            DEFAULT='Argentina'
            def selectbox_with_default(text, values, default=DEFAULT, sidebar=False):
              func = st.selectbox #if sidebar else st.selectbox
              return func(text, np.insert(np.array(values, object), 0, default))
            
            #fig = px.line(df0[df0['ga:pagePath'] == a], 
            #x = "ga:pagePath", y = "ga:pagePath", title = a)
           
            options = ['Depot-Echouani','Lac-au-Saumon'] 
  
            df02 = df02.loc[~df02['ga:city'].isin(options)] 
            df03=df02[df02['ga:city'].apply(checker)]
            df03.columns =['Ciudad','Visitas']
            
          except ValueError as ve:
                      st.warning('No hay visitas') 
          st.table(df03)
          return df




 

  def print_response_side(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)
      try:
        df = pd.DataFrame(list)
        df.columns =['Visitas']


        #df = pd.DataFrame({'c1': destinatarios})
        df = df.reset_index()  # make sure indexes pair with number of rows





        for index, row in df.iterrows():
                st.session_state['key']=row['Visitas']+st.session_state.key

        #st.table(df)

        st.session_state['key']=st.session_state.key+1
      except ValueError as ve:
             st.warning('No hay visitas')    





      return df
  def print_response_side22(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)

      df = pd.DataFrame(list)
      df.columns =['Visitastodo']

      df = df.reset_index()  # make sure indexes pair with number of rows



      #st.sidebar.table(df)

      for index, row in df.iterrows():
              st.session_state['key33']=row['Visitastodo']+st.session_state.key33

      #fig1 = df.plot.bar()

      return df   

  def print_response_side2(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)

      df = pd.DataFrame(list)
      df.columns =['Pais','Visitas Totales']
      
      df = df.reset_index()  # make sure indexes pair with number of rows



      #st.sidebar.table(df)

      for index, row in df.iterrows():
              st.session_state['key1']=row['Visitas Totales']



      return df    
  def ga_response_dataframe(response):
      row_list = []
      # Get each collected report
      for report in response.get('reports', []):
          # Set column headers
          column_header = report.get('columnHeader', {})
          dimension_headers = column_header.get('dimensions', [])
          metric_headers = column_header.get('metricHeader', {}).get('metricHeaderEntries', [])

          # Get each row in the report
          for row in report.get('data', {}).get('rows', []):
              # create dict for each row
              row_dict = {}
              dimensions = row.get('dimensions', [])
              date_range_values = row.get('metrics', [])

              # Fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimension_headers, dimensions):
                  row_dict[header] = dimension

              # Fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(date_range_values):
                  for metric, value in zip(metric_headers, values.get('values')):
                  # Set int as int, float a float
                      if ',' in value or '.' in value:
                          row_dict[metric.get('name')] = float(value)
                      else:
                          row_dict[metric.get('name')] = int(value)

              row_list.append(row_dict)
      return pd.DataFrame(row_list)

  def main():

    analytics = initialize_analyticsreporting()
    response1 = get_report20(analytics) #get the response from the API
    print_response_side22(response1) #print the response from the API
    arriba.markdown('<div style="text-align:center; border-bottom:1px solid #008357;border-top:1px solid #000;font-family: Oswald;">VISITAS TOTALES: '+str(st.session_state.key33)+'</div><br>', unsafe_allow_html=True)                        
      
    response = get_report555(analytics) #get the response from the API
    print_response_side2(response) #print the response from the API
    #st.markdown('<div style="text-align:center; font-size:18px;border-bottom:1px solid #008357;font-family: Oswald"><b>ESTADÍSTICAS DESDE EL 1/10/2020 AL '+today+'</b></div><br>', unsafe_allow_html=True)



    st.markdown('<div style="text-align:center; border-bottom:1px solid #008357;border-top:1px solid #000;font-family: Oswald;">VISITAS TOTALES DEL PAÍS: '+str(st.session_state.key1)+'</div><br>', unsafe_allow_html=True)                        
      

    response = get_reportcity555(analytics) #get the response from the API
    col1, col2 = st.beta_columns([1,1]) 

    df = ga_response_dataframe(response)
    
    
    df["ga:city"]=df["ga:city"].str.replace(r'[0-9]','(not set)')
    df=df[~df["ga:city"].str.contains('(not set)')]
    #st.table(df)
    df['ga:latitude'] = pd.to_numeric(df['ga:latitude'])
    df['ga:longitude'] = pd.to_numeric(df['ga:longitude'])
    
    df.columns =['Pais','ciu',"Longitude", "Latitude","visitas"]


    #folium_static(map)
    
    map_ = folium.Map(location=[df['Latitude'].iloc[0],df['Longitude'].iloc[0]], 
                      tiles='OpenStreetMap',
                      zoom_start = 3,zoom_control=False,
               scrollWheelZoom=False,
               dragging=False)
  
    for index, row in df.iterrows():
          tooltip = 'Visita'
          folium.Marker((row['Latitude'], row['Longitude']),tooltip=tooltip,
          icon=folium.Icon(color='green')).add_to(map_)
    with col1:      
      folium_static(map_)
       #get the response from the API
    with col2:
      with st.beta_expander('Por ciudad:'): 
        response = get_report55(analytics)
        print_responsepais55(response) #print the response from the API 
      with st.beta_expander('Por dispositivo:'):
  
    #if dispo:
        response = get_reportdispo(analytics) #get the response from the API
        print_responsebar(response) #print the response from the API   
      with st.beta_expander('Por día:'): 
        st.markdown("""
  <style>


  .css-glyadz {
      font-size: 1rem;
      color: rgb(38, 39, 48);
      margin-bottom: 0.4rem;
      height: 1.5rem;
      vertical-align: middle;
      display: flex;
      flex-direction: row;
      -webkit-box-align: center;
      align-items: center;
  }
  </style>
  """, unsafe_allow_html=True)
      #dia=st.checkbox('Ver por día:')
      #if dia:
        response = get_report0(analytics) #get the response from the API
        print_responsed(response) #print the response from the API      
  #with container:
    #with st.beta_expander('Ver paises:'): 

        
        
      #response = get_report5(analytics) #get the response from the API
        
      #print_responsepaisolo(response) #print the response from the API 



     
  if __name__ == '__main__':
    main()

def numero():
  pais='Argentina'
  st.session_state['key'] = 0
  st.session_state['key1'] = 0
  st.session_state['key2'] = 0
  #st.markdown('<div style="text-align:left; font-size:18px;border-bottom:1px solid #008357;font-family: Oswald"><b>ESTADÍSTICAS DESDE EL 15/3/2019 AL '+today+'</b></div><br>', unsafe_allow_html=True)
  st.markdown("""
<style>
table td:nth-child(1) {
    display: none
}
table th:nth-child(1) {
    display: none
}
.css-4ux067 {
    width: 1514px;
    margin: 0px 0px 1rem;
    text-align: center;
}
.css-glyadz {
    font-size: 1rem;
    color: rgb(38, 39, 48);
    margin-bottom: 0.4rem;
    height: 1.5rem;
    vertical-align: middle;
    display: flex;
    flex-direction: row;
    -webkit-box-align: center;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)
  #VIEW_ID = '60591749'#'222848977'
  def pull_sheet_data(SCOPES,SPREADSHEET_ID,DATA_TO_PULL):

          service = build('sheets', 'v4', credentials=cred)
          sheet = service.spreadsheets()
          result = sheet.values().get(
          spreadsheetId=SPREADSHEET_ID,
          range=DATA_TO_PULL).execute()
          values = result.get('values', [])

          if not values:
                  print('No data found.')
          else:
                  rows = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                  range=DATA_TO_PULL).execute()
                  data = rows.get('values')
                  print("COMPLETE: Data copied")
                  return data
  SPREADSHEET_ID = ids
  DATA_TO_PULL = 'analytics'
  #display_code = st.sidebar.radio("Mostrar", ( "Por número","Búsqueda"))
  data = [['clayss.org.ar',60591749],['clayss.org',254644946],['noticias.clayss.org',222848977],['Seminario Clayss',225379278],['Seminario Clayss Uruguay',254692529]]
  df = pd.DataFrame(data,columns=['dominio','id'])
  values = df['dominio'].tolist()
  options = df['id'].tolist()
  dic = dict(zip(options, values))
  #VIEW_ID = st.selectbox('Seleccionar Dominio:', options, format_func=lambda x: dic[x])
  VIEW_ID = '201209640'
  #ruta=st.text_input('Escribir ruta:','/es')
  date = datetime.date(2019, 3, 15)
  date2 = date.today()
  #date = st.sidebar.date_input('Desde', datetime.date(2019,6,1))
  #date2 = st.sidebar.date_input('Hasta')



  def initialize_analyticsreporting():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[tools.argparser])
    flags = parser.parse_args([])
    credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", SCOPES)
    if credentials is None or credentials.invalid:
      credentials = tools.run_flow(flow, storage, flags)
    http = credentials.authorize(http=httplib2.Http())
    analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)
    return analytics
  def get_report20(analytics):
    ruta='es/'
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
           
              'metrics': [
          {
              'expression': 'ga:pageviews'
          }
       ]

          ,

                'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()
  def get_report202(analytics):
    
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
            
              'metrics': [
          {
              'expression': 'ga:pageviews'
          }
       ]

          ,

                'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()
  def get_report0(analytics):
              return analytics.reports().batchGet(
                  body={
                    'reportRequests': [
                    {
                      'viewId': VIEW_ID,
                      'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                      'dimensions':[{'name':'ga:date'}],         
                      'metrics': [{'expression': 'ga:pageviews'}],
                      'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                    }
                  ]
                    }]
                  }
              ).execute()



  def get_report3(analytics):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],

            
             'metrics': [
          {
              'expression': 'ga:pageviews'
          }
       ]

          ,
           "dimensions": [
              {"name": "ga:deviceCategory"}
          ],
            'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()

  def get_report5(analytics):
    return analytics.reports().batchGet(
      body=
      {"reportRequests":[{"viewId": VIEW_ID,'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],"metrics":[{"expression": "ga:pageviews"}],

          "dimensions": [{"name": "ga:country"}],

                    'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }] }
          ).execute()
  def get_report55(analytics):
      return analytics.reports().batchGet(
        body=
        {"reportRequests":[{"viewId": VIEW_ID,'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],"metrics":[{"expression": "ga:pageviews"}],

            "dimensions": [{"name": "ga:country"},{"name": "ga:city"}],

                      'dimensionFilterClauses': [
              {
              'filters':[
          {
          "operator": "PARTIAL",
          "dimensionName": "ga:pagePath",

          "expressions": [
            ruta
          ]

          }

        ]
            }
          ]
            }] }
            ).execute()     
           
  def get_reportsolo(analytics):

    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
            
              'metrics': [
          {
              'expression': 'ga:pageviews'
          }
       ]

          ,

                'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()


  def get_reportcity(analytics):
                      return analytics.reports().batchGet(body={
                      'reportRequests': [{
                          'viewId': VIEW_ID,
                          'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                          'metrics': [
                              {"expression": "ga:pageviews"},
                          ], "dimensions": [
                              {"name": "ga:longitude"},
                              {"name": "ga:latitude"}
                          ],            'dimensionFilterClauses': [
                              {
                              'filters':[
                          {
                          "operator": "PARTIAL",
                          "dimensionName": "ga:pagePath",
                          "expressions": [
                            ruta
                          ]
                          }
                        ]
                            }
                          ]
                            }]
                          
                    }).execute()  

  def print_responsebar(response):
      #col1, col2 = st.beta_columns([1,1])  
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)

      df = pd.DataFrame(list)
      df['%']=(df['ga:pageviews'])/df['ga:pageviews'].sum()
      
      fig = px.pie(df, values='%', names='ga:deviceCategory')
      st.plotly_chart(fig, use_container_width=True)

      #col1.dataframe(df.assign(hack='').set_index('hack'),  height=600)
      df = pd.DataFrame(list)
      df.columns =['Dispositivo','Visitas']

      #col1.table(df)
      return df
  def print_responsepais55(response):
           
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)
            df=df[~df["ga:city"].str.contains('(not set)')]
            #fig = px.bar(df, x = "ga:country", y = "ga:pageviews")
            #col1.plotly_chart(fig, use_container_width=True)
            df=df.sort_values(by=['ga:pageviews'],ascending=False)
            df02 = pd.DataFrame(df, columns=['ga:country','ga:city','ga:pageviews']) 
            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
            #df.query('ga:country' == 'Argentina' , inplace = True)
            #values = df['ga:country'].tolist()
            
            DEFAULT='Argentina'
            def selectbox_with_default(text, values, default=DEFAULT, sidebar=False):
              func = st.selectbox #if sidebar else st.selectbox
              return func(text, np.insert(np.array(values, object), 0, default))
            #pais = st.selectbox('Seleccionar pais', values)
            #fig = px.line(df0[df0['ga:pagePath'] == a], 
            #x = "ga:pagePath", y = "ga:pagePath", title = a)

           
            df02.columns =['País','Ciudad','Visitas']
            df02['%']=df02['Visitas']/df02['Visitas'].sum()
          except ValueError as ve:
                      st.warning('No hay visitas') 
          
          st.table(df02.drop(['Visitas'], axis=1))
          return df
  def print_responsed(response):
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)
            df=df.sort_values(by=['ga:date'],ascending=False) 
            
            df['ga:date'] = pd.to_datetime(df['ga:date']).dt.strftime('%d-%m-%y')


            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)

            df.columns =['','visitas']
            
            
            df['%']=df['visitas']/df['visitas'].sum()
            
            st.table(df.drop(['visitas'], axis=1))
          except ValueError as ve:
            st.warning('No hay visitas')                   
          return df

  def print_responsepais(response):
          #col1, col2 = st.beta_columns([1,1])  
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)
            fig = px.pie(df, names = "ga:country", values = "ga:pageviews")
            st.plotly_chart(fig, use_container_width=True)

            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
            df = pd.DataFrame(list)
            df.columns =['País','Visitas']
            #st.table(df)
          except ValueError as ve:
                      st.warning('No hay visitas') 
          #col1.table(df)
          return df



  def print_response_side(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)
      try:
        df = pd.DataFrame(list)
        df.columns =['Visitas']


        #df = pd.DataFrame({'c1': destinatarios})
        df = df.reset_index()  # make sure indexes pair with number of rows





        for index, row in df.iterrows():
                st.session_state['key']=row['Visitas']+st.session_state.key

        #st.table(df)

        st.session_state['key']=st.session_state.key+1
      except ValueError as ve:
             st.warning('No hay visitas')    





      return df
  def print_response_sidenoti(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)
      try:
        df = pd.DataFrame(list)
        df.columns =['Visitas']


        #df = pd.DataFrame({'c1': destinatarios})
        df = df.reset_index()  # make sure indexes pair with number of rows





        for index, row in df.iterrows():
                st.session_state['key2']=row['Visitas']

        #st.table(df)

        st.session_state['key2']=st.session_state.key2+500
      except ValueError as ve:
             st.warning('No hay visitas')    





      return df

  def print_response_side2(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)

      df = pd.DataFrame(list)
      df.columns =['Visitas Totales']

      df = df.reset_index()  # make sure indexes pair with number of rows



      #st.sidebar.table(df)

      for index, row in df.iterrows():
              st.session_state['key1']=row['Visitas Totales']+109403



      return df    
  def ga_response_dataframe(response):
      row_list = []
      # Get each collected report
      for report in response.get('reports', []):
          # Set column headers
          column_header = report.get('columnHeader', {})
          dimension_headers = column_header.get('dimensions', [])
          metric_headers = column_header.get('metricHeader', {}).get('metricHeaderEntries', [])

          # Get each row in the report
          for row in report.get('data', {}).get('rows', []):
              # create dict for each row
              row_dict = {}
              dimensions = row.get('dimensions', [])
              date_range_values = row.get('metrics', [])

              # Fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimension_headers, dimensions):
                  row_dict[header] = dimension

              # Fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(date_range_values):
                  for metric, value in zip(metric_headers, values.get('values')):
                  # Set int as int, float a float
                      if ',' in value or '.' in value:
                          row_dict[metric.get('name')] = float(value)
                      else:
                          row_dict[metric.get('name')] = int(value)

              row_list.append(row_dict)
      return pd.DataFrame(row_list)

  def main():

    analytics = initialize_analyticsreporting()
    response = get_report20(analytics) #get the response from the API
    print_response_side2(response) #print the response from the API
    #st.markdown('<div style="text-align:left; border-bottom:1px solid #008357;border-top:1px solid #000;font-family: Oswald;">VISITAS TOTALES: '+str(st.session_state.key1)+'</div><br>', unsafe_allow_html=True)                        
      



  if __name__ == '__main__':
    main()
  def pull_sheet_data(SCOPES,SPREADSHEET_ID,DATA_TO_PULL):

        service = build('sheets', 'v4', credentials=cred)
        sheet = service.spreadsheets()
        result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=DATA_TO_PULL).execute()
        values = result.get('values', [])

        if not values:
                print('No data found.')
        else:
                rows = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                range=DATA_TO_PULL).execute()
                data = rows.get('values')
                print("COMPLETE: Data copied")
                return data
  SPREADSHEET_ID = ids
  DATA_TO_PULL = 'bases'
  data1 = pull_sheet_data(scopes,SPREADSHEET_ID,DATA_TO_PULL)
  base = pd.DataFrame(data1[1:], columns=data1[0]) 
  SPREADSHEET_ID2 = ids
  DATA_TO_PULL2 = 'remitentes'
  data12 = pull_sheet_data(scopes,SPREADSHEET_ID2,DATA_TO_PULL2)
  base2 = pd.DataFrame(data12[1:], columns=data12[0])
  gclient = authorize(cred)
  def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)  
  #Scrape the source code from the specified link:
  #In this example I'm using my own medium wall
  st.markdown('<link href="https://fonts.googleapis.com/css2?family=Oswald" rel="stylesheet"><style>.css-tsy3mu{font-family: Oswald;}.st-bg,.css-177yq5e, .st-bo,.st-bf,.st-b4,.st-b7,.st-be,.st-bi,.st-dq {position: relative;font-family: Oswald;}.css-1ekf893 {margin-bottom: -1rem;font-family: Oswald;}.css-1v0mbdj {margin-top: -60px;}body{font-family: "Oswald", Arial, sans-serif;}</style>', unsafe_allow_html=True)
  arriba.markdown('<div style="text-align:center; border-bottom:1px solid #008357;border-top:1px solid #000;font-family: Oswald;">VISITAS TOTALES: '+str(st.session_state.key1)+'</div><br>', unsafe_allow_html=True)                        
  #display_code = st.sidebar.radio("Mostrar", ( "Por número","Búsqueda"))

  data = requests.get("https://noticias.usal.edu.ar/es/todas-tapas")  
  URL = "https://noticias.usal.edu.ar/es/todas-tapas"

  #if display_code=='Por número':
  req = requests.get(URL)
  html = BeautifulSoup(req.text, "html.parser")


  previews2=[]
  #entradas1 = html.find('table', {'class': 'cols-0'})



  #numeros0 = entradas1.find_all('td', {'class': 'views-field'})
  numeros = html.find_all('div', {'class': 'col-lg-6'})


  for i, entrada in enumerate(numeros):
        title = entrada.find('div', {'class': 'tapanum'}).getText()
        boletin=entrada.find('a').get_text()
        #html = str(entrada.find('a', attrs = {'href':re.compile(r'^.*\b\b.*$')}))
        html = entrada.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
        image=entrada.find('img') 
        image = str(image.attrs['src']).split(" ")[0]   
        image='https://noticias.usal.edu.ar'+image

        entrada_preview2 = { 
        'title': str(title),
        'image': str(image),
        'linkn': "https://noticias.usal.edu.ar"+html
        }
        previews2.append(entrada_preview2)
  df=pd.DataFrame(previews2) 
  #st.table(df)        
  #df0=df0.sort_values(by=['nombre'],ascending=True)
  values = df['title'].tolist()
  options = df['linkn'].tolist()
  dic = dict(zip(options, values))
  col11, col12= st.beta_columns([1,1]) 


  lunes=col11.selectbox(f'Año', ['2022'	,'2021'	,'2020'	,'2019'], key='a')

  martes=col12.selectbox(f'Mes', ['seleccionar','febrero'	,'marzo'	,'abril'	,'mayo'	,'junio','julio','agosto','septiembre','octubre','noviembre','diciembre'], key='b')
  seleccion=df[df['title'].str.contains(lunes)]
  values = seleccion['title'].tolist()
  options = seleccion['linkn'].tolist()
  dic = dict(zip(options, values))

  if  (lunes!='seleccionar' and martes=='seleccionar'):
        destinatarios = st.selectbox('Seleccionar número del listado:', options, format_func=lambda x: dic[x])

  elif  (lunes!='seleccionar' and martes!='seleccionar'):
        seleccion=seleccion[seleccion['title'].str.contains(martes)]
        values = seleccion['title'].tolist()
        options = seleccion['linkn'].tolist()
        dic = dict(zip(options, values))
        destinatarios = st.selectbox('Seleccionar número del listado:', options, format_func=lambda x: dic[x])                      

  data = requests.get(destinatarios)  
  soup = BeautifulSoup(data.content, 'html5lib') 
  html = str(soup.find_all('a', attrs = {'href':re.compile(r'^.*\b\b.*$')}))
  href_start = [s.start() for s in re.finditer('href="',html)] 
  urls = []
  for start in href_start:  
    url = html[start+6:]
    url = url[:url.find('"')]
    url=url.replace("//send?text=", "") 
    #st.write(url)
    # remove all urls containing special characters we don't want
    if not any(c in '#?^%*()=' for c in url):
        urls.append(url)
  article_template = soup.find('div', attrs={'class':'post-style-grid'})


  titles = df.loc[df['linkn'] == destinatarios, 'title']
  titles= ', '.join(titles) 
  images = df.loc[df['linkn'] == destinatarios, 'image']
  images= ', '.join(images) 


  entradas = soup.find_all('div', {'class': 'col-lg-4'})


  previews = []
  for i, entrada in enumerate(entradas):
    #data = requests.get(article) 

    title = entrada.find('div', {'class': 'post-title'}).getText()
    orden = entrada.find('div', {'class': 'subs'}).getText()
    subtitle = entrada.find('div', {'class': 'post-body-term'})
    subtitle =str(subtitle).replace('<div class="','')
    subtitle =str(subtitle).replace('post-body-term">','')
    subtitle =str(subtitle).replace('</p></div>','')
    subtitle =str(subtitle).replace('</p>...</div>','')
    subtitle =str(subtitle).replace('<p>','')
    fecha = entrada.find('span', {'class': 'post-created'}).getText()
    html = str(entrada.find('a', attrs = {'href':re.compile(r'^.*\b\b.*$')}))
    href_start = [s.start() for s in re.finditer('href="',html)] 


    url = html[start+6:] 
    url = url[:url.find('"')] 
    linko = entrada.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
        # remove all urls containing special characters we don't want
    if not any(c in '#?^%*()=' for c in html):
        html.append(html) 
    #subtitle0 = entrada.find('div', {'class': 'v1fecha'}).contents[0]

    image=entrada.find('img') 
    image = str(image.attrs['src']).split(" ")[0]   
    image=image  
    linko = entrada.find('div', {'class': 'item-image'})
    linki=linko.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']

    #st.write('https://noticias.usal.edu.ar'+url) 


    entrada_preview = { 
        'title': str(title),
        'fecha': str(fecha),
  'image': str(image),
  'orden': str(orden),
  'url': 'https://noticias.usal.edu.ar'+linki,
  'subtitle': str(subtitle)

    }
    previews.append(entrada_preview) 



  st.markdown("<div style='text-align:left; color: #000;font-family: Oswald;font-size:16px;'>Noticias totales: "+str(len(previews))+"</div>", unsafe_allow_html=True)

  


  for i,article in enumerate(previews):


                        


                        t=i+1
                        ruta1=article['url']
                        ruta=ruta1.replace('https://noticias.usal.edu.ar','')
                        st.markdown("<hr style='height:2px;border-width:0;color:gray;background-color:#008357'><div style='text-align:  left; color: #000;font-family: Oswald; font-size:18px;'>"+str(t)+") "+article['title']+"👇 </div>", unsafe_allow_html=True)
                        st.markdown("<div style='text-align:  left; color: #008357;font-family: Oswald; font-size:16px;padding:5px;'>Sección: "+article['orden']+"</div>", unsafe_allow_html=True)                      
                                             
                        st.markdown("<div style='text-align:  left; color: #000;font-family: Oswald; font-size:16px;padding:5px;'>Publicada: "+article['fecha']+"</div>", unsafe_allow_html=True)                      
                       #st.markdown("<div style='text-align:  left; color: #e65100;font-family: Oswald;font-size:18px;padding:5px;'>Visitas:"+str(st.session_state.key+100)+"</div>", unsafe_allow_html=True)

                        col11, col12= st.beta_columns([1,1])

                        col12.markdown("<a href='"+article['url']+"' target='_blank'><img src='https://noticias.usal.edu.ar"+article['image']+"' style='width:90%;border-radius:3px;'></a>", unsafe_allow_html=True) 
                        analytics = initialize_analyticsreporting()
                        response1 = get_reportsolo(analytics) #get the response from the API
                        print_response_sidenoti(response1) #print the response from the API
                        response11= get_report202(analytics) #get the response from the API
                        print_response_side(response11) #print the response from the API                        
                        col11.markdown("<div style='text-align:  left; color: #e65100;font-family: Oswald;font-size:18px;padding:5px;'>Visitas:"+str(st.session_state.key2)+"</div>", unsafe_allow_html=True)



                        #response = get_report22(analytics) #get the response from the API
                        #print_response_side22(response) #print the response from the API
                        #if display_code=='Inicio': 
                        # response = get_report28(analytics) #get the response from the API
                        # print_response(response) #print the response from the API




                        with col11.beta_expander('Ver por país/ciudad:'):
                          st.markdown("""
                          <style>
            
                
                          .css-glyadz {
                              font-size: 1rem;
                              color: rgb(38, 39, 48);
                              margin-bottom: 0.4rem;
                              height: 1.5rem;
                              vertical-align: middle;
                              display: flex;
                              flex-direction: row;
                              -webkit-box-align: center;
                              align-items: center;
                          }
                          </style>
                          """, unsafe_allow_html=True)
                        #pais=st.checkbox('Ver por país:')
                        #if pais:
                          response = get_reportcity(analytics) #get the response from the API


                          df = ga_response_dataframe(response)
                          if df.empty == True:
                              print('DataFrame is empty')
                          else:

                            df['ga:latitude'] = pd.to_numeric(df['ga:latitude'])
                            df['ga:longitude'] = pd.to_numeric(df['ga:longitude'])
                            mylist = ['ga:latitude','ga:longitude']
                            df=df[~df[mylist].eq(0).all(1)]
                            df.columns =["Longitude", "Latitude","visitas"]


                            #folium_static(map)
                            #st.table(df)
                            map_ = folium.Map(location=[df['Latitude'].iloc[0],df['Longitude'].iloc[0]], 
                                              tiles='OpenStreetMap',
                                              zoom_start = 2,zoom_control=True,
                 scrollWheelZoom=False,
                 dragging=False)
                            for index, row in df.iterrows():
                                  tooltip = 'Visita'
                                  folium.Marker((row['Latitude'], row['Longitude']),tooltip=tooltip,
                                  icon=folium.Icon(color='green')).add_to(map_)
                            folium_static(map_)
                            response = get_report55(analytics) #get the response from the API
                            print_responsepais55(response) #print the response from the API
                            response = get_report5(analytics) #get the response from the API
                            print_responsepais(response) #print the response from the API
                        with col11.beta_expander('Ver por dispositivo:'):
               
                          response = get_report3(analytics) #get the response from the API
                          print_responsebar(response) #print the response from the API 
                          #print_response_list_url(response)                           
                        with col11.beta_expander('Ver por día:'):
                      
                          response = get_report0(analytics) #get the response from the API
                          print_responsed(response) #print the response from the API    
                         
                          
  #st.sidebar.markdown("<div style='text-align:  left; color: #e65100;font-family: Oswald;font-size:14px;'>"+titles+"</div>", unsafe_allow_html=True)
  #st.sidebar.markdown("<div style='text-align:  left; color: #008357;font-family: Oswald;font-size:16px;'>Visitas:"+str(st.session_state.key)+"</div>", unsafe_allow_html=True)
                        
  #st.sidebar.markdown("<a href='"+destinatarios+"' target='_blank'><img src='"+images+"' style='width:90%;border-radius:3px;'></a>", unsafe_allow_html=True)                       #print_response_list_url(response)
def busca():                       
  st.session_state['key'] = 0
  st.session_state['key1'] = 0
  st.session_state['key2'] = 0
  pais='Argentina'

  VIEW_ID = '201209640'
  noticias=st.text_input('Palabra:','' )

  if  (noticias!=''):


      data = requests.get("https://noticias.usal.edu.ar/es/buscador-visitas?keys="+noticias)  
      URL = "https://noticias.usal.edu.ar/es/buscador-visitas?keys="+noticias

      #if display_code=='Por número':
      req = requests.get(URL)
      html = BeautifulSoup(req.text, "html.parser")


      previews2=[]
      #entradas1 = html.find('table', {'class': 'cols-0'})



      #numeros0 = entradas1.find_all('td', {'class': 'views-field'})
      numeros = html.find_all('div', {'class': 'gva-view-grid'})


      for i, entrada in enumerate(numeros):
            title = entrada.find('div', {'class': 'post-title'}).getText()
            boletin=entrada.find('a').get_text()

            #html = str(entrada.find('a', attrs = {'href':re.compile(r'^.*\b\b.*$')}))
            html = entrada.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
            image=entrada.find('img') 
            image = str(image.attrs['src']).split(" ")[0]   
            image=image

            entrada_preview2 = { 
            'title': str(title),
            'image': str(image),
              
            'linkn': "https://noticias.usal.edu.ar"+html
            }
            previews2.append(entrada_preview2)
      df=pd.DataFrame(previews2) 
      #st.table(df)        
      #df0=df0.sort_values(by=['nombre'],ascending=True)
      isempty = df.empty         
      #st.table(df)        
      #df0=df0.sort_values(by=['nombre'],ascending=True)
      if isempty:
        st.warning('No hay noticiasque contengan:'+noticias)
      else:   
          values = df['title'].tolist()
          options = df['linkn'].tolist()
          dic = dict(zip(options, values))
          col11, col12= st.beta_columns([1,1]) 
 

          destinatarios = st.selectbox('Noticias que contienen: '+noticias, options, format_func=lambda x: dic[x])
          if destinatarios!='':

            ruta=destinatarios.replace("https://noticias.usal.edu.ar/",'')
            #st.write(destinatarios)
            data = requests.get(destinatarios)  
            soup = BeautifulSoup(data.content, 'html5lib') 
            html = str(soup.find_all('a', attrs = {'href':re.compile(r'^.*\b\b.*$')}))
            meta = soup.find('div', {'class': 'post-meta'})
            fecha = meta.find('span', {'class': 'post-createdit'}).getText()
            orden=meta.find('div', {'class': 'subs'}).getText()
            foto = soup.find('div', {'class': 'image-item'})
            image=foto.find('img') 
            image = str(image.attrs['src']).split(" ")[0]  
            href_start = [s.start() for s in re.finditer('href="',html)] 
            urls = []
            for start in href_start:  
              url = html[start+6:]
              url = url[:url.find('"')]
              url=url.replace("//send?text=", "") 
              #st.write(url)
              # remove all urls containing special characters we don't want
              if not any(c in '#?^%*()=' for c in url):
                  urls.append(url)



            titles = df.loc[df['linkn'] == destinatarios, 'title']
            titles= ', '.join(titles) 
            images = df.loc[df['linkn'] == destinatarios, 'image']
            images= ', '.join(images) 
            orden=str(orden)

            date = datetime.date(2019, 3, 15)
            date2 = date.today()



            def initialize_analyticsreporting():
              parser = argparse.ArgumentParser(
                  formatter_class=argparse.RawDescriptionHelpFormatter,
                  parents=[tools.argparser])
              flags = parser.parse_args([])
              credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", SCOPES)
              if credentials is None or credentials.invalid:
                credentials = tools.run_flow(flow, storage, flags)
              http = credentials.authorize(http=httplib2.Http())
              analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)
              return analytics
            def get_report20(analytics):
              ruta='es/'
              return analytics.reports().batchGet(
                  body={
                    'reportRequests': [
                    {
                      'viewId': VIEW_ID,
                      'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                      'metrics': [{"expression": "ga:pageviews"}],

                          'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                    }
                  ]
                    }]
                  }
              ).execute()
            def get_report0(analytics):
              return analytics.reports().batchGet(
                  body={
                    'reportRequests': [
                    {
                      'viewId': VIEW_ID,
                      'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                      'dimensions':[{'name':'ga:date'}],         
                      'metrics': [{'expression': 'ga:pageviews'}],
                      'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                    }
                  ]
                    }]
                  }
              ).execute()
            def get_report25(analytics):
              return analytics.reports().batchGet(
                    body={ 
                    'reportRequests': [ 
                        { 
                            'viewId': VIEW_ID, 
                              "dimensions": [
                {
                "name": "ga:pagePath"
                }
              ],
              "metrics": [
                {
                "expression": "ga:pageviews"
                }
              ],
                            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],

                            }] 
                            } 
                ).execute()
            def get_report1(analytics):
              return analytics.reports().batchGet(
                  body={
                    'reportRequests': [
                    {
                      'viewId': VIEW_ID,
                      'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],

                        'metrics': [
                    {
                        'expression': 'ga:pageviews'
                    }
                ],
                      'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                    }
                  ]
                    }]
                  }
              ).execute()
            def get_reportcity(analytics):
              return analytics.reports().batchGet(body={
              'reportRequests': [{
                  'viewId': VIEW_ID,
                  'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                  'metrics': [
                      {"expression": "ga:pageviews"},
                  ], "dimensions": [
                      {"name": "ga:longitude"},
                      {"name": "ga:latitude"},{"name": "ga:country"}
                  ],            'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                   "operator": "PARTIAL",
                   "dimensionName": "ga:pagePath",
                   "expressions": [
                    ruta
                   ]
                  }
                 ]
                    }
                  ]
                    }]

             }).execute()
            def get_report28(analytics):
              return analytics.reports().batchGet(
                  body={
                'reportRequests':[
                {
                'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                'metrics': [
                    {
                        'expression': 'ga:pageviews'
                    },
                {"expression": "ga:avgSessionDuration"}],

                'viewId': VIEW_ID,
                'dimensions':[
                {
                  'name':'ga:sessionCount',

                  'histogramBuckets':['1','10','100','200', '400']
                }],

                'orderBys':[
                {
                  'fieldName':'ga:sessionCount',
                  'orderType':'HISTOGRAM_BUCKET'
                }],
              }]
              }
              ).execute()
            def get_report3(analytics):
              return analytics.reports().batchGet(
                  body={
                    'reportRequests': [
                    {
                      'viewId': VIEW_ID,
                      'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],

                      'metrics': [            {"expression": "ga:pageviews"}
                      ],
                    "dimensions": [
                        {"name": "ga:deviceCategory"}
                    ],
                      'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                    }
                  ]
                    }]
                  }
              ).execute()
            def get_report4(analytics):
              return analytics.reports().batchGet(
                body={ 
                    'reportRequests': [ 
                        #first report
                        { 
                            'viewId': VIEW_ID, 
                            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],#'startDate': '6daysAgo', 'endDate': 'today'}], 
                            'metrics': [{"expression": "ga:pageviews"}],
                            'dimensions': [{'name': 'ga:userGender'}],
                      'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                    }
                  ]
                    }]
                    } 
                ).execute()
            def get_report5(analytics):
              return analytics.reports().batchGet(
                body=
                {"reportRequests":[{"viewId": VIEW_ID,'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],"metrics":[{"expression": "ga:pageviews"}],

                    "dimensions": [{"name": "ga:country"}],

                              'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                    }
                  ]
                    }] }
                    ).execute()
            def get_report21(analytics):
              return analytics.reports().batchGet(
                  body={
                    'reportRequests': [
                    {
                      'viewId': VIEW_ID,
                      'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                  'metrics': [{"expression": "ga:pageviews"},           ],

                        'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                    }
                  ]

                    }]
                  }
              ).execute()
            def get_report22(analytics):
              return analytics.reports().batchGet(
                  body={
                    'reportRequests': [
                    {
                      'viewId': VIEW_ID,
                      'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                  'metrics': [{"expression": "ga:pageviews"},           ],
                    "dimensionFilterClauses": [
                {
                "filters": [
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
     ]
                  }
                ]
                    }
                  ]

                    }]
                  }



              ).execute()
            def get_report26(analytics):
              return analytics.reports().batchGet(
                    body={ 
                    'reportRequests': [ 
                        { 
                            'viewId': VIEW_ID, 
                              "dimensions": [
                {
                "name": "ga:pagePath"
                }
              ],
              "metrics": [
                {
                "expression": "ga:pageviews"
                }
              ],"dimensionFilterClauses": [
                {
                "filters": [
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                }
              ],
                            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}] 

                            }] ,
                            } 
                ).execute()
            def get_report29(analytics):
              return analytics.reports().batchGet(
                    body={ 
                    'reportRequests': [ 
                        { 
                            'viewId': VIEW_ID, 
                              "dimensions": [
                {
                "name": "ga:pagePath"
                }
              ],
              "metrics": [
                {
                "expression": "ga:pageviews"
                }
              ],
                            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}] 

                            }] ,
                            } 
                ).execute()
            def get_report55(analytics):
                return analytics.reports().batchGet(
                  body=
                  {"reportRequests":[{"viewId": VIEW_ID,'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],"metrics":[{"expression": "ga:pageviews"}],

                      "dimensions": [{"name": "ga:country"},{"name": "ga:city"}],

                                'dimensionFilterClauses': [
                        {
                        'filters':[
                    {
                    "operator": "PARTIAL",
                    "dimensionName": "ga:pagePath",
                    
                    "expressions": [
                      ruta
                    ]
                    
                    }

                  ]
                      }
                    ]
                      }] }
                      ).execute()     
            def print_response(response):
                list = []
                # get report data
                for report in response.get('reports', []):
                # set column headers
                    columnHeader = report.get('columnHeader', {})
                    dimensionHeaders = columnHeader.get('dimensions', [])
                    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                    rows = report.get('data', {}).get('rows', [])

                for row in rows:
                    # create dict for each row
                    dict = {}
                    dimensions = row.get('dimensions', [])
                    dateRangeValues = row.get('metrics', [])

                    # fill dict with dimension header (key) and dimension value (value)
                    for header, dimension in zip(dimensionHeaders, dimensions):
                        dict[header] = dimension

                    # fill dict with metric header (key) and metric value (value)
                    for i, values in enumerate(dateRangeValues):
                        for metric, value in zip(metricHeaders, values.get('values')):
                        #set int as int, float a float
                            if ',' in value or '.' in value:
                                dict[metric.get('name')] = float(value)
                            else:
                                dict[metric.get('name')] = int(value)

                    list.append(dict)

                df = pd.DataFrame(list)


                st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
                return df
            def print_responsebar(response):
                #col1, col2 = st.beta_columns([1,1])  
                list = []
                # get report data
                for report in response.get('reports', []):
                # set column headers
                    columnHeader = report.get('columnHeader', {})
                    dimensionHeaders = columnHeader.get('dimensions', [])
                    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                    rows = report.get('data', {}).get('rows', [])

                for row in rows:
                    # create dict for each row
                    dict = {}
                    dimensions = row.get('dimensions', [])
                    dateRangeValues = row.get('metrics', [])

                    # fill dict with dimension header (key) and dimension value (value)
                    for header, dimension in zip(dimensionHeaders, dimensions):
                        dict[header] = dimension

                    # fill dict with metric header (key) and metric value (value)
                    for i, values in enumerate(dateRangeValues):
                        for metric, value in zip(metricHeaders, values.get('values')):
                        #set int as int, float a float
                            if ',' in value or '.' in value:
                                dict[metric.get('name')] = float(value)
                            else:
                                dict[metric.get('name')] = int(value)

                    list.append(dict)

                df = pd.DataFrame(list)
                df['%']=(df['ga:pageviews'])/df['ga:pageviews'].sum()
               
                fig = px.pie(df, values='%', names='ga:deviceCategory')
                st.plotly_chart(fig, use_container_width=True)

                #col1.dataframe(df.assign(hack='').set_index('hack'),  height=600)
                df = pd.DataFrame(list)
                df.columns =['Dispositivo','Visitas']

                #col1.table(df)
                return df
            def print_responsesex(response):
                col1, col2 = st.beta_columns([1,1])  
                list = []
                # get report data
                for report in response.get('reports', []):
                # set column headers
                    columnHeader = report.get('columnHeader', {})
                    dimensionHeaders = columnHeader.get('dimensions', [])
                    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                    rows = report.get('data', {}).get('rows', [])

                for row in rows:
                    # create dict for each row
                    dict = {}
                    dimensions = row.get('dimensions', [])
                    dateRangeValues = row.get('metrics', [])

                    # fill dict with dimension header (key) and dimension value (value)
                    for header, dimension in zip(dimensionHeaders, dimensions):
                        dict[header] = dimension

                    # fill dict with metric header (key) and metric value (value)
                    for i, values in enumerate(dateRangeValues):
                        for metric, value in zip(metricHeaders, values.get('values')):
                        #set int as int, float a float
                            if ',' in value or '.' in value:
                                dict[metric.get('name')] = float(value)
                            else:
                                dict[metric.get('name')] = int(value)

                    list.append(dict)

                df = pd.DataFrame(list)
                fig = px.bar(df, x = "ga:userGender", y = "ga:pageviews")
                st.plotly_chart(fig, use_container_width=True)

                #col1.dataframe(df.assign(hack='').set_index('hack'),  height=600)

                df.columns =['Sexo','visitas']

                col1.table(df)
                return df
            def print_responsed(response):
                    list = []
                    # get report data
                    for report in response.get('reports', []):
                    # set column headers
                        columnHeader = report.get('columnHeader', {})
                        dimensionHeaders = columnHeader.get('dimensions', [])
                        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                        rows = report.get('data', {}).get('rows', [])

                    for row in rows:
                        # create dict for each row
                        dict = {}
                        dimensions = row.get('dimensions', [])
                        dateRangeValues = row.get('metrics', [])

                        # fill dict with dimension header (key) and dimension value (value)
                        for header, dimension in zip(dimensionHeaders, dimensions):
                            dict[header] = dimension

                        # fill dict with metric header (key) and metric value (value)
                        for i, values in enumerate(dateRangeValues):
                            for metric, value in zip(metricHeaders, values.get('values')):
                            #set int as int, float a float
                                if ',' in value or '.' in value:
                                    dict[metric.get('name')] = float(value)
                                else:
                                    dict[metric.get('name')] = int(value)

                        list.append(dict)
                    try:
                      df = pd.DataFrame(list)
                      df=df.sort_values(by=['ga:date'],ascending=False) 
                     
                      df['ga:date'] = pd.to_datetime(df['ga:date']).dt.strftime('%d-%m-%y')


                      #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)

                      df.columns =['','visitas']
                      
                      
                      df['%']=df['visitas']/df['visitas'].sum()
                      
                      st.table(df.drop(['visitas'], axis=1))
                    except ValueError as ve:
                      st.warning('No hay visitas')                   
                    return df

            def print_responsepais(response):
                    #col1, col2 = st.beta_columns([1,1])  
                    list = []
                    # get report data
                    for report in response.get('reports', []):
                    # set column headers
                        columnHeader = report.get('columnHeader', {})
                        dimensionHeaders = columnHeader.get('dimensions', [])
                        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                        rows = report.get('data', {}).get('rows', [])

                    for row in rows:
                        # create dict for each row
                        dict = {}
                        dimensions = row.get('dimensions', [])
                        dateRangeValues = row.get('metrics', [])

                        # fill dict with dimension header (key) and dimension value (value)
                        for header, dimension in zip(dimensionHeaders, dimensions):
                            dict[header] = dimension

                        # fill dict with metric header (key) and metric value (value)
                        for i, values in enumerate(dateRangeValues):
                            for metric, value in zip(metricHeaders, values.get('values')):
                            #set int as int, float a float
                                if ',' in value or '.' in value:
                                    dict[metric.get('name')] = float(value)
                                else:
                                    dict[metric.get('name')] = int(value)

                        list.append(dict)
                    try:
                        df = pd.DataFrame(list)
                        df['%']=(df['ga:pageviews'])/df['ga:pageviews'].sum()
                        fig = px.pie(df, values='%', names='ga:country')
                        st.plotly_chart(fig, use_container_width=True)

                        #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
                        df = pd.DataFrame(list)
                        df.columns =['País','visitas']
                        
                        #col1.table(df)
                    except ValueError as ve:
                      st.warning('No hay visitas')                    
                    return df
            def Clean_names(City_name):
                # Search for opening bracket in the name followed by
                # any characters repeated any number of times
                if re.search('\?.*', City_name):

                    # Extract the position of beginning of pattern
                    pos = re.search('\?.*', City_name).start()

                    # return the cleaned name
                    return City_name[:pos]

                else:
                    # if clean up needed return the same name
                    return City_name

            # Updated the city columns
            def print_responsepais55(response):
                    
                    list = []
                    # get report data
                    for report in response.get('reports', []):
                    # set column headers
                        columnHeader = report.get('columnHeader', {})
                        dimensionHeaders = columnHeader.get('dimensions', [])
                        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                        rows = report.get('data', {}).get('rows', [])

                    for row in rows:
                        # create dict for each row
                        dict = {}
                        dimensions = row.get('dimensions', [])
                        dateRangeValues = row.get('metrics', [])

                        # fill dict with dimension header (key) and dimension value (value)
                        for header, dimension in zip(dimensionHeaders, dimensions):
                            dict[header] = dimension

                        # fill dict with metric header (key) and metric value (value)
                        for i, values in enumerate(dateRangeValues):
                            for metric, value in zip(metricHeaders, values.get('values')):
                            #set int as int, float a float
                                if ',' in value or '.' in value:
                                    dict[metric.get('name')] = float(value)
                                else:
                                    dict[metric.get('name')] = int(value)

                        list.append(dict)
                    try:
                      df = pd.DataFrame(list)
                      df=df[~df["ga:city"].str.contains('(not set)')]
                      #fig = px.bar(df, x = "ga:country", y = "ga:pageviews")
                      #col1.plotly_chart(fig, use_container_width=True)
                      df=df.sort_values(by=['ga:pageviews'],ascending=False)
                      df02 = pd.DataFrame(df, columns=['ga:country','ga:city','ga:pageviews']) 
                      #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
                      #df.query('ga:country' == 'Argentina' , inplace = True)
                      #values = df['ga:country'].tolist()
                      
                      DEFAULT='Argentina'
                      def selectbox_with_default(text, values, default=DEFAULT, sidebar=False):
                        func = st.selectbox #if sidebar else st.selectbox
                        return func(text, np.insert(np.array(values, object), 0, default))
                      #pais = st.selectbox('Seleccionar pais', values)
                      #fig = px.line(df0[df0['ga:pagePath'] == a], 
                      #x = "ga:pagePath", y = "ga:pagePath", title = a)

                    
                      df02.columns =['País','Ciudad','visitas']
                     
                      df02['%']=df02['visitas']/df02['visitas'].sum()
                      
                    except ValueError as ve:
                                st.warning('No hay visitas') 
                    st.table(df02.drop(['visitas'], axis=1) )
                    return df
            def print_response_list_url(response):
                DEFAULT = '< Seleccionar >'
                list = []
                # get report data
                for report in response.get('reports', []):
                # set column headers
                    columnHeader = report.get('columnHeader', {})
                    dimensionHeaders = columnHeader.get('dimensions', [])
                    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                    rows = report.get('data', {}).get('rows', [])

                for row in rows:
                    # create dict for each row
                    dict = {}
                    dimensions = row.get('dimensions', [])
                    dateRangeValues = row.get('metrics', [])

                    # fill dict with dimension header (key) and dimension value (value)
                    for header, dimension in zip(dimensionHeaders, dimensions):
                        dict[header] = dimension

                    # fill dict with metric header (key) and metric value (value)
                    for i, values in enumerate(dateRangeValues):
                        for metric, value in zip(metricHeaders, values.get('values')):
                        #set int as int, float a float
                            if ',' in value or '.' in value:
                                dict[metric.get('name')] = float(value)
                            else:
                                dict[metric.get('name')] = int(value)

                    list.append(dict)

                df = pd.DataFrame(list)

                df['ga:pagePath'] = df['ga:pagePath'].apply(Clean_names)
                df02 = pd.DataFrame(df, columns=['ga:pagePath','ga:pageviews'])
                #df02= df02.rename(columns = {'ga:pagePath': 'Ruta'}, inplace = False)
                df02=df02.drop_duplicates(subset=['ga:pagePath'])

                #a = st.selectbox('Seleccionar email', df02)
                #ruta=st.text_input('Ruta',a)






                #df["ga:pagePath"] = df["ga:pagePath"].str.replace('/?.*', '/',inplace=True, regex=True)
                #df["ga:pagePath"]=df["ga:pagePath"].replace({"/": ""}, inplace=True)
                #df0 = pd.DataFrame(df, columns=['ga:pagePath'])
                #df0=df0.sort_values(by=['ga:pagePath'],ascending=True)
                #uso=df[df['ga:pagePath'] == '/english/CEE/']

                values = df02['ga:pagePath'].tolist()
                def selectbox_with_default(text, values, default=DEFAULT, sidebar=False):
                  func = st.selectbox #if sidebar else st.selectbox
                  return func(text, np.insert(np.array(values, object), 0, default))
                a = selectbox_with_default('Seleccionar ruta', values)
                #fig = px.line(df0[df0['ga:pagePath'] == a], 
                #x = "ga:pagePath", y = "ga:pagePath", title = a)

                uso=df02[df02['ga:pagePath'] == a]
                if a == DEFAULT:
                  col1, col2 = st.beta_columns([1,1])         
                  col1.dataframe(df02.assign(hack='').set_index('hack'),   height=600)

                  #col1.dataframe(df02.assign(hack='').set_index('hack'),   height=600)
                  #fig = px.bar(df02, x = "ga:pagePath", y = "ga:pageviews")
                  #col2.plotly_chart(fig, use_container_width=True)
                  #fig = px.pie(df, values='ga:pageviews', names='ga:pagePath', title='')
                  #col2.plotly_chart(fig, use_container_width=True)
                else:
                  uso.index = [""] * len(uso)
                  st.dataframe(uso.assign(hack='').set_index('hack'),    height=600)



                return df
            def print_response_url(response):
                list = []
                # get report data
                for report in response.get('reports', []):
                # set column headers
                    columnHeader = report.get('columnHeader', {})
                    dimensionHeaders = columnHeader.get('dimensions', [])
                    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                    rows = report.get('data', {}).get('rows', [])

                for row in rows:
                    # create dict for each row
                    dict = {}
                    dimensions = row.get('dimensions', [])
                    dateRangeValues = row.get('metrics', [])

                    # fill dict with dimension header (key) and dimension value (value)
                    for header, dimension in zip(dimensionHeaders, dimensions):
                        dict[header] = dimension

                    # fill dict with metric header (key) and metric value (value)
                    for i, values in enumerate(dateRangeValues):
                        for metric, value in zip(metricHeaders, values.get('values')):
                        #set int as int, float a float
                            if ',' in value or '.' in value:
                                dict[metric.get('name')] = float(value)
                            else:
                                dict[metric.get('name')] = int(value)

                    list.append(dict)

                df = pd.DataFrame(list)
                df['ga:pagePath'] = df['ga:pagePath'].apply(Clean_names)
                df=df.groupby("ga:pagePath")['ga:pageviews'].sum()
                #df["ga:pagePath"] = df["ga:pagePath"].str.replace('/?.*', '/',inplace=True, regex=True)
                #df=df["ga:pagePath"].replace({"/?": "x"}, inplace=True)
                st.dataframe(df.assign(hack='').set_index('hack'),  height=600)

                #fig1 = df.plot.bar()

                return df

            def ga_response_dataframe(response):
                row_list = []
                # Get each collected report
                for report in response.get('reports', []):
                    # Set column headers
                    column_header = report.get('columnHeader', {})
                    dimension_headers = column_header.get('dimensions', [])
                    metric_headers = column_header.get('metricHeader', {}).get('metricHeaderEntries', [])

                    # Get each row in the report
                    for row in report.get('data', {}).get('rows', []):
                        # create dict for each row
                        row_dict = {}
                        dimensions = row.get('dimensions', [])
                        date_range_values = row.get('metrics', [])

                        # Fill dict with dimension header (key) and dimension value (value)
                        for header, dimension in zip(dimension_headers, dimensions):
                            row_dict[header] = dimension

                        # Fill dict with metric header (key) and metric value (value)
                        for i, values in enumerate(date_range_values):
                            for metric, value in zip(metric_headers, values.get('values')):
                            # Set int as int, float a float
                                if ',' in value or '.' in value:
                                    row_dict[metric.get('name')] = float(value)
                                else:
                                    row_dict[metric.get('name')] = int(value)

                        row_list.append(row_dict)
                return pd.DataFrame(row_list)
            def print_response_side(response):
                list = []
                # get report data
                for report in response.get('reports', []):
                # set column headers
                    columnHeader = report.get('columnHeader', {})
                    dimensionHeaders = columnHeader.get('dimensions', [])
                    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                    rows = report.get('data', {}).get('rows', [])

                for row in rows:
                    # create dict for each row
                    dict = {}
                    dimensions = row.get('dimensions', [])
                    dateRangeValues = row.get('metrics', [])

                    # fill dict with dimension header (key) and dimension value (value)
                    for header, dimension in zip(dimensionHeaders, dimensions):
                        dict[header] = dimension

                    # fill dict with metric header (key) and metric value (value)
                    for i, values in enumerate(dateRangeValues):
                        for metric, value in zip(metricHeaders, values.get('values')):
                        #set int as int, float a float
                            if ',' in value or '.' in value:
                                dict[metric.get('name')] = float(value)
                            else:
                                dict[metric.get('name')] = int(value)

                    list.append(dict)
                try:    
                  df = pd.DataFrame(list)
                  df.columns =['Visitas']


                  #df = pd.DataFrame({'c1': destinatarios})
                  df = df.reset_index()  # make sure indexes pair with number of rows





                  for index, row in df.iterrows():
                          st.session_state['key']=row['Visitas']+st.session_state.key+500

                  #st.table(df)

                  st.session_state['key']=st.session_state.key
                except ValueError as ve:
                  st.warning('No hay visitas')




                return df
            def print_response_side22(response):
                list = []
                # get report data
                for report in response.get('reports', []):
                # set column headers
                    columnHeader = report.get('columnHeader', {})
                    dimensionHeaders = columnHeader.get('dimensions', [])
                    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                    rows = report.get('data', {}).get('rows', [])

                for row in rows:
                    # create dict for each row
                    dict = {}
                    dimensions = row.get('dimensions', [])
                    dateRangeValues = row.get('metrics', [])

                    # fill dict with dimension header (key) and dimension value (value)
                    for header, dimension in zip(dimensionHeaders, dimensions):
                        dict[header] = dimension

                    # fill dict with metric header (key) and metric value (value)
                    for i, values in enumerate(dateRangeValues):
                        for metric, value in zip(metricHeaders, values.get('values')):
                        #set int as int, float a float
                            if ',' in value or '.' in value:
                                dict[metric.get('name')] = float(value)
                            else:
                                dict[metric.get('name')] = int(value)

                    list.append(dict)

                df = pd.DataFrame(list)
                df.columns =['Visitas repetidas']

                st.table(df)

                #fig1 = df.plot.bar()

                return df   

            def print_response_side2(response):
                list = []
                # get report data
                for report in response.get('reports', []):
                # set column headers
                    columnHeader = report.get('columnHeader', {})
                    dimensionHeaders = columnHeader.get('dimensions', [])
                    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
                    rows = report.get('data', {}).get('rows', [])

                for row in rows:
                    # create dict for each row
                    dict = {}
                    dimensions = row.get('dimensions', [])
                    dateRangeValues = row.get('metrics', [])

                    # fill dict with dimension header (key) and dimension value (value)
                    for header, dimension in zip(dimensionHeaders, dimensions):
                        dict[header] = dimension

                    # fill dict with metric header (key) and metric value (value)
                    for i, values in enumerate(dateRangeValues):
                        for metric, value in zip(metricHeaders, values.get('values')):
                        #set int as int, float a float
                            if ',' in value or '.' in value:
                                dict[metric.get('name')] = float(value)
                            else:
                                dict[metric.get('name')] = int(value)

                    list.append(dict)

                df = pd.DataFrame(list)
                df.columns =['Visitas Totales']

                df = df.reset_index()  # make sure indexes pair with number of rows



                #st.sidebar.table(df)

                for index, row in df.iterrows():
                        st.session_state['key1']=row['Visitas Totales']+109403



                return df    
            def ga_response_dataframe(response):
                row_list = []
                # Get each collected report
                for report in response.get('reports', []):
                    # Set column headers
                    column_header = report.get('columnHeader', {})
                    dimension_headers = column_header.get('dimensions', [])
                    metric_headers = column_header.get('metricHeader', {}).get('metricHeaderEntries', [])

                    # Get each row in the report
                    for row in report.get('data', {}).get('rows', []):
                        # create dict for each row
                        row_dict = {}
                        dimensions = row.get('dimensions', [])
                        date_range_values = row.get('metrics', [])

                        # Fill dict with dimension header (key) and dimension value (value)
                        for header, dimension in zip(dimension_headers, dimensions):
                            row_dict[header] = dimension

                        # Fill dict with metric header (key) and metric value (value)
                        for i, values in enumerate(date_range_values):
                            for metric, value in zip(metric_headers, values.get('values')):
                            # Set int as int, float a float
                                if ',' in value or '.' in value:
                                    row_dict[metric.get('name')] = float(value)
                                else:
                                    row_dict[metric.get('name')] = int(value)

                        row_list.append(row_dict)
                return pd.DataFrame(row_list)


            st.markdown("<hr style='height:2px;border-width:0;color:gray;background-color:#008357'><div style='text-align:  left; color: #000;font-family: Oswald; font-size:18px;'>"+titles+"👇 </div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align:  left; color: #008357;font-family: Oswald; font-size:16px;padding:5px;'>Sección: "+orden+"</div>", unsafe_allow_html=True)
           
            st.markdown("<div style='text-align:  left; color: #000;font-family: Oswald; font-size:16px;padding:5px;'>Publicada: "+fecha+"</div>", unsafe_allow_html=True)
            #st.markdown("<div style='text-align:  left; color: #e65100;font-family: Oswald;font-size:12px;margin-left:5px;'>Visitas: "+str(st.session_state.key)+"</div>", unsafe_allow_html=True)

            analytics = initialize_analyticsreporting()
            response1 = get_report20(analytics) #get the response from the API
            print_response_side2(response1) #print the response from the API
            response1 = get_report22(analytics) #get the response from the API
            print_response_side(response1) #print the response from the API


            #response = get_report22(analytics) #get the response from the API
            #print_response_side22(response) #print the response from the API
            #if display_code=='Inicio': 
            # response = get_report28(analytics) #get the response from the API
            # print_response(response) #print the response from the API
            col1, col2 = st.beta_columns([1,1])
            col1.markdown("<div style='text-align:  left; color: #e65100;font-family: Oswald;font-size:18px;margin-left:5px;'>Visitas: "+str(st.session_state.key)+"</div><br>", unsafe_allow_html=True)

            col2.markdown("<a href='"+destinatarios+"' target='_blank'><img src='https://noticias.usal.edu.ar/"+str(image)+"' style='width:60%;border-radius:3px;'></a>", unsafe_allow_html=True)
            
            with col1.beta_expander('Ver por país:'):
            #pais=st.checkbox('Ver por país:')
            #if pais:
              response = get_reportcity(analytics) #get the response from the API


              df = ga_response_dataframe(response)
              df['ga:latitude'] = pd.to_numeric(df['ga:latitude'])
              df['ga:longitude'] = pd.to_numeric(df['ga:longitude'])
              #df.columns =["Longitude", "Latitude","visitas"]

              mylist = ['ga:latitude','ga:longitude']
              df=df[~df[mylist].eq(0).all(1)]
              #folium_static(map)
              #st.table(df)
              map_ = folium.Map(location=[-34.6000797,-58.3938616], 
                                tiles='OpenStreetMap',
                                zoom_start = 2,zoom_control=True,
               scrollWheelZoom=False,
               dragging=False)
              for index, row in df.iterrows():
                   tooltip = 'Visita'
                   folium.Marker((row['ga:latitude'], row['ga:longitude']),tooltip=tooltip,
                   icon=folium.Icon(color='green')).add_to(map_)
              folium_static(map_)
              st.markdown("""
<style>
table td:nth-child(1) {
display: none
}
table th:nth-child(1) {
display: none
}

.css-glyadz {
font-size: 1rem;
color: rgb(38, 39, 48);
margin-bottom: 0.4rem;
height: 1.5rem;
vertical-align: middle;
display: flex;
flex-direction: row;
-webkit-box-align: center;
align-items: center;
}
</style>
""", unsafe_allow_html=True)
              response = get_report55(analytics) #get the response from the API
              print_responsepais55(response) #print the response from the API
              response = get_report5(analytics) #get the response from the API
              print_responsepais(response) #print the response from the API
            arriba.markdown('<div style="text-align:center; border-bottom:1px solid #008357;border-top:1px solid #000;font-family: Oswald;">VISITAS TOTALES: '+str(st.session_state.key1)+'</div><br>', unsafe_allow_html=True)                        
          
            with col1.beta_expander('Ver por dispositivo:'):
            #dispo=st.checkbox('Ver por dispositivo:')
            #if dispo:
              response = get_report3(analytics) #get the response from the API
              print_responsebar(response) #print the response from the API 
              #print_response_list_url(response)  



            with col1.beta_expander('Ver por día:'):
              st.markdown("""
<style>
table td:nth-child(1) {
display: none
}
table th:nth-child(1) {
display: none
}


.css-glyadz {
    font-size: 1rem;
    color: rgb(38, 39, 48);
    margin-bottom: 0.4rem;
    height: 1.5rem;
    vertical-align: middle;
    display: flex;
    flex-direction: row;
    -webkit-box-align: center;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)
            #dia=st.checkbox('Ver por día:')
            #if dia:
              response = get_report0(analytics) #get the response from the API
              print_responsed(response) #print the response from the API    
def ua():

  st.session_state['key'] = 0
  st.session_state['key1'] = 0
  st.session_state['key2'] = 0
  noticiass = []
  pais='Argentina'
  st.markdown("""
<style>
.table td:first-child {
    text-align: left;
}
</style>
""", unsafe_allow_html=True)
  VIEW_ID = '53262468'
  def initialize_analyticsreporting():
      parser = argparse.ArgumentParser(
          formatter_class=argparse.RawDescriptionHelpFormatter,
          parents=[tools.argparser])
      flags = parser.parse_args([])
      credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", SCOPES)
      if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, flags)
      http = credentials.authorize(http=httplib2.Http())
      analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)
      return analytics

 





  #df['fecha']=[d.strftime('%d-%m-%Y') if not pd.isnull(d) else '' for d in df['fecha']]
  #df['fecha']=pd.to_datetime(df['fecha']).dt.strftime('%Y-%m-%d') 
  #st.table(df)
 
  col111, col222 = st.beta_columns([1,1])
  aca=st.empty()
  import datetime as DT
  today = DT.date.today()
  week_ago = today - DT.timedelta(days=7)
  start_date = col111.date_input('Desde :',week_ago)
  date=start_date
  end_date = col222.date_input('Hasta :')
  date2=end_date
  if start_date <= end_date:
      pass
  else:
      st.error('Error: Desde debe ser anterior a Hasta.')



  def get_reportsolo2(analytics):

    return analytics.reports().batchGet(
        body={
          'reportRequests': [
        {
         'viewId': VIEW_ID,
         #'dateRanges': [{'startDate': '2022-04-07', 'endDate': '2022-04-16'}],
         'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
         'samplingLevel':'LARGE',
         "includeEmptyRows" : True,
         'metrics': [{'expression':'ga:pageviews'}],
         'dimensions': [{"name": "ga:pageTitle"}],'orderBys': [{"fieldName": "ga:pageviews", "sortOrder": "DESCENDING"}],
         'pageSize':'60'
        }]
        }
    ).execute()








    

  def print_response_sidenoti2(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)
      try:

        

        #df = pd.DataFrame({'c1': destinatarios})
        df = pd.DataFrame(list)
        
        df.columns =['Noticia','Visitas']
        options = ['No se ha encontrado la página solicitada. | Diplomaturas USAL','Bienvenidos | Diplomaturas USAL','dolores.giuliani | Diplomaturas USAL','gustavo.blanco | Diplomaturas USAL','f.baccanelli | Diplomaturas USAL','Acceso denegado | Diplomaturas USAL','chtgrant | Diplomaturas USAL', 'm.pombo | Diplomaturas USAL','Log in | Diplomaturas USAL','juan.spina | Diplomaturas USAL' ,'Iniciar sesión | Diplomaturas USAL'] 
    # selecting rows based on condition 
        df = df.loc[~df['Noticia'].isin(options)]
        df["Noticia"]=df["Noticia"].str.replace(r'|Diplomaturas USAL','')


        #df = pd.DataFrame({'c1': destinatarios})
        df = df.reset_index()  # make sure indexes pair with number of rows





        for index, row in df.iterrows():
              
            notis = { 
            'Noticia': row['Noticia'],
            #'Fecha':orden,
            'Visitas': row['Visitas']
            }
            noticiass.append(notis)


            


      except ValueError as ve:
            pass     





      return df






  #st.markdown("<hr style='height:2px;border-width:0;color:gray;background-color:#008357'><div style='text-align:  left; color: #000;font-family: Oswald; font-size:18px;'>"+titles+"👇 </div>", unsafe_allow_html=True)
  #st.markdown("<div style='text-align:  left; color: #008357;font-family: Oswald; font-size:16px;padding:5px;'>Sección: "+orden+"</div>", unsafe_allow_html=True)
  
  #st.markdown("<div style='text-align:  left; color: #000;font-family: Oswald; font-size:16px;padding:5px;'>Publicada: "+orden+"</div>", unsafe_allow_html=True)
  #arriba.markdown("<div style='text-align:  center; color: #008357;font-family: Oswald;font-size:16px;margin-left:5px;'>Ranking de Noticias</div>", unsafe_allow_html=True)

  analytics = initialize_analyticsreporting()

  #response1 = get_reportsolo(analytics) #get the response from the API
  #print_response_sidenoti(response1) #print the response from the API
  #arriba.markdown("<div style='text-align:  left; color: #e65100;font-family: Oswald;font-size:12px;margin-left:5px;'>Visitas: "+str(st.session_state.key1)+"</div>", unsafe_allow_html=True)
  response122 = get_reportsolo2(analytics) #get the response from the API
  print_response_sidenoti2(response122) #print the response from the API

  #response = get_report22(analytics) #get the response from the API
  #print_response_side22(response) #print the response from the API
  #if display_code=='Inicio': 
  # response = get_report28(analytics) #get the response from the API
  # print_response(response) #print the response from the API
  
  #col1.markdown("<div style='text-align:  left; color: #e65100;font-family: Oswald;font-size:18px;margin-left:5px;'>Visitas: "+str(st.session_state.key)+"</div><br>", unsafe_allow_html=True)

  #col2.markdown("<a href='"+destinatarios+"' target='_blank'><img src='https://noticias.usal.edu.ar/"+str(image)+"' style='width:60%;border-radius:3px;'></a>", unsafe_allow_html=True)
  def highlight_max(data, color='yellow'):
      '''
      highlight the maximum in a Series or DataFrame
      '''
      attr = 'background-color: {}'.format(color)
      if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
          is_max = data == data.max()
          return [attr if v else '' for v in is_max]
      else:  # from .apply(axis=None)
          is_max = data == data.max().max()
          return pd.DataFrame(np.where(is_max, attr, ''),
                              index=data.index, columns=data.columns)
  todas=pd.DataFrame(noticiass)
 
  #todas['Fecha']=pd.to_datetime(todas['Fecha']).dt.strftime('%d-%m-%Y')
  todas=todas.sort_values(by=['Visitas'],ascending=False) 
  todas['Noticia']=todas['Noticia'].str.slice(0,100)
  #col111.table(todas.style.apply(highlight_max, subset=['Visitas']))
  fig = px.bar(todas, x = "Visitas", y = "Noticia", orientation='h',text='Visitas',height=2000,color ='Visitas')
  notis=len(todas)

  aca.markdown("<div style='text-align:  center; color: #e65100;font-family: Oswald; font-size:18px;padding:5px;'>Ranking : "+str(notis) +" noticias más leídas en el período elegido</div>", unsafe_allow_html=True)
    
  #fig.update_yaxes(range=(70, 500))
  fig.update_layout(
      font_family="Oswald",
      font_color="#008357",
      title_font_family="Oswald",
      title_font_color="red",
      legend_title_font_color="#008357",
      font=dict(
        family="Oswald",
        size=15,
        color="#000"
        
    )
  )
  fig.update_traces( textposition='outside')
  fig.update_xaxes(title_font_family="Oswald",title_font_color="#000")
  #fig.update_yaxes(visible=False, showticklabels=False)
  fig.update_layout(yaxis={'categoryorder':'total ascending'})
  fig.update_layout(barmode='group', bargap=0.10,bargroupgap=0.0)
  st.plotly_chart(fig, use_container_width=True)
def suple():
  pais='Argentina'
  st.session_state['key'] = 0
  st.session_state['key1'] = 0
  st.session_state['key2'] = 0
  #st.markdown('<div style="text-align:left; font-size:18px;border-bottom:1px solid #008357;font-family: Oswald"><b>ESTADÍSTICAS DESDE EL 15/3/2019 AL '+today+'</b></div><br>', unsafe_allow_html=True)
  st.markdown("""
<style>
table td:nth-child(1) {
    display: none
}
table th:nth-child(1) {
    display: none
}
.css-4ux067 {
    width: 1514px;
    margin: 0px 0px 1rem;
    text-align: center;
}
.css-glyadz {
    font-size: 1rem;
    color: rgb(38, 39, 48);
    margin-bottom: 0.4rem;
    height: 1.5rem;
    vertical-align: middle;
    display: flex;
    flex-direction: row;
    -webkit-box-align: center;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)
  #VIEW_ID = '60591749'#'222848977'
  def pull_sheet_data(SCOPES,SPREADSHEET_ID,DATA_TO_PULL):

          service = build('sheets', 'v4', credentials=cred)
          sheet = service.spreadsheets()
          result = sheet.values().get(
          spreadsheetId=SPREADSHEET_ID,
          range=DATA_TO_PULL).execute()
          values = result.get('values', [])

          if not values:
                  print('No data found.')
          else:
                  rows = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                  range=DATA_TO_PULL).execute()
                  data = rows.get('values')
                  print("COMPLETE: Data copied")
                  return data
  SPREADSHEET_ID = ids
  DATA_TO_PULL = 'analytics'
  #display_code = st.sidebar.radio("Mostrar", ( "Por número","Búsqueda"))
  data = [['clayss.org.ar',60591749],['clayss.org',254644946],['noticias.clayss.org',222848977],['Seminario Clayss',225379278],['Seminario Clayss Uruguay',254692529]]
  df = pd.DataFrame(data,columns=['dominio','id'])
  values = df['dominio'].tolist()
  options = df['id'].tolist()
  dic = dict(zip(options, values))
  #VIEW_ID = st.selectbox('Seleccionar Dominio:', options, format_func=lambda x: dic[x])
  VIEW_ID = '201209640'
  #ruta=st.text_input('Escribir ruta:','/es')
  date = datetime.date(2019, 3, 15)
  date2 = date.today()
  #date = st.sidebar.date_input('Desde', datetime.date(2019,6,1))
  #date2 = st.sidebar.date_input('Hasta')



  def initialize_analyticsreporting():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[tools.argparser])
    flags = parser.parse_args([])
    credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", SCOPES)
    if credentials is None or credentials.invalid:
      credentials = tools.run_flow(flow, storage, flags)
    http = credentials.authorize(http=httplib2.Http())
    analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)
    return analytics
  def get_report20(analytics):
    ruta='es/'
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
           
              'metrics': [
          {
              'expression': 'ga:pageviews'
          }
       ]

          ,

                'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()
  def get_report202(analytics):
    
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
            
              'metrics': [
          {
              'expression': 'ga:pageviews'
          }
       ]

          ,

                'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()
  def get_report0(analytics):
              return analytics.reports().batchGet(
                  body={
                    'reportRequests': [
                    {
                      'viewId': VIEW_ID,
                      'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                      'dimensions':[{'name':'ga:date'}],         
                      'metrics': [{'expression': 'ga:pageviews'}],
                      'dimensionFilterClauses': [
                      {
                      'filters':[
                  {
                  "operator": "PARTIAL",
                  "dimensionName": "ga:pagePath",
                  "expressions": [
                    ruta
                  ]
                  }
                ]
                    }
                  ]
                    }]
                  }
              ).execute()



  def get_report3(analytics):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],

            
             'metrics': [
          {
              'expression': 'ga:pageviews'
          }
       ]

          ,
           "dimensions": [
              {"name": "ga:deviceCategory"}
          ],
            'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()

  def get_report5(analytics):
    return analytics.reports().batchGet(
      body=
      {"reportRequests":[{"viewId": VIEW_ID,'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],"metrics":[{"expression": "ga:pageviews"}],

          "dimensions": [{"name": "ga:country"}],

                    'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }] }
          ).execute()
  def get_report55(analytics):
      return analytics.reports().batchGet(
        body=
        {"reportRequests":[{"viewId": VIEW_ID,'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],"metrics":[{"expression": "ga:pageviews"}],

            "dimensions": [{"name": "ga:country"},{"name": "ga:city"}],

                      'dimensionFilterClauses': [
              {
              'filters':[
          {
          "operator": "PARTIAL",
          "dimensionName": "ga:pagePath",

          "expressions": [
            ruta
          ]

          }

        ]
            }
          ]
            }] }
            ).execute()     
           
  def get_reportsolo(analytics):

    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
            
              'metrics': [
          {
              'expression': 'ga:pageviews'
          }
       ]

          ,

                'dimensionFilterClauses': [
            {
            'filters':[
        {
         "operator": "PARTIAL",
         "dimensionName": "ga:pagePath",
         "expressions": [
          ruta
         ]
        }
       ]
          }
        ]
          }]
        }
    ).execute()


  def get_reportcity(analytics):
                      return analytics.reports().batchGet(body={
                      'reportRequests': [{
                          'viewId': VIEW_ID,
                          'dateRanges': [{'startDate': str(date), 'endDate': str(date2)}],
                          'metrics': [
                              {"expression": "ga:pageviews"},
                          ], "dimensions": [
                              {"name": "ga:longitude"},
                              {"name": "ga:latitude"}
                          ],            'dimensionFilterClauses': [
                              {
                              'filters':[
                          {
                          "operator": "PARTIAL",
                          "dimensionName": "ga:pagePath",
                          "expressions": [
                            ruta
                          ]
                          }
                        ]
                            }
                          ]
                            }]
                          
                    }).execute()  

  def print_responsebar(response):
      #col1, col2 = st.beta_columns([1,1])  
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)

      df = pd.DataFrame(list)
      df['%']=(df['ga:pageviews'])/df['ga:pageviews'].sum()
      
      fig = px.pie(df, values='%', names='ga:deviceCategory')
      st.plotly_chart(fig, use_container_width=True)

      #col1.dataframe(df.assign(hack='').set_index('hack'),  height=600)
      df = pd.DataFrame(list)
      df.columns =['Dispositivo','Visitas']

      #col1.table(df)
      return df
  def print_responsepais55(response):
           
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)
            df=df[~df["ga:city"].str.contains('(not set)')]
            #fig = px.bar(df, x = "ga:country", y = "ga:pageviews")
            #col1.plotly_chart(fig, use_container_width=True)
            df=df.sort_values(by=['ga:pageviews'],ascending=False)
            df02 = pd.DataFrame(df, columns=['ga:country','ga:city','ga:pageviews']) 
            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
            #df.query('ga:country' == 'Argentina' , inplace = True)
            #values = df['ga:country'].tolist()
            
            DEFAULT='Argentina'
            def selectbox_with_default(text, values, default=DEFAULT, sidebar=False):
              func = st.selectbox #if sidebar else st.selectbox
              return func(text, np.insert(np.array(values, object), 0, default))
            #pais = st.selectbox('Seleccionar pais', values)
            #fig = px.line(df0[df0['ga:pagePath'] == a], 
            #x = "ga:pagePath", y = "ga:pagePath", title = a)

           
            df02.columns =['País','Ciudad','Visitas']
            df02['%']=df02['Visitas']/df02['Visitas'].sum()
          except ValueError as ve:
                      st.warning('No hay visitas') 
          
          st.table(df02.drop(['Visitas'], axis=1))
          return df
  def print_responsed(response):
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)
            df=df.sort_values(by=['ga:date'],ascending=False) 
            
            df['ga:date'] = pd.to_datetime(df['ga:date']).dt.strftime('%d-%m-%y')


            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)

            df.columns =['','visitas']
            
            
            df['%']=df['visitas']/df['visitas'].sum()
            
            st.table(df.drop(['visitas'], axis=1))
          except ValueError as ve:
            st.warning('No hay visitas')                   
          return df

  def print_responsepais(response):
          #col1, col2 = st.beta_columns([1,1])  
          list = []
          # get report data
          for report in response.get('reports', []):
          # set column headers
              columnHeader = report.get('columnHeader', {})
              dimensionHeaders = columnHeader.get('dimensions', [])
              metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
              rows = report.get('data', {}).get('rows', [])

          for row in rows:
              # create dict for each row
              dict = {}
              dimensions = row.get('dimensions', [])
              dateRangeValues = row.get('metrics', [])

              # fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimensionHeaders, dimensions):
                  dict[header] = dimension

              # fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(dateRangeValues):
                  for metric, value in zip(metricHeaders, values.get('values')):
                  #set int as int, float a float
                      if ',' in value or '.' in value:
                          dict[metric.get('name')] = float(value)
                      else:
                          dict[metric.get('name')] = int(value)

              list.append(dict)
          try:
            df = pd.DataFrame(list)
            fig = px.pie(df, names = "ga:country", values = "ga:pageviews")
            st.plotly_chart(fig, use_container_width=True)

            #st.dataframe(df.assign(hack='').set_index('hack'),  height=600)
            df = pd.DataFrame(list)
            df.columns =['País','Visitas']
            #st.table(df)
          except ValueError as ve:
                      st.warning('No hay visitas') 
          #col1.table(df)
          return df



  def print_response_side(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)
      try:
        df = pd.DataFrame(list)
        df.columns =['Visitas']


        #df = pd.DataFrame({'c1': destinatarios})
        df = df.reset_index()  # make sure indexes pair with number of rows





        for index, row in df.iterrows():
                st.session_state['key']=row['Visitas']+st.session_state.key

        #st.table(df)

        st.session_state['key']=st.session_state.key+1
      except ValueError as ve:
             st.warning('No hay visitas')    





      return df
  def print_response_sidenoti(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)
      try:
        df = pd.DataFrame(list)
        df.columns =['Visitas']


        #df = pd.DataFrame({'c1': destinatarios})
        df = df.reset_index()  # make sure indexes pair with number of rows





        for index, row in df.iterrows():
                st.session_state['key2']=row['Visitas']

        #st.table(df)

        st.session_state['key2']=st.session_state.key2+50
      except ValueError as ve:
             st.warning('No hay visitas')    





      return df

  def print_response_side2(response):
      list = []
      # get report data
      for report in response.get('reports', []):
      # set column headers
          columnHeader = report.get('columnHeader', {})
          dimensionHeaders = columnHeader.get('dimensions', [])
          metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
          rows = report.get('data', {}).get('rows', [])

      for row in rows:
          # create dict for each row
          dict = {}
          dimensions = row.get('dimensions', [])
          dateRangeValues = row.get('metrics', [])

          # fill dict with dimension header (key) and dimension value (value)
          for header, dimension in zip(dimensionHeaders, dimensions):
              dict[header] = dimension

          # fill dict with metric header (key) and metric value (value)
          for i, values in enumerate(dateRangeValues):
              for metric, value in zip(metricHeaders, values.get('values')):
              #set int as int, float a float
                  if ',' in value or '.' in value:
                      dict[metric.get('name')] = float(value)
                  else:
                      dict[metric.get('name')] = int(value)

          list.append(dict)

      df = pd.DataFrame(list)
      df.columns =['Visitas Totales']

      df = df.reset_index()  # make sure indexes pair with number of rows



      #st.sidebar.table(df)

      for index, row in df.iterrows():
              st.session_state['key1']=row['Visitas Totales']+109403



      return df    
  def ga_response_dataframe(response):
      row_list = []
      # Get each collected report
      for report in response.get('reports', []):
          # Set column headers
          column_header = report.get('columnHeader', {})
          dimension_headers = column_header.get('dimensions', [])
          metric_headers = column_header.get('metricHeader', {}).get('metricHeaderEntries', [])

          # Get each row in the report
          for row in report.get('data', {}).get('rows', []):
              # create dict for each row
              row_dict = {}
              dimensions = row.get('dimensions', [])
              date_range_values = row.get('metrics', [])

              # Fill dict with dimension header (key) and dimension value (value)
              for header, dimension in zip(dimension_headers, dimensions):
                  row_dict[header] = dimension

              # Fill dict with metric header (key) and metric value (value)
              for i, values in enumerate(date_range_values):
                  for metric, value in zip(metric_headers, values.get('values')):
                  # Set int as int, float a float
                      if ',' in value or '.' in value:
                          row_dict[metric.get('name')] = float(value)
                      else:
                          row_dict[metric.get('name')] = int(value)

              row_list.append(row_dict)
      return pd.DataFrame(row_list)

  def main():

    analytics = initialize_analyticsreporting()
    response = get_report20(analytics) #get the response from the API
    print_response_side2(response) #print the response from the API
    #st.markdown('<div style="text-align:left; border-bottom:1px solid #008357;border-top:1px solid #000;font-family: Oswald;">VISITAS TOTALES: '+str(st.session_state.key1)+'</div><br>', unsafe_allow_html=True)                        
      



  if __name__ == '__main__':
    main()
  def pull_sheet_data(SCOPES,SPREADSHEET_ID,DATA_TO_PULL):

        service = build('sheets', 'v4', credentials=cred)
        sheet = service.spreadsheets()
        result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=DATA_TO_PULL).execute()
        values = result.get('values', [])

        if not values:
                print('No data found.')
        else:
                rows = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                range=DATA_TO_PULL).execute()
                data = rows.get('values')
                print("COMPLETE: Data copied")
                return data
  SPREADSHEET_ID = ids
  DATA_TO_PULL = 'bases'
  data1 = pull_sheet_data(scopes,SPREADSHEET_ID,DATA_TO_PULL)
  base = pd.DataFrame(data1[1:], columns=data1[0]) 
  SPREADSHEET_ID2 = ids
  DATA_TO_PULL2 = 'remitentes'
  data12 = pull_sheet_data(scopes,SPREADSHEET_ID2,DATA_TO_PULL2)
  base2 = pd.DataFrame(data12[1:], columns=data12[0])
  gclient = authorize(cred)
  def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)  
  #Scrape the source code from the specified link:
  #In this example I'm using my own medium wall
  st.markdown('<link href="https://fonts.googleapis.com/css2?family=Oswald" rel="stylesheet"><style>.css-tsy3mu{font-family: Oswald;}.st-bg,.css-177yq5e, .st-bo,.st-bf,.st-b4,.st-b7,.st-be,.st-bi,.st-dq {position: relative;font-family: Oswald;}.css-1ekf893 {margin-bottom: -1rem;font-family: Oswald;}.css-1v0mbdj {margin-top: -60px;}body{font-family: "Oswald", Arial, sans-serif;}</style>', unsafe_allow_html=True)
  arriba.markdown('<div style="text-align:center; border-bottom:1px solid #008357;border-top:1px solid #000;font-family: Oswald;">VISITAS TOTALES: '+str(st.session_state.key1)+'</div><br>', unsafe_allow_html=True)                        
  #display_code = st.sidebar.radio("Mostrar", ( "Por número","Búsqueda"))

  data = requests.get("https://noticias.usal.edu.ar/es/suplementos-2022")  
  URL = "https://noticias.usal.edu.ar/es/suplementos-2022"

  #if display_code=='Por número':
  req = requests.get(URL)
  html = BeautifulSoup(req.text, "html.parser")


  previews2=[]
  #entradas1 = html.find('table', {'class': 'cols-0'})



  #numeros0 = entradas1.find_all('td', {'class': 'views-field'})
  numeros = html.find_all('div', {'class': 'col-lg-6'})


  for i, entrada in enumerate(numeros):
        title = entrada.find('div', {'class': 'tapanum'}).getText()
        boletin=entrada.find('a').get_text()
        #html = str(entrada.find('a', attrs = {'href':re.compile(r'^.*\b\b.*$')}))
        html = entrada.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
        image=entrada.find('img') 
        image = str(image.attrs['src']).split(" ")[0]   
        image='https://noticias.usal.edu.ar'+image

        entrada_preview2 = { 
        'title': str(title),
        'image': str(image),
        'linkn': "https://noticias.usal.edu.ar"+html
        }
        previews2.append(entrada_preview2)
  df=pd.DataFrame(previews2) 
  #st.table(df)        
  #df0=df0.sort_values(by=['nombre'],ascending=True)
  values = df['title'].tolist()
  options = df['linkn'].tolist()
  dic = dict(zip(options, values))
  col11, col12= st.beta_columns([1,1]) 





  previews = []



  for i,article in enumerate(previews2):


                        


                        t=i+1
                        ruta1=article['linkn']
                        ruta=ruta1.replace('https://noticias.usal.edu.ar','')
                        st.markdown("<hr style='height:2px;border-width:0;color:gray;background-color:#008357'><div style='text-align:  left; color: #000;font-family: Oswald; font-size:18px;'>"+article['title']+"👇 </div>", unsafe_allow_html=True)
                   
                                             
                   
                       #st.markdown("<div style='text-align:  left; color: #e65100;font-family: Oswald;font-size:18px;padding:5px;'>Visitas:"+str(st.session_state.key+100)+"</div>", unsafe_allow_html=True)

                        col11, col12= st.beta_columns([1,1])

                        col12.markdown("<img src='"+article['image']+"' style='width:80%;border-radius:3px;'>", unsafe_allow_html=True) 
                        analytics = initialize_analyticsreporting()
                        response1 = get_reportsolo(analytics) #get the response from the API
                        print_response_sidenoti(response1) #print the response from the API
                        response11= get_report202(analytics) #get the response from the API
                        print_response_side(response11) #print the response from the API                        
                        col11.markdown("<div style='text-align:  left; color: #e65100;font-family: Oswald;font-size:18px;padding:5px;'>Visitas:"+str(st.session_state.key2)+"</div>", unsafe_allow_html=True)



                        #response = get_report22(analytics) #get the response from the API
                        #print_response_side22(response) #print the response from the API
                        #if display_code=='Inicio': 
                        # response = get_report28(analytics) #get the response from the API
                        # print_response(response) #print the response from the API




                        with col11.beta_expander('Ver por país/ciudad:'):
                          st.markdown("""
                          <style>
            
                
                          .css-glyadz {
                              font-size: 1rem;
                              color: rgb(38, 39, 48);
                              margin-bottom: 0.4rem;
                              height: 1.5rem;
                              vertical-align: middle;
                              display: flex;
                              flex-direction: row;
                              -webkit-box-align: center;
                              align-items: center;
                          }
                          </style>
                          """, unsafe_allow_html=True)
                        #pais=st.checkbox('Ver por país:')
                        #if pais:
                          response = get_reportcity(analytics) #get the response from the API


                          df = ga_response_dataframe(response)
                          if df.empty == True:
                              print('DataFrame is empty')
                          else:

                            df['ga:latitude'] = pd.to_numeric(df['ga:latitude'])
                            df['ga:longitude'] = pd.to_numeric(df['ga:longitude'])
                            mylist = ['ga:latitude','ga:longitude']
                            df=df[~df[mylist].eq(0).all(1)]
                            df.columns =["Longitude", "Latitude","visitas"]


                            #folium_static(map)
                            #st.table(df)
                            map_ = folium.Map(location=[df['Latitude'].iloc[0],df['Longitude'].iloc[0]], 
                                              tiles='OpenStreetMap',
                                              zoom_start = 2,zoom_control=True,
                 scrollWheelZoom=False,
                 dragging=False)
                            for index, row in df.iterrows():
                                  tooltip = 'Visita'
                                  folium.Marker((row['Latitude'], row['Longitude']),tooltip=tooltip,
                                  icon=folium.Icon(color='green')).add_to(map_)
                            folium_static(map_)
                            response = get_report55(analytics) #get the response from the API
                            print_responsepais55(response) #print the response from the API
                            response = get_report5(analytics) #get the response from the API
                            print_responsepais(response) #print the response from the API
                        with col11.beta_expander('Ver por dispositivo:'):
               
                          response = get_report3(analytics) #get the response from the API
                          print_responsebar(response) #print the response from the API 
                          #print_response_list_url(response)                           
                        with col11.beta_expander('Ver por día:'):
                      
                          response = get_report0(analytics) #get the response from the API
                          print_responsed(response) #print the response from the API    
   

app = MultiPage()
# Add pages

app.add_page("🌎 Totales x país", total)
app.add_page("📰 Por Número", numero)
app.add_page("🗞️ Suplementos",suple)
app.add_page("🏆 Ranking",ua)
app.add_page("🔍 Búsqueda",busca)
app.run()

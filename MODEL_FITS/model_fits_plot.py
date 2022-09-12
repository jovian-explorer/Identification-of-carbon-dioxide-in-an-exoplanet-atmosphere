
#importing libraries required
#-----------------------------------------------------------------------------------------------------------------
#importing libraries
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------------------------------------------
fig = plt.figure()
#-------------------------------------------------ATMO------------------------------------------------------------
#importing data 
ATMO = '/home/dev/Desktop/jwst_data/MODEL_FITS/ATMO_MODEL.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
atmo = pd.read_csv(ATMO,delimiter = '  ')
# print(atmo.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
atmo.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl = np.array(atmo.wl)            # Values of wavelength
depth= np.array(atmo.depth)       # Values of transit depth
plt.plot(wl,depth*100,label = "ATMO")
#-----------------------------------------------------------------------------------------------------------------
#-------------------------------------------PHOENIX---------------------------------------------------------------
#importing data 
PHOENIX_MODEL = '/home/dev/Desktop/jwst_data/MODEL_FITS/PHOENIX_MODEL.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
phoenix = pd.read_csv(PHOENIX_MODEL,delimiter = ' ')
# print(phoenix.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
phoenix.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl = np.array(phoenix.wl)             # Values of wavelength
depth= np.array(phoenix.depth)        # Values of transit depth
plt.plot(wl,depth*100,label = "PHOENIX")
#-----------------------------------------------------------------------------------------------------------------
#--------------------------------------------PICASO---------------------------------------------------------------
#importing data 
PICASO_MODEL = '/home/dev/Desktop/jwst_data/MODEL_FITS/PICASO_MODEL.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
picaso = pd.read_csv(PICASO_MODEL,delimiter = ' ')
# print(picaso.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
picaso.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl =np.array(picaso.wl)           		   # Values of iteration
depth= np.array(picaso.depth)              # Values of transit depth
plt.plot(wl,depth*100,label = "PICASO")
#-----------------------------------------------------------------------------------------------------------------
#-------------------------------------------ScCHIMERA_MODEL-------------------------------------------------------
#importing data 
ScCHIMERA_MODEL = '/home/dev/Desktop/jwst_data/MODEL_FITS/ScCHIMERA_MODEL.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
scchimera = pd.read_csv(ScCHIMERA_MODEL,delimiter = ' ')
# print(scchimera.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
scchimera.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl =np.array(scchimera.wl)           		  # Values of wavelength
depth= np.array(scchimera.depth)              # Values of transit depth
plt.plot(wl,depth*100,label = "ScCHIMERA")
#-----------------------------------------------------------------------------------------------------------------
#-------------------------------------------ScCHIMERA_MODEL_noCH4-------------------------------------------------
#importing data 
ScCHIMERA_MODEL_noCH4 = '/home/dev/Desktop/jwst_data/MODEL_FITS/ScCHIMERA_MODEL_noCH4.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
scchimera_noch4 = pd.read_csv(ScCHIMERA_MODEL_noCH4,delimiter = ' ')
# print(scchimera_noch4.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
scchimera_noch4.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl =np.array(scchimera_noch4.wl)           		  # Values of wavelength
depth= np.array(scchimera_noch4.depth)            # Values of transit depth
plt.plot(wl,depth*100,label = "noCH4")
#-----------------------------------------------------------------------------------------------------------------
#-------------------------------------------ScCHIMERA_MODEL_noCloud-----------------------------------------------
#importing data 
ScCHIMERA_MODEL_noCloud = '/home/dev/Desktop/jwst_data/MODEL_FITS/ScCHIMERA_MODEL_noCloud.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
scchimera_nocloud = pd.read_csv(ScCHIMERA_MODEL_noCloud,delimiter = ' ')
# print(scchimera_nocloud.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
scchimera_nocloud.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl =np.array(scchimera_nocloud.wl)           		  # Values of wavelength
depth= np.array(scchimera_nocloud.depth)              # Values of transit depth
plt.plot(wl,depth*100,label = "noCloud")
#-----------------------------------------------------------------------------------------------------------------
#-------------------------------------------ScCHIMERA_MODEL_noCO--------------------------------------------------
#importing data 
ScCHIMERA_MODEL_noCO = '/home/dev/Desktop/jwst_data/MODEL_FITS/ScCHIMERA_MODEL_noCO.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
scchimera_noCO = pd.read_csv(ScCHIMERA_MODEL_noCO,delimiter = ' ')
# print(scchimera_noCO.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
scchimera_noCO.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl =np.array(scchimera_noCO.wl)           		  # Values of wavelength
depth= np.array(scchimera_noCO.depth)             # Values of transit depth
plt.plot(wl,depth*100,label = "noCO")
#-----------------------------------------------------------------------------------------------------------------
#-------------------------------------------ScCHIMERA_MODEL_noCO2-------------------------------------------------
#importing data 
ScCHIMERA_MODEL_noCO2 = '/home/dev/Desktop/jwst_data/MODEL_FITS/ScCHIMERA_MODEL_noCO2.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
scchimera_noCO2 = pd.read_csv(ScCHIMERA_MODEL_noCO2,delimiter = ' ')
# print(scchimera_noCO2.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
scchimera_noCO2.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl =np.array(scchimera_noCO2.wl)           		  # Values of wavelength
depth= np.array(scchimera_noCO2.depth)            # Values of transit depth
plt.plot(wl,depth*100,label = "noCO2")
#-----------------------------------------------------------------------------------------------------------------
#-------------------------------------------ScCHIMERA_MODEL_noH2O-------------------------------------------------
#importing data 
ScCHIMERA_MODEL_noH2O = '/home/dev/Desktop/jwst_data/MODEL_FITS/ScCHIMERA_MODEL_noH2O.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
noH2O = pd.read_csv(ScCHIMERA_MODEL_noH2O,delimiter = ' ')
# print(noH2O.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
noH2O.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl =np.array(noH2O.wl)           		  # Values of wavelength
depth= np.array(noH2O.depth)              # Values of transit depth
plt.plot(wl,depth*100,label = "noH2O")
#-----------------------------------------------------------------------------------------------------------------
#-------------------------------------------ScCHIMERA_MODEL_noH2S-------------------------------------------------
#importing data 
ScCHIMERA_MODEL_noH2S = '/home/dev/Desktop/jwst_data/MODEL_FITS/ScCHIMERA_MODEL_noH2S.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
noH2S = pd.read_csv(ScCHIMERA_MODEL_noH2S,delimiter = ' ')
# print(noH2S.head())
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
noH2S.columns = ["wl","depth"]
#storing values for each column into a separate arrays
wl =np.array(noH2S.wl)           		  # Values of wavelength
depth= np.array(noH2S.depth)              # Values of transit depth
plt.plot(wl,depth*100,label = "noH2S")


plt.xlim(3.0,5.5)
plt.legend(loc = 'best')
plt.tight_layout()
fig.savefig('plot.png')
plt.legend()
plt.show()


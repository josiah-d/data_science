# Forecasting-HIV-Infections Case Study
- [Forecasting-HIV-Infections Case Study](#forecasting-hiv-infections-case-study)
  - [Case Study Goal](#case-study-goal)
  - [Background](#background)
  - [Data](#data)
    - [Data merging](#data-merging)
  - [Credit](#credit)
## Case Study Goal
1)	To accurately model HIV `incidences` (new infections per 100,000) in US
counties by building a linear regression model that utilizes HIV infection data, census data, data on the opioid crisis, and data on sexual orientation.

2)	Identify features that are the most significant drivers of HIV infection rates and learn how these drivers differ between different regions.

## Background
Due to the development of anti-retroviral therapies the HIV/AIDS epidemic is 
generally considered to be under control in the US.  However, as of 2015 there 
were 971,524 people living with diagnosed HIV in the US with an estimation of 
37,600 new HIV diagnoses in 2014.  HIV infection rates continue to be particularly
problematic in communities of color, among men who have sex with men (MSM), the
transgender community, and other vulnerable populations in the US. Socioeconomic 
factors are a significant risk factor for HIV infection and likely contribute 
to HIV infection risk in these communities.  The current US opioid crisis has 
further complicated the efforts to combat HIV with HIV infection outbreaks now 
hitting regions that weren’t previously thought to be vulnerable to such outbreaks.  

A model that can accurately forecast regional HIV infection rates would be 
beneficial to local public health officials.  Provided with this information, 
these officials will be able to better marshal the resources necessary to combat
HIV and prevent outbreaks from occurring.  Accurate modeling will also identify 
risk factors for communities with high HIV infection rates and provide clues 
as to how officials may better combat HIV in their respective communities.


## Data


The `./data` folder contains data from three publically available sources.  Groups should feel
free to supplement this data if they wish.
1. The largest collection of HIV and opioid data was obtained from the [opioid database](http://opioid.amfar.org/) maintained by the American Foundation for AIDS Research (amfAR).  
2. Demographic and economic data were obtained from the 5yr - American Community Survey which are available at the [US census bureau website](https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t).
3. Estimates for the [MSM population](http://emorycamp.org/item.php?i=48) in each county were obtained from the Emory Coalition for Applied Modeling for Prevention (CAMP).

Data dictionaries that indicate what each column in the data means are included in the folder associated with each data set.

## Data merging  

The `merge_data.ipynb` notebook reads and merges most of the data in the 
`data` folder into one dataframe.  Read through and execute this notebook cell-by-cell to
better understand the data and bring it together for EDA.


## Credit
This case study is based on [Eric Logue's capstone project](https://github.com/elogue01/Forecasting-HIV-Infections).  
You may wish to consult his Github repository devoted to this analysis for inspiration and insight.

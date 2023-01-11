import streamlit as st
#import pandas as pd
#import numpy as np

st.title('History of Computer!')
st.write("""History of Computer! 
_This is some really cool stuff._  
_One of the earliest and most well-known devices was an abacus. Then in 1822, the father of computers, 
Charles Babbage began developing what would be the first mechanical computer. 
And then in 1833 he actually designed an Analytical Engine which was a general-purpose computer.""")
st.image('surprise.gif')
st.markdown("""# About adding Headings
To add headers in your webpage, simply use the '#' character. Using multiple 
'#' will create smaller subheadings like this one 
### Small Sub Heading
#### More smaller sub-sub heading
##### Even more smaller sub-sub-sub heading
###### You got the point! :-D
#Adding Interactive Elements!
StreamLit allows to :green[easily] add checkboxes, sliders, progress bars etc.""")
st.markdown(":green[Hello!]")
chkRed = st.checkbox("Show in Red")
if chkRed:
	st.markdown(":red[Red highlight on.]")
else:
	st.write("Red highlight is off!")	

sliderValue = st.slider("TEST", min_value=0, max_value=10, value=4, step=2, on_change=None);
st.write("This is so easy. Slider is set at value ",sliderValue,".")

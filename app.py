import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid

st.set_page_config(layout='wide')

st.title('ACS Project for TA')

st.header('KOMAL TRISHNA BEHERA')
st.subheader('118EE0276')

def matrix_power(A, k):

    for column in A.columns:
        A[column] = A[column].astype(int)
    A = A.values
    
    return np.linalg.matrix_power(A, k)

st.write('\n\n\n\n')
st.write('Write the dimension n of an nxn square matrix')
n = st.number_input('n value :', min_value=1, value=1)

st.write('Give power k')
k = st.number_input('k value :', min_value=1, value=1)
if st.checkbox('Feed Input Matrix'):
    st.text('* Press tab to go to next input field')
    st.text('* Press Enter after the input')

    input_dataframe = pd.DataFrame(
        '',
        index=[i for i in range(n)],
        columns=['col-'+str(i+1) for i in range(n)]
    )

    resp = AgGrid(
            input_dataframe, 
        editable=True,
        sortable=False,
        filter=False,
        resizable=False,
        defaultWidth=5,
        fit_columns_on_grid_load=True,
        key='input_frame')
    
    st.write('Input Matrix')
    st.write(resp['data'].values)

    if st.button('Power of the matrix'):
        ans = matrix_power(resp['data'], k)
        
        st.write('Output Matrix', ans)

        

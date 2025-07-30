import streamlit as st
#--------------------------------------------SIDEBAR
st.sidebar.title('VENDAS DE PERFUMES')
st.sidebar.write('Seja bem vindo(a)')

perfumes = ['EGEO', 'FLORATTA', 'LILY', 'ELYSÉE']
perfume = st.sidebar.selectbox('Selecione um perfume', perfumes)

if perfume == 'EGEO':
    valor = 100

elif perfume == 'FLORATTA':
    valor = 130

elif perfume == 'LILY':
    valor = 160 

elif perfume == 'ELYSÉE':
    valor = 187          

  
#---------------------------------------------PRINCIPAL
st.title('VENDAS DE PERFUMES')
st.write('Seja bem vindo(a)')
st.image(f'{perfume}.png')
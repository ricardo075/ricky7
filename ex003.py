import streamlit as st
import math
# Função para calcular o Delta
def calcular_delta(a, b, c):
    delta = b ** 2 - 4 * a * c
    st.write(f'Passo 1: Calculando o Delta (Δ)')
    st.write(f'Δ = b² - 4ac')
    st.write(f'Δ = {b}² - 4* {a} * {c}')
    st.write(f'Δ = {b ** 2} - {4 * a * c}')
    st.write(f'Δ = {delta}')
    return delta


# Função para calcular x1 e x2
def calcular_x1_x2(a, b, delta):
    if delta >= 0:
        x3 = (math.sqrt(delta))
        x5 = (-b + x3)
        x4 = (-b - x3)
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        st.write('Passo 2: Calculando x1 e x2')
        st.write('x1 = (-b - √Δ) / 2a')
        st.write(f'x1 = (-{b} - √{delta}) / {2 * a}')
        st.write(f'x1 = (-{b} - {x3}) / {2 * a}')
        st.write(f'x1 = {x4}  / {2 * a}')
        st.write(f'x1 = {x1}')
        st.write('CALCULANDO X2')
        st.write('x2 = (-b + √Δ) / 2a')
        st.write(f'x2 = (-{b} + √{delta}) / {2 * a}')
        st.write(f'x2 = (-{b} + {x3}) / {2 * a}')
        st.write(f'x1 = {x5}  / {2 * a}')
        st.write(f'x2 = {x2}')
        st.write('MUITO OBRIGADO POR ESCOLHER ESTE METODO, SE TIVER ALGO DE ERRADO CONTACTE 868787572')
        st.write('DUVIDAS E RECLAMAÇOES POR FAVOR CONTACTEM 841038887 OU 868787572')
    else:
        st.write('Não é possível calcular x1 e x2 para Δ < 0')


# Criando o site com Streamlit
st.title('Calculadora de Delta, x1 e x2')

a = st.number_input('Digite o valor de a:')
b = st.number_input('Digite o valor de b:')
c = st.number_input('Digite o valor de c:')

if st.button('Calcular'):
    st.write('Valores inseridos:')
    st.write(f'a = {a}, b = {b}, c = {c}')
    delta = calcular_delta(a, b, c)
    calcular_x1_x2(a, b, delta)
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Simulering av Gauss-Markov prosess")

st.sidebar.header("Simuleringsparametere")
T = st.sidebar.slider("Tidskonstant T (s)", min_value=0.000001, max_value=1000.0, value=10.0, step=0.1)
dt = st.sidebar.number_input("Tidssteg Δt (s)", value=0.01, step=0.001, format="%.3f")
t_final = st.sidebar.number_input("Sluttid t_final (s)", value=100.0, step=1.0)
q = st.sidebar.number_input("Diskret støyvarianse q", value=1.0, step=0.1)
x0_mean = st.sidebar.number_input("Initial mean x̄0", value=10.0, step=0.5)
x0_var = st.sidebar.number_input("Initial variance p0", value=2.0, step=0.1)

# Beregn antall tidsskritt og overgangsparameteren phi
num_steps = int(t_final / dt) + 1
phi = np.exp(-dt / T)

# Initialiser prosessen
x = np.zeros(num_steps)
x[0] = np.random.normal(x0_mean, np.sqrt(x0_var))
time = np.linspace(0, t_final, num_steps)

# Simuler den diskretiserte Gauss-Markov prosessen
for k in range(1, num_steps):
    v_k = np.random.normal(0, np.sqrt(q))
    x[k] = phi * x[k - 1] + v_k

# Plot med plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=time, y=x, mode='lines', name='Gauss-Markov prosess'))
fig.update_layout(
    title='Simulering av diskret Gauss-Markov prosess',
    xaxis_title='Tid (s)',
    yaxis_title='x',
    template='plotly_white',
    height=400
)
st.plotly_chart(fig, use_container_width=True)

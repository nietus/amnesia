import matplotlib.pyplot as plt
import numpy as np

# Dados: (espacial, random, temporal) para cada configuração de cache
tempos_totais = [(164, 374, 394), (134, 197, 203), (168, 252, 260)]
configs = ['L1', 'L1 + L2', 'L1 + L2 + L3']
traces = ['Espacial', 'Random', 'Temporal']
trace_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # azul, laranja, verde

# Transpor os dados para facilitar plotagem por trace
tempos_por_trace = list(zip(*tempos_totais))  # [[L1, L1+L2, L1+L2+L3], ...]

x = np.arange(len(configs))  # posições no eixo X
width = 0.25  # largura das barras

plt.figure(figsize=(10, 6))

# Plotar cada conjunto de barras para cada trace
for i, (trace_label, trace_data, color) in enumerate(zip(traces, tempos_por_trace, trace_colors)):
    plt.bar(x + i * width, trace_data, width=width, label=trace_label, color=color)

plt.xticks(x + width, configs)
plt.ylabel('Tempo Total')
plt.title('Tempo Total por Configuração de Cache em Diferentes Traces', fontsize=12, weight='bold')
plt.legend(title='Tipo de Trace')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

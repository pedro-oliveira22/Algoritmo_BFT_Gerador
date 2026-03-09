# BFT-Selector: Otimização e Seleção de Microgeração Hidrelétrica

> **Algoritmo para seleção integrada e otimizada de Bombas Funcionando como Turbinas (BFT) e Geradores de Indução.**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![UNIFEI](https://img.shields.io/badge/Instituição-UNIFEI-red)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Visão Geral

Este software foi desenvolvido como Trabalho de Conclusão de Curso (TCC) em Engenharia Elétrica na **UNIFEI - Campus Itabira**. O objetivo é mitigar as barreiras financeiras da microgeração hidrelétrica, onde o custo de turbinas convencionais ($Pelton, Francis, Kaplan$) muitas vezes inviabiliza projetos de pequeno porte.

O **BFT-Selector** automatiza a engenharia de aplicação de **Bombas Centrífugas operando em modo reverso**, uma solução que pode ser até 2,2 vezes mais barata que sistemas convencionais.

## 🚀 Diferenciais Técnicos

O algoritmo não apenas seleciona o equipamento, mas garante a **Confiabilidade Operacional** através de:

* **Otimização do BEP (Best Efficiency Point):** Identifica o ponto de máxima eficiência exato através da derivada nula da curva de rendimento, minimizando perdas e estresse mecânico.
* **Big Data de Ativos:** Banco de dados **SQLite** integrado com 22.847 configurações de motores **WEG** e curvas polinomiais de 5º grau para 78 modelos de bombas nacionais.
* **Transposição de Curvas:** Implementação rigorosa das correlações de **Viana (1987)** e **Sharma (1985)** para predição precisa de performance Turbina vs. Bomba.
* **Integração MATLAB/Simulink:** Função de exportação de scripts (`.m`) para validação dinâmica e análise de regime transitório.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x.
* **Interface Gráfica (GUI):** Tkinter.
* **Banco de Dados:** SQLite3.
* **Processamento Numérico:** NumPy para modelagem polinomial e álgebra linear.

## 📊 Validação e Resultados

O sistema foi validado através de estudos de caso, comparando o dimensionamento automatizado com métodos analíticos de **Chapallaz (1990)** e **Viana (1987)**.
* **Convergência:** Alta precisão entre os cálculos do algoritmo e a resposta dinâmica do Simulink.
* **Eficiência:** Identificação de ganhos globais de geração ao operar no ponto ótimo otimizado.

## 🔧 Como Executar

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/pedro-oliveira22/Algoritmo_BFT_Gerador.git](https://github.com/pedro-oliveira22/Algoritmo_BFT_Gerador.git)
    ```
2.  Certifique-se de que os bancos de dados `pump_data.db` e `generators.db` estejam na raiz do projeto.
3.  Execute o script principal:
    ```bash
    python BFT_Gerador.py
    ```

## 🎓 Créditos e Referências

**Autor:** Pedro Henrique Barbosa Oliveira.
**Orientadora:** Profa. Dra. Danielle Silva Gontijo.

Metodologias aplicadas:
* VIANA, A. N. C. (UNIFEI, 1987).
* SHARMA, K. R. (1985).
* CHAPALLAZ, J. M. (1990).

---
*Este projeto foi apresentado em 04 de dezembro de 2025 como requisito para obtenção do título de Bacharel em Engenharia Elétrica.*

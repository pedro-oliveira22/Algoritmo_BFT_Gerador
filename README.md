# BFT-Selector: Otimização e Seleção de Microgeração Hidrelétrica

> **Algoritmo para seleção integrada e otimizada de Bombas Funcionando como Turbinas (BFT) e Geradores de Indução.**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![UNIFEI](https://img.shields.io/badge/Instituição-UNIFEI-red)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Visão Geral

[cite_start]Este software foi desenvolvido como Trabalho de Conclusão de Curso (TCC) em Engenharia Elétrica na **UNIFEI - Campus Itabira**[cite: 8, 9, 13]. [cite_start]O objetivo é mitigar as barreiras financeiras da microgeração hidrelétrica, onde o custo de turbinas convencionais ($Pelton, Francis, Kaplan$) muitas vezes inviabiliza projetos de pequeno porte[cite: 30, 150].

[cite_start]O **BFT-Selector** automatiza a engenharia de aplicação de **Bombas Centrífugas operando em modo reverso**, uma solução que pode ser até 2,2 vezes mais barata que sistemas convencionais[cite: 31, 358].

## 🚀 Diferenciais Técnicos

O algoritmo não apenas seleciona o equipamento, mas garante a **Confiabilidade Operacional** através de:

* [cite_start]**Otimização do BEP (Best Efficiency Point):** Identifica o ponto de máxima eficiência exato através da derivada nula da curva de rendimento, minimizando perdas e estresse mecânico[cite: 35, 543, 604, 605].
* [cite_start]**Big Data de Ativos:** Banco de dados **SQLite** integrado com 22.847 configurações de motores **WEG** e curvas polinomiais de 5º grau para 78 modelos de bombas nacionais[cite: 629, 630, 639, 642].
* [cite_start]**Transposição de Curvas:** Implementação rigorosa das correlações de **Viana (1987)** e **Sharma (1985)** para predição precisa de performance Turbina vs. Bomba[cite: 215, 361, 551, 609].
* [cite_start]**Integração MATLAB/Simulink:** Função de exportação de scripts (`.m`) para validação dinâmica e análise de regime transitório[cite: 615, 684, 685].

## 🛠️ Tecnologias Utilizadas

* [cite_start]**Linguagem:** Python 3.x[cite: 33, 44].
* [cite_start]**Interface Gráfica (GUI):** Tkinter[cite: 669].
* [cite_start]**Banco de Dados:** SQLite3[cite: 630, 644].
* **Processamento Numérico:** NumPy para modelagem polinomial e álgebra linear.

## 📊 Validação e Resultados

[cite_start]O sistema foi validado através de estudos de caso, comparando o dimensionamento automatizado com métodos analíticos de **Chapallaz (1990)** e **Viana (1987)**[cite: 36, 1192, 1194].
* [cite_start]**Convergência:** Alta precisão entre os cálculos do algoritmo e a resposta dinâmica do Simulink[cite: 1208, 1220].
* [cite_start]**Eficiência:** Identificação de ganhos globais de geração ao operar no ponto ótimo otimizado[cite: 37, 1219].

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

[cite_start]**Autor:** Pedro Henrique Barbosa Oliveira[cite: 1, 6].
**Orientadora:** Profa. Dra. [cite_start]Danielle Silva Gontijo[cite: 12, 17].

Metodologias aplicadas:
* [cite_start]VIANA, A. N. C. (UNIFEI, 1987)[cite: 1253].
* [cite_start]SHARMA, K. R. (1985)[cite: 1249].
* [cite_start]CHAPALLAZ, J. M. (1990)[cite: 1237].

---
[cite_start]*Este projeto foi apresentado em 04 de dezembro de 2025 como requisito para obtenção do título de Bacharel em Engenharia Elétrica.* [cite: 5, 14]

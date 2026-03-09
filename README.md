# BFT-Selector: Algoritmo de Seleção para BFTs e Geradores de Indução

> **Ferramenta computacional para seleção automatizada e otimizada de Bombas Funcionando como Turbinas (BFT) em Microcentrais Hidrelétricas.**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Sobre o Projeto

Este software foi desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) em Engenharia Elétrica na **Universidade Federal de Itajubá (UNIFEI)**.

O objetivo da ferramenta é mitigar as barreiras técnicas da microgeração hidrelétrica, automatizando o complexo processo de seleção de equipamentos. O algoritmo cruza dados hidráulicos de entrada com um banco de dados real de bombas comerciais e geradores de indução, aplicando métodos consagrados (Viana, Sharma, Chapallaz) para identificar o conjunto mais eficiente e economicamente viável.

## 🚀 Funcionalidades Principais

* **Seleção Automatizada:** Escolha de bombas comerciais (BFT) e geradores de indução (WEG) baseada em Altura ($H$) e Vazão ($Q$).
* **Otimização do BEP:** Algoritmo numérico que identifica o Ponto de Melhor Eficiência real da máquina, garantindo operação no ponto de derivada nula da curva de rendimento.
* **Banco de Dados Real:** Integração via SQLite com curvas características de 78 bombas nacionais e mais de 22.000 configurações de motores WEG.
* **Métodos Teóricos:** Implementação dos métodos de **Viana (1987)** para pré-seleção e **Sharma (1985)** para transposição de curvas (Bomba → Turbina).
* **Exportação de Dados:** Geração automática de relatórios em `.txt`, `.csv` e scripts prontos para simulação dinâmica no **MATLAB/Simulink**.
* **Interface Gráfica (GUI):** Interface intuitiva e amigável desenvolvida com Tkinter.

## 📸 Interface

![Interface do Software](interface_print.png)
*(Substitua "interface_print.png" pelo nome do arquivo da sua imagem na pasta do projeto)*

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface:** Tkinter
* **Banco de Dados:** SQLite3
* **Cálculo Numérico:** Pandas, NumPy, SciPy

## 🔧 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/pedro-oliveira22/Algoritmo_BFT_Gerador.git](https://github.com/pedro-oliveira22/Algoritmo_BFT_Gerador.git)

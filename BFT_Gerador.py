#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Seleção BFT + Gerador - BEP
Foco: Encontrar e utilizar o Ponto de Máxima Eficiência (BEP) exato da bomba.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import numpy as np
import ast
import os
import csv
from datetime import datetime

# ==================== CONSTANTES ====================

VIANA_DATA = np.array([
(30,0.88,0.81),(31,0.877,0.811),(32,0.874,0.812),(33,0.871,0.813),
(34,0.868,0.814),(35,0.865,0.815),(36,0.862,0.816),(37,0.859,0.817),
(38,0.856,0.818),(39,0.853,0.819),(40,0.85,0.82),(41,0.841,0.82),
(42,0.832,0.82),(43,0.823,0.82),(44,0.814,0.82),(45,0.805,0.82),
(46,0.796,0.82),(47,0.787,0.82),(48,0.778,0.82),(49,0.769,0.82),
(50,0.76,0.82),(51,0.751,0.82),(52,0.742,0.82),(53,0.733,0.82),
(54,0.724,0.82),(55,0.715,0.82),(56,0.706,0.82),(57,0.697,0.82),
(58,0.688,0.82),(59,0.679,0.82),(60,0.67,0.82),(61,0.665,0.82),
(62,0.66,0.82),(63,0.655,0.82),(64,0.65,0.82),(65,0.645,0.82),
(66,0.64,0.82),(67,0.635,0.82),(68,0.63,0.82),(69,0.625,0.82),
(70,0.62,0.82),(71,0.615,0.82),(72,0.61,0.82),(73,0.605,0.82),
(74,0.6,0.82),(75,0.6,0.82),(76,0.6,0.82),(77,0.6,0.82),
(78,0.6,0.82),(79,0.6,0.82),(80,0.6,0.82),(81,0.595,0.819),
(82,0.59,0.818),(83,0.585,0.817),(84,0.58,0.816),(85,0.575,0.815),
(86,0.57,0.814),(87,0.565,0.813),(88,0.56,0.812),(89,0.555,0.811),
(90,0.55,0.81),(91,0.545,0.808),(92,0.54,0.806),(93,0.535,0.804),
(94,0.53,0.802),(95,0.53,0.8),(96,0.53,0.798),(97,0.53,0.796),
(98,0.53,0.794),(99,0.53,0.792),(100,0.53,0.79),(101,0.529,0.789),
(102,0.528,0.788),(103,0.527,0.787),(104,0.526,0.786),(105,0.525,0.785),
(106,0.524,0.784),(107,0.523,0.783),(108,0.522,0.782),(109,0.521,0.781),
(110,0.52,0.78),(111,0.52,0.78),(112,0.52,0.78),(113,0.52,0.78),
(114,0.52,0.78),(115,0.52,0.78),(116,0.52,0.78),(117,0.52,0.78),
(118,0.52,0.78),(119,0.52,0.78),(120,0.52,0.78),(121,0.528,0.776),
(122,0.536,0.772),(123,0.544,0.768),(124,0.552,0.764),(125,0.56,0.76),
(126,0.568,0.756),(127,0.576,0.752),(128,0.584,0.748),(129,0.592,0.744),
(130,0.6,0.74),(131,0.596,0.736),(132,0.592,0.732),(133,0.588,0.728),
(134,0.584,0.724),(135,0.58,0.72),(136,0.576,0.716),(137,0.572,0.712),
(138,0.568,0.708),(139,0.564,0.704),(140,0.56,0.7),(141,0.566,0.694),
(142,0.572,0.688),(143,0.578,0.682),(144,0.584,0.676),(145,0.59,0.67),
(146,0.596,0.664),(147,0.602,0.658),(148,0.608,0.652),(149,0.614,0.646),
(150,0.62,0.64),(151,0.626,0.635),(152,0.632,0.63),(153,0.638,0.625),
(154,0.644,0.62),(155,0.65,0.615),(156,0.656,0.61),(157,0.662,0.605),
(158,0.668,0.6),(159,0.674,0.595),(160,0.68,0.59),(161,0.686,0.583),
(162,0.692,0.576),(163,0.698,0.569),(164,0.704,0.562),(165,0.71,0.555),
(166,0.716,0.548),(167,0.722,0.541),(168,0.728,0.534),(169,0.734,0.527),
(170,0.74,0.52),(171,0.746,0.513),(172,0.752,0.506),(173,0.758,0.499),
(174,0.764,0.492),(175,0.77,0.485),(176,0.776,0.478),(177,0.782,0.471),
(178,0.788,0.464),(179,0.794,0.457),(180,0.8,0.45),(181,0.795,0.467),
(182,0.79,0.484),(183,0.785,0.501),(184,0.78,0.518),(185,0.775,0.535),
(186,0.77,0.552),(187,0.765,0.569),(188,0.76,0.586),(189,0.755,0.603),
(190,0.75,0.62),(191,0.758,0.611),(192,0.766,0.602),(193,0.774,0.593),
(194,0.782,0.584),(195,0.79,0.575),(196,0.798,0.566),(197,0.806,0.557),
(198,0.814,0.548),(199,0.822,0.539),(200,0.83,0.53)
])

CHAPALLAZ = {
     1:0.965,2:0.9782,3:0.99,4:1.0005,5:1.01,6:1.019,7:1.0276,8:1.0358,9:1.0433,10:1.05,
    11:1.0559,12:1.0614,13:1.0665,14:1.071,15:1.075,16:1.0785,17:1.0815,18:1.0844,19:1.0871,20:1.09,
    21:1.0931,22:1.0963,23:1.0994,24:1.1024,25:1.105,26:1.1073,27:1.1093,28:1.1112,29:1.1131,30:1.115,
    31:1.117,32:1.119,33:1.121,34:1.123,35:1.125
}

# ==================== FUNÇÕES AUXILIARES ====================

def interp_viana(nqa):
    """Interpola coeficientes CH e CQ"""
    ch = np.interp(nqa, VIANA_DATA[:,0], VIANA_DATA[:,1])
    cq = np.interp(nqa, VIANA_DATA[:,0], VIANA_DATA[:,2])
    return float(ch), float(cq)

def chapallaz_ratio(Pet_kw):
    """Retorna razão Chapallaz"""
    k = max(1, min(int(round(Pet_kw)), 35))
    return CHAPALLAZ.get(k, 1.125)

def safe_eval_list(s):
    """Converte string para lista"""
    if isinstance(s, (list, tuple)):
        return list(s)
    if s is None:
        return []
    try:
        return list(ast.literal_eval(str(s)))
    except:
        return []

def eval_poly(coef, x):
    """Avalia polinômio"""
    if not coef:
        return None
    return float(np.polyval(coef, x))

def normalize_eta(eta):
    """Normaliza eficiência [0,1]"""
    if eta is None or np.isnan(eta):
        return 0.0
    eta = float(eta)
    if eta > 1.5:
        eta /= 100.0
    return min(eta, 0.95)

def sharma_transform(Q, H, eta):
    """Sharma: bomba → turbina"""
    eta = eta / 100.0 if eta > 1 else eta
    return Q / (eta ** 0.8), H / (eta ** 1.2)

def find_optimal_flow(coef_eff, qmin, qmax, eta_max_ref):
    """
    Encontra vazão ótima (Qbep) onde η é máxima.
    """
    if not coef_eff or len(coef_eff) < 2:
        return None
    
    try:
        deriv = np.polyder(coef_eff)
        roots = np.roots(deriv)
        real_roots = [r.real for r in roots if np.isreal(r) and qmin <= r.real <= qmax]
        candidates = real_roots + [qmin, qmax]
        
        best_Q = None
        max_eff_found = -1
        
        for Q in candidates:
            eta = eval_poly(coef_eff, Q)
            if eta and eta > max_eff_found:
                max_eff_found = eta
                best_Q = Q
        
        if best_Q and max_eff_found > 0:
            return float(best_Q)
    except:
        pass
    
    return None

# ==================== INTERFACE ====================

class BFTApp:
    def __init__(self, root):
        self.root = root
        root.title("Algoritmo BFT + Gerador")
        root.geometry("1280x800")
        root.configure(bg='#ecf0f1')
        
        # Estilo
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Header.TLabel', font=('Segoe UI', 18, 'bold'), 
                       foreground='#2c3e50', background='#ecf0f1')
        style.configure('Subtitle.TLabel', font=('Segoe UI', 9), 
                       foreground='#7f8c8d', background='#ecf0f1')
        style.configure('Card.TFrame', background='white', relief='flat')
        style.configure('Action.TButton', font=('Segoe UI', 10), padding=8)
        
        # Container principal
        main_frame = ttk.Frame(root, padding=20, style='Card.TFrame')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === CABEÇALHO ===
        header_frame = tk.Frame(main_frame, bg='#3498db', height=80)
        header_frame.pack(fill='x', pady=(0,20))
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text="⚡ Sistema BFT + Gerador", 
                font=('Segoe UI', 16, 'bold'), fg='white', bg='#3498db').pack(pady=(10,5))
        tk.Label(header_frame, text="TCC  •  Pedro Oliveira", 
                font=('Segoe UI', 9), fg='#ecf0f1', bg='#3498db').pack()
        
        # === PAINEL PRINCIPAL ===
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill='both', expand=True)
        
        # === COLUNA ESQUERDA ===
        left_frame = tk.Frame(content_frame, width=380, bg='white')
        left_frame.pack(side='left', fill='y', padx=(0,15))
        left_frame.pack_propagate(False)
        
        # Card Entrada
        input_card = tk.Frame(left_frame, bg='#3498db', padx=2, pady=2)
        input_card.pack(fill='x', pady=(0,15))
        
        input_inner = tk.Frame(input_card, bg='white', padx=15, pady=15)
        input_inner.pack(fill='both', expand=True)
        
        tk.Label(input_inner, text="📊 Parâmetros de Entrada", 
                font=('Segoe UI', 11, 'bold'), fg='#2c3e50', bg='white').pack(anchor='w', pady=(0,10))
        
        self.entries = {}
        for label, var_name, unit, default in [
            ("Altura", "Ht", "m", ""),
            ("Vazão", "Qt", "m³/h", ""),
            ("Rotação", "rpm", "rpm", "3600")
        ]:
            row = tk.Frame(input_inner, bg='white')
            row.pack(fill='x', pady=6)
            
            tk.Label(row, text=f"{label}:", font=('Segoe UI', 10), 
                    fg='#34495e', bg='white', width=8, anchor='w').pack(side='left')
            
            entry = tk.Entry(row, font=('Segoe UI', 11), width=12, relief='solid', bd=1)
            entry.insert(0, default)
            entry.pack(side='left', padx=8)
            
            tk.Label(row, text=unit, font=('Segoe UI', 9), 
                    fg='#95a5a6', bg='white').pack(side='left')
            
            self.entries[var_name] = entry
        
        # Card Ações
        action_card = tk.Frame(left_frame, bg='#27ae60', padx=2, pady=2)
        action_card.pack(fill='x', pady=(0,15))
        
        action_inner = tk.Frame(action_card, bg='white', padx=15, pady=15)
        action_inner.pack(fill='both', expand=True)
        
        tk.Label(action_inner, text="🎯 Ações", 
                font=('Segoe UI', 11, 'bold'), fg='#2c3e50', bg='white').pack(anchor='w', pady=(0,10))
        
        tk.Button(action_inner, text="▶  Calcular Seleção", 
                 command=self.calculate_selection,
                 font=('Segoe UI', 10, 'bold'), bg='#3498db', fg='white',
                 relief='flat', cursor='hand2', padx=20, pady=8).pack(fill='x', pady=5)
        
        tk.Button(action_inner, text="⚡ Calcular BFT no BEP", 
                 command=self.calculate_nominal,
                 font=('Segoe UI', 10, 'bold'), bg='#e74c3c', fg='white',
                 relief='flat', cursor='hand2', padx=20, pady=8).pack(fill='x', pady=5)
        
        tk.Frame(action_inner, height=1, bg='#bdc3c7').pack(fill='x', pady=12)
        
        # Exportação
        export_frame = tk.Frame(action_inner, bg='white')
        export_frame.pack(fill='x')
        
        tk.Button(export_frame, text="📊 CSV", command=self.export_csv,
                 font=('Segoe UI', 9), bg='#16a085', fg='white',
                 relief='flat', cursor='hand2', width=10).grid(row=0, column=0, padx=2, pady=2)
        
        tk.Button(export_frame, text="📄 TXT", command=self.export_txt,
                 font=('Segoe UI', 9), bg='#2980b9', fg='white',
                 relief='flat', cursor='hand2', width=10).grid(row=0, column=1, padx=2, pady=2)
        
        tk.Button(export_frame, text="📜 Script MATLAB", command=self.export_matlab,
                 font=('Segoe UI', 9), bg='#8e44ad', fg='white',
                 relief='flat', cursor='hand2').grid(row=1, column=0, columnspan=2, pady=2, sticky='ew')
        
        # Card Info
        info_card = tk.Frame(left_frame, bg='#f39c12', padx=2, pady=2)
        info_card.pack(fill='both', expand=True)
        
        info_inner = tk.Frame(info_card, bg='#fff9e6', padx=12, pady=12)
        info_inner.pack(fill='both', expand=True)
        
        tk.Label(info_inner, text="Sobre o Sistema", 
                font=('Segoe UI', 10, 'bold'), fg='#2c3e50', bg='#fff9e6').pack(anchor='w', pady=(0,8))
        
        tutorial_text = """COMO USAR:

1. Insira Altura, Vazão e RPM.
2. Clique em 'Calcular Seleção'.
3. Use 'Calcular BFT no BEP' para otimizar.
4. Confira os resultados ao lado.
5. Exporte os dados (CSV/MATLAB)."""
        
        tk.Label(info_inner, text=tutorial_text, justify='left', 
                font=('Courier New', 8), fg='#34495e', bg='#fff9e6').pack(anchor='w')
        
        # === COLUNA DIREITA ===
        right_frame = ttk.Frame(content_frame)
        right_frame.pack(side='right', fill='both', expand=True)
        
        result_card = tk.Frame(right_frame, bg='#2ecc71', padx=2, pady=2)
        result_card.pack(fill='both', expand=True)
        
        result_inner = tk.Frame(result_card, bg='white', padx=10, pady=10)
        result_inner.pack(fill='both', expand=True)
        
        tk.Label(result_inner, text="📈 Resultados da Análise", 
                font=('Segoe UI', 11, 'bold'), fg='#2c3e50', bg='white').pack(anchor='w', pady=(0,8))
        
        text_frame = tk.Frame(result_inner, bg='white')
        text_frame.pack(fill='both', expand=True)
        
        scroll = tk.Scrollbar(text_frame)
        scroll.pack(side='right', fill='y')
        
        self.output = tk.Text(text_frame, font=('Consolas', 9), wrap='none',
                             yscrollcommand=scroll.set, bg='#2c3e50', fg='#ecf0f1',
                             insertbackground='white', selectbackground='#3498db')
        self.output.pack(side='left', fill='both', expand=True)
        scroll.config(command=self.output.yview)
        
        # === RODAPÉ ===
        footer_frame = tk.Frame(main_frame, bg='white', height=40)
        footer_frame.pack(fill='x', pady=(15,0))
        footer_frame.pack_propagate(False)
        
        self.status = tk.Label(footer_frame, text="✓ Sistema pronto", 
                              font=('Segoe UI', 10, 'bold'), fg='#27ae60', bg='white')
        self.status.pack(pady=10)
        
        # Dados
        self.selection = None
        self.optimized = None
        self.current_pump = None
    
    def log(self, text):
        self.output.insert(tk.END, text)
        self.output.see(tk.END)
        self.root.update()
    
    def calculate_selection(self):
        """Calcula seleção: Reduz p/ busca (3500), Amplia p/ resultado e potência (3600)"""
        self.output.delete('1.0', tk.END)
        self.status.config(text="⏳ Calculando...", fg='#f39c12')
        self.root.update()
        
        try:
            Ht = float(self.entries['Ht'].get())
            Qt = float(self.entries['Qt'].get())
            rpm_user = float(self.entries['rpm'].get())
            
            if Ht <= 0 or Qt <= 0 or rpm_user <= 0:
                raise ValueError()
        except:
            messagebox.showerror("Erro", "Valores inválidos!")
            self.status.config(text="❌ Erro", fg='#e74c3c')
            return
        
        # Viana (Turbina -> Bomba @ rpm_user)
        g = 9.81
        Qt_m3s = Qt / 3600
        n_rps = rpm_user / 60
        nqa = n_rps * 1000 * np.sqrt(Qt_m3s) / ((g * Ht) ** 0.75)
        
        if not (30 <= nqa <= 200):
            rpm_sug = rpm_user * (50/nqa if nqa < 30 else 150/nqa)
            messagebox.showerror("nqa Inválido", 
                f"nqa={nqa:.2f} fora de [30,200]\n\nSugestão: rpm={rpm_sug:.0f}")
            self.status.config(text="❌ nqa inválido", fg='#e74c3c')
            return
        
        CH, CQ = interp_viana(nqa)
        Hb_viana = Ht * CH
        Qb_viana = Qt * CQ
        
        self.log(f"""
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                        RELATÓRIO DE SELEÇÃO BFT + GERADOR                            ║
╚══════════════════════════════════════════════════════════════════════════════════════╝

┌─ DADOS DE ENTRADA (TURBINA) ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  Altura Turbina:        {Ht:8.2f} m                                                  
│  Vazão Turbina:         {Qt:8.2f} m³/h  ({Qt_m3s:.4f} m³/s)                          
│  Rotação Operação:      {rpm_user:8.0f} rpm                                         
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

┌─ CONVERSÃO VIANA (Turbina → Bomba) ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  nqa:                   {nqa:8.4f} ✓                                                 
│  Coeficientes:          CH = {CH:.4f}  |  CQ = {CQ:.4f}                              
│  Altura Bomba (Viana):  {Hb_viana:8.2f} m                                            
│  Vazão Bomba (Viana):   {Qb_viana:8.2f} m³/h                                         
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

""")
        
        # Busca bomba no DB
        try:
            conn = sqlite3.connect("pump_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM pump_models")
            pumps = [dict(zip([d[0] for d in cur.description], row)) for row in cur.fetchall()]
            conn.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro DB: {e}")
            self.status.config(text="❌ Erro DB", fg='#e74c3c')
            return
        
        # Filtra candidatos
        candidates = []
        for p in pumps:
            try:
                # Dados do catálogo (3500 rpm)
                qmin = float(p.get('vazao_min', 0))
                qmax = float(p.get('vazao_max', 9999))
                rpm_catalog = float(p.get('rpm', 3500)) 
                
                coef_h = safe_eval_list(p.get('coef_head'))
                coef_e = safe_eval_list(p.get('coef_eff'))
                if not coef_h or not coef_e:
                    continue

                # AJUSTE PARA BUSCA (DESCER PARA ROTAÇÃO DE CATÁLOGO)
                # Reduzir de 3600 rpm → 3500 rpm: usar razão 3500/3600
                ratio_down = rpm_catalog / rpm_user  # 3500/3600 = 0.9722
                
                Q_search = Qb_viana * ratio_down       # Q reduz linearmente
                H_search = Hb_viana * (ratio_down ** 2)  # H reduz ao quadrado
                
                # Verificações na curva do catálogo (3500)
                if not (qmin <= Q_search <= qmax):
                    continue
                
                H_pump_at_catalog = eval_poly(coef_h, Q_search)
                if not H_pump_at_catalog or H_pump_at_catalog <= 0:
                    continue
                
                dev_H = abs(H_pump_at_catalog - H_search) / H_search
                if dev_H > 0.30:
                    continue
                
                # PROJEÇÃO PARA RESULTADO (SUBIR PARA ROTAÇÃO DE OPERAÇÃO)
                # Aumentar de 3500 rpm → 3600 rpm: usar razão 3600/3500
                ratio_up = rpm_user / rpm_catalog  # 3600/3500 = 1.0286
                
                # Ponto de operação real @ 3600 rpm
                H_real_user = H_pump_at_catalog * (ratio_up ** 2)  # H aumenta ao quadrado
                Q_real_user = Q_search * ratio_up  # Q aumenta linearmente
                
                # BEP no Catálogo (3500)
                eff_bop_catalog = float(p['eff_bop'])
                Qbep_cat = find_optimal_flow(coef_e, qmin, qmax, eff_bop_catalog)
                if not Qbep_cat:
                    Qbep_cat = float(p['eff_bop_flow'])

                # Eficiência na vazão reduzida
                eta_atual = normalize_eta(eval_poly(coef_e, Q_search))
                eta_bep = normalize_eta(eval_poly(coef_e, Qbep_cat))

                # Distância do BEP em 3500 rpm (sem converter para 3600)
                dist_bep = abs(Q_search - Qbep_cat) / Qbep_cat

                # Score da bomba no catálogo
                score = (eta_atual / (1 + dist_bep)) * (1 / (1 + dev_H))

                candidates.append({
                    'pump': p,
                    'score': score,
                    'H_at_Qob': H_pump_at_catalog,
                    'H_ob': H_real_user,
                    'Q_ob': Q_real_user,
                    'eta_bep': eta_bep,
                    'eta_atual': eta_atual,
                    'Qbep': Qbep_cat,
                    'dev_H': dev_H,
                    'rpm_catalog': rpm_catalog,
                    'coef_head': coef_h,
                    'coef_eff': coef_e,
                    'Q_search': Q_search,
                    'H_search': H_search
                })

            except:
                continue

        
        if not candidates:
            self.log("❌ Nenhuma bomba compatível encontrada.\n")
            self.status.config(text="❌ Sem bomba", fg='#e74c3c')
            return
        
        best = max(candidates, key=lambda x: x['score'])
        p = best['pump']
        
        self.log(f"""┌─ LEIS DA SEMELHANÇA  ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  Rotação Operação:      {rpm_user:8.0f} rpm                                          
│  Rotação Catálogo:      {best['rpm_catalog']:8.0f} rpm                               
│  Razão (n_ob/n_b):      {rpm_user/best['rpm_catalog']:8.4f}                          
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

┌─ BOMBA SELECIONADA ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  Fabricante:            {p.get('marca', 'N/A'):20s}                                  
│  Modelo:                {p.get('modelo', 'N/A'):20s}  Diâmetro: {p.get('diametro', 'N/A')}mm   
│                                                                                      
│  PONTO DE OPERAÇÃO @ {rpm_catalog:.0f} rpm:                                                                                     
│  • Vazão BFB:         {best['Q_search']:8.2f} m³/h         
   • Altura BFB:         {best['H_search']:8.2f} m                          
│  • Rendimento Bomba:    {best['eta_atual']*100:8.2f} %  ⭐                           
│                                                                                      
│  PONTO BEP @ {rpm_catalog:.0f} rpm:                                                     
│  • Qbep Ótimo:          {best['Qbep']:8.2f} m³/h                                    
│  • η no BEP:            {best['eta_bep']*100:8.2f} %                                
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

""")
        
        # CÁLCULO DE POTÊNCIA SEMPRE A 3600 RPM
        eta_Qob = best['eta_atual']
        P_hid = (1000 * g * Qt_m3s * Ht) / 1000
        Pet = P_hid * eta_Qob
        
        self.log(f"""┌─ POTÊNCIAS (@ {rpm_user:.0f} rpm) ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  Potência Hidráulica:   {P_hid:8.3f} kW                                              
│  Potência no Eixo:      {Pet:8.3f} kW                                                
│  Rendimento BFT:        {eta_Qob*100:8.2f} %                                         
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")
        
        # Gerador
        try:
            conn = sqlite3.connect("generators.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM generators ORDER BY P_kW ASC")
            gens = [dict(zip([d[0] for d in cur.description], row)) for row in cur.fetchall()]
            conn.close()
        except:
            gens = []
        
        ratio = chapallaz_ratio(Pet)
        P_req = Pet / ratio
        
        gen = next((g for g in gens if float(g.get('P_kW', 0)) * 0.7457 >= P_req), gens[-1] if gens else None)
        
        if gen:
            P_HP = float(gen['P_kW'])
            P_kW = P_HP * 0.7457
            eta_gen = normalize_eta(gen.get('eficiencia', 85))
            P_el = P_req * eta_gen
            eta_global = eta_Qob * eta_gen
            
            self.log(f"""┌─ GERADOR SELECIONADO ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  Fabricante:            {gen.get('marca', 'N/A'):20s}                                
│  Modelo:                {gen.get('modelo', 'N/A'):20s}                               
│  Relação Chapallaz:     {ratio:8.4f}                                                 
│                                                                                      
│  Potência:              {P_HP:8.1f} HP  ({P_kW:6.2f} kW)                             
│  Rotação:               {gen.get('rpm', 'N/A')} rpm                                  
│  Rendimento Gerador:    {eta_gen*100:8.2f} %                                         
│  Rendimento Global:     {eta_global*100:8.2f} %  ⭐⭐                                
│  Potência Elétrica:     {P_el:8.3f} kW                                               
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

╔══════════════════════════════════════════════════════════════════════════════════════╗
║  ✅ SELEÇÃO CONCLUÍDA - Use 'Calcular BFT no BEP' para ponto ótimo                   ║ 
╚══════════════════════════════════════════════════════════════════════════════════════╝
""")
        else:
            eta_gen = 0.85
            P_el = Pet * eta_gen
            eta_global = eta_Qob * eta_gen
        
        self.selection = {
            'pump': p,
            'pump_data': best,
            'gen': gen if gen else {},
            'Ht': Ht, 'Qt': Qt, 'Qt_m3s': Qt_m3s, 'rpm': rpm_user,
            'Hb_viana': Hb_viana, 'Qb_viana': Qb_viana,
            'Hb': best['H_ob'], 'Qb': best['Q_ob'],
            'eta_bomba': eta_Qob, 'eta_gen': eta_gen,
            'eta_global': eta_global, 'Pet': Pet, 'Pel': P_el,
            'coef_head': best['coef_head'],
            'coef_eff': best['coef_eff'],
            'rpm_catalog': best['rpm_catalog'],
            'chapallaz': ratio
        }
        
        self.current_pump = best
        
        self.status.config(text="✅ Seleção OK", fg='#27ae60')
    
    def calculate_nominal(self):
        """
        Calcula o BFT no ponto BEP com Leis da Semelhança:
        1. Pega BEP no catálogo (3500)
        2. Projeta para operação (3600)
        3. Calcula potências em 3600
        """
        if not self.current_pump:
            messagebox.showwarning("Aviso", "Execute 'Calcular Seleção' primeiro!")
            return
        
        self.status.config(text="⚙️ Calculando BEP...", fg='#f39c12')
        self.root.update()
        
        # Recupera dados
        p = self.current_pump['pump']
        rpm_catalog = self.current_pump['rpm_catalog']
        rpm_operation = self.selection['rpm']
        
        # 1. ENCONTRA BEP NO CATÁLOGO (3500 RPM)
        coef_e = safe_eval_list(p.get('coef_eff'))
        coef_h = safe_eval_list(p.get('coef_head'))
        eff_bop_catalog = float(p['eff_bop'])
        qmin = float(p.get('vazao_min', 0))
        qmax = float(p.get('vazao_max', 9999))
        
        Qbep_cat_raw = find_optimal_flow(coef_e, qmin, qmax, eff_bop_catalog)
        if not Qbep_cat_raw: Qbep_cat_raw = float(p['eff_bop_flow'])
        
        # Calcula H e Eta no catálogo
        Hbep_cat_raw = eval_poly(coef_h, Qbep_cat_raw)
        eta_fixed = normalize_eta(eval_poly(coef_e, Qbep_cat_raw))
        
        self.log(f"""

╔══════════════════════════════════════════════════════════════════════════════════════╗
║                     CÁLCULO BFT NO PONTO BEP (OTIMIZAÇÃO)                            ║
╚══════════════════════════════════════════════════════════════════════════════════════╝

┌─ PASSO 1: BEP no Catálogo (@ {rpm_catalog:.0f} rpm) ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  Qbep (catálogo):       {Qbep_cat_raw:8.2f} m³/h                                     
│  H (catálogo):          {Hbep_cat_raw:8.2f} m                                        
│  η máxima:              {eta_fixed*100:8.2f} %  ⭐                                  
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

""")
        
        # 2. PROJETA PARA OPERAÇÃO (3600 RPM)
        ratio_up = rpm_operation / rpm_catalog
        
        Q_opt_3600 = Qbep_cat_raw * ratio_up
        H_opt_3600 = Hbep_cat_raw * (ratio_up ** 2)
        
        # Potência da bomba a 3600 rpm
        g = 9.81
        P_bomba_3600 = (1000 * g * (Q_opt_3600/3600) * H_opt_3600 * eta_fixed) / 1000
        
        self.log(f"""┌─ PASSO 2: Projeção para Operação (@ {rpm_operation:.0f} rpm) ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  Razão (n_ob/n_b):      {ratio_up:8.4f}                                              
│  Q ajustado:            {Q_opt_3600:8.2f} m³/h  ({Q_opt_3600/3600:.4f} m³/s)         
│  H ajustado:            {H_opt_3600:8.2f} m                                          
│  η (mantém):            {eta_fixed*100:8.2f} %                                       
│  P_eixo (Bomba):        {P_bomba_3600:8.3f} kW                                       
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


""")
        
        # 3. SHARMA PARA TURBINA
        Qbft, Hbft = sharma_transform(Q_opt_3600, H_opt_3600, eta_fixed)
        
        P_hid_t = (1000 * g * (Qbft/3600) * Hbft) / 1000
        Pet_t = P_hid_t * eta_fixed
        
        # APLICA CHAPALLAZ NA OTIMIZAÇÃO
        ratio_opt = chapallaz_ratio(Pet_t)
        P_gen_req_opt = Pet_t / ratio_opt
        
        eta_gen = self.selection['eta_gen']
        P_el_opt = P_gen_req_opt * eta_gen  # Potência elétrica após Chapallaz
        eta_global_opt = (P_el_opt / P_hid_t) if P_hid_t > 0 else 0
        
        self.log(f"""┌─ PASSO 3: SHARMA → Turbina ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  Q turbina:             {Qbft:8.2f} m³/h  ({Qbft/3600:.4f} m³/s)                                          
│  H turbina:             {Hbft:8.2f} m                                                                     
│  P hidráulica:          {P_hid_t:8.3f} kW                                                                 
│  P eixo turbina:        {Pet_t:8.3f} kW                                                                   
│  P elétrica:            {P_el_opt:8.3f} kW                                                                
│  η global:              {eta_global_opt*100:8.2f} %  ⭐⭐                                                 
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

""")
        
        # Comparação com entrada
        Ht_user = self.selection['Ht']
        Qt_user = self.selection['Qt']
        Pet_in = self.selection['Pet']
        P_el_in = self.selection['Pel']
        eta_in = self.selection['eta_global']
        
        var_H = ((Hbft - Ht_user) / Ht_user) * 100
        var_Q = ((Qbft - Qt_user) / Qt_user) * 100
        var_Pet = ((Pet_t - Pet_in) / Pet_in) * 100
        var_Pel = ((P_el_opt - P_el_in) / P_el_in) * 100
        var_eta = ((eta_global_opt - eta_in) / eta_in) * 100
        
        self.log(f"""
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                        COMPARAÇÃO: ENTRADA vs BEP OTIMIZADO                                    ║
╠════════════════════════════════════════════════════════════════════════════════════════════════╣
║  PARÂMETRO             ENTRADA      BEP ÓTIMO    VARIAÇÃO                                      ║
╠════════════════════════════════════════════════════════════════════════════════════════════════╣
║  Altura (m)            {Ht_user:8.2f}      {Hbft:8.2f}       {var_H:+7.2f} %                   
║  Vazão (m³/h)          {Qt_user:8.2f}      {Qbft:8.2f}       {var_Q:+7.2f} %                   
║  P_eixo (kW)           {Pet_in:8.3f}      {Pet_t:8.3f}       {var_Pet:+7.2f} %                
║  P_elétrica (kW)       {P_el_in:8.3f}      {P_el_opt:8.3f}       {var_Pel:+7.2f} %             
║  η_global (%)          {eta_in*100:8.2f}      {eta_global_opt*100:8.2f}       {var_eta:+7.2f} %
╚════════════════════════════════════════════════════════════════════════════════════════════════╝

┌─ RECOMENDAÇÃO FINAL ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  💡 Operar em:  Ht = {Hbft:.2f} m  |  Qt = {Qbft:.2f} m³/h  @ {rpm_operation:.0f} rpm
│  🎯 Ganho de eficiência global: {'+' if var_eta > 0 else ''}{var_eta:.2f} %          
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

╔══════════════════════════════════════════════════════════════════════════════════════╗
║  ✅ CÁLCULO CONCLUÍDO COM SUCESSO                                                    ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
""")
        
        self.optimized = {
            'Q_opt': Q_opt_3600, 'Q_opt_m3s': Q_opt_3600/3600, 'H_opt': H_opt_3600, 'eta_opt': eta_fixed,
            'Q_catalog': Qbep_cat_raw, 'H_catalog': Hbep_cat_raw,
            'Qbft': Qbft, 'Qbft_m3s': Qbft/3600, 'Hbft': Hbft,
            'Pet_opt': Pet_t, 'Pel_opt': P_el_opt,
            'eta_global_opt': eta_global_opt,
            'var_eta': var_eta,
            'rpm_catalog': rpm_catalog,
            'rpm_operation': rpm_operation,
            'chapallaz_opt': ratio_opt
        }
        
        self.status.config(text=f"✅ BEP: η_global={eta_global_opt*100:.1f}%", fg='#27ae60')
    
    def export_csv(self):
        if not self.selection:
            messagebox.showwarning("Aviso", "Execute análise primeiro")
            return
        
        fname = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            initialfile=f"BFT_Semelhanca_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
        if not fname:
            return
        
        try:
            with open(fname, 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f)
                w.writerow(['SISTEMA_BFT_GERADOR_LEIS_3SEMELHANCA'])
                w.writerow(['Data', datetime.now().strftime('%d/%m/%Y %H:%M:%S')])
                w.writerow([])
                
                w.writerow(['BOMBA'])
                w.writerow(['Marca', self.selection['pump'].get('marca')])
                w.writerow(['Modelo', self.selection['pump'].get('modelo')])
                w.writerow(['Diametro_mm', self.selection['pump'].get('diametro')])
                w.writerow(['RPM_Catalogo', self.selection['rpm_catalog']])
                w.writerow(['RPM_Operacao', self.selection['rpm']])
                w.writerow([])
                
                if self.selection['gen']:
                    w.writerow(['GERADOR'])
                    w.writerow(['Marca', self.selection['gen'].get('marca')])
                    w.writerow(['Modelo', self.selection['gen'].get('modelo')])
                    w.writerow(['Potencia_HP', self.selection['gen'].get('P_kW')])
                    w.writerow([])
                
                w.writerow(['ENTRADA'])
                w.writerow(['Ht_m', self.selection['Ht']])
                w.writerow(['Qt_m3h', self.selection['Qt']])
                w.writerow(['rpm', self.selection['rpm']])
                w.writerow(['Rendimento_Bomba_%', self.selection['eta_bomba']*100])
                w.writerow(['Pet_kW', self.selection['Pet']])
                w.writerow(['Pel_kW', self.selection['Pel']])
                w.writerow(['Eta_global_%', self.selection['eta_global']*100])
                w.writerow([])
                
                if self.optimized:
                    w.writerow(['OTIMIZADO_BEP'])
                    w.writerow(['RPM_Catalogo', self.optimized['rpm_catalog']])
                    w.writerow(['RPM_Operacao', self.optimized['rpm_operation']])
                    w.writerow(['Q_catalogo_m3h', self.optimized['Q_catalog']])
                    w.writerow(['H_catalogo_m', self.optimized['H_catalog']])
                    w.writerow(['Q_operacao_m3h', self.optimized['Q_opt']])
                    w.writerow(['H_operacao_m', self.optimized['H_opt']])
                    w.writerow(['Qt_turbina_m3h', self.optimized['Qbft']])
                    w.writerow(['Ht_turbina_m', self.optimized['Hbft']])
                    w.writerow(['Rendimento_Bomba_%', self.optimized['eta_opt']*100])
                    w.writerow(['Pet_kW', self.optimized['Pet_opt']])
                    w.writerow(['Pel_kW', self.optimized['Pel_opt']])
                    w.writerow(['Eta_global_%', self.optimized['eta_global_opt']*100])
                    w.writerow(['Ganho_%', self.optimized['var_eta']])
            
            messagebox.showinfo("✅", f"CSV salvo:\n{fname}")
            self.status.config(text="✅ CSV exportado", fg='#27ae60')
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    def export_txt(self):
        if not self.selection:
            messagebox.showwarning("Aviso", "Execute análise primeiro")
            return
        
        fname = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text", "*.txt")],
            initialfile=f"BFT_Semelhanca_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        if not fname:
            return
        
        try:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(self.output.get('1.0', tk.END))
            messagebox.showinfo("✅", f"TXT salvo:\n{fname}")
            self.status.config(text="✅ TXT exportado", fg='#27ae60')
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    def export_matlab(self):
        if not self.selection:
            messagebox.showwarning("Aviso", "Execute análise primeiro")
            return
        
        fname = filedialog.asksaveasfilename(
            defaultextension=".m",
            filetypes=[("MATLAB Script", "*.m")],
            initialfile=f"config_BFT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.m"
        )
        if not fname:
            return
        
        try:
            sel = self.selection
            
            coef_head_str = '[' + ', '.join([f'{c}' for c in sel['coef_head']]) + ']'
            coef_eff_str = '[' + ', '.join([f'{c}' for c in sel['coef_eff']]) + ']'
            
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(f"""% Script BFT + Gerador 
% Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
% Bomba: {sel['pump'].get('marca')} {sel['pump'].get('modelo')}
% Gerador: {sel['gen'].get('marca', 'N/A')} {sel['gen'].get('modelo', 'N/A')}

clear all; clc;

%% ========== POLINÔMIOS DA BOMBA ==========
coef_head = {coef_head_str};
coef_eff = {coef_eff_str};

H_poly = @(Q) polyval(coef_head, Q);
Eta_poly = @(Q) polyval(coef_eff, Q);

%% ========== LEIS DA SEMELHANÇA ==========
n_b = {sel['rpm_catalog']};      % RPM catálogo
n_ob = {sel['rpm']};     % RPM operação
ratio = n_ob / n_b;

fprintf('\\n========== LEIS DA SEMELHANÇA ==========\\n');
fprintf('RPM Catálogo (n_b): %.0f rpm\\n', n_b);
fprintf('RPM Operação (n_ob): %.0f rpm\\n', n_ob);
fprintf('Razão (n_ob/n_b): %.4f\\n', ratio);

%% ========== PARÂMETROS INICIAIS ==========
Ht1 = {sel['Ht']};
Qt3 = {sel['Qt']};
Qt3_m3s = {sel['Qt_m3s']};
Gravidade1 = 9.81;
Densidade1 = 1000;
Rendimento_BFT1 = {sel['eta_bomba']};
EixoMecanico1 = 0.95;
Rendimento_Gerador1 = {sel['eta_gen']};
rpm_nominal = {sel['rpm']};
K_P = (Densidade1 * Gravidade1 / 3600) / 1000;
Chapallaz_selecao = {sel['chapallaz']};


fprintf('\\n========== ENTRADA ==========\\n');
fprintf('Altura: %.2f m\\n', Ht1);
fprintf('Vazão: %.2f m³/h (%.4f m³/s)\\n', Qt3, Qt3_m3s);
fprintf('η BFT: %.2f%%\\n', Rendimento_BFT1*100);
fprintf('η Gerador: %.2f%%\\n', Rendimento_Gerador1*100);
fprintf('Chapallaz: %.4f\\n', Chapallaz_selecao); 
fprintf('P_eixo: %.3f kW\\n', {sel['Pet']});
fprintf('P_elétrica: %.3f kW\\n', {sel['Pel']});
fprintf('η_global: %.2f%%\\n', {sel['eta_global']*100});
""")
                
                if self.optimized:
                    opt = self.optimized
                    f.write(f"""

%% ========== PONTO OTIMIZADO (BEP) ==========
Ht1_opt = {opt['Hbft']};
Qt3_opt = {opt['Qbft']};
Qt3_opt_m3s = {opt['Qbft_m3s']};
Rendimento_BFT1_opt = {opt['eta_opt']};
Rendimento_Gerador1_opt = {sel['eta_gen']};
Eta_global_opt = {opt['eta_global_opt']};
Chapallaz_otimizado = {opt['chapallaz_opt']};

fprintf('\\n========== BEP OTIMIZADO ==========\\n');
fprintf('Altura: %.2f m\\n', Ht1_opt);
fprintf('Vazão: %.2f m³/h (%.4f m³/s)\\n', Qt3_opt, Qt3_opt_m3s);
fprintf('η BFT: %.2f%%\\n', Rendimento_BFT1_opt*100);
fprintf('Chapallaz: %.4f\\n', Chapallaz_otimizado);
fprintf('P_eixo: %.3f kW\\n', {opt['Pet_opt']});
fprintf('P_elétrica: %.3f kW\\n', {opt['Pel_opt']});
fprintf('η_global: %.2f%%\\n', Eta_global_opt*100);
fprintf('Ganho: %.2f%%\\n', {opt['var_eta']});

%% Para usar valores otimizados, descomente:
% Ht1 = Ht1_opt;
% Qt3 = Qt3_opt;
% Qt3_m3s = Qt3_opt_m3s;
% Rendimento_BFT1 = Rendimento_BFT1_opt;
""")
                
                f.write(f"""

%% ========== SIMULINK ==========
% 1. Abra o modelo Simulink
% 2. Execute este script
% 3. Variáveis carregadas no workspace
% 4. Rode a simulação

fprintf('\\n✅ Parâmetros carregados no workspace\\n');
fprintf('✅ Leis da Semelhança aplicadas\\n');
fprintf('✅ Polinômios H_poly(Q) e Eta_poly(Q) disponíveis\\n\\n');
""")
            
            messagebox.showinfo("✅", 
                f"MATLAB gerado:\n{fname}\n\n"
                "✓ Vazão em m³/h e m³/s\n"
                "✓ Rendimentos incluídos\n"
                f"Execute: >> run('{os.path.basename(fname)}')")
            
            self.status.config(text="✅ MATLAB exportado", fg='#27ae60')
        except Exception as e:
            messagebox.showerror("Erro", str(e))

# ==================== MAIN ====================

def main():
    root = tk.Tk()
    app = BFTApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

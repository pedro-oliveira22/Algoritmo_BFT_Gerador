%% ═══════════════════════════════════════════════════════════
%  ANÁLISE PONTO ÓTIMO BFT - Usando timeseries do Simulink
%  Execute após rodar a simulação no Simulink
%% ═══════════════════════════════════════════════════════════

clc;  % Não use clear! Mantém variáveis do config_bomba.m

%% ========== CARREGAR DADOS DO SIMULINK ==========
fprintf('🔍 Procurando dados da simulação...\n\n');

% Verificar se existe a variável "out"
if ~exist('out', 'var')
    error('❌ Variável "out" não encontrada! Rode a simulação primeiro.');
end

fprintf('✅ Variável "out" encontrada!\n');
fprintf('📊 Estrutura identificada: timeseries\n\n');

%% ========== EXTRAIR DADOS DOS TIMESERIES ==========
try
    % Tempo
    tempo = out.tout;
    
    % Extrair dados dos timeseries
    vazao = out.vazao.Data;
    altura = out.altura.Data;
    eficiencia = out.eficiencia.Data;
    
    fprintf('✅ Dados extraídos com sucesso!\n');
    fprintf('   ✅ Vazão (vazao.Data)\n');
    fprintf('   ✅ Altura (altura.Data)\n');
    fprintf('   ✅ Eficiência (eficiencia.Data)\n');
    
catch ME
    fprintf('❌ Erro ao extrair dados: %s\n\n', ME.message);
    
    % Tentar alternativas
    try
        vazao = out.vazao.signals.values;
        altura = out.altura.signals.values;
        eficiencia = out.eficiencia.signals.values;
        fprintf('✅ Dados extraídos via .signals.values\n');
    catch
        fprintf('❌ Não consegui extrair os dados!\n');
        fprintf('\n📋 DEBUG - Estrutura de out.vazao:\n');
        disp(out.vazao);
        return;
    end
end

%% ========== GARANTIR VETORES COLUNA ==========
tempo = tempo(:);
vazao = vazao(:);
altura = altura(:);
eficiencia = eficiencia(:);

% Estatísticas dos dados
fprintf('\n📊 ESTATÍSTICAS DOS DADOS:\n');
fprintf('═══════════════════════════════════════════════════════════════\n');
fprintf('   Pontos simulados:    %d\n', length(tempo));
fprintf('   Tempo simulação:     %.2f a %.2f s\n', tempo(1), tempo(end));
fprintf('   Vazão:               %.2f a %.2f m³/h\n', min(vazao), max(vazao));
fprintf('   Altura:              %.2f a %.2f m\n', min(altura), max(altura));
fprintf('   Eficiência:          %.2f a %.2f %%\n', min(eficiencia), max(eficiencia));
fprintf('═══════════════════════════════════════════════════════════════\n');

%% ========== ENCONTRAR MÁXIMA EFICIÊNCIA ==========

[eta_max, idx_max] = max(eficiencia);
t_max = tempo(idx_max);
Q_max = vazao(idx_max);
H_max = altura(idx_max);

% Calcular potência no ponto ótimo
K_P = 0.0027252777777;  % (ρ * g / 3600) / 1000
P_eixo_max = K_P * Q_max * H_max * (eta_max/100);

%% ========== EXIBIR RESULTADOS PRINCIPAIS ==========
fprintf('\n');
fprintf('╔═══════════════════════════════════════════════════════════════╗\n');
fprintf('║          PONTO DE MÁXIMA EFICIÊNCIA IDENTIFICADO             ║\n');
fprintf('╠═══════════════════════════════════════════════════════════════╣\n');
fprintf('║                                                               ║\n');
fprintf('║  ⏱️  Tempo:              %8.4f s                           ║\n', t_max);
fprintf('║  📈 Eficiência Máxima:   %8.2f %%                          ║\n', eta_max);
fprintf('║  💧 Vazão (Q):           %8.2f m³/h                        ║\n', Q_max);
fprintf('║  📊 Altura (H):          %8.2f m                           ║\n', H_max);
fprintf('║  ⚡ Potência Eixo:       %8.3f kW                          ║\n', P_eixo_max);
fprintf('║                                                               ║\n');
fprintf('╚═══════════════════════════════════════════════════════════════╝\n');
fprintf('\n');

%% ========== COMPARAÇÃO COM VALORES DE ENTRADA ==========
if exist('Ht1', 'var') && exist('Qt3', 'var')
    fprintf('📊 COMPARAÇÃO: PONTO ENTRADA vs PONTO ÓTIMO\n');
    fprintf('═══════════════════════════════════════════════════════════════\n');
    
    var_Q = ((Q_max - Qt3) / Qt3) * 100;
    var_H = ((H_max - Ht1) / Ht1) * 100;
    var_eta = ((eta_max - Rendimento_BFT1*100) / (Rendimento_BFT1*100)) * 100;
    
    fprintf('   Altura:       %.2f m  →  %.2f m  (%+.2f%%)\n', Ht1, H_max, var_H);
    fprintf('   Vazão:        %.2f m³/h  →  %.2f m³/h  (%+.2f%%)\n', Qt3, Q_max, var_Q);
    fprintf('   Eficiência:   %.2f%%  →  %.2f%%  (%+.2f%%)\n', Rendimento_BFT1*100, eta_max, var_eta);
    fprintf('═══════════════════════════════════════════════════════════════\n\n');
end

%% ========== GRÁFICO 1: TRÊS SUBPLOTS ==========
figure('Name', 'Análise BFT - Ponto de Máxima Eficiência', 'NumberTitle', 'off', ...
       'Position', [100, 100, 1200, 800]);

% Subplot 1: Eficiência
subplot(3,1,1);
plot(tempo, eficiencia, 'Color', [0.85 0.33 0.10], 'LineWidth', 2.5);
hold on;
plot(t_max, eta_max, 'o', 'MarkerSize', 14, 'MarkerFaceColor', 'red', ...
     'MarkerEdgeColor', 'black', 'LineWidth', 2);
plot([t_max t_max], [min(eficiencia)-2 eta_max], 'r--', 'LineWidth', 1.5);
grid on;
ylabel('Eficiência (%)', 'FontSize', 11, 'FontWeight', 'bold');
title('Eficiência vs Tempo', 'FontSize', 12, 'FontWeight', 'bold');
legend('η(t)', sprintf('η_{MAX} = %.2f%%', eta_max), ...
       'Location', 'best', 'FontSize', 10);
xlim([tempo(1) tempo(end)]);
hold off;

% Subplot 2: Altura
subplot(3,1,2);
plot(tempo, altura, 'Color', [0.93 0.69 0.13], 'LineWidth', 2.5);
hold on;
plot(t_max, H_max, 'o', 'MarkerSize', 14, 'MarkerFaceColor', 'red', ...
     'MarkerEdgeColor', 'black', 'LineWidth', 2);
plot([t_max t_max], [min(altura)-1 H_max], 'r--', 'LineWidth', 1.5);
grid on;
ylabel('Altura (m)', 'FontSize', 11, 'FontWeight', 'bold');
title('Altura vs Tempo', 'FontSize', 12, 'FontWeight', 'bold');
legend('H(t)', sprintf('H = %.2f m @ η_{MAX}', H_max), ...
       'Location', 'best', 'FontSize', 10);
xlim([tempo(1) tempo(end)]);
hold off;

% Subplot 3: Vazão
subplot(3,1,3);
plot(tempo, vazao, 'Color', [0.00 0.45 0.74], 'LineWidth', 2.5);
hold on;
plot(t_max, Q_max, 'o', 'MarkerSize', 14, 'MarkerFaceColor', 'red', ...
     'MarkerEdgeColor', 'black', 'LineWidth', 2);
plot([t_max t_max], [min(vazao)-1 Q_max], 'r--', 'LineWidth', 1.5);
grid on;
xlabel('Tempo (s)', 'FontSize', 11, 'FontWeight', 'bold');
ylabel('Vazão (m³/h)', 'FontSize', 11, 'FontWeight', 'bold');
title('Vazão vs Tempo', 'FontSize', 12, 'FontWeight', 'bold');
legend('Q(t)', sprintf('Q = %.2f m³/h @ η_{MAX}', Q_max), ...
       'Location', 'best', 'FontSize', 10);
xlim([tempo(1) tempo(end)]);
hold off;


%% ========== SALVAR RESULTADOS NO WORKSPACE ==========
PONTO_OTIMO = struct(...
    'tempo_s', t_max, ...
    'vazao_m3h', Q_max, ...
    'altura_m', H_max, ...
    'eficiencia_perc', eta_max, ...
    'potencia_eixo_kW', P_eixo_max, ...
    'indice', idx_max ...
);

% Salvar no workspace base
assignin('base', 'PONTO_OTIMO', PONTO_OTIMO);

% Também salvar os vetores completos
DADOS_COMPLETOS = struct(...
    'tempo', tempo, ...
    'vazao', vazao, ...
    'altura', altura, ...
    'eficiencia', eficiencia ...
);

assignin('base', 'DADOS_COMPLETOS', DADOS_COMPLETOS);

%% ========== TABELA RESUMO ==========
fprintf('\n📊 TABELA RESUMO DOS RESULTADOS:\n');
fprintf('═══════════════════════════════════════════════════════════════\n');

T = table(t_max, Q_max, H_max, eta_max, P_eixo_max, ...
    'VariableNames', {'Tempo_s', 'Vazao_m3h', 'Altura_m', 'Efic_%', 'Pot_kW'});
disp(T);

fprintf('═══════════════════════════════════════════════════════════════\n');

%% ========== ANÁLISE ESTATÍSTICA ADICIONAL ==========
fprintf('\n📈 ANÁLISE ESTATÍSTICA:\n');
fprintf('═══════════════════════════════════════════════════════════════\n');
fprintf('   Eficiência Média:         %.2f %%\n', mean(eficiencia));
fprintf('   Eficiência Mediana:       %.2f %%\n', median(eficiencia));
fprintf('   Desvio Padrão:            %.2f %%\n', std(eficiencia));
fprintf('   Faixa de Operação Q:      %.2f a %.2f m³/h\n', min(vazao), max(vazao));
fprintf('   Faixa de Operação H:      %.2f a %.2f m\n', min(altura), max(altura));
fprintf('   Duração Simulação:        %.2f s\n', tempo(end) - tempo(1));
fprintf('═══════════════════════════════════════════════════════════════\n');

%% ========== MENSAGENS FINAIS ==========
fprintf('\n✅ ANÁLISE CONCLUÍDA COM SUCESSO!\n');
fprintf('✅ 4 gráficos gerados\n');
fprintf('✅ Variáveis criadas no workspace:\n');
fprintf('   • PONTO_OTIMO - Estrutura com o ponto ótimo\n');
fprintf('   • DADOS_COMPLETOS - Todos os dados da simulação\n\n');
fprintf('💡 Para acessar os resultados:\n');
fprintf('   PONTO_OTIMO.vazao_m3h\n');
fprintf('   PONTO_OTIMO.altura_m\n');
fprintf('   PONTO_OTIMO.eficiencia_perc\n');
fprintf('   PONTO_OTIMO.potencia_eixo_kW\n\n');

% Beep de conclusão
try
    beep;
    pause(0.2);
    beep;
catch
    % Ignora se não tiver som
end
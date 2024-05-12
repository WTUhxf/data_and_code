% 读取 stocks2.csv 文件
data = readtable('stocks2.csv');

% 提取时间序列数据
time_series_data = table2array(data(:, 2:end));  % 排除第一列日期数据

% 初始化邻接矩阵单元格数组
adj_matrices = cell(size(time_series_data, 2), 1);

% 对每个企业的时间序列数据计算 CVG 的邻接矩阵
for i = 1:size(time_series_data, 2)
    % 获取当前企业的时间序列数据
    time_series = time_series_data(:, i);
    
    % 计算 CVG 的邻接矩阵
    adjMatrix = CVG(time_series);
    
    % 将邻接矩阵存储在单元格数组中的相应位置
    adj_matrices{i} = adjMatrix;
end

% 将邻接矩阵单元格数组保存为.mat文件
save('adjacency_matrices.mat', 'adj_matrices');

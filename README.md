# 整数求和与文件存储工作流

## 项目概述
这是一个基于LangGraph的工作流，用于计算两个整数的和，并将结果保存为JSON文件上传到对象存储。

## 工作流结构
工作流包含以下四个节点：

### 1. 开始节点 (start_node)
- **输入参数**：
  - `int1`: integer类型 - 第一个整数
  - `int2`: integer类型 - 第二个整数
- **功能**：接收输入参数并传递给后续节点

### 2. 计算节点 (calculate_node)
- **输入参数**：
  - `int1`: 来自开始节点的第一个整数
  - `int2`: 来自开始节点的第二个整数
- **处理过程**：计算两个整数的和
- **输出参数**：
  - `sum`: integer类型 - 两个整数的和

### 3. 文件节点 (file_node)
- **输入参数**：
  - `int1`: 开始节点的int1参数
  - `int2`: 开始节点的int2参数
  - `sum`: 计算节点的sum参数
- **处理过程**：
  1. 将int1、int2、sum按照JSON格式写入文本文件
  2. 文件名为`sum.json`（例如：`8.json`）
  3. 将文件上传到对象存储
- **输出参数**：
  - `file`: File类型 - 生成的JSON文件
  - `url`: string类型 - 文件在对象存储中的预签名URL（30分钟有效期）

### 4. 结束节点 (end_node)
- **输出参数**：
  - `int1`: 开始节点的int1参数
  - `int2`: 开始节点的int2参数
  - `sum`: 计算节点输出的sum参数
  - `url`: 文件节点输出的url参数

## 数据流向
```
开始节点 → 计算节点 → 文件节点 → 结束节点
```

## 使用示例

### 输入示例
```json
{
  "int1": 5,
  "int2": 3
}
```

### 输出示例
```json
{
  "int1": 5,
  "int2": 3,
  "sum": 8,
  "url": "https://coze-coding-project.tos.coze.site/coze_storage_7587728898973073442/8_0a0326e7.json?sign=..."
}
```

### 生成的JSON文件内容
```json
{
  "int1": 5,
  "int2": 3,
  "sum": 8
}
```

## 运行方式

### 本地运行工作流
```bash
bash scripts/local_run.sh -m flow
```

### 运行单个节点
```bash
bash scripts/local_run.sh -m node -n node_name
```

### 启动HTTP服务
```bash
bash scripts/http_run.sh -m http -p 5000
```

## 项目结构
```
├── config/              # 配置文件目录
├── assets/              # 资源文件目录
├── docs/                # 文档目录
├── src/
│   ├── graphs/
│   │   ├── state.py     # 状态定义
│   │   ├── node.py      # 节点函数实现
│   │   ├── graph.py     # 图编排
│   │   └── loop_graph.py # 子图定义
│   ├── storage/         # 存储相关代码
│   └── utils/           # 工具函数
└── requirements.txt     # 依赖包列表
```

## 技术特点
- 使用LangGraph 1.0框架
- 遵循工程规范，支持可视化画布
- 集成对象存储服务
- 类型安全的状态管理
- 模块化的节点设计


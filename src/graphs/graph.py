from langgraph.graph import StateGraph, END
from graphs.state import GlobalState, GraphInput, GraphOutput
from graphs.node import start_node, calculate_node, end_node

# 创建状态图
builder = StateGraph(GlobalState, input_schema=GraphInput, output_schema=GraphOutput)

# 添加节点
builder.add_node("start_node", start_node)
builder.add_node("calculate_node", calculate_node)
builder.add_node("end_node", end_node)

# 设置入口点
builder.set_entry_point("start_node")

# 添加边连接
builder.add_edge("start_node", "calculate_node")
builder.add_edge("calculate_node", "end_node")
builder.add_edge("end_node", END)

# 编译图
main_graph = builder.compile()
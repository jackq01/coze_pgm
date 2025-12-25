from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import (
    StartNodeInput, StartNodeOutput,
    CalculateNodeInput, CalculateNodeOutput,
    EndNodeInput, EndNodeOutput
)

def start_node(state: StartNodeInput, config: RunnableConfig, runtime: Runtime[Context]) -> StartNodeOutput:
    """
    title: 开始节点
    desc: 接收两个整数输入并传递给后续节点
    """
    # 直接将输入传递到输出
    return StartNodeOutput(
        int1=state.int1,
        int2=state.int2
    )

def calculate_node(state: CalculateNodeInput, config: RunnableConfig, runtime: Runtime[Context]) -> CalculateNodeOutput:
    """
    title: 计算节点
    desc: 计算两个整数的和
    """
    # 计算两个整数的和
    result = state.int1 + state.int2
    return CalculateNodeOutput(sum=result)

def end_node(state: EndNodeInput, config: RunnableConfig, runtime: Runtime[Context]) -> EndNodeOutput:
    """
    title: 结束节点
    desc: 输出计算结果
    """
    # 直接传递和值
    return EndNodeOutput(sum=state.sum)
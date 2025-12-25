from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
import json
import os
from storage.s3.s3_storage import S3SyncStorage
from utils.file.file import File
from graphs.state import (
    StartNodeInput, StartNodeOutput,
    CalculateNodeInput, CalculateNodeOutput,
    FileNodeInput, FileNodeOutput,
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

def file_node(state: FileNodeInput, config: RunnableConfig, runtime: Runtime[Context]) -> FileNodeOutput:
    """
    title: 文件节点
    desc: 将计算结果保存为JSON文件并上传到对象存储
    integrations: 对象存储
    """
    # 创建JSON数据
    data = {
        "int1": state.int1,
        "int2": state.int2,
        "sum": state.sum
    }
    
    # 将数据转换为JSON字符串
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    
    # 生成文件名：sum.json（例如10.json）
    file_name = f"{state.sum}.json"
    
    # 初始化对象存储客户端
    storage = S3SyncStorage(
        endpoint_url=os.getenv("COZE_BUCKET_ENDPOINT_URL"),
        access_key="",
        secret_key="",
        bucket_name=os.getenv("COZE_BUCKET_NAME"),
        region="cn-beijing",
    )
    
    # 上传文件到对象存储
    object_key = storage.upload_file(
        file_content=json_str.encode('utf-8'),
        file_name=file_name,
        content_type="application/json",
    )
    
    # 生成预签名URL（30分钟有效期）
    signed_url = storage.generate_presigned_url(
        key=object_key,
        expire_time=1800  # 30分钟
    )
    
    # 创建File对象
    file_obj = File(url=signed_url, file_type="document")
    
    return FileNodeOutput(
        file=file_obj,
        url=signed_url
    )

def end_node(state: EndNodeInput, config: RunnableConfig, runtime: Runtime[Context]) -> EndNodeOutput:
    """
    title: 结束节点
    desc: 输出计算结果和文件URL
    """
    # 传递所有参数
    return EndNodeOutput(
        int1=state.int1,
        int2=state.int2,
        sum=state.sum,
        url=state.url
    )
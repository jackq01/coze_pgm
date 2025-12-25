from typing import Optional
from pydantic import BaseModel, Field
from utils.file.file import File

class GlobalState(BaseModel):
    """全局状态定义"""
    int1: Optional[int] = Field(default=None, description="第一个整数")
    int2: Optional[int] = Field(default=None, description="第二个整数")
    sum: Optional[int] = Field(default=None, description="两个整数的和")
    file_url: Optional[str] = Field(default=None, description="文件在对象存储中的URL")

class GraphInput(BaseModel):
    """工作流的输入"""
    int1: int = Field(..., description="第一个整数")
    int2: int = Field(..., description="第二个整数")

class GraphOutput(BaseModel):
    """工作流的输出"""
    int1: int = Field(..., description="第一个整数")
    int2: int = Field(..., description="第二个整数")
    sum: int = Field(..., description="两个整数的和")
    url: str = Field(..., description="文件在对象存储中的URL")

class StartNodeInput(BaseModel):
    """开始节点的输入"""
    int1: int = Field(..., description="第一个整数")
    int2: int = Field(..., description="第二个整数")

class StartNodeOutput(BaseModel):
    """开始节点的输出"""
    int1: int = Field(..., description="第一个整数")
    int2: int = Field(..., description="第二个整数")

class CalculateNodeInput(BaseModel):
    """计算节点的输入"""
    int1: int = Field(..., description="第一个整数")
    int2: int = Field(..., description="第二个整数")

class CalculateNodeOutput(BaseModel):
    """计算节点的输出"""
    sum: int = Field(..., description="两个整数的和")

class FileNodeInput(BaseModel):
    """文件节点的输入"""
    int1: int = Field(..., description="第一个整数")
    int2: int = Field(..., description="第二个整数")
    sum: int = Field(..., description="两个整数的和")

class FileNodeOutput(BaseModel):
    """文件节点的输出"""
    file: File = Field(..., description="生成的JSON文件")
    url: str = Field(..., description="文件在对象存储中的URL")

class EndNodeInput(BaseModel):
    """结束节点的输入"""
    int1: int = Field(..., description="第一个整数")
    int2: int = Field(..., description="第二个整数")
    sum: int = Field(..., description="两个整数的和")
    url: str = Field(..., description="文件在对象存储中的URL")

class EndNodeOutput(BaseModel):
    """结束节点的输出"""
    int1: int = Field(..., description="第一个整数")
    int2: int = Field(..., description="第二个整数")
    sum: int = Field(..., description="两个整数的和")
    url: str = Field(..., description="文件在对象存储中的URL")
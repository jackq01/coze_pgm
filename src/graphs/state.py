from typing import Optional
from pydantic import BaseModel, Field

class GlobalState(BaseModel):
    """全局状态定义"""
    int1: Optional[int] = Field(default=None, description="第一个整数")
    int2: Optional[int] = Field(default=None, description="第二个整数")
    sum: Optional[int] = Field(default=None, description="两个整数的和")

class GraphInput(BaseModel):
    """工作流的输入"""
    int1: int = Field(..., description="第一个整数")
    int2: int = Field(..., description="第二个整数")

class GraphOutput(BaseModel):
    """工作流的输出"""
    sum: int = Field(..., description="两个整数的和")

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

class EndNodeInput(BaseModel):
    """结束节点的输入"""
    sum: int = Field(..., description="两个整数的和")

class EndNodeOutput(BaseModel):
    """结束节点的输出"""
    sum: int = Field(..., description="两个整数的和")
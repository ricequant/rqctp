from .TraderApi import TraderApi as CTraderApi
from .structs import *


class TraderApi(CTraderApi):
    def __init__(self, pszFlowPath: str = ""):
        ...

    def Init(self):
        ...

    def Release(self):
        ...

    def RegisterFront(self, pszFrontAddress: str):
        ...

    def SubscribePrivateTopic(self, nResumeType: int):
        ...

    def SubscribePublicTopic(self, nResumeType: int):
        ...

    def ReqUserLogin(self, reqUserLoginField: ReqUserLogin, nRequestID: int) -> int:
        ...

    def ReqQrySettlementInfo(self, pQrySettlementInfo: QrySettlementInfo, nRequestID: int) -> int:
        ...

    def OnFrontConnected(self):
        ...

    def OnFrontDisconnected(self, nReason: int):
        ...

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        ...

    def OnRtnTrade(self, pTrade):
        ...

    def OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
        ...

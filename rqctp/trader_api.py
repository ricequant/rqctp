from .ctp.TraderApi import TraderApi


class PyTraderApi(TraderApi):
    def __init__(self, pszFlowPath: str = ""):
        super(PyTraderApi, self).__init__(pszFlowPath.encode("GBK"))

    def Init(self):
        return super(PyTraderApi, self).Init()

    def Release(self):
        return super(PyTraderApi, self).Release()

    def RegisterFront(self, pszFrontAddress: str):
        return super(PyTraderApi, self).RegisterFront(pszFrontAddress.encode("GBK"))

    def ReqUserLogin(self, reqUserLoginField, nRequestID):
        return super(PyTraderApi, self).ReqUserLogin(reqUserLoginField, nRequestID)

    def OnFrontConnected(self):
        pass

    def OnFrontDisconnected(self, nReason: int):
        pass

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        pass

"""
标准CTP：
    第一组：Trade Front：180.168.146.187:10100，Market Front：180.168.146.187:10110；【电信】
    第二组：Trade Front：180.168.146.187:10101，Market Front：180.168.146.187:10111；【电信】
    第三组：Trade Front： 218.202.237.33 :10102，Market Front：218.202.237.33 :10112；【移动】
7*24小时环境：
    第一组：Trade Front： 180.168.146.187:10130，Market Front：180.168.146.187:10131；【电信】
"""
import sys
from datetime import datetime
from time import sleep
from typing import Callable, List

from rqctp import MdApi, TraderApi
from rqctp.structs import ReqUserLogin, QryInstrument, Instrument, ReqAuthenticate


class ApiMixin:
    RegisterFront: Callable[[str], None]
    Init: Callable[[], None]
    ReqUserLogin: Callable[[ReqUserLogin, int], int]

    def __init__(self, url, username, password):
        super(ApiMixin, self).__init__()
        self._username = username
        self._password = password
        self._req_id = 0
        self.RegisterFront(url)
        self.Init()

    @property
    def req_id(self):
        self._req_id += 1
        return self._req_id

    def OnFrontConnected(self):
        print(f"{self.__class__.__name__} connected")

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestId, bIsLast):
        if pRspInfo.ErrorID == 0:
            print(f"{self.__class__.__name__} logged in")
        else:
            raise RuntimeError(f"{self.__class__.__name__} login failed: {pRspInfo}")


class TestMdApi(ApiMixin, MdApi):
    def OnFrontConnected(self):
        super(TestMdApi, self).OnFrontConnected()
        self.ReqUserLogin(ReqUserLogin(UserID=self._username, Password=self._password), self.req_id)

    def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        if pRspInfo.ErrorID == 0:
            print(f"SubscribeMarketData succeeded: {pSpecificInstrument}, {pRspInfo}")
        else:
            raise RuntimeError(f"SubscribeMarketData failed: {pRspInfo}")

    def OnRtnDepthMarketData(self, pDepthMarketData):
        print(pDepthMarketData)


class TestTraderApi(ApiMixin, TraderApi):
    def __init__(self, url, username, password):
        super(TestTraderApi, self).__init__(url, username, password)
        self.instruments: List[Instrument] = []
        self.instruments_got = False

    def OnFrontConnected(self):
        super(TestTraderApi, self).OnFrontConnected()
        self.ReqAuthenticate(ReqAuthenticate(
            BrokerID="9999",
            UserID=self._username,
            AuthCode="0000000000000000",
            AppID="simnow_client_test"
        ), self.req_id)

    def OnRspAuthenticate(self, pRspAuthenticateField, pRspInfo, nRequestID, bIsLast):
        if pRspInfo.ErrorID != 0:
            raise RuntimeError("ReqAuthenticate failed")
        print(f"ReqAuthenticate succeeded: {pRspAuthenticateField}, {pRspInfo}")
        self.ReqUserLogin(ReqUserLogin(
            UserID=self._username,
            Password=self._password,
            BrokerID="9999"
        ), self.req_id)

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        super(TestTraderApi, self).OnRspUserLogin(pRspUserLogin, pRspInfo, nRequestID, bIsLast)
        self.ReqQryInstrument(QryInstrument(), self.req_id)

    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        if pInstrument is not None:
            self.instruments.append(pInstrument)
        if bIsLast:
            self.instruments_got = True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python test.py <SIMNOW_username> <SIMNOW_password>")
    else:
        _, username, password = sys.argv

        now = datetime.now()
        if 9 <= now.hour <= 15 or now.hour >= 21 or now.hour <= 2:
            MD_URL = "tcp://180.168.146.187:10110"
            TRADER_URL = "tcp://180.168.146.187:10100"
        else:
            MD_URL = "tcp://180.168.146.187:10131"
            TRADER_URL = "tcp://180.168.146.187:10130"
        print(f"use urls: trader: {TRADER_URL}, md: {MD_URL}")

        trader_api = TestTraderApi(TRADER_URL, username, password)
        md_api = TestMdApi(MD_URL, username, password)

        for i in range(100):
            if trader_api.instruments_got:
                break
            sleep(0.1)
        else:
            raise TimeoutError("QryInstrument timeout")
        md_api.SubscribeMarketData([i.InstrumentID for i in trader_api.instruments])
        sleep(1)
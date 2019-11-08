# -*- coding: utf-8 -*-
#
# Copyright 2019 Ricequant, Inc
#
# * Commercial Usage: please contact public@ricequant.com
# * Non-Commercial Usage:
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from .TraderApi import TraderApi


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

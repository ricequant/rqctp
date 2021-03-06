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

from cpython cimport PyObject
from libc.string cimport const_char
from libcpp cimport bool as cbool

from .ThostFtdcTraderApi cimport CTraderApi, CTraderSpi, CreateFtdcTraderApi
from .ThostFtdcUserApiStruct cimport *

import ctypes

from .structs import *


cdef class TraderApi:
    cdef CTraderApi *_api
    cdef CTraderSpi *_spi

    def __cinit__(self):
        self._api = NULL
        self._spi = NULL

    def __init__(self, const_char *pszFlowPath):
        self._api = CreateFtdcTraderApi(pszFlowPath)
        if self._api is NULL:
            raise MemoryError()
        self._spi = new CTraderSpi(<PyObject *>self)
        if self._spi is NULL:
            raise MemoryError()
        self._api.RegisterSpi(self._spi)

    def __dealloc__(self):
        if self._api is not NULL:
            self._api.RegisterSpi(NULL)
            self._api.Release()
            self._api = NULL
            self._spi = NULL

    def _ensure_api_not_null(self):
        if self._api is NULL:
            raise MemoryError()

    def Release(self):
        if self._api is not NULL:
            self._api.RegisterSpi(NULL)
            self._api.Release()
            self._api = NULL
            self._spi = NULL

    def Init(self):
        self._ensure_api_not_null()
        self._api.Init()

    def Join(self):
        cdef int result
        self._ensure_api_not_null()
        if self._spi is not NULL:

            print("before api join")
            with nogil:
                result = self._api.Join()
            return result

    def RegisterFront(self, char *pszFrontAddress):
        self._ensure_api_not_null()
        self._api.RegisterFront(pszFrontAddress)

    def SubscribePrivateTopic(self, THOST_TE_RESUME_TYPE nResumeType):
        self._ensure_api_not_null()
        self._api.SubscribePrivateTopic(nResumeType)

    def SubscribePublicTopic(self, THOST_TE_RESUME_TYPE nResumeType):
        self._ensure_api_not_null()
        self._api.SubscribePublicTopic(nResumeType)

    def ReqUserLogin(self, reqUserLoginField, int nRequestID):
        cdef int result
        cdef size_t address
        self._ensure_api_not_null()
        address = ctypes.addressof(reqUserLoginField)
        with nogil:
            result = self._api.ReqUserLogin(<CThostFtdcReqUserLoginField *> address, nRequestID)
        return result

    def ReqQrySettlementInfo(self, pQrySettlementInfo, int nRequestID):
        cdef int result
        cdef size_t address
        self._ensure_api_not_null()
        address = ctypes.addressof(pQrySettlementInfo)
        with nogil:
            result = self._api.ReqQrySettlementInfo(<CThostFtdcQrySettlementInfoField *> address, nRequestID)
        return result

    def ReqAuthenticate(self, pReqAuthenticateField, int nRequestID):
        cdef int result
        cdef size_t address
        self._ensure_api_not_null()
        address = ctypes.addressof(pReqAuthenticateField)
        with nogil:
            result = self._api.ReqAuthenticate(<CThostFtdcReqAuthenticateField *> address, nRequestID)
        return result


cdef extern int TraderSpi__OnFrontConnected(api) except -1:
    api.OnFrontConnected()
    return 0


cdef extern int TraderSpi__OnFrontDisconnected(api, int nReason) except -1:
    api.OnFrontDisconnected(nReason)
    return 0


cdef extern int TraderSpi__OnRspUserLogin(api, CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUserLogin(
        None if pRspUserLogin is NULL else RspUserLogin.from_address(<size_t> pRspUserLogin).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRtnTrade(api, CThostFtdcTradeField *pTrade) except -1:
    api.OnRtnTrade(None if pTrade is NULL else Trade.from_address(<size_t> pTrade).to_tuple())
    return 0


cdef extern int TraderSpi__OnRspQrySettlementInfo(api, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQrySettlementInfo(
        None if pSettlementInfo is NULL else SettlementInfo.from_address(<size_t> pSettlementInfo).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspAuthenticate(api, CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspAuthenticate(
        None if pRspAuthenticateField is NULL else RspAuthenticate.from_address(<size_t> pRspAuthenticateField).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0

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
from libc.stdlib cimport malloc, free
from libcpp cimport bool as cbool

from .ThostFtdcMdApi cimport CMdApi, CMdSpi, CreateFtdcMdApi
from .ThostFtdcUserApiStruct cimport *

import ctypes

from .structs import *


cdef class MdApi:
    cdef CMdApi *_api
    cdef CMdSpi *_spi

    def __cinit__(self):
        self._api = NULL
        self._spi = NULL

    def __init__(self, const_char *pszFlowPath, cbool bIsUsingUdp, cbool bIsMulticast):
        self._api = CreateFtdcMdApi(pszFlowPath, bIsUsingUdp, bIsMulticast)
        if self._api is NULL:
            raise MemoryError()
        self._spi = new CMdSpi(<PyObject *>self)
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


    def RegisterFront(self, pszFrontAddress):
        cdef char *address_pszFrontAddress
        if self._api is NULL:
            raise MemoryError()
        try:
            b_pszFrontAddress = pszFrontAddress.encode("GBK")
            address_pszFrontAddress = b_pszFrontAddress
            with nogil:
                self._api.RegisterFront(address_pszFrontAddress)
        finally:
            pass
        return

    def RegisterNameServer(self, pszNsAddress):
        cdef char *address_pszNsAddress
        if self._api is NULL:
            raise MemoryError()
        try:
            b_pszNsAddress = pszNsAddress.encode("GBK")
            address_pszNsAddress = b_pszNsAddress
            with nogil:
                self._api.RegisterNameServer(address_pszNsAddress)
        finally:
            pass
        return

    def RegisterFensUserInfo(self, pFensUserInfo):
        cdef size_t address_pFensUserInfo = ctypes.addressof(pFensUserInfo)
        if self._api is NULL:
            raise MemoryError()
        try:
            with nogil:
                self._api.RegisterFensUserInfo(<CThostFtdcFensUserInfoField *> address_pFensUserInfo)
        finally:
            pass
        return

    def SubscribeMarketData(self, ppInstrumentID):
        cdef int result
        cdef int nCount = len(ppInstrumentID)
        cdef char **address_ppInstrumentID = <char **>malloc(nCount * sizeof(char *))
        if self._api is NULL:
            raise MemoryError()
        try:
            ppInstrumentID = [i.encode("GBK") for i in ppInstrumentID]
            for i in range(nCount):
                address_ppInstrumentID[i] = ppInstrumentID[i]
            with nogil:
                result = self._api.SubscribeMarketData(address_ppInstrumentID, nCount)
        finally:
            free(address_ppInstrumentID)
        return result

    def UnSubscribeMarketData(self, ppInstrumentID):
        cdef int result
        cdef int nCount = len(ppInstrumentID)
        cdef char **address_ppInstrumentID = <char **>malloc(nCount * sizeof(char *))
        if self._api is NULL:
            raise MemoryError()
        try:
            ppInstrumentID = [i.encode("GBK") for i in ppInstrumentID]
            for i in range(nCount):
                address_ppInstrumentID[i] = ppInstrumentID[i]
            with nogil:
                result = self._api.UnSubscribeMarketData(address_ppInstrumentID, nCount)
        finally:
            free(address_ppInstrumentID)
        return result

    def SubscribeForQuoteRsp(self, ppInstrumentID):
        cdef int result
        cdef int nCount = len(ppInstrumentID)
        cdef char **address_ppInstrumentID = <char **>malloc(nCount * sizeof(char *))
        if self._api is NULL:
            raise MemoryError()
        try:
            ppInstrumentID = [i.encode("GBK") for i in ppInstrumentID]
            for i in range(nCount):
                address_ppInstrumentID[i] = ppInstrumentID[i]
            with nogil:
                result = self._api.SubscribeForQuoteRsp(address_ppInstrumentID, nCount)
        finally:
            free(address_ppInstrumentID)
        return result

    def UnSubscribeForQuoteRsp(self, ppInstrumentID):
        cdef int result
        cdef int nCount = len(ppInstrumentID)
        cdef char **address_ppInstrumentID = <char **>malloc(nCount * sizeof(char *))
        if self._api is NULL:
            raise MemoryError()
        try:
            ppInstrumentID = [i.encode("GBK") for i in ppInstrumentID]
            for i in range(nCount):
                address_ppInstrumentID[i] = ppInstrumentID[i]
            with nogil:
                result = self._api.UnSubscribeForQuoteRsp(address_ppInstrumentID, nCount)
        finally:
            free(address_ppInstrumentID)
        return result

    def ReqUserLogin(self, pReqUserLoginField, int nRequestID):
        cdef int result
        cdef size_t address_pReqUserLoginField = ctypes.addressof(pReqUserLoginField)
        if self._api is NULL:
            raise MemoryError()
        try:
            with nogil:
                result = self._api.ReqUserLogin(<CThostFtdcReqUserLoginField *> address_pReqUserLoginField, nRequestID)
        finally:
            pass
        return result

    def ReqUserLogout(self, pUserLogout, int nRequestID):
        cdef int result
        cdef size_t address_pUserLogout = ctypes.addressof(pUserLogout)
        if self._api is NULL:
            raise MemoryError()
        try:
            with nogil:
                result = self._api.ReqUserLogout(<CThostFtdcUserLogoutField *> address_pUserLogout, nRequestID)
        finally:
            pass
        return result

    def ReqQryMulticastInstrument(self, pQryMulticastInstrument, int nRequestID):
        cdef int result
        cdef size_t address_pQryMulticastInstrument = ctypes.addressof(pQryMulticastInstrument)
        if self._api is NULL:
            raise MemoryError()
        try:
            with nogil:
                result = self._api.ReqQryMulticastInstrument(<CThostFtdcQryMulticastInstrumentField *> address_pQryMulticastInstrument, nRequestID)
        finally:
            pass
        return result


cdef extern int MdSpi__OnFrontConnected(api) except -1:
    api.OnFrontConnected()
    return 0


cdef extern int MdSpi__OnFrontDisconnected(api, int nReason) except -1:
    api.OnFrontDisconnected(
        nReason
    )
    return 0


cdef extern int MdSpi__OnHeartBeatWarning(api, int nTimeLapse) except -1:
    api.OnHeartBeatWarning(
        nTimeLapse
    )
    return 0


cdef extern int MdSpi__OnRspUserLogin(api, CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUserLogin(
        None if pRspUserLogin is NULL else RspUserLogin.from_address(<size_t> pRspUserLogin).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int MdSpi__OnRspUserLogout(api, CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUserLogout(
        None if pUserLogout is NULL else UserLogout.from_address(<size_t> pUserLogout).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int MdSpi__OnRspQryMulticastInstrument(api, CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryMulticastInstrument(
        None if pMulticastInstrument is NULL else MulticastInstrument.from_address(<size_t> pMulticastInstrument).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int MdSpi__OnRspError(api, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspError(
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int MdSpi__OnRspSubMarketData(api, CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspSubMarketData(
        None if pSpecificInstrument is NULL else SpecificInstrument.from_address(<size_t> pSpecificInstrument).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int MdSpi__OnRspUnSubMarketData(api, CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUnSubMarketData(
        None if pSpecificInstrument is NULL else SpecificInstrument.from_address(<size_t> pSpecificInstrument).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int MdSpi__OnRspSubForQuoteRsp(api, CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspSubForQuoteRsp(
        None if pSpecificInstrument is NULL else SpecificInstrument.from_address(<size_t> pSpecificInstrument).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int MdSpi__OnRspUnSubForQuoteRsp(api, CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUnSubForQuoteRsp(
        None if pSpecificInstrument is NULL else SpecificInstrument.from_address(<size_t> pSpecificInstrument).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int MdSpi__OnRtnDepthMarketData(api, CThostFtdcDepthMarketDataField *pDepthMarketData) except -1:
    api.OnRtnDepthMarketData(
        None if pDepthMarketData is NULL else DepthMarketData.from_address(<size_t> pDepthMarketData).to_tuple()
    )
    return 0


cdef extern int MdSpi__OnRtnForQuoteRsp(api, CThostFtdcForQuoteRspField *pForQuoteRsp) except -1:
    api.OnRtnForQuoteRsp(
        None if pForQuoteRsp is NULL else ForQuoteRsp.from_address(<size_t> pForQuoteRsp).to_tuple()
    )
    return 0

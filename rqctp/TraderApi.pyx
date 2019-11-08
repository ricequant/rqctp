from cpython cimport PyObject
from libc.string cimport const_char
from libcpp cimport bool as cbool

from .ThostFtdcTraderApi cimport CTraderApi, CTraderSpi, CreateFtdcTraderApi
from .ThostFtdcUserApiStruct cimport CThostFtdcReqUserLoginField, CThostFtdcRspUserLoginField, CThostFtdcRspInfoField

import ctypes

from .structs import RspUserLogin, RspInfo


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

    def ReqUserLogin(self, reqUserLoginField, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(reqUserLoginField)
            with nogil:
                result = self._api.ReqUserLogin(<CThostFtdcReqUserLoginField *> address, nRequestID)
            return result


cdef extern int TraderSpi__OnFrontConnected(api) except -1:
    api.OnFrontConnected()
    return 0


cdef extern int TraderSpi__OnFrontDisconnected(api, int nReason) except -1:
    api.OnFrontDisconnected(nReason)
    return 0


cdef extern int TraderSpi__OnRspUserLogin(api, CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUserLogin(None if pRspUserLogin is NULL else RspUserLogin.from_address(<size_t> pRspUserLogin).to_tuple(), None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(), nRequestID, bIsLast)
    return 0

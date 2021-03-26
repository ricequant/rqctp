from cpython cimport PyObject
import ctypes
from libc.string cimport const_char
from libc.stdlib cimport malloc, free
from libcpp cimport bool as cbool

from .ThostFtdcMdApi cimport CMdApi, CMdSpi, CreateFtdcMdApi
from .ThostFtdcUserApiStruct cimport *

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
        self.Release()

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

    def ReqUserLogin(self, pReqUserLoginField, int nRequestID):
        cdef int result
        cdef size_t address
        self._ensure_api_not_null()
        address = ctypes.addressof(pReqUserLoginField)
        with nogil:
            result = self._api.ReqUserLogin(<CThostFtdcReqUserLoginField *> address, nRequestID)
        return result

    def SubscribeMarketData(self, ppInstrumentID, int cCount):
        cdef int result
        cdef char **cppInstrumentId

        self._ensure_api_not_null()
        cppInstrumentId = <char **>malloc(cCount * sizeof(char *))
        try:
            for i in range(cCount):
                cppInstrumentId[i] = ppInstrumentID[i]
                with nogil:
                    result = self._api.SubscribeMarketData(cppInstrumentId, cCount)
        finally:
            free(cppInstrumentId)
        return result


cdef extern int MdSpi__OnFrontConnected(api) except -1:
    api.OnFrontConnected()
    return 0


cdef extern int MdSpi__OnFrontDisconnected(api, int nReason) except -1:
    api.OnFrontDisconnected(
        nReason
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


cdef extern int MdSpi__OnRspSubMarketData(api, CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspSubMarketdata(
        None if pSpecificInstrument is NULL else SpecificInstrument.from_address(<size_t> pSpecificInstrument).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )


cdef extern int MdSpi__OnRtnDepthMarketData(api, CThostFtdcDepthMarketDataField *pDepthMarketData):
    api.OnRthDepthMarketData(
        None if pDepthMarketData is NULL else DepthMarketData.from_address(<size_t> pDepthMarketData).to_tuple(),
    )

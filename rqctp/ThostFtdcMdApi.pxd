from cpython cimport PyObject
from libc.string cimport const_char
from libcpp cimport bool as cbool

from .ThostFtdcUserApiStruct cimport *

cdef extern from "ThostFtdcMdApi.h":
    cdef cppclass CMdApi "CThostFtdcMdApi":
        void Release() nogil
        void Init() nogil
        int Join() nogil
        void RegisterFront(char *pszFrontAddress) nogil except +
        void RegisterSpi(CMdSpi *pSpi) nogil except +
        int SubscribeMarketData(char *ppInstrumentId[], int cCount) nogil except +
        int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestId) nogil except +


cdef extern from "ThostFtdcMdApi.h" namespace "CThostFtdcMdApi":
    CMdApi *CreateFtdcMdApi(const_char *pszFlowPath, cbool bIsUsingUdp, cbool bIsMulticast) nogil except +
    const_char *GetApiVersion() nogil


cdef extern from "CMdSpi.h":
    cdef cppclass CMdSpi:
        CMdSpi(PyObject *obj)
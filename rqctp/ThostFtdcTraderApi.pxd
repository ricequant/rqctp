from cpython cimport PyObject
from libc.string cimport const_char

from .ThostFtdcUserApiStruct cimport *

cdef extern from "ThostFtdcTraderApi.h":
    cdef cppclass CTraderApi "CThostFtdcTraderApi":
        void Release() nogil
        void Init() nogil
        int Join() nogil
        void RegisterFront(char *pszFrontAddress) nogil except +
        void RegisterSpi(CTraderSpi *pSpi) nogil except +
        int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) nogil except +


cdef extern from "ThostFtdcTraderApi.h" namespace "CThostFtdcTraderApi":
    CTraderApi *CreateFtdcTraderApi(const_char *pszFlowPath) nogil except +


cdef extern from "CTraderSpi.h":
    cdef cppclass CTraderSpi:
        CTraderSpi(PyObject *obj)

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

from .ThostFtdcUserApiStruct cimport *


cdef extern from "ThostFtdcMdApi.h":
    cdef cppclass CMdApi "CThostFtdcMdApi":
        void Release() nogil
        void Init() nogil
        int Join() nogil
        void RegisterSpi(CMdSpi *pSpi) nogil except +
        void SubscribePrivateTopic(THOST_TE_RESUME_TYPE nResumeType) nogil except +
        void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) nogil except +
        void RegisterFront(char *pszFrontAddress) nogil except +
        void RegisterNameServer(char *pszNsAddress) nogil except +
        void RegisterFensUserInfo(CThostFtdcFensUserInfoField *pFensUserInfo) nogil except +
        int SubscribeMarketData(char *ppInstrumentID[], int nCount) nogil except +
        int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) nogil except +
        int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) nogil except +
        int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) nogil except +
        int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) nogil except +
        int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) nogil except +
        int ReqQryMulticastInstrument(CThostFtdcQryMulticastInstrumentField *pQryMulticastInstrument, int nRequestID) nogil except +


cdef extern from "ThostFtdcMdApi.h" namespace "CThostFtdcMdApi":
    CMdApi *CreateFtdcMdApi(const_char *pszFlowPath, cbool bIsUsingUdp, cbool bIsMulticast) nogil except +
    const_char *GetApiVersion() nogil


cdef extern from "CMdSpi.h":
    cdef cppclass CMdSpi:
        CMdSpi(PyObject *obj)
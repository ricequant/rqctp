// -*- coding: utf-8 -*-
//
// Copyright 2019 Ricequant, Inc
//
// * Commercial Usage: please contact public@ricequant.com
// * Non-Commercial Usage:
//     Licensed under the Apache License, Version 2.0 (the "License");
//     you may not use this file except in compliance with the License.
//     You may obtain a copy of the License at
//
//         http://www.apache.org/licenses/LICENSE-2.0
//
//     Unless required by applicable law or agreed to in writing, software
//     distributed under the License is distributed on an "AS IS" BASIS,
//     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//     See the License for the specific language governing permissions and
//     limitations under the License.

#include "Python.h"
#include "pythread.h"
#include "ThostFtdcMdApi.h"

static inline int MdSpi__OnFrontConnected(PyObject *);
static inline int MdSpi__OnFrontDisconnected(PyObject *, int);
static inline int MdSpi__OnHeartBeatWarning(PyObject *, int);
static inline int MdSpi__OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRspQryMulticastInstrument(PyObject *, CThostFtdcMulticastInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRspSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRspUnSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRspSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRspUnSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRtnDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *);
static inline int MdSpi__OnRtnForQuoteRsp(PyObject *, CThostFtdcForQuoteRspField *);


#define PyGIL(func) \
    do { \
        PyGILState_STATE gil_state = PyGILState_Ensure(); \
        if ((func) == -1) PyErr_Print(); \
        PyGILState_Release(gil_state); \
    } while (false)


class CMdSpi: public CThostFtdcMdSpi {
    public:
        CMdSpi(PyObject *obj): api(obj) {};
        virtual ~CMdSpi() {};

        virtual void OnFrontConnected() {
            PyGIL(MdSpi__OnFrontConnected(api));
        };

        virtual void OnFrontDisconnected(int nReason) {
            PyGIL(MdSpi__OnFrontDisconnected(api, nReason));
        };

        virtual void OnHeartBeatWarning(int nTimeLapse) {
            PyGIL(MdSpi__OnHeartBeatWarning(api, nTimeLapse));
        };

        virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(MdSpi__OnRspUserLogin(api, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(MdSpi__OnRspUserLogout(api, pUserLogout, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryMulticastInstrument(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(MdSpi__OnRspQryMulticastInstrument(api, pMulticastInstrument, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(MdSpi__OnRspError(api, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(MdSpi__OnRspSubMarketData(api, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(MdSpi__OnRspUnSubMarketData(api, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(MdSpi__OnRspSubForQuoteRsp(api, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(MdSpi__OnRspUnSubForQuoteRsp(api, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {
            PyGIL(MdSpi__OnRtnDepthMarketData(api, pDepthMarketData));
        };

        virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
            PyGIL(MdSpi__OnRtnForQuoteRsp(api, pForQuoteRsp));
        };

    private:
        PyObject *api;
};
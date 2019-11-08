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
#include "ThostFtdcTraderApi.h"


static inline int TraderSpi__OnFrontConnected(PyObject *);
static inline int TraderSpi__OnFrontDisconnected(PyObject *, int);
static inline int TraderSpi__OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);


#define PyGIL(func) \
    do { \
        PyGILState_STATE gil_state = PyGILState_Ensure(); \
        if ((func) == -1) PyErr_Print(); \
        PyGILState_Release(gil_state); \
    } while (false)


class CTraderSpi: public CThostFtdcTraderSpi {
    public:
        CTraderSpi(PyObject *obj): api(obj) {};
        virtual ~CTraderSpi() {};

        virtual void OnFrontConnected() {
            PyGIL(TraderSpi__OnFrontConnected(api));
        };

        virtual void OnFrontDisconnected(int nReason) {
            PyGIL(TraderSpi__OnFrontDisconnected(api, nReason));
        };

        virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspUserLogin(api, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
        };

    private:
        PyObject *api;
};

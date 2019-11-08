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

#include "Python.h"
#include "pythread.h"
#include "ThostFtdcMdApi.h"

static inline int MdSpi__OnFrontConnected(PyObject *);
static inline int MdSpi__OnFrontDisconnected(PyObject *, int);
static inline int MdSpi__OnRspUserLogin(PyObject *, CTHostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRspSubMarketData(CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi__OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *);


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

        virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(MdSpi__OnRspUserLogin(api, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestId, bool bIsLast) {
            PyGIL(MdSpi__OnRspSubMarketData(api, pSpecificInstrument, pRspInfo, nRequestId, bIsLast));
        };

        virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {
            PyGIL(MdSpi__OnRtnDepthMarketData(api, pDepthMarketData));
        };

private:
    PyObject *api;


}
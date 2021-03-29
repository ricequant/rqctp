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
static inline int TraderSpi__OnHeartBeatWarning(PyObject *, int);
static inline int TraderSpi__OnRspAuthenticate(PyObject *, CThostFtdcRspAuthenticateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspUserPasswordUpdate(PyObject *, CThostFtdcUserPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspTradingAccountPasswordUpdate(PyObject *, CThostFtdcTradingAccountPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspUserAuthMethod(PyObject *, CThostFtdcRspUserAuthMethodField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspGenUserCaptcha(PyObject *, CThostFtdcRspGenUserCaptchaField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspGenUserText(PyObject *, CThostFtdcRspGenUserTextField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspOrderInsert(PyObject *, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspParkedOrderInsert(PyObject *, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspParkedOrderAction(PyObject *, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspOrderAction(PyObject *, CThostFtdcInputOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryMaxOrderVolume(PyObject *, CThostFtdcQryMaxOrderVolumeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspSettlementInfoConfirm(PyObject *, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspRemoveParkedOrder(PyObject *, CThostFtdcRemoveParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspRemoveParkedOrderAction(PyObject *, CThostFtdcRemoveParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspExecOrderInsert(PyObject *, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspExecOrderAction(PyObject *, CThostFtdcInputExecOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspForQuoteInsert(PyObject *, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQuoteInsert(PyObject *, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQuoteAction(PyObject *, CThostFtdcInputQuoteActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspBatchOrderAction(PyObject *, CThostFtdcInputBatchOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspOptionSelfCloseInsert(PyObject *, CThostFtdcInputOptionSelfCloseField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspOptionSelfCloseAction(PyObject *, CThostFtdcInputOptionSelfCloseActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspCombActionInsert(PyObject *, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryOrder(PyObject *, CThostFtdcOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryTrade(PyObject *, CThostFtdcTradeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInvestorPosition(PyObject *, CThostFtdcInvestorPositionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryTradingAccount(PyObject *, CThostFtdcTradingAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInvestor(PyObject *, CThostFtdcInvestorField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryTradingCode(PyObject *, CThostFtdcTradingCodeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInstrumentMarginRate(PyObject *, CThostFtdcInstrumentMarginRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInstrumentCommissionRate(PyObject *, CThostFtdcInstrumentCommissionRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryExchange(PyObject *, CThostFtdcExchangeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryProduct(PyObject *, CThostFtdcProductField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInstrument(PyObject *, CThostFtdcInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQrySettlementInfo(PyObject *, CThostFtdcSettlementInfoField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryTransferBank(PyObject *, CThostFtdcTransferBankField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInvestorPositionDetail(PyObject *, CThostFtdcInvestorPositionDetailField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryNotice(PyObject *, CThostFtdcNoticeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQrySettlementInfoConfirm(PyObject *, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInvestorPositionCombineDetail(PyObject *, CThostFtdcInvestorPositionCombineDetailField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryCFMMCTradingAccountKey(PyObject *, CThostFtdcCFMMCTradingAccountKeyField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryEWarrantOffset(PyObject *, CThostFtdcEWarrantOffsetField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInvestorProductGroupMargin(PyObject *, CThostFtdcInvestorProductGroupMarginField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryExchangeMarginRate(PyObject *, CThostFtdcExchangeMarginRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryExchangeMarginRateAdjust(PyObject *, CThostFtdcExchangeMarginRateAdjustField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryExchangeRate(PyObject *, CThostFtdcExchangeRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQrySecAgentACIDMap(PyObject *, CThostFtdcSecAgentACIDMapField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryProductExchRate(PyObject *, CThostFtdcProductExchRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryProductGroup(PyObject *, CThostFtdcProductGroupField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryMMInstrumentCommissionRate(PyObject *, CThostFtdcMMInstrumentCommissionRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryMMOptionInstrCommRate(PyObject *, CThostFtdcMMOptionInstrCommRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInstrumentOrderCommRate(PyObject *, CThostFtdcInstrumentOrderCommRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQrySecAgentTradingAccount(PyObject *, CThostFtdcTradingAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQrySecAgentCheckMode(PyObject *, CThostFtdcSecAgentCheckModeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQrySecAgentTradeInfo(PyObject *, CThostFtdcSecAgentTradeInfoField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryOptionInstrTradeCost(PyObject *, CThostFtdcOptionInstrTradeCostField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryOptionInstrCommRate(PyObject *, CThostFtdcOptionInstrCommRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryExecOrder(PyObject *, CThostFtdcExecOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryForQuote(PyObject *, CThostFtdcForQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryQuote(PyObject *, CThostFtdcQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryOptionSelfClose(PyObject *, CThostFtdcOptionSelfCloseField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryInvestUnit(PyObject *, CThostFtdcInvestUnitField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryCombInstrumentGuard(PyObject *, CThostFtdcCombInstrumentGuardField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryCombAction(PyObject *, CThostFtdcCombActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryTransferSerial(PyObject *, CThostFtdcTransferSerialField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryAccountregister(PyObject *, CThostFtdcAccountregisterField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRtnOrder(PyObject *, CThostFtdcOrderField *);
static inline int TraderSpi__OnRtnTrade(PyObject *, CThostFtdcTradeField *);
static inline int TraderSpi__OnErrRtnOrderInsert(PyObject *, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnErrRtnOrderAction(PyObject *, CThostFtdcOrderActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnRtnInstrumentStatus(PyObject *, CThostFtdcInstrumentStatusField *);
static inline int TraderSpi__OnRtnBulletin(PyObject *, CThostFtdcBulletinField *);
static inline int TraderSpi__OnRtnTradingNotice(PyObject *, CThostFtdcTradingNoticeInfoField *);
static inline int TraderSpi__OnRtnErrorConditionalOrder(PyObject *, CThostFtdcErrorConditionalOrderField *);
static inline int TraderSpi__OnRtnExecOrder(PyObject *, CThostFtdcExecOrderField *);
static inline int TraderSpi__OnErrRtnExecOrderInsert(PyObject *, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnErrRtnExecOrderAction(PyObject *, CThostFtdcExecOrderActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnErrRtnForQuoteInsert(PyObject *, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnRtnQuote(PyObject *, CThostFtdcQuoteField *);
static inline int TraderSpi__OnErrRtnQuoteInsert(PyObject *, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnErrRtnQuoteAction(PyObject *, CThostFtdcQuoteActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnRtnForQuoteRsp(PyObject *, CThostFtdcForQuoteRspField *);
static inline int TraderSpi__OnRtnCFMMCTradingAccountToken(PyObject *, CThostFtdcCFMMCTradingAccountTokenField *);
static inline int TraderSpi__OnErrRtnBatchOrderAction(PyObject *, CThostFtdcBatchOrderActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnRtnOptionSelfClose(PyObject *, CThostFtdcOptionSelfCloseField *);
static inline int TraderSpi__OnErrRtnOptionSelfCloseInsert(PyObject *, CThostFtdcInputOptionSelfCloseField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnErrRtnOptionSelfCloseAction(PyObject *, CThostFtdcOptionSelfCloseActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnRtnCombAction(PyObject *, CThostFtdcCombActionField *);
static inline int TraderSpi__OnErrRtnCombActionInsert(PyObject *, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnRspQryContractBank(PyObject *, CThostFtdcContractBankField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryParkedOrder(PyObject *, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryParkedOrderAction(PyObject *, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryTradingNotice(PyObject *, CThostFtdcTradingNoticeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryBrokerTradingParams(PyObject *, CThostFtdcBrokerTradingParamsField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryBrokerTradingAlgos(PyObject *, CThostFtdcBrokerTradingAlgosField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQueryCFMMCTradingAccountToken(PyObject *, CThostFtdcQueryCFMMCTradingAccountTokenField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRtnFromBankToFutureByBank(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi__OnRtnFromFutureToBankByBank(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi__OnRtnRepealFromBankToFutureByBank(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi__OnRtnRepealFromFutureToBankByBank(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi__OnRtnFromBankToFutureByFuture(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi__OnRtnFromFutureToBankByFuture(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi__OnRtnRepealFromBankToFutureByFutureManual(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi__OnRtnRepealFromFutureToBankByFutureManual(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi__OnRtnQueryBankBalanceByFuture(PyObject *, CThostFtdcNotifyQueryAccountField *);
static inline int TraderSpi__OnErrRtnBankToFutureByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnErrRtnFutureToBankByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnErrRtnRepealBankToFutureByFutureManual(PyObject *, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnErrRtnRepealFutureToBankByFutureManual(PyObject *, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnErrRtnQueryBankBalanceByFuture(PyObject *, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *);
static inline int TraderSpi__OnRtnRepealFromBankToFutureByFuture(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi__OnRtnRepealFromFutureToBankByFuture(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi__OnRspFromBankToFutureByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspFromFutureToBankByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQueryBankAccountMoneyByFuture(PyObject *, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRtnOpenAccountByBank(PyObject *, CThostFtdcOpenAccountField *);
static inline int TraderSpi__OnRtnCancelAccountByBank(PyObject *, CThostFtdcCancelAccountField *);
static inline int TraderSpi__OnRtnChangeAccountByBank(PyObject *, CThostFtdcChangeAccountField *);
static inline int TraderSpi__OnRspQryClassifiedInstrument(PyObject *, CThostFtdcInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi__OnRspQryCombPromotionParam(PyObject *, CThostFtdcCombPromotionParamField *, CThostFtdcRspInfoField *, int, bool);


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

        virtual void OnHeartBeatWarning(int nTimeLapse) {
            PyGIL(TraderSpi__OnHeartBeatWarning(api, nTimeLapse));
        };

        virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspAuthenticate(api, pRspAuthenticateField, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspUserLogin(api, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspUserLogout(api, pUserLogout, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspUserPasswordUpdate(api, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspTradingAccountPasswordUpdate(api, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspUserAuthMethod(api, pRspUserAuthMethod, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspGenUserCaptcha(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspGenUserCaptcha(api, pRspGenUserCaptcha, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspGenUserText(api, pRspGenUserText, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspOrderInsert(api, pInputOrder, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspParkedOrderInsert(api, pParkedOrder, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspParkedOrderAction(api, pParkedOrderAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspOrderAction(api, pInputOrderAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryMaxOrderVolume(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryMaxOrderVolume(api, pQryMaxOrderVolume, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspSettlementInfoConfirm(api, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspRemoveParkedOrder(api, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspRemoveParkedOrderAction(api, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspExecOrderInsert(api, pInputExecOrder, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspExecOrderAction(api, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspForQuoteInsert(api, pInputForQuote, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQuoteInsert(api, pInputQuote, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQuoteAction(api, pInputQuoteAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspBatchOrderAction(api, pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspOptionSelfCloseInsert(api, pInputOptionSelfClose, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspOptionSelfCloseAction(api, pInputOptionSelfCloseAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspCombActionInsert(api, pInputCombAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryOrder(api, pOrder, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryTrade(api, pTrade, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInvestorPosition(api, pInvestorPosition, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryTradingAccount(api, pTradingAccount, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInvestor(api, pInvestor, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryTradingCode(api, pTradingCode, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInstrumentMarginRate(api, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInstrumentCommissionRate(api, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryExchange(api, pExchange, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryProduct(api, pProduct, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInstrument(api, pInstrument, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryDepthMarketData(api, pDepthMarketData, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQrySettlementInfo(api, pSettlementInfo, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryTransferBank(api, pTransferBank, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInvestorPositionDetail(api, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryNotice(api, pNotice, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQrySettlementInfoConfirm(api, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInvestorPositionCombineDetail(api, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryCFMMCTradingAccountKey(api, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryEWarrantOffset(api, pEWarrantOffset, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInvestorProductGroupMargin(api, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryExchangeMarginRate(api, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryExchangeMarginRateAdjust(api, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryExchangeRate(api, pExchangeRate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQrySecAgentACIDMap(api, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryProductExchRate(api, pProductExchRate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryProductGroup(api, pProductGroup, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryMMInstrumentCommissionRate(api, pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryMMOptionInstrCommRate(api, pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInstrumentOrderCommRate(api, pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQrySecAgentTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQrySecAgentTradingAccount(api, pTradingAccount, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQrySecAgentCheckMode(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQrySecAgentCheckMode(api, pSecAgentCheckMode, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQrySecAgentTradeInfo(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQrySecAgentTradeInfo(api, pSecAgentTradeInfo, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryOptionInstrTradeCost(api, pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryOptionInstrCommRate(api, pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryExecOrder(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryExecOrder(api, pExecOrder, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryForQuote(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryForQuote(api, pForQuote, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryQuote(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryQuote(api, pQuote, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryOptionSelfClose(api, pOptionSelfClose, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryInvestUnit(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryInvestUnit(api, pInvestUnit, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryCombInstrumentGuard(api, pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryCombAction(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryCombAction(api, pCombAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryTransferSerial(api, pTransferSerial, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryAccountregister(api, pAccountregister, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspError(api, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRtnOrder(CThostFtdcOrderField *pOrder) {
            PyGIL(TraderSpi__OnRtnOrder(api, pOrder));
        };

        virtual void OnRtnTrade(CThostFtdcTradeField *pTrade) {
            PyGIL(TraderSpi__OnRtnTrade(api, pTrade));
        };

        virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnOrderInsert(api, pInputOrder, pRspInfo));
        };

        virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnOrderAction(api, pOrderAction, pRspInfo));
        };

        virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {
            PyGIL(TraderSpi__OnRtnInstrumentStatus(api, pInstrumentStatus));
        };

        virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) {
            PyGIL(TraderSpi__OnRtnBulletin(api, pBulletin));
        };

        virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {
            PyGIL(TraderSpi__OnRtnTradingNotice(api, pTradingNoticeInfo));
        };

        virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) {
            PyGIL(TraderSpi__OnRtnErrorConditionalOrder(api, pErrorConditionalOrder));
        };

        virtual void OnRtnExecOrder(CThostFtdcExecOrderField *pExecOrder) {
            PyGIL(TraderSpi__OnRtnExecOrder(api, pExecOrder));
        };

        virtual void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnExecOrderInsert(api, pInputExecOrder, pRspInfo));
        };

        virtual void OnErrRtnExecOrderAction(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnExecOrderAction(api, pExecOrderAction, pRspInfo));
        };

        virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnForQuoteInsert(api, pInputForQuote, pRspInfo));
        };

        virtual void OnRtnQuote(CThostFtdcQuoteField *pQuote) {
            PyGIL(TraderSpi__OnRtnQuote(api, pQuote));
        };

        virtual void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnQuoteInsert(api, pInputQuote, pRspInfo));
        };

        virtual void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnQuoteAction(api, pQuoteAction, pRspInfo));
        };

        virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
            PyGIL(TraderSpi__OnRtnForQuoteRsp(api, pForQuoteRsp));
        };

        virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {
            PyGIL(TraderSpi__OnRtnCFMMCTradingAccountToken(api, pCFMMCTradingAccountToken));
        };

        virtual void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnBatchOrderAction(api, pBatchOrderAction, pRspInfo));
        };

        virtual void OnRtnOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose) {
            PyGIL(TraderSpi__OnRtnOptionSelfClose(api, pOptionSelfClose));
        };

        virtual void OnErrRtnOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnOptionSelfCloseInsert(api, pInputOptionSelfClose, pRspInfo));
        };

        virtual void OnErrRtnOptionSelfCloseAction(CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnOptionSelfCloseAction(api, pOptionSelfCloseAction, pRspInfo));
        };

        virtual void OnRtnCombAction(CThostFtdcCombActionField *pCombAction) {
            PyGIL(TraderSpi__OnRtnCombAction(api, pCombAction));
        };

        virtual void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnCombActionInsert(api, pInputCombAction, pRspInfo));
        };

        virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryContractBank(api, pContractBank, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryParkedOrder(api, pParkedOrder, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryParkedOrderAction(api, pParkedOrderAction, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryTradingNotice(api, pTradingNotice, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryBrokerTradingParams(api, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryBrokerTradingAlgos(api, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQueryCFMMCTradingAccountToken(api, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer) {
            PyGIL(TraderSpi__OnRtnFromBankToFutureByBank(api, pRspTransfer));
        };

        virtual void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer) {
            PyGIL(TraderSpi__OnRtnFromFutureToBankByBank(api, pRspTransfer));
        };

        virtual void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal) {
            PyGIL(TraderSpi__OnRtnRepealFromBankToFutureByBank(api, pRspRepeal));
        };

        virtual void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal) {
            PyGIL(TraderSpi__OnRtnRepealFromFutureToBankByBank(api, pRspRepeal));
        };

        virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer) {
            PyGIL(TraderSpi__OnRtnFromBankToFutureByFuture(api, pRspTransfer));
        };

        virtual void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer) {
            PyGIL(TraderSpi__OnRtnFromFutureToBankByFuture(api, pRspTransfer));
        };

        virtual void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
            PyGIL(TraderSpi__OnRtnRepealFromBankToFutureByFutureManual(api, pRspRepeal));
        };

        virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
            PyGIL(TraderSpi__OnRtnRepealFromFutureToBankByFutureManual(api, pRspRepeal));
        };

        virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) {
            PyGIL(TraderSpi__OnRtnQueryBankBalanceByFuture(api, pNotifyQueryAccount));
        };

        virtual void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnBankToFutureByFuture(api, pReqTransfer, pRspInfo));
        };

        virtual void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnFutureToBankByFuture(api, pReqTransfer, pRspInfo));
        };

        virtual void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnRepealBankToFutureByFutureManual(api, pReqRepeal, pRspInfo));
        };

        virtual void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnRepealFutureToBankByFutureManual(api, pReqRepeal, pRspInfo));
        };

        virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo) {
            PyGIL(TraderSpi__OnErrRtnQueryBankBalanceByFuture(api, pReqQueryAccount, pRspInfo));
        };

        virtual void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal) {
            PyGIL(TraderSpi__OnRtnRepealFromBankToFutureByFuture(api, pRspRepeal));
        };

        virtual void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal) {
            PyGIL(TraderSpi__OnRtnRepealFromFutureToBankByFuture(api, pRspRepeal));
        };

        virtual void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspFromBankToFutureByFuture(api, pReqTransfer, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspFromFutureToBankByFuture(api, pReqTransfer, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQueryBankAccountMoneyByFuture(api, pReqQueryAccount, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) {
            PyGIL(TraderSpi__OnRtnOpenAccountByBank(api, pOpenAccount));
        };

        virtual void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount) {
            PyGIL(TraderSpi__OnRtnCancelAccountByBank(api, pCancelAccount));
        };

        virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount) {
            PyGIL(TraderSpi__OnRtnChangeAccountByBank(api, pChangeAccount));
        };

        virtual void OnRspQryClassifiedInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryClassifiedInstrument(api, pInstrument, pRspInfo, nRequestID, bIsLast));
        };

        virtual void OnRspQryCombPromotionParam(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
            PyGIL(TraderSpi__OnRspQryCombPromotionParam(api, pCombPromotionParam, pRspInfo, nRequestID, bIsLast));
        };

    private:
        PyObject *api;
};
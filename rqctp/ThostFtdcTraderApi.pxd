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

from .ThostFtdcUserApiStruct cimport *


cdef extern from "ThostFtdcTraderApi.h":
    cdef cppclass CTraderApi "CThostFtdcTraderApi":
        void Release() nogil
        void Init() nogil
        int Join() nogil
        void RegisterSpi(CTraderSpi *pSpi) nogil except +
        void SubscribePrivateTopic(THOST_TE_RESUME_TYPE nResumeType) nogil except +
        void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) nogil except +
        void RegisterFront(char *pszFrontAddress) nogil except +
        void RegisterNameServer(char *pszNsAddress) nogil except +
        void RegisterFensUserInfo(CThostFtdcFensUserInfoField *pFensUserInfo) nogil except +
        int ReqAuthenticate(CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID) nogil except +
        int RegisterUserSystemInfo(CThostFtdcUserSystemInfoField *pUserSystemInfo) nogil except +
        int SubmitUserSystemInfo(CThostFtdcUserSystemInfoField *pUserSystemInfo) nogil except +
        int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) nogil except +
        int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) nogil except +
        int ReqUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) nogil except +
        int ReqTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID) nogil except +
        int ReqUserAuthMethod(CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID) nogil except +
        int ReqGenUserCaptcha(CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID) nogil except +
        int ReqGenUserText(CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID) nogil except +
        int ReqUserLoginWithCaptcha(CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID) nogil except +
        int ReqUserLoginWithText(CThostFtdcReqUserLoginWithTextField *pReqUserLoginWithText, int nRequestID) nogil except +
        int ReqUserLoginWithOTP(CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID) nogil except +
        int ReqOrderInsert(CThostFtdcInputOrderField *pInputOrder, int nRequestID) nogil except +
        int ReqParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, int nRequestID) nogil except +
        int ReqParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID) nogil except +
        int ReqOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID) nogil except +
        int ReqQryMaxOrderVolume(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, int nRequestID) nogil except +
        int ReqSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID) nogil except +
        int ReqRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID) nogil except +
        int ReqRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID) nogil except +
        int ReqExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID) nogil except +
        int ReqExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID) nogil except +
        int ReqForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID) nogil except +
        int ReqQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, int nRequestID) nogil except +
        int ReqQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID) nogil except +
        int ReqBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID) nogil except +
        int ReqOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, int nRequestID) nogil except +
        int ReqOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, int nRequestID) nogil except +
        int ReqCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, int nRequestID) nogil except +
        int ReqQryOrder(CThostFtdcQryOrderField *pQryOrder, int nRequestID) nogil except +
        int ReqQryTrade(CThostFtdcQryTradeField *pQryTrade, int nRequestID) nogil except +
        int ReqQryInvestorPosition(CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID) nogil except +
        int ReqQryTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) nogil except +
        int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) nogil except +
        int ReqQryTradingCode(CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID) nogil except +
        int ReqQryInstrumentMarginRate(CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID) nogil except +
        int ReqQryInstrumentCommissionRate(CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID) nogil except +
        int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) nogil except +
        int ReqQryProduct(CThostFtdcQryProductField *pQryProduct, int nRequestID) nogil except +
        int ReqQryInstrument(CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID) nogil except +
        int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) nogil except +
        int ReqQrySettlementInfo(CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID) nogil except +
        int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) nogil except +
        int ReqQryInvestorPositionDetail(CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID) nogil except +
        int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) nogil except +
        int ReqQrySettlementInfoConfirm(CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID) nogil except +
        int ReqQryInvestorPositionCombineDetail(CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID) nogil except +
        int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID) nogil except +
        int ReqQryEWarrantOffset(CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID) nogil except +
        int ReqQryInvestorProductGroupMargin(CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID) nogil except +
        int ReqQryExchangeMarginRate(CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID) nogil except +
        int ReqQryExchangeMarginRateAdjust(CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID) nogil except +
        int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) nogil except +
        int ReqQrySecAgentACIDMap(CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID) nogil except +
        int ReqQryProductExchRate(CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID) nogil except +
        int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) nogil except +
        int ReqQryMMInstrumentCommissionRate(CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID) nogil except +
        int ReqQryMMOptionInstrCommRate(CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID) nogil except +
        int ReqQryInstrumentOrderCommRate(CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID) nogil except +
        int ReqQrySecAgentTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) nogil except +
        int ReqQrySecAgentCheckMode(CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID) nogil except +
        int ReqQrySecAgentTradeInfo(CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID) nogil except +
        int ReqQryOptionInstrTradeCost(CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID) nogil except +
        int ReqQryOptionInstrCommRate(CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID) nogil except +
        int ReqQryExecOrder(CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID) nogil except +
        int ReqQryForQuote(CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID) nogil except +
        int ReqQryQuote(CThostFtdcQryQuoteField *pQryQuote, int nRequestID) nogil except +
        int ReqQryOptionSelfClose(CThostFtdcQryOptionSelfCloseField *pQryOptionSelfClose, int nRequestID) nogil except +
        int ReqQryInvestUnit(CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID) nogil except +
        int ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) nogil except +
        int ReqQryCombAction(CThostFtdcQryCombActionField *pQryCombAction, int nRequestID) nogil except +
        int ReqQryTransferSerial(CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID) nogil except +
        int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) nogil except +
        int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) nogil except +
        int ReqQryParkedOrder(CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID) nogil except +
        int ReqQryParkedOrderAction(CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID) nogil except +
        int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) nogil except +
        int ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) nogil except +
        int ReqQryBrokerTradingAlgos(CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID) nogil except +
        int ReqQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID) nogil except +
        int ReqFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) nogil except +
        int ReqFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) nogil except +
        int ReqQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID) nogil except +
        int ReqQryClassifiedInstrument(CThostFtdcQryClassifiedInstrumentField *pQryClassifiedInstrument, int nRequestID) nogil except +
        int ReqQryCombPromotionParam(CThostFtdcQryCombPromotionParamField *pQryCombPromotionParam, int nRequestID) nogil except +


cdef extern from "ThostFtdcTraderApi.h" namespace "CThostFtdcTraderApi":
    CTraderApi *CreateFtdcTraderApi(const_char *pszFlowPath) nogil except +
    const_char *GetApiVersion() nogil


cdef extern from "CTraderSpi.h":
    cdef cppclass CTraderSpi:
        CTraderSpi(PyObject *obj)
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

from .ThostFtdcTraderApi cimport CTraderApi, CTraderSpi, CreateFtdcTraderApi
from .ThostFtdcUserApiStruct cimport *

import ctypes

from .structs import *


cdef class TraderApi:
    cdef CTraderApi *_api
    cdef CTraderSpi *_spi

    def __cinit__(self):
        self._api = NULL
        self._spi = NULL

    def __init__(self, const_char *pszFlowPath):
        self._api = CreateFtdcTraderApi(pszFlowPath)
        if self._api is NULL:
            raise MemoryError()
        self._spi = new CTraderSpi(<PyObject *>self)
        if self._spi is NULL:
            raise MemoryError()
        self._api.RegisterSpi(self._spi)

    def __dealloc__(self):
        if self._api is not NULL:
            self._api.RegisterSpi(NULL)
            self._api.Release()
            self._api = NULL
            self._spi = NULL

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

    def SubscribePrivateTopic(self, THOST_TE_RESUME_TYPE nResumeType):
        self._ensure_api_not_null()
        self._api.SubscribePrivateTopic(nResumeType)

    def SubscribePublicTopic(self, THOST_TE_RESUME_TYPE nResumeType):
        self._ensure_api_not_null()
        self._api.SubscribePublicTopic(nResumeType)

    def RegisterFront(self, char *pszFrontAddress):

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            self._api.RegisterFront(pszFrontAddress)
        return

    def RegisterNameServer(self, char *pszNsAddress):

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            self._api.RegisterNameServer(pszNsAddress)
        return

    def RegisterFensUserInfo(self, pFensUserInfo):
        cdef size_t address_pFensUserInfo = ctypes.addressof(pFensUserInfo)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            self._api.RegisterFensUserInfo(<CThostFtdcFensUserInfoField *> address_pFensUserInfo)
        return

    def ReqAuthenticate(self, pReqAuthenticateField, int nRequestID):
        cdef int result
        cdef size_t address_pReqAuthenticateField = ctypes.addressof(pReqAuthenticateField)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqAuthenticate(<CThostFtdcReqAuthenticateField *> address_pReqAuthenticateField, nRequestID)
        return result

    def RegisterUserSystemInfo(self, pUserSystemInfo):
        cdef int result
        cdef size_t address_pUserSystemInfo = ctypes.addressof(pUserSystemInfo)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.RegisterUserSystemInfo(<CThostFtdcUserSystemInfoField *> address_pUserSystemInfo)
        return result

    def SubmitUserSystemInfo(self, pUserSystemInfo):
        cdef int result
        cdef size_t address_pUserSystemInfo = ctypes.addressof(pUserSystemInfo)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.SubmitUserSystemInfo(<CThostFtdcUserSystemInfoField *> address_pUserSystemInfo)
        return result

    def ReqUserLogin(self, pReqUserLoginField, int nRequestID):
        cdef int result
        cdef size_t address_pReqUserLoginField = ctypes.addressof(pReqUserLoginField)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqUserLogin(<CThostFtdcReqUserLoginField *> address_pReqUserLoginField, nRequestID)
        return result

    def ReqUserLogout(self, pUserLogout, int nRequestID):
        cdef int result
        cdef size_t address_pUserLogout = ctypes.addressof(pUserLogout)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqUserLogout(<CThostFtdcUserLogoutField *> address_pUserLogout, nRequestID)
        return result

    def ReqUserPasswordUpdate(self, pUserPasswordUpdate, int nRequestID):
        cdef int result
        cdef size_t address_pUserPasswordUpdate = ctypes.addressof(pUserPasswordUpdate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqUserPasswordUpdate(<CThostFtdcUserPasswordUpdateField *> address_pUserPasswordUpdate, nRequestID)
        return result

    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, int nRequestID):
        cdef int result
        cdef size_t address_pTradingAccountPasswordUpdate = ctypes.addressof(pTradingAccountPasswordUpdate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqTradingAccountPasswordUpdate(<CThostFtdcTradingAccountPasswordUpdateField *> address_pTradingAccountPasswordUpdate, nRequestID)
        return result

    def ReqUserAuthMethod(self, pReqUserAuthMethod, int nRequestID):
        cdef int result
        cdef size_t address_pReqUserAuthMethod = ctypes.addressof(pReqUserAuthMethod)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqUserAuthMethod(<CThostFtdcReqUserAuthMethodField *> address_pReqUserAuthMethod, nRequestID)
        return result

    def ReqGenUserCaptcha(self, pReqGenUserCaptcha, int nRequestID):
        cdef int result
        cdef size_t address_pReqGenUserCaptcha = ctypes.addressof(pReqGenUserCaptcha)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqGenUserCaptcha(<CThostFtdcReqGenUserCaptchaField *> address_pReqGenUserCaptcha, nRequestID)
        return result

    def ReqGenUserText(self, pReqGenUserText, int nRequestID):
        cdef int result
        cdef size_t address_pReqGenUserText = ctypes.addressof(pReqGenUserText)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqGenUserText(<CThostFtdcReqGenUserTextField *> address_pReqGenUserText, nRequestID)
        return result

    def ReqUserLoginWithCaptcha(self, pReqUserLoginWithCaptcha, int nRequestID):
        cdef int result
        cdef size_t address_pReqUserLoginWithCaptcha = ctypes.addressof(pReqUserLoginWithCaptcha)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqUserLoginWithCaptcha(<CThostFtdcReqUserLoginWithCaptchaField *> address_pReqUserLoginWithCaptcha, nRequestID)
        return result

    def ReqUserLoginWithText(self, pReqUserLoginWithText, int nRequestID):
        cdef int result
        cdef size_t address_pReqUserLoginWithText = ctypes.addressof(pReqUserLoginWithText)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqUserLoginWithText(<CThostFtdcReqUserLoginWithTextField *> address_pReqUserLoginWithText, nRequestID)
        return result

    def ReqUserLoginWithOTP(self, pReqUserLoginWithOTP, int nRequestID):
        cdef int result
        cdef size_t address_pReqUserLoginWithOTP = ctypes.addressof(pReqUserLoginWithOTP)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqUserLoginWithOTP(<CThostFtdcReqUserLoginWithOTPField *> address_pReqUserLoginWithOTP, nRequestID)
        return result

    def ReqOrderInsert(self, pInputOrder, int nRequestID):
        cdef int result
        cdef size_t address_pInputOrder = ctypes.addressof(pInputOrder)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqOrderInsert(<CThostFtdcInputOrderField *> address_pInputOrder, nRequestID)
        return result

    def ReqParkedOrderInsert(self, pParkedOrder, int nRequestID):
        cdef int result
        cdef size_t address_pParkedOrder = ctypes.addressof(pParkedOrder)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqParkedOrderInsert(<CThostFtdcParkedOrderField *> address_pParkedOrder, nRequestID)
        return result

    def ReqParkedOrderAction(self, pParkedOrderAction, int nRequestID):
        cdef int result
        cdef size_t address_pParkedOrderAction = ctypes.addressof(pParkedOrderAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqParkedOrderAction(<CThostFtdcParkedOrderActionField *> address_pParkedOrderAction, nRequestID)
        return result

    def ReqOrderAction(self, pInputOrderAction, int nRequestID):
        cdef int result
        cdef size_t address_pInputOrderAction = ctypes.addressof(pInputOrderAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqOrderAction(<CThostFtdcInputOrderActionField *> address_pInputOrderAction, nRequestID)
        return result

    def ReqQryMaxOrderVolume(self, pQryMaxOrderVolume, int nRequestID):
        cdef int result
        cdef size_t address_pQryMaxOrderVolume = ctypes.addressof(pQryMaxOrderVolume)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryMaxOrderVolume(<CThostFtdcQryMaxOrderVolumeField *> address_pQryMaxOrderVolume, nRequestID)
        return result

    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm, int nRequestID):
        cdef int result
        cdef size_t address_pSettlementInfoConfirm = ctypes.addressof(pSettlementInfoConfirm)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqSettlementInfoConfirm(<CThostFtdcSettlementInfoConfirmField *> address_pSettlementInfoConfirm, nRequestID)
        return result

    def ReqRemoveParkedOrder(self, pRemoveParkedOrder, int nRequestID):
        cdef int result
        cdef size_t address_pRemoveParkedOrder = ctypes.addressof(pRemoveParkedOrder)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqRemoveParkedOrder(<CThostFtdcRemoveParkedOrderField *> address_pRemoveParkedOrder, nRequestID)
        return result

    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction, int nRequestID):
        cdef int result
        cdef size_t address_pRemoveParkedOrderAction = ctypes.addressof(pRemoveParkedOrderAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqRemoveParkedOrderAction(<CThostFtdcRemoveParkedOrderActionField *> address_pRemoveParkedOrderAction, nRequestID)
        return result

    def ReqExecOrderInsert(self, pInputExecOrder, int nRequestID):
        cdef int result
        cdef size_t address_pInputExecOrder = ctypes.addressof(pInputExecOrder)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqExecOrderInsert(<CThostFtdcInputExecOrderField *> address_pInputExecOrder, nRequestID)
        return result

    def ReqExecOrderAction(self, pInputExecOrderAction, int nRequestID):
        cdef int result
        cdef size_t address_pInputExecOrderAction = ctypes.addressof(pInputExecOrderAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqExecOrderAction(<CThostFtdcInputExecOrderActionField *> address_pInputExecOrderAction, nRequestID)
        return result

    def ReqForQuoteInsert(self, pInputForQuote, int nRequestID):
        cdef int result
        cdef size_t address_pInputForQuote = ctypes.addressof(pInputForQuote)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqForQuoteInsert(<CThostFtdcInputForQuoteField *> address_pInputForQuote, nRequestID)
        return result

    def ReqQuoteInsert(self, pInputQuote, int nRequestID):
        cdef int result
        cdef size_t address_pInputQuote = ctypes.addressof(pInputQuote)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQuoteInsert(<CThostFtdcInputQuoteField *> address_pInputQuote, nRequestID)
        return result

    def ReqQuoteAction(self, pInputQuoteAction, int nRequestID):
        cdef int result
        cdef size_t address_pInputQuoteAction = ctypes.addressof(pInputQuoteAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQuoteAction(<CThostFtdcInputQuoteActionField *> address_pInputQuoteAction, nRequestID)
        return result

    def ReqBatchOrderAction(self, pInputBatchOrderAction, int nRequestID):
        cdef int result
        cdef size_t address_pInputBatchOrderAction = ctypes.addressof(pInputBatchOrderAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqBatchOrderAction(<CThostFtdcInputBatchOrderActionField *> address_pInputBatchOrderAction, nRequestID)
        return result

    def ReqOptionSelfCloseInsert(self, pInputOptionSelfClose, int nRequestID):
        cdef int result
        cdef size_t address_pInputOptionSelfClose = ctypes.addressof(pInputOptionSelfClose)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqOptionSelfCloseInsert(<CThostFtdcInputOptionSelfCloseField *> address_pInputOptionSelfClose, nRequestID)
        return result

    def ReqOptionSelfCloseAction(self, pInputOptionSelfCloseAction, int nRequestID):
        cdef int result
        cdef size_t address_pInputOptionSelfCloseAction = ctypes.addressof(pInputOptionSelfCloseAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqOptionSelfCloseAction(<CThostFtdcInputOptionSelfCloseActionField *> address_pInputOptionSelfCloseAction, nRequestID)
        return result

    def ReqCombActionInsert(self, pInputCombAction, int nRequestID):
        cdef int result
        cdef size_t address_pInputCombAction = ctypes.addressof(pInputCombAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqCombActionInsert(<CThostFtdcInputCombActionField *> address_pInputCombAction, nRequestID)
        return result

    def ReqQryOrder(self, pQryOrder, int nRequestID):
        cdef int result
        cdef size_t address_pQryOrder = ctypes.addressof(pQryOrder)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryOrder(<CThostFtdcQryOrderField *> address_pQryOrder, nRequestID)
        return result

    def ReqQryTrade(self, pQryTrade, int nRequestID):
        cdef int result
        cdef size_t address_pQryTrade = ctypes.addressof(pQryTrade)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryTrade(<CThostFtdcQryTradeField *> address_pQryTrade, nRequestID)
        return result

    def ReqQryInvestorPosition(self, pQryInvestorPosition, int nRequestID):
        cdef int result
        cdef size_t address_pQryInvestorPosition = ctypes.addressof(pQryInvestorPosition)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInvestorPosition(<CThostFtdcQryInvestorPositionField *> address_pQryInvestorPosition, nRequestID)
        return result

    def ReqQryTradingAccount(self, pQryTradingAccount, int nRequestID):
        cdef int result
        cdef size_t address_pQryTradingAccount = ctypes.addressof(pQryTradingAccount)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryTradingAccount(<CThostFtdcQryTradingAccountField *> address_pQryTradingAccount, nRequestID)
        return result

    def ReqQryInvestor(self, pQryInvestor, int nRequestID):
        cdef int result
        cdef size_t address_pQryInvestor = ctypes.addressof(pQryInvestor)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInvestor(<CThostFtdcQryInvestorField *> address_pQryInvestor, nRequestID)
        return result

    def ReqQryTradingCode(self, pQryTradingCode, int nRequestID):
        cdef int result
        cdef size_t address_pQryTradingCode = ctypes.addressof(pQryTradingCode)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryTradingCode(<CThostFtdcQryTradingCodeField *> address_pQryTradingCode, nRequestID)
        return result

    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate, int nRequestID):
        cdef int result
        cdef size_t address_pQryInstrumentMarginRate = ctypes.addressof(pQryInstrumentMarginRate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInstrumentMarginRate(<CThostFtdcQryInstrumentMarginRateField *> address_pQryInstrumentMarginRate, nRequestID)
        return result

    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate, int nRequestID):
        cdef int result
        cdef size_t address_pQryInstrumentCommissionRate = ctypes.addressof(pQryInstrumentCommissionRate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInstrumentCommissionRate(<CThostFtdcQryInstrumentCommissionRateField *> address_pQryInstrumentCommissionRate, nRequestID)
        return result

    def ReqQryExchange(self, pQryExchange, int nRequestID):
        cdef int result
        cdef size_t address_pQryExchange = ctypes.addressof(pQryExchange)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryExchange(<CThostFtdcQryExchangeField *> address_pQryExchange, nRequestID)
        return result

    def ReqQryProduct(self, pQryProduct, int nRequestID):
        cdef int result
        cdef size_t address_pQryProduct = ctypes.addressof(pQryProduct)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryProduct(<CThostFtdcQryProductField *> address_pQryProduct, nRequestID)
        return result

    def ReqQryInstrument(self, pQryInstrument, int nRequestID):
        cdef int result
        cdef size_t address_pQryInstrument = ctypes.addressof(pQryInstrument)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInstrument(<CThostFtdcQryInstrumentField *> address_pQryInstrument, nRequestID)
        return result

    def ReqQryDepthMarketData(self, pQryDepthMarketData, int nRequestID):
        cdef int result
        cdef size_t address_pQryDepthMarketData = ctypes.addressof(pQryDepthMarketData)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryDepthMarketData(<CThostFtdcQryDepthMarketDataField *> address_pQryDepthMarketData, nRequestID)
        return result

    def ReqQrySettlementInfo(self, pQrySettlementInfo, int nRequestID):
        cdef int result
        cdef size_t address_pQrySettlementInfo = ctypes.addressof(pQrySettlementInfo)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQrySettlementInfo(<CThostFtdcQrySettlementInfoField *> address_pQrySettlementInfo, nRequestID)
        return result

    def ReqQryTransferBank(self, pQryTransferBank, int nRequestID):
        cdef int result
        cdef size_t address_pQryTransferBank = ctypes.addressof(pQryTransferBank)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryTransferBank(<CThostFtdcQryTransferBankField *> address_pQryTransferBank, nRequestID)
        return result

    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail, int nRequestID):
        cdef int result
        cdef size_t address_pQryInvestorPositionDetail = ctypes.addressof(pQryInvestorPositionDetail)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInvestorPositionDetail(<CThostFtdcQryInvestorPositionDetailField *> address_pQryInvestorPositionDetail, nRequestID)
        return result

    def ReqQryNotice(self, pQryNotice, int nRequestID):
        cdef int result
        cdef size_t address_pQryNotice = ctypes.addressof(pQryNotice)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryNotice(<CThostFtdcQryNoticeField *> address_pQryNotice, nRequestID)
        return result

    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm, int nRequestID):
        cdef int result
        cdef size_t address_pQrySettlementInfoConfirm = ctypes.addressof(pQrySettlementInfoConfirm)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQrySettlementInfoConfirm(<CThostFtdcQrySettlementInfoConfirmField *> address_pQrySettlementInfoConfirm, nRequestID)
        return result

    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail, int nRequestID):
        cdef int result
        cdef size_t address_pQryInvestorPositionCombineDetail = ctypes.addressof(pQryInvestorPositionCombineDetail)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInvestorPositionCombineDetail(<CThostFtdcQryInvestorPositionCombineDetailField *> address_pQryInvestorPositionCombineDetail, nRequestID)
        return result

    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey, int nRequestID):
        cdef int result
        cdef size_t address_pQryCFMMCTradingAccountKey = ctypes.addressof(pQryCFMMCTradingAccountKey)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryCFMMCTradingAccountKey(<CThostFtdcQryCFMMCTradingAccountKeyField *> address_pQryCFMMCTradingAccountKey, nRequestID)
        return result

    def ReqQryEWarrantOffset(self, pQryEWarrantOffset, int nRequestID):
        cdef int result
        cdef size_t address_pQryEWarrantOffset = ctypes.addressof(pQryEWarrantOffset)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryEWarrantOffset(<CThostFtdcQryEWarrantOffsetField *> address_pQryEWarrantOffset, nRequestID)
        return result

    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin, int nRequestID):
        cdef int result
        cdef size_t address_pQryInvestorProductGroupMargin = ctypes.addressof(pQryInvestorProductGroupMargin)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInvestorProductGroupMargin(<CThostFtdcQryInvestorProductGroupMarginField *> address_pQryInvestorProductGroupMargin, nRequestID)
        return result

    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate, int nRequestID):
        cdef int result
        cdef size_t address_pQryExchangeMarginRate = ctypes.addressof(pQryExchangeMarginRate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryExchangeMarginRate(<CThostFtdcQryExchangeMarginRateField *> address_pQryExchangeMarginRate, nRequestID)
        return result

    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust, int nRequestID):
        cdef int result
        cdef size_t address_pQryExchangeMarginRateAdjust = ctypes.addressof(pQryExchangeMarginRateAdjust)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryExchangeMarginRateAdjust(<CThostFtdcQryExchangeMarginRateAdjustField *> address_pQryExchangeMarginRateAdjust, nRequestID)
        return result

    def ReqQryExchangeRate(self, pQryExchangeRate, int nRequestID):
        cdef int result
        cdef size_t address_pQryExchangeRate = ctypes.addressof(pQryExchangeRate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryExchangeRate(<CThostFtdcQryExchangeRateField *> address_pQryExchangeRate, nRequestID)
        return result

    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap, int nRequestID):
        cdef int result
        cdef size_t address_pQrySecAgentACIDMap = ctypes.addressof(pQrySecAgentACIDMap)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQrySecAgentACIDMap(<CThostFtdcQrySecAgentACIDMapField *> address_pQrySecAgentACIDMap, nRequestID)
        return result

    def ReqQryProductExchRate(self, pQryProductExchRate, int nRequestID):
        cdef int result
        cdef size_t address_pQryProductExchRate = ctypes.addressof(pQryProductExchRate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryProductExchRate(<CThostFtdcQryProductExchRateField *> address_pQryProductExchRate, nRequestID)
        return result

    def ReqQryProductGroup(self, pQryProductGroup, int nRequestID):
        cdef int result
        cdef size_t address_pQryProductGroup = ctypes.addressof(pQryProductGroup)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryProductGroup(<CThostFtdcQryProductGroupField *> address_pQryProductGroup, nRequestID)
        return result

    def ReqQryMMInstrumentCommissionRate(self, pQryMMInstrumentCommissionRate, int nRequestID):
        cdef int result
        cdef size_t address_pQryMMInstrumentCommissionRate = ctypes.addressof(pQryMMInstrumentCommissionRate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryMMInstrumentCommissionRate(<CThostFtdcQryMMInstrumentCommissionRateField *> address_pQryMMInstrumentCommissionRate, nRequestID)
        return result

    def ReqQryMMOptionInstrCommRate(self, pQryMMOptionInstrCommRate, int nRequestID):
        cdef int result
        cdef size_t address_pQryMMOptionInstrCommRate = ctypes.addressof(pQryMMOptionInstrCommRate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryMMOptionInstrCommRate(<CThostFtdcQryMMOptionInstrCommRateField *> address_pQryMMOptionInstrCommRate, nRequestID)
        return result

    def ReqQryInstrumentOrderCommRate(self, pQryInstrumentOrderCommRate, int nRequestID):
        cdef int result
        cdef size_t address_pQryInstrumentOrderCommRate = ctypes.addressof(pQryInstrumentOrderCommRate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInstrumentOrderCommRate(<CThostFtdcQryInstrumentOrderCommRateField *> address_pQryInstrumentOrderCommRate, nRequestID)
        return result

    def ReqQrySecAgentTradingAccount(self, pQryTradingAccount, int nRequestID):
        cdef int result
        cdef size_t address_pQryTradingAccount = ctypes.addressof(pQryTradingAccount)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQrySecAgentTradingAccount(<CThostFtdcQryTradingAccountField *> address_pQryTradingAccount, nRequestID)
        return result

    def ReqQrySecAgentCheckMode(self, pQrySecAgentCheckMode, int nRequestID):
        cdef int result
        cdef size_t address_pQrySecAgentCheckMode = ctypes.addressof(pQrySecAgentCheckMode)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQrySecAgentCheckMode(<CThostFtdcQrySecAgentCheckModeField *> address_pQrySecAgentCheckMode, nRequestID)
        return result

    def ReqQrySecAgentTradeInfo(self, pQrySecAgentTradeInfo, int nRequestID):
        cdef int result
        cdef size_t address_pQrySecAgentTradeInfo = ctypes.addressof(pQrySecAgentTradeInfo)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQrySecAgentTradeInfo(<CThostFtdcQrySecAgentTradeInfoField *> address_pQrySecAgentTradeInfo, nRequestID)
        return result

    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost, int nRequestID):
        cdef int result
        cdef size_t address_pQryOptionInstrTradeCost = ctypes.addressof(pQryOptionInstrTradeCost)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryOptionInstrTradeCost(<CThostFtdcQryOptionInstrTradeCostField *> address_pQryOptionInstrTradeCost, nRequestID)
        return result

    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate, int nRequestID):
        cdef int result
        cdef size_t address_pQryOptionInstrCommRate = ctypes.addressof(pQryOptionInstrCommRate)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryOptionInstrCommRate(<CThostFtdcQryOptionInstrCommRateField *> address_pQryOptionInstrCommRate, nRequestID)
        return result

    def ReqQryExecOrder(self, pQryExecOrder, int nRequestID):
        cdef int result
        cdef size_t address_pQryExecOrder = ctypes.addressof(pQryExecOrder)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryExecOrder(<CThostFtdcQryExecOrderField *> address_pQryExecOrder, nRequestID)
        return result

    def ReqQryForQuote(self, pQryForQuote, int nRequestID):
        cdef int result
        cdef size_t address_pQryForQuote = ctypes.addressof(pQryForQuote)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryForQuote(<CThostFtdcQryForQuoteField *> address_pQryForQuote, nRequestID)
        return result

    def ReqQryQuote(self, pQryQuote, int nRequestID):
        cdef int result
        cdef size_t address_pQryQuote = ctypes.addressof(pQryQuote)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryQuote(<CThostFtdcQryQuoteField *> address_pQryQuote, nRequestID)
        return result

    def ReqQryOptionSelfClose(self, pQryOptionSelfClose, int nRequestID):
        cdef int result
        cdef size_t address_pQryOptionSelfClose = ctypes.addressof(pQryOptionSelfClose)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryOptionSelfClose(<CThostFtdcQryOptionSelfCloseField *> address_pQryOptionSelfClose, nRequestID)
        return result

    def ReqQryInvestUnit(self, pQryInvestUnit, int nRequestID):
        cdef int result
        cdef size_t address_pQryInvestUnit = ctypes.addressof(pQryInvestUnit)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryInvestUnit(<CThostFtdcQryInvestUnitField *> address_pQryInvestUnit, nRequestID)
        return result

    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard, int nRequestID):
        cdef int result
        cdef size_t address_pQryCombInstrumentGuard = ctypes.addressof(pQryCombInstrumentGuard)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryCombInstrumentGuard(<CThostFtdcQryCombInstrumentGuardField *> address_pQryCombInstrumentGuard, nRequestID)
        return result

    def ReqQryCombAction(self, pQryCombAction, int nRequestID):
        cdef int result
        cdef size_t address_pQryCombAction = ctypes.addressof(pQryCombAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryCombAction(<CThostFtdcQryCombActionField *> address_pQryCombAction, nRequestID)
        return result

    def ReqQryTransferSerial(self, pQryTransferSerial, int nRequestID):
        cdef int result
        cdef size_t address_pQryTransferSerial = ctypes.addressof(pQryTransferSerial)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryTransferSerial(<CThostFtdcQryTransferSerialField *> address_pQryTransferSerial, nRequestID)
        return result

    def ReqQryAccountregister(self, pQryAccountregister, int nRequestID):
        cdef int result
        cdef size_t address_pQryAccountregister = ctypes.addressof(pQryAccountregister)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryAccountregister(<CThostFtdcQryAccountregisterField *> address_pQryAccountregister, nRequestID)
        return result

    def ReqQryContractBank(self, pQryContractBank, int nRequestID):
        cdef int result
        cdef size_t address_pQryContractBank = ctypes.addressof(pQryContractBank)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryContractBank(<CThostFtdcQryContractBankField *> address_pQryContractBank, nRequestID)
        return result

    def ReqQryParkedOrder(self, pQryParkedOrder, int nRequestID):
        cdef int result
        cdef size_t address_pQryParkedOrder = ctypes.addressof(pQryParkedOrder)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryParkedOrder(<CThostFtdcQryParkedOrderField *> address_pQryParkedOrder, nRequestID)
        return result

    def ReqQryParkedOrderAction(self, pQryParkedOrderAction, int nRequestID):
        cdef int result
        cdef size_t address_pQryParkedOrderAction = ctypes.addressof(pQryParkedOrderAction)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryParkedOrderAction(<CThostFtdcQryParkedOrderActionField *> address_pQryParkedOrderAction, nRequestID)
        return result

    def ReqQryTradingNotice(self, pQryTradingNotice, int nRequestID):
        cdef int result
        cdef size_t address_pQryTradingNotice = ctypes.addressof(pQryTradingNotice)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryTradingNotice(<CThostFtdcQryTradingNoticeField *> address_pQryTradingNotice, nRequestID)
        return result

    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams, int nRequestID):
        cdef int result
        cdef size_t address_pQryBrokerTradingParams = ctypes.addressof(pQryBrokerTradingParams)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryBrokerTradingParams(<CThostFtdcQryBrokerTradingParamsField *> address_pQryBrokerTradingParams, nRequestID)
        return result

    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos, int nRequestID):
        cdef int result
        cdef size_t address_pQryBrokerTradingAlgos = ctypes.addressof(pQryBrokerTradingAlgos)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryBrokerTradingAlgos(<CThostFtdcQryBrokerTradingAlgosField *> address_pQryBrokerTradingAlgos, nRequestID)
        return result

    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, int nRequestID):
        cdef int result
        cdef size_t address_pQueryCFMMCTradingAccountToken = ctypes.addressof(pQueryCFMMCTradingAccountToken)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQueryCFMMCTradingAccountToken(<CThostFtdcQueryCFMMCTradingAccountTokenField *> address_pQueryCFMMCTradingAccountToken, nRequestID)
        return result

    def ReqFromBankToFutureByFuture(self, pReqTransfer, int nRequestID):
        cdef int result
        cdef size_t address_pReqTransfer = ctypes.addressof(pReqTransfer)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqFromBankToFutureByFuture(<CThostFtdcReqTransferField *> address_pReqTransfer, nRequestID)
        return result

    def ReqFromFutureToBankByFuture(self, pReqTransfer, int nRequestID):
        cdef int result
        cdef size_t address_pReqTransfer = ctypes.addressof(pReqTransfer)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqFromFutureToBankByFuture(<CThostFtdcReqTransferField *> address_pReqTransfer, nRequestID)
        return result

    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount, int nRequestID):
        cdef int result
        cdef size_t address_pReqQueryAccount = ctypes.addressof(pReqQueryAccount)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQueryBankAccountMoneyByFuture(<CThostFtdcReqQueryAccountField *> address_pReqQueryAccount, nRequestID)
        return result

    def ReqQryClassifiedInstrument(self, pQryClassifiedInstrument, int nRequestID):
        cdef int result
        cdef size_t address_pQryClassifiedInstrument = ctypes.addressof(pQryClassifiedInstrument)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryClassifiedInstrument(<CThostFtdcQryClassifiedInstrumentField *> address_pQryClassifiedInstrument, nRequestID)
        return result

    def ReqQryCombPromotionParam(self, pQryCombPromotionParam, int nRequestID):
        cdef int result
        cdef size_t address_pQryCombPromotionParam = ctypes.addressof(pQryCombPromotionParam)

        if self._api is NULL:
            raise MemoryError()
        with nogil:
            result = self._api.ReqQryCombPromotionParam(<CThostFtdcQryCombPromotionParamField *> address_pQryCombPromotionParam, nRequestID)
        return result


cdef extern int TraderSpi__OnFrontConnected(api) except -1:
    api.OnFrontConnected()
    return 0


cdef extern int TraderSpi__OnFrontDisconnected(api, int nReason) except -1:
    api.OnFrontDisconnected(
        nReason
    )
    return 0


cdef extern int TraderSpi__OnHeartBeatWarning(api, int nTimeLapse) except -1:
    api.OnHeartBeatWarning(
        nTimeLapse
    )
    return 0


cdef extern int TraderSpi__OnRspAuthenticate(api, CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspAuthenticate(
        None if pRspAuthenticateField is NULL else RspAuthenticate.from_address(<size_t> pRspAuthenticateField).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspUserLogin(api, CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUserLogin(
        None if pRspUserLogin is NULL else RspUserLogin.from_address(<size_t> pRspUserLogin).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspUserLogout(api, CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUserLogout(
        None if pUserLogout is NULL else UserLogout.from_address(<size_t> pUserLogout).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspUserPasswordUpdate(api, CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUserPasswordUpdate(
        None if pUserPasswordUpdate is NULL else UserPasswordUpdate.from_address(<size_t> pUserPasswordUpdate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspTradingAccountPasswordUpdate(api, CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspTradingAccountPasswordUpdate(
        None if pTradingAccountPasswordUpdate is NULL else TradingAccountPasswordUpdate.from_address(<size_t> pTradingAccountPasswordUpdate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspUserAuthMethod(api, CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspUserAuthMethod(
        None if pRspUserAuthMethod is NULL else RspUserAuthMethod.from_address(<size_t> pRspUserAuthMethod).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspGenUserCaptcha(api, CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspGenUserCaptcha(
        None if pRspGenUserCaptcha is NULL else RspGenUserCaptcha.from_address(<size_t> pRspGenUserCaptcha).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspGenUserText(api, CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspGenUserText(
        None if pRspGenUserText is NULL else RspGenUserText.from_address(<size_t> pRspGenUserText).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspOrderInsert(api, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspOrderInsert(
        None if pInputOrder is NULL else InputOrder.from_address(<size_t> pInputOrder).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspParkedOrderInsert(api, CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspParkedOrderInsert(
        None if pParkedOrder is NULL else ParkedOrder.from_address(<size_t> pParkedOrder).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspParkedOrderAction(api, CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspParkedOrderAction(
        None if pParkedOrderAction is NULL else ParkedOrderAction.from_address(<size_t> pParkedOrderAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspOrderAction(api, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspOrderAction(
        None if pInputOrderAction is NULL else InputOrderAction.from_address(<size_t> pInputOrderAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryMaxOrderVolume(api, CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryMaxOrderVolume(
        None if pQryMaxOrderVolume is NULL else QryMaxOrderVolume.from_address(<size_t> pQryMaxOrderVolume).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspSettlementInfoConfirm(api, CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspSettlementInfoConfirm(
        None if pSettlementInfoConfirm is NULL else SettlementInfoConfirm.from_address(<size_t> pSettlementInfoConfirm).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspRemoveParkedOrder(api, CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspRemoveParkedOrder(
        None if pRemoveParkedOrder is NULL else RemoveParkedOrder.from_address(<size_t> pRemoveParkedOrder).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspRemoveParkedOrderAction(api, CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspRemoveParkedOrderAction(
        None if pRemoveParkedOrderAction is NULL else RemoveParkedOrderAction.from_address(<size_t> pRemoveParkedOrderAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspExecOrderInsert(api, CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspExecOrderInsert(
        None if pInputExecOrder is NULL else InputExecOrder.from_address(<size_t> pInputExecOrder).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspExecOrderAction(api, CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspExecOrderAction(
        None if pInputExecOrderAction is NULL else InputExecOrderAction.from_address(<size_t> pInputExecOrderAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspForQuoteInsert(api, CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspForQuoteInsert(
        None if pInputForQuote is NULL else InputForQuote.from_address(<size_t> pInputForQuote).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQuoteInsert(api, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQuoteInsert(
        None if pInputQuote is NULL else InputQuote.from_address(<size_t> pInputQuote).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQuoteAction(api, CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQuoteAction(
        None if pInputQuoteAction is NULL else InputQuoteAction.from_address(<size_t> pInputQuoteAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspBatchOrderAction(api, CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspBatchOrderAction(
        None if pInputBatchOrderAction is NULL else InputBatchOrderAction.from_address(<size_t> pInputBatchOrderAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspOptionSelfCloseInsert(api, CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspOptionSelfCloseInsert(
        None if pInputOptionSelfClose is NULL else InputOptionSelfClose.from_address(<size_t> pInputOptionSelfClose).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspOptionSelfCloseAction(api, CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspOptionSelfCloseAction(
        None if pInputOptionSelfCloseAction is NULL else InputOptionSelfCloseAction.from_address(<size_t> pInputOptionSelfCloseAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspCombActionInsert(api, CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspCombActionInsert(
        None if pInputCombAction is NULL else InputCombAction.from_address(<size_t> pInputCombAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryOrder(api, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryOrder(
        None if pOrder is NULL else Order.from_address(<size_t> pOrder).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryTrade(api, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryTrade(
        None if pTrade is NULL else Trade.from_address(<size_t> pTrade).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInvestorPosition(api, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInvestorPosition(
        None if pInvestorPosition is NULL else InvestorPosition.from_address(<size_t> pInvestorPosition).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryTradingAccount(api, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryTradingAccount(
        None if pTradingAccount is NULL else TradingAccount.from_address(<size_t> pTradingAccount).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInvestor(api, CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInvestor(
        None if pInvestor is NULL else Investor.from_address(<size_t> pInvestor).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryTradingCode(api, CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryTradingCode(
        None if pTradingCode is NULL else TradingCode.from_address(<size_t> pTradingCode).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInstrumentMarginRate(api, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInstrumentMarginRate(
        None if pInstrumentMarginRate is NULL else InstrumentMarginRate.from_address(<size_t> pInstrumentMarginRate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInstrumentCommissionRate(api, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInstrumentCommissionRate(
        None if pInstrumentCommissionRate is NULL else InstrumentCommissionRate.from_address(<size_t> pInstrumentCommissionRate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryExchange(api, CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryExchange(
        None if pExchange is NULL else Exchange.from_address(<size_t> pExchange).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryProduct(api, CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryProduct(
        None if pProduct is NULL else Product.from_address(<size_t> pProduct).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInstrument(api, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInstrument(
        None if pInstrument is NULL else Instrument.from_address(<size_t> pInstrument).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryDepthMarketData(api, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryDepthMarketData(
        None if pDepthMarketData is NULL else DepthMarketData.from_address(<size_t> pDepthMarketData).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQrySettlementInfo(api, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQrySettlementInfo(
        None if pSettlementInfo is NULL else SettlementInfo.from_address(<size_t> pSettlementInfo).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryTransferBank(api, CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryTransferBank(
        None if pTransferBank is NULL else TransferBank.from_address(<size_t> pTransferBank).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInvestorPositionDetail(api, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInvestorPositionDetail(
        None if pInvestorPositionDetail is NULL else InvestorPositionDetail.from_address(<size_t> pInvestorPositionDetail).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryNotice(api, CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryNotice(
        None if pNotice is NULL else Notice.from_address(<size_t> pNotice).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQrySettlementInfoConfirm(api, CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQrySettlementInfoConfirm(
        None if pSettlementInfoConfirm is NULL else SettlementInfoConfirm.from_address(<size_t> pSettlementInfoConfirm).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInvestorPositionCombineDetail(api, CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInvestorPositionCombineDetail(
        None if pInvestorPositionCombineDetail is NULL else InvestorPositionCombineDetail.from_address(<size_t> pInvestorPositionCombineDetail).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryCFMMCTradingAccountKey(api, CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryCFMMCTradingAccountKey(
        None if pCFMMCTradingAccountKey is NULL else CFMMCTradingAccountKey.from_address(<size_t> pCFMMCTradingAccountKey).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryEWarrantOffset(api, CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryEWarrantOffset(
        None if pEWarrantOffset is NULL else EWarrantOffset.from_address(<size_t> pEWarrantOffset).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInvestorProductGroupMargin(api, CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInvestorProductGroupMargin(
        None if pInvestorProductGroupMargin is NULL else InvestorProductGroupMargin.from_address(<size_t> pInvestorProductGroupMargin).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryExchangeMarginRate(api, CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryExchangeMarginRate(
        None if pExchangeMarginRate is NULL else ExchangeMarginRate.from_address(<size_t> pExchangeMarginRate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryExchangeMarginRateAdjust(api, CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryExchangeMarginRateAdjust(
        None if pExchangeMarginRateAdjust is NULL else ExchangeMarginRateAdjust.from_address(<size_t> pExchangeMarginRateAdjust).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryExchangeRate(api, CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryExchangeRate(
        None if pExchangeRate is NULL else ExchangeRate.from_address(<size_t> pExchangeRate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQrySecAgentACIDMap(api, CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQrySecAgentACIDMap(
        None if pSecAgentACIDMap is NULL else SecAgentACIDMap.from_address(<size_t> pSecAgentACIDMap).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryProductExchRate(api, CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryProductExchRate(
        None if pProductExchRate is NULL else ProductExchRate.from_address(<size_t> pProductExchRate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryProductGroup(api, CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryProductGroup(
        None if pProductGroup is NULL else ProductGroup.from_address(<size_t> pProductGroup).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryMMInstrumentCommissionRate(api, CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryMMInstrumentCommissionRate(
        None if pMMInstrumentCommissionRate is NULL else MMInstrumentCommissionRate.from_address(<size_t> pMMInstrumentCommissionRate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryMMOptionInstrCommRate(api, CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryMMOptionInstrCommRate(
        None if pMMOptionInstrCommRate is NULL else MMOptionInstrCommRate.from_address(<size_t> pMMOptionInstrCommRate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInstrumentOrderCommRate(api, CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInstrumentOrderCommRate(
        None if pInstrumentOrderCommRate is NULL else InstrumentOrderCommRate.from_address(<size_t> pInstrumentOrderCommRate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQrySecAgentTradingAccount(api, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQrySecAgentTradingAccount(
        None if pTradingAccount is NULL else TradingAccount.from_address(<size_t> pTradingAccount).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQrySecAgentCheckMode(api, CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQrySecAgentCheckMode(
        None if pSecAgentCheckMode is NULL else SecAgentCheckMode.from_address(<size_t> pSecAgentCheckMode).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQrySecAgentTradeInfo(api, CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQrySecAgentTradeInfo(
        None if pSecAgentTradeInfo is NULL else SecAgentTradeInfo.from_address(<size_t> pSecAgentTradeInfo).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryOptionInstrTradeCost(api, CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryOptionInstrTradeCost(
        None if pOptionInstrTradeCost is NULL else OptionInstrTradeCost.from_address(<size_t> pOptionInstrTradeCost).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryOptionInstrCommRate(api, CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryOptionInstrCommRate(
        None if pOptionInstrCommRate is NULL else OptionInstrCommRate.from_address(<size_t> pOptionInstrCommRate).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryExecOrder(api, CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryExecOrder(
        None if pExecOrder is NULL else ExecOrder.from_address(<size_t> pExecOrder).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryForQuote(api, CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryForQuote(
        None if pForQuote is NULL else ForQuote.from_address(<size_t> pForQuote).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryQuote(api, CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryQuote(
        None if pQuote is NULL else Quote.from_address(<size_t> pQuote).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryOptionSelfClose(api, CThostFtdcOptionSelfCloseField *pOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryOptionSelfClose(
        None if pOptionSelfClose is NULL else OptionSelfClose.from_address(<size_t> pOptionSelfClose).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryInvestUnit(api, CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryInvestUnit(
        None if pInvestUnit is NULL else InvestUnit.from_address(<size_t> pInvestUnit).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryCombInstrumentGuard(api, CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryCombInstrumentGuard(
        None if pCombInstrumentGuard is NULL else CombInstrumentGuard.from_address(<size_t> pCombInstrumentGuard).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryCombAction(api, CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryCombAction(
        None if pCombAction is NULL else CombAction.from_address(<size_t> pCombAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryTransferSerial(api, CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryTransferSerial(
        None if pTransferSerial is NULL else TransferSerial.from_address(<size_t> pTransferSerial).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryAccountregister(api, CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryAccountregister(
        None if pAccountregister is NULL else Accountregister.from_address(<size_t> pAccountregister).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspError(api, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspError(
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRtnOrder(api, CThostFtdcOrderField *pOrder) except -1:
    api.OnRtnOrder(
        None if pOrder is NULL else Order.from_address(<size_t> pOrder).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnTrade(api, CThostFtdcTradeField *pTrade) except -1:
    api.OnRtnTrade(
        None if pTrade is NULL else Trade.from_address(<size_t> pTrade).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnOrderInsert(api, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnOrderInsert(
        None if pInputOrder is NULL else InputOrder.from_address(<size_t> pInputOrder).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnOrderAction(api, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnOrderAction(
        None if pOrderAction is NULL else OrderAction.from_address(<size_t> pOrderAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnInstrumentStatus(api, CThostFtdcInstrumentStatusField *pInstrumentStatus) except -1:
    api.OnRtnInstrumentStatus(
        None if pInstrumentStatus is NULL else InstrumentStatus.from_address(<size_t> pInstrumentStatus).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnBulletin(api, CThostFtdcBulletinField *pBulletin) except -1:
    api.OnRtnBulletin(
        None if pBulletin is NULL else Bulletin.from_address(<size_t> pBulletin).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnTradingNotice(api, CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) except -1:
    api.OnRtnTradingNotice(
        None if pTradingNoticeInfo is NULL else TradingNoticeInfo.from_address(<size_t> pTradingNoticeInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnErrorConditionalOrder(api, CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) except -1:
    api.OnRtnErrorConditionalOrder(
        None if pErrorConditionalOrder is NULL else ErrorConditionalOrder.from_address(<size_t> pErrorConditionalOrder).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnExecOrder(api, CThostFtdcExecOrderField *pExecOrder) except -1:
    api.OnRtnExecOrder(
        None if pExecOrder is NULL else ExecOrder.from_address(<size_t> pExecOrder).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnExecOrderInsert(api, CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnExecOrderInsert(
        None if pInputExecOrder is NULL else InputExecOrder.from_address(<size_t> pInputExecOrder).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnExecOrderAction(api, CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnExecOrderAction(
        None if pExecOrderAction is NULL else ExecOrderAction.from_address(<size_t> pExecOrderAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnForQuoteInsert(api, CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnForQuoteInsert(
        None if pInputForQuote is NULL else InputForQuote.from_address(<size_t> pInputForQuote).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnQuote(api, CThostFtdcQuoteField *pQuote) except -1:
    api.OnRtnQuote(
        None if pQuote is NULL else Quote.from_address(<size_t> pQuote).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnQuoteInsert(api, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnQuoteInsert(
        None if pInputQuote is NULL else InputQuote.from_address(<size_t> pInputQuote).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnQuoteAction(api, CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnQuoteAction(
        None if pQuoteAction is NULL else QuoteAction.from_address(<size_t> pQuoteAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnForQuoteRsp(api, CThostFtdcForQuoteRspField *pForQuoteRsp) except -1:
    api.OnRtnForQuoteRsp(
        None if pForQuoteRsp is NULL else ForQuoteRsp.from_address(<size_t> pForQuoteRsp).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnCFMMCTradingAccountToken(api, CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) except -1:
    api.OnRtnCFMMCTradingAccountToken(
        None if pCFMMCTradingAccountToken is NULL else CFMMCTradingAccountToken.from_address(<size_t> pCFMMCTradingAccountToken).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnBatchOrderAction(api, CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnBatchOrderAction(
        None if pBatchOrderAction is NULL else BatchOrderAction.from_address(<size_t> pBatchOrderAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnOptionSelfClose(api, CThostFtdcOptionSelfCloseField *pOptionSelfClose) except -1:
    api.OnRtnOptionSelfClose(
        None if pOptionSelfClose is NULL else OptionSelfClose.from_address(<size_t> pOptionSelfClose).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnOptionSelfCloseInsert(api, CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnOptionSelfCloseInsert(
        None if pInputOptionSelfClose is NULL else InputOptionSelfClose.from_address(<size_t> pInputOptionSelfClose).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnOptionSelfCloseAction(api, CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnOptionSelfCloseAction(
        None if pOptionSelfCloseAction is NULL else OptionSelfCloseAction.from_address(<size_t> pOptionSelfCloseAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnCombAction(api, CThostFtdcCombActionField *pCombAction) except -1:
    api.OnRtnCombAction(
        None if pCombAction is NULL else CombAction.from_address(<size_t> pCombAction).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnCombActionInsert(api, CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnCombActionInsert(
        None if pInputCombAction is NULL else InputCombAction.from_address(<size_t> pInputCombAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRspQryContractBank(api, CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryContractBank(
        None if pContractBank is NULL else ContractBank.from_address(<size_t> pContractBank).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryParkedOrder(api, CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryParkedOrder(
        None if pParkedOrder is NULL else ParkedOrder.from_address(<size_t> pParkedOrder).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryParkedOrderAction(api, CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryParkedOrderAction(
        None if pParkedOrderAction is NULL else ParkedOrderAction.from_address(<size_t> pParkedOrderAction).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryTradingNotice(api, CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryTradingNotice(
        None if pTradingNotice is NULL else TradingNotice.from_address(<size_t> pTradingNotice).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryBrokerTradingParams(api, CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryBrokerTradingParams(
        None if pBrokerTradingParams is NULL else BrokerTradingParams.from_address(<size_t> pBrokerTradingParams).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryBrokerTradingAlgos(api, CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryBrokerTradingAlgos(
        None if pBrokerTradingAlgos is NULL else BrokerTradingAlgos.from_address(<size_t> pBrokerTradingAlgos).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQueryCFMMCTradingAccountToken(api, CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQueryCFMMCTradingAccountToken(
        None if pQueryCFMMCTradingAccountToken is NULL else QueryCFMMCTradingAccountToken.from_address(<size_t> pQueryCFMMCTradingAccountToken).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRtnFromBankToFutureByBank(api, CThostFtdcRspTransferField *pRspTransfer) except -1:
    api.OnRtnFromBankToFutureByBank(
        None if pRspTransfer is NULL else RspTransfer.from_address(<size_t> pRspTransfer).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnFromFutureToBankByBank(api, CThostFtdcRspTransferField *pRspTransfer) except -1:
    api.OnRtnFromFutureToBankByBank(
        None if pRspTransfer is NULL else RspTransfer.from_address(<size_t> pRspTransfer).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnRepealFromBankToFutureByBank(api, CThostFtdcRspRepealField *pRspRepeal) except -1:
    api.OnRtnRepealFromBankToFutureByBank(
        None if pRspRepeal is NULL else RspRepeal.from_address(<size_t> pRspRepeal).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnRepealFromFutureToBankByBank(api, CThostFtdcRspRepealField *pRspRepeal) except -1:
    api.OnRtnRepealFromFutureToBankByBank(
        None if pRspRepeal is NULL else RspRepeal.from_address(<size_t> pRspRepeal).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnFromBankToFutureByFuture(api, CThostFtdcRspTransferField *pRspTransfer) except -1:
    api.OnRtnFromBankToFutureByFuture(
        None if pRspTransfer is NULL else RspTransfer.from_address(<size_t> pRspTransfer).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnFromFutureToBankByFuture(api, CThostFtdcRspTransferField *pRspTransfer) except -1:
    api.OnRtnFromFutureToBankByFuture(
        None if pRspTransfer is NULL else RspTransfer.from_address(<size_t> pRspTransfer).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnRepealFromBankToFutureByFutureManual(api, CThostFtdcRspRepealField *pRspRepeal) except -1:
    api.OnRtnRepealFromBankToFutureByFutureManual(
        None if pRspRepeal is NULL else RspRepeal.from_address(<size_t> pRspRepeal).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnRepealFromFutureToBankByFutureManual(api, CThostFtdcRspRepealField *pRspRepeal) except -1:
    api.OnRtnRepealFromFutureToBankByFutureManual(
        None if pRspRepeal is NULL else RspRepeal.from_address(<size_t> pRspRepeal).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnQueryBankBalanceByFuture(api, CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) except -1:
    api.OnRtnQueryBankBalanceByFuture(
        None if pNotifyQueryAccount is NULL else NotifyQueryAccount.from_address(<size_t> pNotifyQueryAccount).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnBankToFutureByFuture(api, CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnBankToFutureByFuture(
        None if pReqTransfer is NULL else ReqTransfer.from_address(<size_t> pReqTransfer).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnFutureToBankByFuture(api, CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnFutureToBankByFuture(
        None if pReqTransfer is NULL else ReqTransfer.from_address(<size_t> pReqTransfer).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnRepealBankToFutureByFutureManual(api, CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnRepealBankToFutureByFutureManual(
        None if pReqRepeal is NULL else ReqRepeal.from_address(<size_t> pReqRepeal).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnRepealFutureToBankByFutureManual(api, CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnRepealFutureToBankByFutureManual(
        None if pReqRepeal is NULL else ReqRepeal.from_address(<size_t> pReqRepeal).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnErrRtnQueryBankBalanceByFuture(api, CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo) except -1:
    api.OnErrRtnQueryBankBalanceByFuture(
        None if pReqQueryAccount is NULL else ReqQueryAccount.from_address(<size_t> pReqQueryAccount).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnRepealFromBankToFutureByFuture(api, CThostFtdcRspRepealField *pRspRepeal) except -1:
    api.OnRtnRepealFromBankToFutureByFuture(
        None if pRspRepeal is NULL else RspRepeal.from_address(<size_t> pRspRepeal).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnRepealFromFutureToBankByFuture(api, CThostFtdcRspRepealField *pRspRepeal) except -1:
    api.OnRtnRepealFromFutureToBankByFuture(
        None if pRspRepeal is NULL else RspRepeal.from_address(<size_t> pRspRepeal).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRspFromBankToFutureByFuture(api, CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspFromBankToFutureByFuture(
        None if pReqTransfer is NULL else ReqTransfer.from_address(<size_t> pReqTransfer).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspFromFutureToBankByFuture(api, CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspFromFutureToBankByFuture(
        None if pReqTransfer is NULL else ReqTransfer.from_address(<size_t> pReqTransfer).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQueryBankAccountMoneyByFuture(api, CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQueryBankAccountMoneyByFuture(
        None if pReqQueryAccount is NULL else ReqQueryAccount.from_address(<size_t> pReqQueryAccount).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRtnOpenAccountByBank(api, CThostFtdcOpenAccountField *pOpenAccount) except -1:
    api.OnRtnOpenAccountByBank(
        None if pOpenAccount is NULL else OpenAccount.from_address(<size_t> pOpenAccount).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnCancelAccountByBank(api, CThostFtdcCancelAccountField *pCancelAccount) except -1:
    api.OnRtnCancelAccountByBank(
        None if pCancelAccount is NULL else CancelAccount.from_address(<size_t> pCancelAccount).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRtnChangeAccountByBank(api, CThostFtdcChangeAccountField *pChangeAccount) except -1:
    api.OnRtnChangeAccountByBank(
        None if pChangeAccount is NULL else ChangeAccount.from_address(<size_t> pChangeAccount).to_tuple()
    )
    return 0


cdef extern int TraderSpi__OnRspQryClassifiedInstrument(api, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryClassifiedInstrument(
        None if pInstrument is NULL else Instrument.from_address(<size_t> pInstrument).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0


cdef extern int TraderSpi__OnRspQryCombPromotionParam(api, CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    api.OnRspQryCombPromotionParam(
        None if pCombPromotionParam is NULL else CombPromotionParam.from_address(<size_t> pCombPromotionParam).to_tuple(),
        None if pRspInfo is NULL else RspInfo.from_address(<size_t> pRspInfo).to_tuple(),
        nRequestID,
        bIsLast
    )
    return 0

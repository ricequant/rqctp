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

from ctypes import c_int, c_short, c_char, c_double

from .utils import Struct

c_char_Array_2 = c_char * 2
c_char_Array_3 = c_char * 3
c_char_Array_4 = c_char * 4
c_char_Array_5 = c_char * 5
c_char_Array_6 = c_char * 6
c_char_Array_7 = c_char * 7
c_char_Array_9 = c_char * 9
c_char_Array_10 = c_char * 10
c_char_Array_11 = c_char * 11
c_char_Array_12 = c_char * 12
c_char_Array_13 = c_char * 13
c_char_Array_15 = c_char * 15
c_char_Array_16 = c_char * 16
c_char_Array_17 = c_char * 17
c_char_Array_20 = c_char * 20
c_char_Array_21 = c_char * 21
c_char_Array_22 = c_char * 22
c_char_Array_23 = c_char * 23
c_char_Array_24 = c_char * 24
c_char_Array_25 = c_char * 25
c_char_Array_31 = c_char * 31
c_char_Array_33 = c_char * 33
c_char_Array_36 = c_char * 36
c_char_Array_41 = c_char * 41
c_char_Array_51 = c_char * 51
c_char_Array_61 = c_char * 61
c_char_Array_65 = c_char * 65
c_char_Array_71 = c_char * 71
c_char_Array_81 = c_char * 81
c_char_Array_100 = c_char * 100
c_char_Array_101 = c_char * 101
c_char_Array_129 = c_char * 129
c_char_Array_151 = c_char * 151
c_char_Array_161 = c_char * 161
c_char_Array_201 = c_char * 201
c_char_Array_256 = c_char * 256
c_char_Array_257 = c_char * 257
c_char_Array_261 = c_char * 261
c_char_Array_273 = c_char * 273
c_char_Array_301 = c_char * 301
c_char_Array_349 = c_char * 349
c_char_Array_365 = c_char * 365
c_char_Array_401 = c_char * 401
c_char_Array_501 = c_char * 501
c_char_Array_513 = c_char * 513
c_char_Array_1001 = c_char * 1001
c_char_Array_1025 = c_char * 1025
c_char_Array_2049 = c_char * 2049
c_char_Array_2561 = c_char * 2561


class Dissemination(Struct):
    _fields_ = [
        ("SequenceSeries", c_short),
        ("SequenceNo", c_int),
    ]

    def __init__(self, SequenceSeries=None, SequenceNo=None):
        super().__init__()
        if SequenceSeries:
            self.SequenceSeries = SequenceSeries
        if SequenceNo:
            self.SequenceNo = SequenceNo


class ReqUserLogin(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("Password", c_char_Array_41),
        ("UserProductInfo", c_char_Array_11),
        ("InterfaceProductInfo", c_char_Array_11),
        ("ProtocolInfo", c_char_Array_11),
        ("MacAddress", c_char_Array_21),
        ("OneTimePassword", c_char_Array_41),
        ("reserve1", c_char_Array_16),
        ("LoginRemark", c_char_Array_36),
        ("ClientIPPort", c_int),
        ("ClientIPAddress", c_char_Array_33),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, UserID=None, Password=None, UserProductInfo=None, InterfaceProductInfo=None, ProtocolInfo=None, MacAddress=None, OneTimePassword=None, reserve1=None, LoginRemark=None, ClientIPPort=None, ClientIPAddress=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if InterfaceProductInfo:
            self.InterfaceProductInfo = InterfaceProductInfo.encode("GBK")
        if ProtocolInfo:
            self.ProtocolInfo = ProtocolInfo.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if OneTimePassword:
            self.OneTimePassword = OneTimePassword.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort
        if ClientIPAddress:
            self.ClientIPAddress = ClientIPAddress.encode("GBK")


class RspUserLogin(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("LoginTime", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("SystemName", c_char_Array_41),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("MaxOrderRef", c_char_Array_13),
        ("SHFETime", c_char_Array_9),
        ("DCETime", c_char_Array_9),
        ("CZCETime", c_char_Array_9),
        ("FFEXTime", c_char_Array_9),
        ("INETime", c_char_Array_9),
        ("SysVersion", c_char_Array_41),
        ("GFEXTime", c_char_Array_9),
    ]

    def __init__(self, TradingDay=None, LoginTime=None, BrokerID=None, UserID=None, SystemName=None, FrontID=None, SessionID=None, MaxOrderRef=None, SHFETime=None, DCETime=None, CZCETime=None, FFEXTime=None, INETime=None, SysVersion=None, GFEXTime=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if LoginTime:
            self.LoginTime = LoginTime.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if SystemName:
            self.SystemName = SystemName.encode("GBK")
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if MaxOrderRef:
            self.MaxOrderRef = MaxOrderRef.encode("GBK")
        if SHFETime:
            self.SHFETime = SHFETime.encode("GBK")
        if DCETime:
            self.DCETime = DCETime.encode("GBK")
        if CZCETime:
            self.CZCETime = CZCETime.encode("GBK")
        if FFEXTime:
            self.FFEXTime = FFEXTime.encode("GBK")
        if INETime:
            self.INETime = INETime.encode("GBK")
        if SysVersion:
            self.SysVersion = SysVersion.encode("GBK")
        if GFEXTime:
            self.GFEXTime = GFEXTime.encode("GBK")


class UserLogout(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, BrokerID=None, UserID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class ForceUserLogout(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, BrokerID=None, UserID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class ReqAuthenticate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("UserProductInfo", c_char_Array_11),
        ("AuthCode", c_char_Array_17),
        ("AppID", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, UserID=None, UserProductInfo=None, AuthCode=None, AppID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if AuthCode:
            self.AuthCode = AuthCode.encode("GBK")
        if AppID:
            self.AppID = AppID.encode("GBK")


class RspAuthenticate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("UserProductInfo", c_char_Array_11),
        ("AppID", c_char_Array_33),
        ("AppType", c_char),
    ]

    def __init__(self, BrokerID=None, UserID=None, UserProductInfo=None, AppID=None, AppType=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if AppID:
            self.AppID = AppID.encode("GBK")
        if AppType:
            self.AppType = AppType.encode("GBK")


class AuthenticationInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("UserProductInfo", c_char_Array_11),
        ("AuthInfo", c_char_Array_129),
        ("IsResult", c_int),
        ("AppID", c_char_Array_33),
        ("AppType", c_char),
        ("reserve1", c_char_Array_16),
        ("ClientIPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, UserID=None, UserProductInfo=None, AuthInfo=None, IsResult=None, AppID=None, AppType=None, reserve1=None, ClientIPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if AuthInfo:
            self.AuthInfo = AuthInfo.encode("GBK")
        if IsResult:
            self.IsResult = IsResult
        if AppID:
            self.AppID = AppID.encode("GBK")
        if AppType:
            self.AppType = AppType.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ClientIPAddress:
            self.ClientIPAddress = ClientIPAddress.encode("GBK")


class RspUserLogin2(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("LoginTime", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("SystemName", c_char_Array_41),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("MaxOrderRef", c_char_Array_13),
        ("SHFETime", c_char_Array_9),
        ("DCETime", c_char_Array_9),
        ("CZCETime", c_char_Array_9),
        ("FFEXTime", c_char_Array_9),
        ("INETime", c_char_Array_9),
        ("RandomString", c_char_Array_17),
    ]

    def __init__(self, TradingDay=None, LoginTime=None, BrokerID=None, UserID=None, SystemName=None, FrontID=None, SessionID=None, MaxOrderRef=None, SHFETime=None, DCETime=None, CZCETime=None, FFEXTime=None, INETime=None, RandomString=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if LoginTime:
            self.LoginTime = LoginTime.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if SystemName:
            self.SystemName = SystemName.encode("GBK")
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if MaxOrderRef:
            self.MaxOrderRef = MaxOrderRef.encode("GBK")
        if SHFETime:
            self.SHFETime = SHFETime.encode("GBK")
        if DCETime:
            self.DCETime = DCETime.encode("GBK")
        if CZCETime:
            self.CZCETime = CZCETime.encode("GBK")
        if FFEXTime:
            self.FFEXTime = FFEXTime.encode("GBK")
        if INETime:
            self.INETime = INETime.encode("GBK")
        if RandomString:
            self.RandomString = RandomString.encode("GBK")


class TransferHeader(Struct):
    _fields_ = [
        ("Version", c_char_Array_4),
        ("TradeCode", c_char_Array_7),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("TradeSerial", c_char_Array_9),
        ("FutureID", c_char_Array_11),
        ("BankID", c_char_Array_4),
        ("BankBrchID", c_char_Array_5),
        ("OperNo", c_char_Array_17),
        ("DeviceID", c_char_Array_3),
        ("RecordNum", c_char_Array_7),
        ("SessionID", c_int),
        ("RequestID", c_int),
    ]

    def __init__(self, Version=None, TradeCode=None, TradeDate=None, TradeTime=None, TradeSerial=None, FutureID=None, BankID=None, BankBrchID=None, OperNo=None, DeviceID=None, RecordNum=None, SessionID=None, RequestID=None):
        super().__init__()
        if Version:
            self.Version = Version.encode("GBK")
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if TradeSerial:
            self.TradeSerial = TradeSerial.encode("GBK")
        if FutureID:
            self.FutureID = FutureID.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBrchID:
            self.BankBrchID = BankBrchID.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if RecordNum:
            self.RecordNum = RecordNum.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if RequestID:
            self.RequestID = RequestID


class TransferBankToFutureReq(Struct):
    _fields_ = [
        ("FutureAccount", c_char_Array_13),
        ("FuturePwdFlag", c_char),
        ("FutureAccPwd", c_char_Array_17),
        ("TradeAmt", c_double),
        ("CustFee", c_double),
        ("CurrencyCode", c_char_Array_4),
    ]

    def __init__(self, FutureAccount=None, FuturePwdFlag=None, FutureAccPwd=None, TradeAmt=None, CustFee=None, CurrencyCode=None):
        super().__init__()
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if FuturePwdFlag:
            self.FuturePwdFlag = FuturePwdFlag.encode("GBK")
        if FutureAccPwd:
            self.FutureAccPwd = FutureAccPwd.encode("GBK")
        if TradeAmt:
            self.TradeAmt = TradeAmt
        if CustFee:
            self.CustFee = CustFee
        if CurrencyCode:
            self.CurrencyCode = CurrencyCode.encode("GBK")


class TransferBankToFutureRsp(Struct):
    _fields_ = [
        ("RetCode", c_char_Array_5),
        ("RetInfo", c_char_Array_129),
        ("FutureAccount", c_char_Array_13),
        ("TradeAmt", c_double),
        ("CustFee", c_double),
        ("CurrencyCode", c_char_Array_4),
    ]

    def __init__(self, RetCode=None, RetInfo=None, FutureAccount=None, TradeAmt=None, CustFee=None, CurrencyCode=None):
        super().__init__()
        if RetCode:
            self.RetCode = RetCode.encode("GBK")
        if RetInfo:
            self.RetInfo = RetInfo.encode("GBK")
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if TradeAmt:
            self.TradeAmt = TradeAmt
        if CustFee:
            self.CustFee = CustFee
        if CurrencyCode:
            self.CurrencyCode = CurrencyCode.encode("GBK")


class TransferFutureToBankReq(Struct):
    _fields_ = [
        ("FutureAccount", c_char_Array_13),
        ("FuturePwdFlag", c_char),
        ("FutureAccPwd", c_char_Array_17),
        ("TradeAmt", c_double),
        ("CustFee", c_double),
        ("CurrencyCode", c_char_Array_4),
    ]

    def __init__(self, FutureAccount=None, FuturePwdFlag=None, FutureAccPwd=None, TradeAmt=None, CustFee=None, CurrencyCode=None):
        super().__init__()
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if FuturePwdFlag:
            self.FuturePwdFlag = FuturePwdFlag.encode("GBK")
        if FutureAccPwd:
            self.FutureAccPwd = FutureAccPwd.encode("GBK")
        if TradeAmt:
            self.TradeAmt = TradeAmt
        if CustFee:
            self.CustFee = CustFee
        if CurrencyCode:
            self.CurrencyCode = CurrencyCode.encode("GBK")


class TransferFutureToBankRsp(Struct):
    _fields_ = [
        ("RetCode", c_char_Array_5),
        ("RetInfo", c_char_Array_129),
        ("FutureAccount", c_char_Array_13),
        ("TradeAmt", c_double),
        ("CustFee", c_double),
        ("CurrencyCode", c_char_Array_4),
    ]

    def __init__(self, RetCode=None, RetInfo=None, FutureAccount=None, TradeAmt=None, CustFee=None, CurrencyCode=None):
        super().__init__()
        if RetCode:
            self.RetCode = RetCode.encode("GBK")
        if RetInfo:
            self.RetInfo = RetInfo.encode("GBK")
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if TradeAmt:
            self.TradeAmt = TradeAmt
        if CustFee:
            self.CustFee = CustFee
        if CurrencyCode:
            self.CurrencyCode = CurrencyCode.encode("GBK")


class TransferQryBankReq(Struct):
    _fields_ = [
        ("FutureAccount", c_char_Array_13),
        ("FuturePwdFlag", c_char),
        ("FutureAccPwd", c_char_Array_17),
        ("CurrencyCode", c_char_Array_4),
    ]

    def __init__(self, FutureAccount=None, FuturePwdFlag=None, FutureAccPwd=None, CurrencyCode=None):
        super().__init__()
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if FuturePwdFlag:
            self.FuturePwdFlag = FuturePwdFlag.encode("GBK")
        if FutureAccPwd:
            self.FutureAccPwd = FutureAccPwd.encode("GBK")
        if CurrencyCode:
            self.CurrencyCode = CurrencyCode.encode("GBK")


class TransferQryBankRsp(Struct):
    _fields_ = [
        ("RetCode", c_char_Array_5),
        ("RetInfo", c_char_Array_129),
        ("FutureAccount", c_char_Array_13),
        ("TradeAmt", c_double),
        ("UseAmt", c_double),
        ("FetchAmt", c_double),
        ("CurrencyCode", c_char_Array_4),
    ]

    def __init__(self, RetCode=None, RetInfo=None, FutureAccount=None, TradeAmt=None, UseAmt=None, FetchAmt=None, CurrencyCode=None):
        super().__init__()
        if RetCode:
            self.RetCode = RetCode.encode("GBK")
        if RetInfo:
            self.RetInfo = RetInfo.encode("GBK")
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if TradeAmt:
            self.TradeAmt = TradeAmt
        if UseAmt:
            self.UseAmt = UseAmt
        if FetchAmt:
            self.FetchAmt = FetchAmt
        if CurrencyCode:
            self.CurrencyCode = CurrencyCode.encode("GBK")


class TransferQryDetailReq(Struct):
    _fields_ = [
        ("FutureAccount", c_char_Array_13),
    ]

    def __init__(self, FutureAccount=None):
        super().__init__()
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")


class TransferQryDetailRsp(Struct):
    _fields_ = [
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("TradeCode", c_char_Array_7),
        ("FutureSerial", c_int),
        ("FutureID", c_char_Array_11),
        ("FutureAccount", c_char_Array_22),
        ("BankSerial", c_int),
        ("BankID", c_char_Array_4),
        ("BankBrchID", c_char_Array_5),
        ("BankAccount", c_char_Array_41),
        ("CertCode", c_char_Array_21),
        ("CurrencyCode", c_char_Array_4),
        ("TxAmount", c_double),
        ("Flag", c_char),
    ]

    def __init__(self, TradeDate=None, TradeTime=None, TradeCode=None, FutureSerial=None, FutureID=None, FutureAccount=None, BankSerial=None, BankID=None, BankBrchID=None, BankAccount=None, CertCode=None, CurrencyCode=None, TxAmount=None, Flag=None):
        super().__init__()
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if FutureID:
            self.FutureID = FutureID.encode("GBK")
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBrchID:
            self.BankBrchID = BankBrchID.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if CertCode:
            self.CertCode = CertCode.encode("GBK")
        if CurrencyCode:
            self.CurrencyCode = CurrencyCode.encode("GBK")
        if TxAmount:
            self.TxAmount = TxAmount
        if Flag:
            self.Flag = Flag.encode("GBK")


class RspInfo(Struct):
    _fields_ = [
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class Exchange(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ExchangeName", c_char_Array_61),
        ("ExchangeProperty", c_char),
    ]

    def __init__(self, ExchangeID=None, ExchangeName=None, ExchangeProperty=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExchangeName:
            self.ExchangeName = ExchangeName.encode("GBK")
        if ExchangeProperty:
            self.ExchangeProperty = ExchangeProperty.encode("GBK")


class Product(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("ProductName", c_char_Array_21),
        ("ExchangeID", c_char_Array_9),
        ("ProductClass", c_char),
        ("VolumeMultiple", c_int),
        ("PriceTick", c_double),
        ("MaxMarketOrderVolume", c_int),
        ("MinMarketOrderVolume", c_int),
        ("MaxLimitOrderVolume", c_int),
        ("MinLimitOrderVolume", c_int),
        ("PositionType", c_char),
        ("PositionDateType", c_char),
        ("CloseDealType", c_char),
        ("TradeCurrencyID", c_char_Array_4),
        ("MortgageFundUseRange", c_char),
        ("reserve2", c_char_Array_31),
        ("UnderlyingMultiple", c_double),
        ("ProductID", c_char_Array_81),
        ("ExchangeProductID", c_char_Array_81),
        ("OpenLimitControlLevel", c_char),
        ("OrderFreqControlLevel", c_char),
    ]

    def __init__(self, reserve1=None, ProductName=None, ExchangeID=None, ProductClass=None, VolumeMultiple=None, PriceTick=None, MaxMarketOrderVolume=None, MinMarketOrderVolume=None, MaxLimitOrderVolume=None, MinLimitOrderVolume=None, PositionType=None, PositionDateType=None, CloseDealType=None, TradeCurrencyID=None, MortgageFundUseRange=None, reserve2=None, UnderlyingMultiple=None, ProductID=None, ExchangeProductID=None, OpenLimitControlLevel=None, OrderFreqControlLevel=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ProductName:
            self.ProductName = ProductName.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProductClass:
            self.ProductClass = ProductClass.encode("GBK")
        if VolumeMultiple:
            self.VolumeMultiple = VolumeMultiple
        if PriceTick:
            self.PriceTick = PriceTick
        if MaxMarketOrderVolume:
            self.MaxMarketOrderVolume = MaxMarketOrderVolume
        if MinMarketOrderVolume:
            self.MinMarketOrderVolume = MinMarketOrderVolume
        if MaxLimitOrderVolume:
            self.MaxLimitOrderVolume = MaxLimitOrderVolume
        if MinLimitOrderVolume:
            self.MinLimitOrderVolume = MinLimitOrderVolume
        if PositionType:
            self.PositionType = PositionType.encode("GBK")
        if PositionDateType:
            self.PositionDateType = PositionDateType.encode("GBK")
        if CloseDealType:
            self.CloseDealType = CloseDealType.encode("GBK")
        if TradeCurrencyID:
            self.TradeCurrencyID = TradeCurrencyID.encode("GBK")
        if MortgageFundUseRange:
            self.MortgageFundUseRange = MortgageFundUseRange.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if UnderlyingMultiple:
            self.UnderlyingMultiple = UnderlyingMultiple
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ExchangeProductID:
            self.ExchangeProductID = ExchangeProductID.encode("GBK")
        if OpenLimitControlLevel:
            self.OpenLimitControlLevel = OpenLimitControlLevel.encode("GBK")
        if OrderFreqControlLevel:
            self.OrderFreqControlLevel = OrderFreqControlLevel.encode("GBK")


class Instrument(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentName", c_char_Array_21),
        ("reserve2", c_char_Array_31),
        ("reserve3", c_char_Array_31),
        ("ProductClass", c_char),
        ("DeliveryYear", c_int),
        ("DeliveryMonth", c_int),
        ("MaxMarketOrderVolume", c_int),
        ("MinMarketOrderVolume", c_int),
        ("MaxLimitOrderVolume", c_int),
        ("MinLimitOrderVolume", c_int),
        ("VolumeMultiple", c_int),
        ("PriceTick", c_double),
        ("CreateDate", c_char_Array_9),
        ("OpenDate", c_char_Array_9),
        ("ExpireDate", c_char_Array_9),
        ("StartDelivDate", c_char_Array_9),
        ("EndDelivDate", c_char_Array_9),
        ("InstLifePhase", c_char),
        ("IsTrading", c_int),
        ("PositionType", c_char),
        ("PositionDateType", c_char),
        ("LongMarginRatio", c_double),
        ("ShortMarginRatio", c_double),
        ("MaxMarginSideAlgorithm", c_char),
        ("reserve4", c_char_Array_31),
        ("StrikePrice", c_double),
        ("OptionsType", c_char),
        ("UnderlyingMultiple", c_double),
        ("CombinationType", c_char),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("ProductID", c_char_Array_81),
        ("UnderlyingInstrID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, ExchangeID=None, InstrumentName=None, reserve2=None, reserve3=None, ProductClass=None, DeliveryYear=None, DeliveryMonth=None, MaxMarketOrderVolume=None, MinMarketOrderVolume=None, MaxLimitOrderVolume=None, MinLimitOrderVolume=None, VolumeMultiple=None, PriceTick=None, CreateDate=None, OpenDate=None, ExpireDate=None, StartDelivDate=None, EndDelivDate=None, InstLifePhase=None, IsTrading=None, PositionType=None, PositionDateType=None, LongMarginRatio=None, ShortMarginRatio=None, MaxMarginSideAlgorithm=None, reserve4=None, StrikePrice=None, OptionsType=None, UnderlyingMultiple=None, CombinationType=None, InstrumentID=None, ExchangeInstID=None, ProductID=None, UnderlyingInstrID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentName:
            self.InstrumentName = InstrumentName.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if reserve3:
            self.reserve3 = reserve3.encode("GBK")
        if ProductClass:
            self.ProductClass = ProductClass.encode("GBK")
        if DeliveryYear:
            self.DeliveryYear = DeliveryYear
        if DeliveryMonth:
            self.DeliveryMonth = DeliveryMonth
        if MaxMarketOrderVolume:
            self.MaxMarketOrderVolume = MaxMarketOrderVolume
        if MinMarketOrderVolume:
            self.MinMarketOrderVolume = MinMarketOrderVolume
        if MaxLimitOrderVolume:
            self.MaxLimitOrderVolume = MaxLimitOrderVolume
        if MinLimitOrderVolume:
            self.MinLimitOrderVolume = MinLimitOrderVolume
        if VolumeMultiple:
            self.VolumeMultiple = VolumeMultiple
        if PriceTick:
            self.PriceTick = PriceTick
        if CreateDate:
            self.CreateDate = CreateDate.encode("GBK")
        if OpenDate:
            self.OpenDate = OpenDate.encode("GBK")
        if ExpireDate:
            self.ExpireDate = ExpireDate.encode("GBK")
        if StartDelivDate:
            self.StartDelivDate = StartDelivDate.encode("GBK")
        if EndDelivDate:
            self.EndDelivDate = EndDelivDate.encode("GBK")
        if InstLifePhase:
            self.InstLifePhase = InstLifePhase.encode("GBK")
        if IsTrading:
            self.IsTrading = IsTrading
        if PositionType:
            self.PositionType = PositionType.encode("GBK")
        if PositionDateType:
            self.PositionDateType = PositionDateType.encode("GBK")
        if LongMarginRatio:
            self.LongMarginRatio = LongMarginRatio
        if ShortMarginRatio:
            self.ShortMarginRatio = ShortMarginRatio
        if MaxMarginSideAlgorithm:
            self.MaxMarginSideAlgorithm = MaxMarginSideAlgorithm.encode("GBK")
        if reserve4:
            self.reserve4 = reserve4.encode("GBK")
        if StrikePrice:
            self.StrikePrice = StrikePrice
        if OptionsType:
            self.OptionsType = OptionsType.encode("GBK")
        if UnderlyingMultiple:
            self.UnderlyingMultiple = UnderlyingMultiple
        if CombinationType:
            self.CombinationType = CombinationType.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if UnderlyingInstrID:
            self.UnderlyingInstrID = UnderlyingInstrID.encode("GBK")


class Broker(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("BrokerAbbr", c_char_Array_9),
        ("BrokerName", c_char_Array_81),
        ("IsActive", c_int),
    ]

    def __init__(self, BrokerID=None, BrokerAbbr=None, BrokerName=None, IsActive=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerAbbr:
            self.BrokerAbbr = BrokerAbbr.encode("GBK")
        if BrokerName:
            self.BrokerName = BrokerName.encode("GBK")
        if IsActive:
            self.IsActive = IsActive


class Trader(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("ParticipantID", c_char_Array_11),
        ("Password", c_char_Array_41),
        ("InstallCount", c_int),
        ("BrokerID", c_char_Array_11),
        ("OrderCancelAlg", c_char),
    ]

    def __init__(self, ExchangeID=None, TraderID=None, ParticipantID=None, Password=None, InstallCount=None, BrokerID=None, OrderCancelAlg=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallCount:
            self.InstallCount = InstallCount
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if OrderCancelAlg:
            self.OrderCancelAlg = OrderCancelAlg.encode("GBK")


class Investor(Struct):
    _fields_ = [
        ("InvestorID", c_char_Array_13),
        ("BrokerID", c_char_Array_11),
        ("InvestorGroupID", c_char_Array_13),
        ("InvestorName", c_char_Array_81),
        ("IdentifiedCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("IsActive", c_int),
        ("Telephone", c_char_Array_41),
        ("Address", c_char_Array_101),
        ("OpenDate", c_char_Array_9),
        ("Mobile", c_char_Array_41),
        ("CommModelID", c_char_Array_13),
        ("MarginModelID", c_char_Array_13),
        ("IsOrderFreq", c_char),
        ("IsOpenVolLimit", c_char),
    ]

    def __init__(self, InvestorID=None, BrokerID=None, InvestorGroupID=None, InvestorName=None, IdentifiedCardType=None, IdentifiedCardNo=None, IsActive=None, Telephone=None, Address=None, OpenDate=None, Mobile=None, CommModelID=None, MarginModelID=None, IsOrderFreq=None, IsOpenVolLimit=None):
        super().__init__()
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorGroupID:
            self.InvestorGroupID = InvestorGroupID.encode("GBK")
        if InvestorName:
            self.InvestorName = InvestorName.encode("GBK")
        if IdentifiedCardType:
            self.IdentifiedCardType = IdentifiedCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if IsActive:
            self.IsActive = IsActive
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if OpenDate:
            self.OpenDate = OpenDate.encode("GBK")
        if Mobile:
            self.Mobile = Mobile.encode("GBK")
        if CommModelID:
            self.CommModelID = CommModelID.encode("GBK")
        if MarginModelID:
            self.MarginModelID = MarginModelID.encode("GBK")
        if IsOrderFreq:
            self.IsOrderFreq = IsOrderFreq.encode("GBK")
        if IsOpenVolLimit:
            self.IsOpenVolLimit = IsOpenVolLimit.encode("GBK")


class TradingCode(Struct):
    _fields_ = [
        ("InvestorID", c_char_Array_13),
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("ClientID", c_char_Array_11),
        ("IsActive", c_int),
        ("ClientIDType", c_char),
        ("BranchID", c_char_Array_9),
        ("BizType", c_char),
        ("InvestUnitID", c_char_Array_17),
    ]

    def __init__(self, InvestorID=None, BrokerID=None, ExchangeID=None, ClientID=None, IsActive=None, ClientIDType=None, BranchID=None, BizType=None, InvestUnitID=None):
        super().__init__()
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if IsActive:
            self.IsActive = IsActive
        if ClientIDType:
            self.ClientIDType = ClientIDType.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if BizType:
            self.BizType = BizType.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class PartBroker(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("IsActive", c_int),
    ]

    def __init__(self, BrokerID=None, ExchangeID=None, ParticipantID=None, IsActive=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if IsActive:
            self.IsActive = IsActive


class SuperUser(Struct):
    _fields_ = [
        ("UserID", c_char_Array_16),
        ("UserName", c_char_Array_81),
        ("Password", c_char_Array_41),
        ("IsActive", c_int),
    ]

    def __init__(self, UserID=None, UserName=None, Password=None, IsActive=None):
        super().__init__()
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserName:
            self.UserName = UserName.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if IsActive:
            self.IsActive = IsActive


class SuperUserFunction(Struct):
    _fields_ = [
        ("UserID", c_char_Array_16),
        ("FunctionCode", c_char),
    ]

    def __init__(self, UserID=None, FunctionCode=None):
        super().__init__()
        if UserID:
            self.UserID = UserID.encode("GBK")
        if FunctionCode:
            self.FunctionCode = FunctionCode.encode("GBK")


class InvestorGroup(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorGroupID", c_char_Array_13),
        ("InvestorGroupName", c_char_Array_41),
    ]

    def __init__(self, BrokerID=None, InvestorGroupID=None, InvestorGroupName=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorGroupID:
            self.InvestorGroupID = InvestorGroupID.encode("GBK")
        if InvestorGroupName:
            self.InvestorGroupName = InvestorGroupName.encode("GBK")


class TradingAccount(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("PreMortgage", c_double),
        ("PreCredit", c_double),
        ("PreDeposit", c_double),
        ("PreBalance", c_double),
        ("PreMargin", c_double),
        ("InterestBase", c_double),
        ("Interest", c_double),
        ("Deposit", c_double),
        ("Withdraw", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CurrMargin", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("Balance", c_double),
        ("Available", c_double),
        ("WithdrawQuota", c_double),
        ("Reserve", c_double),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("Credit", c_double),
        ("Mortgage", c_double),
        ("ExchangeMargin", c_double),
        ("DeliveryMargin", c_double),
        ("ExchangeDeliveryMargin", c_double),
        ("ReserveBalance", c_double),
        ("CurrencyID", c_char_Array_4),
        ("PreFundMortgageIn", c_double),
        ("PreFundMortgageOut", c_double),
        ("FundMortgageIn", c_double),
        ("FundMortgageOut", c_double),
        ("FundMortgageAvailable", c_double),
        ("MortgageableFund", c_double),
        ("SpecProductMargin", c_double),
        ("SpecProductFrozenMargin", c_double),
        ("SpecProductCommission", c_double),
        ("SpecProductFrozenCommission", c_double),
        ("SpecProductPositionProfit", c_double),
        ("SpecProductCloseProfit", c_double),
        ("SpecProductPositionProfitByAlg", c_double),
        ("SpecProductExchangeMargin", c_double),
        ("BizType", c_char),
        ("FrozenSwap", c_double),
        ("RemainSwap", c_double),
    ]

    def __init__(self, BrokerID=None, AccountID=None, PreMortgage=None, PreCredit=None, PreDeposit=None, PreBalance=None, PreMargin=None, InterestBase=None, Interest=None, Deposit=None, Withdraw=None, FrozenMargin=None, FrozenCash=None, FrozenCommission=None, CurrMargin=None, CashIn=None, Commission=None, CloseProfit=None, PositionProfit=None, Balance=None, Available=None, WithdrawQuota=None, Reserve=None, TradingDay=None, SettlementID=None, Credit=None, Mortgage=None, ExchangeMargin=None, DeliveryMargin=None, ExchangeDeliveryMargin=None, ReserveBalance=None, CurrencyID=None, PreFundMortgageIn=None, PreFundMortgageOut=None, FundMortgageIn=None, FundMortgageOut=None, FundMortgageAvailable=None, MortgageableFund=None, SpecProductMargin=None, SpecProductFrozenMargin=None, SpecProductCommission=None, SpecProductFrozenCommission=None, SpecProductPositionProfit=None, SpecProductCloseProfit=None, SpecProductPositionProfitByAlg=None, SpecProductExchangeMargin=None, BizType=None, FrozenSwap=None, RemainSwap=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if PreMortgage:
            self.PreMortgage = PreMortgage
        if PreCredit:
            self.PreCredit = PreCredit
        if PreDeposit:
            self.PreDeposit = PreDeposit
        if PreBalance:
            self.PreBalance = PreBalance
        if PreMargin:
            self.PreMargin = PreMargin
        if InterestBase:
            self.InterestBase = InterestBase
        if Interest:
            self.Interest = Interest
        if Deposit:
            self.Deposit = Deposit
        if Withdraw:
            self.Withdraw = Withdraw
        if FrozenMargin:
            self.FrozenMargin = FrozenMargin
        if FrozenCash:
            self.FrozenCash = FrozenCash
        if FrozenCommission:
            self.FrozenCommission = FrozenCommission
        if CurrMargin:
            self.CurrMargin = CurrMargin
        if CashIn:
            self.CashIn = CashIn
        if Commission:
            self.Commission = Commission
        if CloseProfit:
            self.CloseProfit = CloseProfit
        if PositionProfit:
            self.PositionProfit = PositionProfit
        if Balance:
            self.Balance = Balance
        if Available:
            self.Available = Available
        if WithdrawQuota:
            self.WithdrawQuota = WithdrawQuota
        if Reserve:
            self.Reserve = Reserve
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if Credit:
            self.Credit = Credit
        if Mortgage:
            self.Mortgage = Mortgage
        if ExchangeMargin:
            self.ExchangeMargin = ExchangeMargin
        if DeliveryMargin:
            self.DeliveryMargin = DeliveryMargin
        if ExchangeDeliveryMargin:
            self.ExchangeDeliveryMargin = ExchangeDeliveryMargin
        if ReserveBalance:
            self.ReserveBalance = ReserveBalance
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if PreFundMortgageIn:
            self.PreFundMortgageIn = PreFundMortgageIn
        if PreFundMortgageOut:
            self.PreFundMortgageOut = PreFundMortgageOut
        if FundMortgageIn:
            self.FundMortgageIn = FundMortgageIn
        if FundMortgageOut:
            self.FundMortgageOut = FundMortgageOut
        if FundMortgageAvailable:
            self.FundMortgageAvailable = FundMortgageAvailable
        if MortgageableFund:
            self.MortgageableFund = MortgageableFund
        if SpecProductMargin:
            self.SpecProductMargin = SpecProductMargin
        if SpecProductFrozenMargin:
            self.SpecProductFrozenMargin = SpecProductFrozenMargin
        if SpecProductCommission:
            self.SpecProductCommission = SpecProductCommission
        if SpecProductFrozenCommission:
            self.SpecProductFrozenCommission = SpecProductFrozenCommission
        if SpecProductPositionProfit:
            self.SpecProductPositionProfit = SpecProductPositionProfit
        if SpecProductCloseProfit:
            self.SpecProductCloseProfit = SpecProductCloseProfit
        if SpecProductPositionProfitByAlg:
            self.SpecProductPositionProfitByAlg = SpecProductPositionProfitByAlg
        if SpecProductExchangeMargin:
            self.SpecProductExchangeMargin = SpecProductExchangeMargin
        if BizType:
            self.BizType = BizType.encode("GBK")
        if FrozenSwap:
            self.FrozenSwap = FrozenSwap
        if RemainSwap:
            self.RemainSwap = RemainSwap


class InvestorPosition(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("PosiDirection", c_char),
        ("HedgeFlag", c_char),
        ("PositionDate", c_char),
        ("YdPosition", c_int),
        ("Position", c_int),
        ("LongFrozen", c_int),
        ("ShortFrozen", c_int),
        ("LongFrozenAmount", c_double),
        ("ShortFrozenAmount", c_double),
        ("OpenVolume", c_int),
        ("CloseVolume", c_int),
        ("OpenAmount", c_double),
        ("CloseAmount", c_double),
        ("PositionCost", c_double),
        ("PreMargin", c_double),
        ("UseMargin", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("PreSettlementPrice", c_double),
        ("SettlementPrice", c_double),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("OpenCost", c_double),
        ("ExchangeMargin", c_double),
        ("CombPosition", c_int),
        ("CombLongFrozen", c_int),
        ("CombShortFrozen", c_int),
        ("CloseProfitByDate", c_double),
        ("CloseProfitByTrade", c_double),
        ("TodayPosition", c_int),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("StrikeFrozen", c_int),
        ("StrikeFrozenAmount", c_double),
        ("AbandonFrozen", c_int),
        ("ExchangeID", c_char_Array_9),
        ("YdStrikeFrozen", c_int),
        ("InvestUnitID", c_char_Array_17),
        ("PositionCostOffset", c_double),
        ("TasPosition", c_int),
        ("TasPositionCost", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, BrokerID=None, InvestorID=None, PosiDirection=None, HedgeFlag=None, PositionDate=None, YdPosition=None, Position=None, LongFrozen=None, ShortFrozen=None, LongFrozenAmount=None, ShortFrozenAmount=None, OpenVolume=None, CloseVolume=None, OpenAmount=None, CloseAmount=None, PositionCost=None, PreMargin=None, UseMargin=None, FrozenMargin=None, FrozenCash=None, FrozenCommission=None, CashIn=None, Commission=None, CloseProfit=None, PositionProfit=None, PreSettlementPrice=None, SettlementPrice=None, TradingDay=None, SettlementID=None, OpenCost=None, ExchangeMargin=None, CombPosition=None, CombLongFrozen=None, CombShortFrozen=None, CloseProfitByDate=None, CloseProfitByTrade=None, TodayPosition=None, MarginRateByMoney=None, MarginRateByVolume=None, StrikeFrozen=None, StrikeFrozenAmount=None, AbandonFrozen=None, ExchangeID=None, YdStrikeFrozen=None, InvestUnitID=None, PositionCostOffset=None, TasPosition=None, TasPositionCost=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if PosiDirection:
            self.PosiDirection = PosiDirection.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if PositionDate:
            self.PositionDate = PositionDate.encode("GBK")
        if YdPosition:
            self.YdPosition = YdPosition
        if Position:
            self.Position = Position
        if LongFrozen:
            self.LongFrozen = LongFrozen
        if ShortFrozen:
            self.ShortFrozen = ShortFrozen
        if LongFrozenAmount:
            self.LongFrozenAmount = LongFrozenAmount
        if ShortFrozenAmount:
            self.ShortFrozenAmount = ShortFrozenAmount
        if OpenVolume:
            self.OpenVolume = OpenVolume
        if CloseVolume:
            self.CloseVolume = CloseVolume
        if OpenAmount:
            self.OpenAmount = OpenAmount
        if CloseAmount:
            self.CloseAmount = CloseAmount
        if PositionCost:
            self.PositionCost = PositionCost
        if PreMargin:
            self.PreMargin = PreMargin
        if UseMargin:
            self.UseMargin = UseMargin
        if FrozenMargin:
            self.FrozenMargin = FrozenMargin
        if FrozenCash:
            self.FrozenCash = FrozenCash
        if FrozenCommission:
            self.FrozenCommission = FrozenCommission
        if CashIn:
            self.CashIn = CashIn
        if Commission:
            self.Commission = Commission
        if CloseProfit:
            self.CloseProfit = CloseProfit
        if PositionProfit:
            self.PositionProfit = PositionProfit
        if PreSettlementPrice:
            self.PreSettlementPrice = PreSettlementPrice
        if SettlementPrice:
            self.SettlementPrice = SettlementPrice
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OpenCost:
            self.OpenCost = OpenCost
        if ExchangeMargin:
            self.ExchangeMargin = ExchangeMargin
        if CombPosition:
            self.CombPosition = CombPosition
        if CombLongFrozen:
            self.CombLongFrozen = CombLongFrozen
        if CombShortFrozen:
            self.CombShortFrozen = CombShortFrozen
        if CloseProfitByDate:
            self.CloseProfitByDate = CloseProfitByDate
        if CloseProfitByTrade:
            self.CloseProfitByTrade = CloseProfitByTrade
        if TodayPosition:
            self.TodayPosition = TodayPosition
        if MarginRateByMoney:
            self.MarginRateByMoney = MarginRateByMoney
        if MarginRateByVolume:
            self.MarginRateByVolume = MarginRateByVolume
        if StrikeFrozen:
            self.StrikeFrozen = StrikeFrozen
        if StrikeFrozenAmount:
            self.StrikeFrozenAmount = StrikeFrozenAmount
        if AbandonFrozen:
            self.AbandonFrozen = AbandonFrozen
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if YdStrikeFrozen:
            self.YdStrikeFrozen = YdStrikeFrozen
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if PositionCostOffset:
            self.PositionCostOffset = PositionCostOffset
        if TasPosition:
            self.TasPosition = TasPosition
        if TasPositionCost:
            self.TasPositionCost = TasPositionCost
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InstrumentMarginRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, HedgeFlag=None, LongMarginRatioByMoney=None, LongMarginRatioByVolume=None, ShortMarginRatioByMoney=None, ShortMarginRatioByVolume=None, IsRelative=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume
        if IsRelative:
            self.IsRelative = IsRelative
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InstrumentCommissionRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("ExchangeID", c_char_Array_9),
        ("BizType", c_char),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, OpenRatioByMoney=None, OpenRatioByVolume=None, CloseRatioByMoney=None, CloseRatioByVolume=None, CloseTodayRatioByMoney=None, CloseTodayRatioByVolume=None, ExchangeID=None, BizType=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OpenRatioByMoney:
            self.OpenRatioByMoney = OpenRatioByMoney
        if OpenRatioByVolume:
            self.OpenRatioByVolume = OpenRatioByVolume
        if CloseRatioByMoney:
            self.CloseRatioByMoney = CloseRatioByMoney
        if CloseRatioByVolume:
            self.CloseRatioByVolume = CloseRatioByVolume
        if CloseTodayRatioByMoney:
            self.CloseTodayRatioByMoney = CloseTodayRatioByMoney
        if CloseTodayRatioByVolume:
            self.CloseTodayRatioByVolume = CloseTodayRatioByVolume
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if BizType:
            self.BizType = BizType.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class DepthMarketData(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("reserve2", c_char_Array_31),
        ("LastPrice", c_double),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("Volume", c_int),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
        ("ClosePrice", c_double),
        ("SettlementPrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("PreDelta", c_double),
        ("CurrDelta", c_double),
        ("UpdateTime", c_char_Array_9),
        ("UpdateMillisec", c_int),
        ("BidPrice1", c_double),
        ("BidVolume1", c_int),
        ("AskPrice1", c_double),
        ("AskVolume1", c_int),
        ("BidPrice2", c_double),
        ("BidVolume2", c_int),
        ("AskPrice2", c_double),
        ("AskVolume2", c_int),
        ("BidPrice3", c_double),
        ("BidVolume3", c_int),
        ("AskPrice3", c_double),
        ("AskVolume3", c_int),
        ("BidPrice4", c_double),
        ("BidVolume4", c_int),
        ("AskPrice4", c_double),
        ("AskVolume4", c_int),
        ("BidPrice5", c_double),
        ("BidVolume5", c_int),
        ("AskPrice5", c_double),
        ("AskVolume5", c_int),
        ("AveragePrice", c_double),
        ("ActionDay", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("BandingUpperPrice", c_double),
        ("BandingLowerPrice", c_double),
    ]

    def __init__(self, TradingDay=None, reserve1=None, ExchangeID=None, reserve2=None, LastPrice=None, PreSettlementPrice=None, PreClosePrice=None, PreOpenInterest=None, OpenPrice=None, HighestPrice=None, LowestPrice=None, Volume=None, Turnover=None, OpenInterest=None, ClosePrice=None, SettlementPrice=None, UpperLimitPrice=None, LowerLimitPrice=None, PreDelta=None, CurrDelta=None, UpdateTime=None, UpdateMillisec=None, BidPrice1=None, BidVolume1=None, AskPrice1=None, AskVolume1=None, BidPrice2=None, BidVolume2=None, AskPrice2=None, AskVolume2=None, BidPrice3=None, BidVolume3=None, AskPrice3=None, AskVolume3=None, BidPrice4=None, BidVolume4=None, AskPrice4=None, AskVolume4=None, BidPrice5=None, BidVolume5=None, AskPrice5=None, AskVolume5=None, AveragePrice=None, ActionDay=None, InstrumentID=None, ExchangeInstID=None, BandingUpperPrice=None, BandingLowerPrice=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if LastPrice:
            self.LastPrice = LastPrice
        if PreSettlementPrice:
            self.PreSettlementPrice = PreSettlementPrice
        if PreClosePrice:
            self.PreClosePrice = PreClosePrice
        if PreOpenInterest:
            self.PreOpenInterest = PreOpenInterest
        if OpenPrice:
            self.OpenPrice = OpenPrice
        if HighestPrice:
            self.HighestPrice = HighestPrice
        if LowestPrice:
            self.LowestPrice = LowestPrice
        if Volume:
            self.Volume = Volume
        if Turnover:
            self.Turnover = Turnover
        if OpenInterest:
            self.OpenInterest = OpenInterest
        if ClosePrice:
            self.ClosePrice = ClosePrice
        if SettlementPrice:
            self.SettlementPrice = SettlementPrice
        if UpperLimitPrice:
            self.UpperLimitPrice = UpperLimitPrice
        if LowerLimitPrice:
            self.LowerLimitPrice = LowerLimitPrice
        if PreDelta:
            self.PreDelta = PreDelta
        if CurrDelta:
            self.CurrDelta = CurrDelta
        if UpdateTime:
            self.UpdateTime = UpdateTime.encode("GBK")
        if UpdateMillisec:
            self.UpdateMillisec = UpdateMillisec
        if BidPrice1:
            self.BidPrice1 = BidPrice1
        if BidVolume1:
            self.BidVolume1 = BidVolume1
        if AskPrice1:
            self.AskPrice1 = AskPrice1
        if AskVolume1:
            self.AskVolume1 = AskVolume1
        if BidPrice2:
            self.BidPrice2 = BidPrice2
        if BidVolume2:
            self.BidVolume2 = BidVolume2
        if AskPrice2:
            self.AskPrice2 = AskPrice2
        if AskVolume2:
            self.AskVolume2 = AskVolume2
        if BidPrice3:
            self.BidPrice3 = BidPrice3
        if BidVolume3:
            self.BidVolume3 = BidVolume3
        if AskPrice3:
            self.AskPrice3 = AskPrice3
        if AskVolume3:
            self.AskVolume3 = AskVolume3
        if BidPrice4:
            self.BidPrice4 = BidPrice4
        if BidVolume4:
            self.BidVolume4 = BidVolume4
        if AskPrice4:
            self.AskPrice4 = AskPrice4
        if AskVolume4:
            self.AskVolume4 = AskVolume4
        if BidPrice5:
            self.BidPrice5 = BidPrice5
        if BidVolume5:
            self.BidVolume5 = BidVolume5
        if AskPrice5:
            self.AskPrice5 = AskPrice5
        if AskVolume5:
            self.AskVolume5 = AskVolume5
        if AveragePrice:
            self.AveragePrice = AveragePrice
        if ActionDay:
            self.ActionDay = ActionDay.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if BandingUpperPrice:
            self.BandingUpperPrice = BandingUpperPrice
        if BandingLowerPrice:
            self.BandingLowerPrice = BandingLowerPrice


class InstrumentTradingRight(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("TradingRight", c_char),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, TradingRight=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if TradingRight:
            self.TradingRight = TradingRight.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class BrokerUser(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("UserName", c_char_Array_81),
        ("UserType", c_char),
        ("IsActive", c_int),
        ("IsUsingOTP", c_int),
        ("IsAuthForce", c_int),
    ]

    def __init__(self, BrokerID=None, UserID=None, UserName=None, UserType=None, IsActive=None, IsUsingOTP=None, IsAuthForce=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserName:
            self.UserName = UserName.encode("GBK")
        if UserType:
            self.UserType = UserType.encode("GBK")
        if IsActive:
            self.IsActive = IsActive
        if IsUsingOTP:
            self.IsUsingOTP = IsUsingOTP
        if IsAuthForce:
            self.IsAuthForce = IsAuthForce


class BrokerUserPassword(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("Password", c_char_Array_41),
        ("LastUpdateTime", c_char_Array_17),
        ("LastLoginTime", c_char_Array_17),
        ("ExpireDate", c_char_Array_9),
        ("WeakExpireDate", c_char_Array_9),
    ]

    def __init__(self, BrokerID=None, UserID=None, Password=None, LastUpdateTime=None, LastLoginTime=None, ExpireDate=None, WeakExpireDate=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if LastUpdateTime:
            self.LastUpdateTime = LastUpdateTime.encode("GBK")
        if LastLoginTime:
            self.LastLoginTime = LastLoginTime.encode("GBK")
        if ExpireDate:
            self.ExpireDate = ExpireDate.encode("GBK")
        if WeakExpireDate:
            self.WeakExpireDate = WeakExpireDate.encode("GBK")


class BrokerUserFunction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("BrokerFunctionCode", c_char),
    ]

    def __init__(self, BrokerID=None, UserID=None, BrokerFunctionCode=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if BrokerFunctionCode:
            self.BrokerFunctionCode = BrokerFunctionCode.encode("GBK")


class TraderOffer(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("ParticipantID", c_char_Array_11),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("TraderConnectStatus", c_char),
        ("ConnectRequestDate", c_char_Array_9),
        ("ConnectRequestTime", c_char_Array_9),
        ("LastReportDate", c_char_Array_9),
        ("LastReportTime", c_char_Array_9),
        ("ConnectDate", c_char_Array_9),
        ("ConnectTime", c_char_Array_9),
        ("StartDate", c_char_Array_9),
        ("StartTime", c_char_Array_9),
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("MaxTradeID", c_char_Array_21),
        ("MaxOrderMessageReference", c_char_Array_7),
        ("OrderCancelAlg", c_char),
    ]

    def __init__(self, ExchangeID=None, TraderID=None, ParticipantID=None, Password=None, InstallID=None, OrderLocalID=None, TraderConnectStatus=None, ConnectRequestDate=None, ConnectRequestTime=None, LastReportDate=None, LastReportTime=None, ConnectDate=None, ConnectTime=None, StartDate=None, StartTime=None, TradingDay=None, BrokerID=None, MaxTradeID=None, MaxOrderMessageReference=None, OrderCancelAlg=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if TraderConnectStatus:
            self.TraderConnectStatus = TraderConnectStatus.encode("GBK")
        if ConnectRequestDate:
            self.ConnectRequestDate = ConnectRequestDate.encode("GBK")
        if ConnectRequestTime:
            self.ConnectRequestTime = ConnectRequestTime.encode("GBK")
        if LastReportDate:
            self.LastReportDate = LastReportDate.encode("GBK")
        if LastReportTime:
            self.LastReportTime = LastReportTime.encode("GBK")
        if ConnectDate:
            self.ConnectDate = ConnectDate.encode("GBK")
        if ConnectTime:
            self.ConnectTime = ConnectTime.encode("GBK")
        if StartDate:
            self.StartDate = StartDate.encode("GBK")
        if StartTime:
            self.StartTime = StartTime.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if MaxTradeID:
            self.MaxTradeID = MaxTradeID.encode("GBK")
        if MaxOrderMessageReference:
            self.MaxOrderMessageReference = MaxOrderMessageReference.encode("GBK")
        if OrderCancelAlg:
            self.OrderCancelAlg = OrderCancelAlg.encode("GBK")


class SettlementInfo(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("SequenceNo", c_int),
        ("Content", c_char_Array_501),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, TradingDay=None, SettlementID=None, BrokerID=None, InvestorID=None, SequenceNo=None, Content=None, AccountID=None, CurrencyID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if Content:
            self.Content = Content.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class InstrumentMarginRateAdjust(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, HedgeFlag=None, LongMarginRatioByMoney=None, LongMarginRatioByVolume=None, ShortMarginRatioByMoney=None, ShortMarginRatioByVolume=None, IsRelative=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume
        if IsRelative:
            self.IsRelative = IsRelative
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ExchangeMarginRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, reserve1=None, HedgeFlag=None, LongMarginRatioByMoney=None, LongMarginRatioByVolume=None, ShortMarginRatioByMoney=None, ShortMarginRatioByVolume=None, ExchangeID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ExchangeMarginRateAdjust(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("ExchLongMarginRatioByMoney", c_double),
        ("ExchLongMarginRatioByVolume", c_double),
        ("ExchShortMarginRatioByMoney", c_double),
        ("ExchShortMarginRatioByVolume", c_double),
        ("NoLongMarginRatioByMoney", c_double),
        ("NoLongMarginRatioByVolume", c_double),
        ("NoShortMarginRatioByMoney", c_double),
        ("NoShortMarginRatioByVolume", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, reserve1=None, HedgeFlag=None, LongMarginRatioByMoney=None, LongMarginRatioByVolume=None, ShortMarginRatioByMoney=None, ShortMarginRatioByVolume=None, ExchLongMarginRatioByMoney=None, ExchLongMarginRatioByVolume=None, ExchShortMarginRatioByMoney=None, ExchShortMarginRatioByVolume=None, NoLongMarginRatioByMoney=None, NoLongMarginRatioByVolume=None, NoShortMarginRatioByMoney=None, NoShortMarginRatioByVolume=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume
        if ExchLongMarginRatioByMoney:
            self.ExchLongMarginRatioByMoney = ExchLongMarginRatioByMoney
        if ExchLongMarginRatioByVolume:
            self.ExchLongMarginRatioByVolume = ExchLongMarginRatioByVolume
        if ExchShortMarginRatioByMoney:
            self.ExchShortMarginRatioByMoney = ExchShortMarginRatioByMoney
        if ExchShortMarginRatioByVolume:
            self.ExchShortMarginRatioByVolume = ExchShortMarginRatioByVolume
        if NoLongMarginRatioByMoney:
            self.NoLongMarginRatioByMoney = NoLongMarginRatioByMoney
        if NoLongMarginRatioByVolume:
            self.NoLongMarginRatioByVolume = NoLongMarginRatioByVolume
        if NoShortMarginRatioByMoney:
            self.NoShortMarginRatioByMoney = NoShortMarginRatioByMoney
        if NoShortMarginRatioByVolume:
            self.NoShortMarginRatioByVolume = NoShortMarginRatioByVolume
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ExchangeRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("FromCurrencyID", c_char_Array_4),
        ("FromCurrencyUnit", c_double),
        ("ToCurrencyID", c_char_Array_4),
        ("ExchangeRate", c_double),
    ]

    def __init__(self, BrokerID=None, FromCurrencyID=None, FromCurrencyUnit=None, ToCurrencyID=None, ExchangeRate=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if FromCurrencyID:
            self.FromCurrencyID = FromCurrencyID.encode("GBK")
        if FromCurrencyUnit:
            self.FromCurrencyUnit = FromCurrencyUnit
        if ToCurrencyID:
            self.ToCurrencyID = ToCurrencyID.encode("GBK")
        if ExchangeRate:
            self.ExchangeRate = ExchangeRate


class SettlementRef(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
    ]

    def __init__(self, TradingDay=None, SettlementID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID


class CurrentTime(Struct):
    _fields_ = [
        ("CurrDate", c_char_Array_9),
        ("CurrTime", c_char_Array_9),
        ("CurrMillisec", c_int),
        ("ActionDay", c_char_Array_9),
    ]

    def __init__(self, CurrDate=None, CurrTime=None, CurrMillisec=None, ActionDay=None):
        super().__init__()
        if CurrDate:
            self.CurrDate = CurrDate.encode("GBK")
        if CurrTime:
            self.CurrTime = CurrTime.encode("GBK")
        if CurrMillisec:
            self.CurrMillisec = CurrMillisec
        if ActionDay:
            self.ActionDay = ActionDay.encode("GBK")


class CommPhase(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("CommPhaseNo", c_short),
        ("SystemID", c_char_Array_21),
    ]

    def __init__(self, TradingDay=None, CommPhaseNo=None, SystemID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if CommPhaseNo:
            self.CommPhaseNo = CommPhaseNo
        if SystemID:
            self.SystemID = SystemID.encode("GBK")


class LoginInfo(Struct):
    _fields_ = [
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("LoginDate", c_char_Array_9),
        ("LoginTime", c_char_Array_9),
        ("reserve1", c_char_Array_16),
        ("UserProductInfo", c_char_Array_11),
        ("InterfaceProductInfo", c_char_Array_11),
        ("ProtocolInfo", c_char_Array_11),
        ("SystemName", c_char_Array_41),
        ("PasswordDeprecated", c_char_Array_41),
        ("MaxOrderRef", c_char_Array_13),
        ("SHFETime", c_char_Array_9),
        ("DCETime", c_char_Array_9),
        ("CZCETime", c_char_Array_9),
        ("FFEXTime", c_char_Array_9),
        ("MacAddress", c_char_Array_21),
        ("OneTimePassword", c_char_Array_41),
        ("INETime", c_char_Array_9),
        ("IsQryControl", c_int),
        ("LoginRemark", c_char_Array_36),
        ("Password", c_char_Array_41),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, FrontID=None, SessionID=None, BrokerID=None, UserID=None, LoginDate=None, LoginTime=None, reserve1=None, UserProductInfo=None, InterfaceProductInfo=None, ProtocolInfo=None, SystemName=None, PasswordDeprecated=None, MaxOrderRef=None, SHFETime=None, DCETime=None, CZCETime=None, FFEXTime=None, MacAddress=None, OneTimePassword=None, INETime=None, IsQryControl=None, LoginRemark=None, Password=None, IPAddress=None):
        super().__init__()
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if LoginDate:
            self.LoginDate = LoginDate.encode("GBK")
        if LoginTime:
            self.LoginTime = LoginTime.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if InterfaceProductInfo:
            self.InterfaceProductInfo = InterfaceProductInfo.encode("GBK")
        if ProtocolInfo:
            self.ProtocolInfo = ProtocolInfo.encode("GBK")
        if SystemName:
            self.SystemName = SystemName.encode("GBK")
        if PasswordDeprecated:
            self.PasswordDeprecated = PasswordDeprecated.encode("GBK")
        if MaxOrderRef:
            self.MaxOrderRef = MaxOrderRef.encode("GBK")
        if SHFETime:
            self.SHFETime = SHFETime.encode("GBK")
        if DCETime:
            self.DCETime = DCETime.encode("GBK")
        if CZCETime:
            self.CZCETime = CZCETime.encode("GBK")
        if FFEXTime:
            self.FFEXTime = FFEXTime.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if OneTimePassword:
            self.OneTimePassword = OneTimePassword.encode("GBK")
        if INETime:
            self.INETime = INETime.encode("GBK")
        if IsQryControl:
            self.IsQryControl = IsQryControl
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class LogoutAll(Struct):
    _fields_ = [
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("SystemName", c_char_Array_41),
    ]

    def __init__(self, FrontID=None, SessionID=None, SystemName=None):
        super().__init__()
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if SystemName:
            self.SystemName = SystemName.encode("GBK")


class FrontStatus(Struct):
    _fields_ = [
        ("FrontID", c_int),
        ("LastReportDate", c_char_Array_9),
        ("LastReportTime", c_char_Array_9),
        ("IsActive", c_int),
    ]

    def __init__(self, FrontID=None, LastReportDate=None, LastReportTime=None, IsActive=None):
        super().__init__()
        if FrontID:
            self.FrontID = FrontID
        if LastReportDate:
            self.LastReportDate = LastReportDate.encode("GBK")
        if LastReportTime:
            self.LastReportTime = LastReportTime.encode("GBK")
        if IsActive:
            self.IsActive = IsActive


class UserPasswordUpdate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("OldPassword", c_char_Array_41),
        ("NewPassword", c_char_Array_41),
    ]

    def __init__(self, BrokerID=None, UserID=None, OldPassword=None, NewPassword=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OldPassword:
            self.OldPassword = OldPassword.encode("GBK")
        if NewPassword:
            self.NewPassword = NewPassword.encode("GBK")


class InputOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("OrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char_Array_5),
        ("CombHedgeFlag", c_char_Array_5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int),
        ("TimeCondition", c_char),
        ("GTDDate", c_char_Array_9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("RequestID", c_int),
        ("UserForceClose", c_int),
        ("IsSwapOrder", c_int),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, OrderRef=None, UserID=None, OrderPriceType=None, Direction=None, CombOffsetFlag=None, CombHedgeFlag=None, LimitPrice=None, VolumeTotalOriginal=None, TimeCondition=None, GTDDate=None, VolumeCondition=None, MinVolume=None, ContingentCondition=None, StopPrice=None, ForceCloseReason=None, IsAutoSuspend=None, BusinessUnit=None, RequestID=None, UserForceClose=None, IsSwapOrder=None, ExchangeID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, ClientID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition.encode("GBK")
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition.encode("GBK")
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition.encode("GBK")
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason.encode("GBK")
        if IsAutoSuspend:
            self.IsAutoSuspend = IsAutoSuspend
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if UserForceClose:
            self.UserForceClose = UserForceClose
        if IsSwapOrder:
            self.IsSwapOrder = IsSwapOrder
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class Order(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("OrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char_Array_5),
        ("CombHedgeFlag", c_char_Array_5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int),
        ("TimeCondition", c_char),
        ("GTDDate", c_char_Array_9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("RequestID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("OrderSysID", c_char_Array_21),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("VolumeTraded", c_int),
        ("VolumeTotal", c_int),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("ActiveTime", c_char_Array_9),
        ("SuspendTime", c_char_Array_9),
        ("UpdateTime", c_char_Array_9),
        ("CancelTime", c_char_Array_9),
        ("ActiveTraderID", c_char_Array_21),
        ("ClearingPartID", c_char_Array_11),
        ("SequenceNo", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("UserProductInfo", c_char_Array_11),
        ("StatusMsg", c_char_Array_81),
        ("UserForceClose", c_int),
        ("ActiveUserID", c_char_Array_16),
        ("BrokerOrderSeq", c_int),
        ("RelativeOrderSysID", c_char_Array_21),
        ("ZCETotalTradedVolume", c_int),
        ("IsSwapOrder", c_int),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("reserve3", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, OrderRef=None, UserID=None, OrderPriceType=None, Direction=None, CombOffsetFlag=None, CombHedgeFlag=None, LimitPrice=None, VolumeTotalOriginal=None, TimeCondition=None, GTDDate=None, VolumeCondition=None, MinVolume=None, ContingentCondition=None, StopPrice=None, ForceCloseReason=None, IsAutoSuspend=None, BusinessUnit=None, RequestID=None, OrderLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve2=None, TraderID=None, InstallID=None, OrderSubmitStatus=None, NotifySequence=None, TradingDay=None, SettlementID=None, OrderSysID=None, OrderSource=None, OrderStatus=None, OrderType=None, VolumeTraded=None, VolumeTotal=None, InsertDate=None, InsertTime=None, ActiveTime=None, SuspendTime=None, UpdateTime=None, CancelTime=None, ActiveTraderID=None, ClearingPartID=None, SequenceNo=None, FrontID=None, SessionID=None, UserProductInfo=None, StatusMsg=None, UserForceClose=None, ActiveUserID=None, BrokerOrderSeq=None, RelativeOrderSysID=None, ZCETotalTradedVolume=None, IsSwapOrder=None, BranchID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, reserve3=None, MacAddress=None, InstrumentID=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition.encode("GBK")
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition.encode("GBK")
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition.encode("GBK")
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason.encode("GBK")
        if IsAutoSuspend:
            self.IsAutoSuspend = IsAutoSuspend
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus.encode("GBK")
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if OrderSource:
            self.OrderSource = OrderSource.encode("GBK")
        if OrderStatus:
            self.OrderStatus = OrderStatus.encode("GBK")
        if OrderType:
            self.OrderType = OrderType.encode("GBK")
        if VolumeTraded:
            self.VolumeTraded = VolumeTraded
        if VolumeTotal:
            self.VolumeTotal = VolumeTotal
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if ActiveTime:
            self.ActiveTime = ActiveTime.encode("GBK")
        if SuspendTime:
            self.SuspendTime = SuspendTime.encode("GBK")
        if UpdateTime:
            self.UpdateTime = UpdateTime.encode("GBK")
        if CancelTime:
            self.CancelTime = CancelTime.encode("GBK")
        if ActiveTraderID:
            self.ActiveTraderID = ActiveTraderID.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if UserForceClose:
            self.UserForceClose = UserForceClose
        if ActiveUserID:
            self.ActiveUserID = ActiveUserID.encode("GBK")
        if BrokerOrderSeq:
            self.BrokerOrderSeq = BrokerOrderSeq
        if RelativeOrderSysID:
            self.RelativeOrderSysID = RelativeOrderSysID.encode("GBK")
        if ZCETotalTradedVolume:
            self.ZCETotalTradedVolume = ZCETotalTradedVolume
        if IsSwapOrder:
            self.IsSwapOrder = IsSwapOrder
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if reserve3:
            self.reserve3 = reserve3.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ExchangeOrder(Struct):
    _fields_ = [
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char_Array_5),
        ("CombHedgeFlag", c_char_Array_5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int),
        ("TimeCondition", c_char),
        ("GTDDate", c_char_Array_9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("RequestID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("OrderSysID", c_char_Array_21),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("VolumeTraded", c_int),
        ("VolumeTotal", c_int),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("ActiveTime", c_char_Array_9),
        ("SuspendTime", c_char_Array_9),
        ("UpdateTime", c_char_Array_9),
        ("CancelTime", c_char_Array_9),
        ("ActiveTraderID", c_char_Array_21),
        ("ClearingPartID", c_char_Array_11),
        ("SequenceNo", c_int),
        ("BranchID", c_char_Array_9),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, OrderPriceType=None, Direction=None, CombOffsetFlag=None, CombHedgeFlag=None, LimitPrice=None, VolumeTotalOriginal=None, TimeCondition=None, GTDDate=None, VolumeCondition=None, MinVolume=None, ContingentCondition=None, StopPrice=None, ForceCloseReason=None, IsAutoSuspend=None, BusinessUnit=None, RequestID=None, OrderLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve1=None, TraderID=None, InstallID=None, OrderSubmitStatus=None, NotifySequence=None, TradingDay=None, SettlementID=None, OrderSysID=None, OrderSource=None, OrderStatus=None, OrderType=None, VolumeTraded=None, VolumeTotal=None, InsertDate=None, InsertTime=None, ActiveTime=None, SuspendTime=None, UpdateTime=None, CancelTime=None, ActiveTraderID=None, ClearingPartID=None, SequenceNo=None, BranchID=None, reserve2=None, MacAddress=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition.encode("GBK")
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition.encode("GBK")
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition.encode("GBK")
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason.encode("GBK")
        if IsAutoSuspend:
            self.IsAutoSuspend = IsAutoSuspend
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus.encode("GBK")
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if OrderSource:
            self.OrderSource = OrderSource.encode("GBK")
        if OrderStatus:
            self.OrderStatus = OrderStatus.encode("GBK")
        if OrderType:
            self.OrderType = OrderType.encode("GBK")
        if VolumeTraded:
            self.VolumeTraded = VolumeTraded
        if VolumeTotal:
            self.VolumeTotal = VolumeTotal
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if ActiveTime:
            self.ActiveTime = ActiveTime.encode("GBK")
        if SuspendTime:
            self.SuspendTime = SuspendTime.encode("GBK")
        if UpdateTime:
            self.UpdateTime = UpdateTime.encode("GBK")
        if CancelTime:
            self.CancelTime = CancelTime.encode("GBK")
        if ActiveTraderID:
            self.ActiveTraderID = ActiveTraderID.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ExchangeOrderInsertError(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, ParticipantID=None, TraderID=None, InstallID=None, OrderLocalID=None, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class InputOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OrderActionRef", c_int),
        ("OrderRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, OrderActionRef=None, OrderRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, OrderSysID=None, ActionFlag=None, LimitPrice=None, VolumeChange=None, UserID=None, reserve1=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OrderActionRef:
            self.OrderActionRef = OrderActionRef
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeChange:
            self.VolumeChange = VolumeChange
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class OrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OrderActionRef", c_int),
        ("OrderRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("StatusMsg", c_char_Array_81),
        ("reserve1", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, OrderActionRef=None, OrderRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, OrderSysID=None, ActionFlag=None, LimitPrice=None, VolumeChange=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, OrderLocalID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, StatusMsg=None, reserve1=None, BranchID=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OrderActionRef:
            self.OrderActionRef = OrderActionRef
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeChange:
            self.VolumeChange = VolumeChange
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ExchangeOrderAction(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("BranchID", c_char_Array_9),
        ("reserve1", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, ExchangeID=None, OrderSysID=None, ActionFlag=None, LimitPrice=None, VolumeChange=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, OrderLocalID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, BranchID=None, reserve1=None, MacAddress=None, IPAddress=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeChange:
            self.VolumeChange = VolumeChange
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ExchangeOrderActionError(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, OrderSysID=None, TraderID=None, InstallID=None, OrderLocalID=None, ActionLocalID=None, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class ExchangeTrade(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("TradeID", c_char_Array_21),
        ("Direction", c_char),
        ("OrderSysID", c_char_Array_21),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("TradingRole", c_char),
        ("reserve1", c_char_Array_31),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("Price", c_double),
        ("Volume", c_int),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("TradeType", c_char),
        ("PriceSource", c_char),
        ("TraderID", c_char_Array_21),
        ("OrderLocalID", c_char_Array_13),
        ("ClearingPartID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("SequenceNo", c_int),
        ("TradeSource", c_char),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, TradeID=None, Direction=None, OrderSysID=None, ParticipantID=None, ClientID=None, TradingRole=None, reserve1=None, OffsetFlag=None, HedgeFlag=None, Price=None, Volume=None, TradeDate=None, TradeTime=None, TradeType=None, PriceSource=None, TraderID=None, OrderLocalID=None, ClearingPartID=None, BusinessUnit=None, SequenceNo=None, TradeSource=None, ExchangeInstID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TradeID:
            self.TradeID = TradeID.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if TradingRole:
            self.TradingRole = TradingRole.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if Price:
            self.Price = Price
        if Volume:
            self.Volume = Volume
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if TradeType:
            self.TradeType = TradeType.encode("GBK")
        if PriceSource:
            self.PriceSource = PriceSource.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if TradeSource:
            self.TradeSource = TradeSource.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class Trade(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("OrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("ExchangeID", c_char_Array_9),
        ("TradeID", c_char_Array_21),
        ("Direction", c_char),
        ("OrderSysID", c_char_Array_21),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("TradingRole", c_char),
        ("reserve2", c_char_Array_31),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("Price", c_double),
        ("Volume", c_int),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("TradeType", c_char),
        ("PriceSource", c_char),
        ("TraderID", c_char_Array_21),
        ("OrderLocalID", c_char_Array_13),
        ("ClearingPartID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("SequenceNo", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("BrokerOrderSeq", c_int),
        ("TradeSource", c_char),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, OrderRef=None, UserID=None, ExchangeID=None, TradeID=None, Direction=None, OrderSysID=None, ParticipantID=None, ClientID=None, TradingRole=None, reserve2=None, OffsetFlag=None, HedgeFlag=None, Price=None, Volume=None, TradeDate=None, TradeTime=None, TradeType=None, PriceSource=None, TraderID=None, OrderLocalID=None, ClearingPartID=None, BusinessUnit=None, SequenceNo=None, TradingDay=None, SettlementID=None, BrokerOrderSeq=None, TradeSource=None, InvestUnitID=None, InstrumentID=None, ExchangeInstID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TradeID:
            self.TradeID = TradeID.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if TradingRole:
            self.TradingRole = TradingRole.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if Price:
            self.Price = Price
        if Volume:
            self.Volume = Volume
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if TradeType:
            self.TradeType = TradeType.encode("GBK")
        if PriceSource:
            self.PriceSource = PriceSource.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if BrokerOrderSeq:
            self.BrokerOrderSeq = BrokerOrderSeq
        if TradeSource:
            self.TradeSource = TradeSource.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class UserSession(Struct):
    _fields_ = [
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("LoginDate", c_char_Array_9),
        ("LoginTime", c_char_Array_9),
        ("reserve1", c_char_Array_16),
        ("UserProductInfo", c_char_Array_11),
        ("InterfaceProductInfo", c_char_Array_11),
        ("ProtocolInfo", c_char_Array_11),
        ("MacAddress", c_char_Array_21),
        ("LoginRemark", c_char_Array_36),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, FrontID=None, SessionID=None, BrokerID=None, UserID=None, LoginDate=None, LoginTime=None, reserve1=None, UserProductInfo=None, InterfaceProductInfo=None, ProtocolInfo=None, MacAddress=None, LoginRemark=None, IPAddress=None):
        super().__init__()
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if LoginDate:
            self.LoginDate = LoginDate.encode("GBK")
        if LoginTime:
            self.LoginTime = LoginTime.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if InterfaceProductInfo:
            self.InterfaceProductInfo = InterfaceProductInfo.encode("GBK")
        if ProtocolInfo:
            self.ProtocolInfo = ProtocolInfo.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryMaxOrderVolume(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("MaxVolume", c_int),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, Direction=None, OffsetFlag=None, HedgeFlag=None, MaxVolume=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if MaxVolume:
            self.MaxVolume = MaxVolume
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class SettlementInfoConfirm(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ConfirmDate", c_char_Array_9),
        ("ConfirmTime", c_char_Array_9),
        ("SettlementID", c_int),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ConfirmDate=None, ConfirmTime=None, SettlementID=None, AccountID=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ConfirmDate:
            self.ConfirmDate = ConfirmDate.encode("GBK")
        if ConfirmTime:
            self.ConfirmTime = ConfirmTime.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class SyncDeposit(Struct):
    _fields_ = [
        ("DepositSeqNo", c_char_Array_15),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Deposit", c_double),
        ("IsForce", c_int),
        ("CurrencyID", c_char_Array_4),
        ("IsFromSopt", c_int),
        ("TradingPassword", c_char_Array_41),
    ]

    def __init__(self, DepositSeqNo=None, BrokerID=None, InvestorID=None, Deposit=None, IsForce=None, CurrencyID=None, IsFromSopt=None, TradingPassword=None):
        super().__init__()
        if DepositSeqNo:
            self.DepositSeqNo = DepositSeqNo.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Deposit:
            self.Deposit = Deposit
        if IsForce:
            self.IsForce = IsForce
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if IsFromSopt:
            self.IsFromSopt = IsFromSopt
        if TradingPassword:
            self.TradingPassword = TradingPassword.encode("GBK")


class SyncFundMortgage(Struct):
    _fields_ = [
        ("MortgageSeqNo", c_char_Array_15),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("FromCurrencyID", c_char_Array_4),
        ("MortgageAmount", c_double),
        ("ToCurrencyID", c_char_Array_4),
    ]

    def __init__(self, MortgageSeqNo=None, BrokerID=None, InvestorID=None, FromCurrencyID=None, MortgageAmount=None, ToCurrencyID=None):
        super().__init__()
        if MortgageSeqNo:
            self.MortgageSeqNo = MortgageSeqNo.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if FromCurrencyID:
            self.FromCurrencyID = FromCurrencyID.encode("GBK")
        if MortgageAmount:
            self.MortgageAmount = MortgageAmount
        if ToCurrencyID:
            self.ToCurrencyID = ToCurrencyID.encode("GBK")


class BrokerSync(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
    ]

    def __init__(self, BrokerID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")


class SyncingInvestor(Struct):
    _fields_ = [
        ("InvestorID", c_char_Array_13),
        ("BrokerID", c_char_Array_11),
        ("InvestorGroupID", c_char_Array_13),
        ("InvestorName", c_char_Array_81),
        ("IdentifiedCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("IsActive", c_int),
        ("Telephone", c_char_Array_41),
        ("Address", c_char_Array_101),
        ("OpenDate", c_char_Array_9),
        ("Mobile", c_char_Array_41),
        ("CommModelID", c_char_Array_13),
        ("MarginModelID", c_char_Array_13),
        ("IsOrderFreq", c_char),
        ("IsOpenVolLimit", c_char),
    ]

    def __init__(self, InvestorID=None, BrokerID=None, InvestorGroupID=None, InvestorName=None, IdentifiedCardType=None, IdentifiedCardNo=None, IsActive=None, Telephone=None, Address=None, OpenDate=None, Mobile=None, CommModelID=None, MarginModelID=None, IsOrderFreq=None, IsOpenVolLimit=None):
        super().__init__()
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorGroupID:
            self.InvestorGroupID = InvestorGroupID.encode("GBK")
        if InvestorName:
            self.InvestorName = InvestorName.encode("GBK")
        if IdentifiedCardType:
            self.IdentifiedCardType = IdentifiedCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if IsActive:
            self.IsActive = IsActive
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if OpenDate:
            self.OpenDate = OpenDate.encode("GBK")
        if Mobile:
            self.Mobile = Mobile.encode("GBK")
        if CommModelID:
            self.CommModelID = CommModelID.encode("GBK")
        if MarginModelID:
            self.MarginModelID = MarginModelID.encode("GBK")
        if IsOrderFreq:
            self.IsOrderFreq = IsOrderFreq.encode("GBK")
        if IsOpenVolLimit:
            self.IsOpenVolLimit = IsOpenVolLimit.encode("GBK")


class SyncingTradingCode(Struct):
    _fields_ = [
        ("InvestorID", c_char_Array_13),
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("ClientID", c_char_Array_11),
        ("IsActive", c_int),
        ("ClientIDType", c_char),
    ]

    def __init__(self, InvestorID=None, BrokerID=None, ExchangeID=None, ClientID=None, IsActive=None, ClientIDType=None):
        super().__init__()
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if IsActive:
            self.IsActive = IsActive
        if ClientIDType:
            self.ClientIDType = ClientIDType.encode("GBK")


class SyncingInvestorGroup(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorGroupID", c_char_Array_13),
        ("InvestorGroupName", c_char_Array_41),
    ]

    def __init__(self, BrokerID=None, InvestorGroupID=None, InvestorGroupName=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorGroupID:
            self.InvestorGroupID = InvestorGroupID.encode("GBK")
        if InvestorGroupName:
            self.InvestorGroupName = InvestorGroupName.encode("GBK")


class SyncingTradingAccount(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("PreMortgage", c_double),
        ("PreCredit", c_double),
        ("PreDeposit", c_double),
        ("PreBalance", c_double),
        ("PreMargin", c_double),
        ("InterestBase", c_double),
        ("Interest", c_double),
        ("Deposit", c_double),
        ("Withdraw", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CurrMargin", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("Balance", c_double),
        ("Available", c_double),
        ("WithdrawQuota", c_double),
        ("Reserve", c_double),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("Credit", c_double),
        ("Mortgage", c_double),
        ("ExchangeMargin", c_double),
        ("DeliveryMargin", c_double),
        ("ExchangeDeliveryMargin", c_double),
        ("ReserveBalance", c_double),
        ("CurrencyID", c_char_Array_4),
        ("PreFundMortgageIn", c_double),
        ("PreFundMortgageOut", c_double),
        ("FundMortgageIn", c_double),
        ("FundMortgageOut", c_double),
        ("FundMortgageAvailable", c_double),
        ("MortgageableFund", c_double),
        ("SpecProductMargin", c_double),
        ("SpecProductFrozenMargin", c_double),
        ("SpecProductCommission", c_double),
        ("SpecProductFrozenCommission", c_double),
        ("SpecProductPositionProfit", c_double),
        ("SpecProductCloseProfit", c_double),
        ("SpecProductPositionProfitByAlg", c_double),
        ("SpecProductExchangeMargin", c_double),
        ("FrozenSwap", c_double),
        ("RemainSwap", c_double),
    ]

    def __init__(self, BrokerID=None, AccountID=None, PreMortgage=None, PreCredit=None, PreDeposit=None, PreBalance=None, PreMargin=None, InterestBase=None, Interest=None, Deposit=None, Withdraw=None, FrozenMargin=None, FrozenCash=None, FrozenCommission=None, CurrMargin=None, CashIn=None, Commission=None, CloseProfit=None, PositionProfit=None, Balance=None, Available=None, WithdrawQuota=None, Reserve=None, TradingDay=None, SettlementID=None, Credit=None, Mortgage=None, ExchangeMargin=None, DeliveryMargin=None, ExchangeDeliveryMargin=None, ReserveBalance=None, CurrencyID=None, PreFundMortgageIn=None, PreFundMortgageOut=None, FundMortgageIn=None, FundMortgageOut=None, FundMortgageAvailable=None, MortgageableFund=None, SpecProductMargin=None, SpecProductFrozenMargin=None, SpecProductCommission=None, SpecProductFrozenCommission=None, SpecProductPositionProfit=None, SpecProductCloseProfit=None, SpecProductPositionProfitByAlg=None, SpecProductExchangeMargin=None, FrozenSwap=None, RemainSwap=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if PreMortgage:
            self.PreMortgage = PreMortgage
        if PreCredit:
            self.PreCredit = PreCredit
        if PreDeposit:
            self.PreDeposit = PreDeposit
        if PreBalance:
            self.PreBalance = PreBalance
        if PreMargin:
            self.PreMargin = PreMargin
        if InterestBase:
            self.InterestBase = InterestBase
        if Interest:
            self.Interest = Interest
        if Deposit:
            self.Deposit = Deposit
        if Withdraw:
            self.Withdraw = Withdraw
        if FrozenMargin:
            self.FrozenMargin = FrozenMargin
        if FrozenCash:
            self.FrozenCash = FrozenCash
        if FrozenCommission:
            self.FrozenCommission = FrozenCommission
        if CurrMargin:
            self.CurrMargin = CurrMargin
        if CashIn:
            self.CashIn = CashIn
        if Commission:
            self.Commission = Commission
        if CloseProfit:
            self.CloseProfit = CloseProfit
        if PositionProfit:
            self.PositionProfit = PositionProfit
        if Balance:
            self.Balance = Balance
        if Available:
            self.Available = Available
        if WithdrawQuota:
            self.WithdrawQuota = WithdrawQuota
        if Reserve:
            self.Reserve = Reserve
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if Credit:
            self.Credit = Credit
        if Mortgage:
            self.Mortgage = Mortgage
        if ExchangeMargin:
            self.ExchangeMargin = ExchangeMargin
        if DeliveryMargin:
            self.DeliveryMargin = DeliveryMargin
        if ExchangeDeliveryMargin:
            self.ExchangeDeliveryMargin = ExchangeDeliveryMargin
        if ReserveBalance:
            self.ReserveBalance = ReserveBalance
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if PreFundMortgageIn:
            self.PreFundMortgageIn = PreFundMortgageIn
        if PreFundMortgageOut:
            self.PreFundMortgageOut = PreFundMortgageOut
        if FundMortgageIn:
            self.FundMortgageIn = FundMortgageIn
        if FundMortgageOut:
            self.FundMortgageOut = FundMortgageOut
        if FundMortgageAvailable:
            self.FundMortgageAvailable = FundMortgageAvailable
        if MortgageableFund:
            self.MortgageableFund = MortgageableFund
        if SpecProductMargin:
            self.SpecProductMargin = SpecProductMargin
        if SpecProductFrozenMargin:
            self.SpecProductFrozenMargin = SpecProductFrozenMargin
        if SpecProductCommission:
            self.SpecProductCommission = SpecProductCommission
        if SpecProductFrozenCommission:
            self.SpecProductFrozenCommission = SpecProductFrozenCommission
        if SpecProductPositionProfit:
            self.SpecProductPositionProfit = SpecProductPositionProfit
        if SpecProductCloseProfit:
            self.SpecProductCloseProfit = SpecProductCloseProfit
        if SpecProductPositionProfitByAlg:
            self.SpecProductPositionProfitByAlg = SpecProductPositionProfitByAlg
        if SpecProductExchangeMargin:
            self.SpecProductExchangeMargin = SpecProductExchangeMargin
        if FrozenSwap:
            self.FrozenSwap = FrozenSwap
        if RemainSwap:
            self.RemainSwap = RemainSwap


class SyncingInvestorPosition(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("PosiDirection", c_char),
        ("HedgeFlag", c_char),
        ("PositionDate", c_char),
        ("YdPosition", c_int),
        ("Position", c_int),
        ("LongFrozen", c_int),
        ("ShortFrozen", c_int),
        ("LongFrozenAmount", c_double),
        ("ShortFrozenAmount", c_double),
        ("OpenVolume", c_int),
        ("CloseVolume", c_int),
        ("OpenAmount", c_double),
        ("CloseAmount", c_double),
        ("PositionCost", c_double),
        ("PreMargin", c_double),
        ("UseMargin", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("PreSettlementPrice", c_double),
        ("SettlementPrice", c_double),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("OpenCost", c_double),
        ("ExchangeMargin", c_double),
        ("CombPosition", c_int),
        ("CombLongFrozen", c_int),
        ("CombShortFrozen", c_int),
        ("CloseProfitByDate", c_double),
        ("CloseProfitByTrade", c_double),
        ("TodayPosition", c_int),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("StrikeFrozen", c_int),
        ("StrikeFrozenAmount", c_double),
        ("AbandonFrozen", c_int),
        ("ExchangeID", c_char_Array_9),
        ("YdStrikeFrozen", c_int),
        ("InvestUnitID", c_char_Array_17),
        ("PositionCostOffset", c_double),
        ("TasPosition", c_int),
        ("TasPositionCost", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, BrokerID=None, InvestorID=None, PosiDirection=None, HedgeFlag=None, PositionDate=None, YdPosition=None, Position=None, LongFrozen=None, ShortFrozen=None, LongFrozenAmount=None, ShortFrozenAmount=None, OpenVolume=None, CloseVolume=None, OpenAmount=None, CloseAmount=None, PositionCost=None, PreMargin=None, UseMargin=None, FrozenMargin=None, FrozenCash=None, FrozenCommission=None, CashIn=None, Commission=None, CloseProfit=None, PositionProfit=None, PreSettlementPrice=None, SettlementPrice=None, TradingDay=None, SettlementID=None, OpenCost=None, ExchangeMargin=None, CombPosition=None, CombLongFrozen=None, CombShortFrozen=None, CloseProfitByDate=None, CloseProfitByTrade=None, TodayPosition=None, MarginRateByMoney=None, MarginRateByVolume=None, StrikeFrozen=None, StrikeFrozenAmount=None, AbandonFrozen=None, ExchangeID=None, YdStrikeFrozen=None, InvestUnitID=None, PositionCostOffset=None, TasPosition=None, TasPositionCost=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if PosiDirection:
            self.PosiDirection = PosiDirection.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if PositionDate:
            self.PositionDate = PositionDate.encode("GBK")
        if YdPosition:
            self.YdPosition = YdPosition
        if Position:
            self.Position = Position
        if LongFrozen:
            self.LongFrozen = LongFrozen
        if ShortFrozen:
            self.ShortFrozen = ShortFrozen
        if LongFrozenAmount:
            self.LongFrozenAmount = LongFrozenAmount
        if ShortFrozenAmount:
            self.ShortFrozenAmount = ShortFrozenAmount
        if OpenVolume:
            self.OpenVolume = OpenVolume
        if CloseVolume:
            self.CloseVolume = CloseVolume
        if OpenAmount:
            self.OpenAmount = OpenAmount
        if CloseAmount:
            self.CloseAmount = CloseAmount
        if PositionCost:
            self.PositionCost = PositionCost
        if PreMargin:
            self.PreMargin = PreMargin
        if UseMargin:
            self.UseMargin = UseMargin
        if FrozenMargin:
            self.FrozenMargin = FrozenMargin
        if FrozenCash:
            self.FrozenCash = FrozenCash
        if FrozenCommission:
            self.FrozenCommission = FrozenCommission
        if CashIn:
            self.CashIn = CashIn
        if Commission:
            self.Commission = Commission
        if CloseProfit:
            self.CloseProfit = CloseProfit
        if PositionProfit:
            self.PositionProfit = PositionProfit
        if PreSettlementPrice:
            self.PreSettlementPrice = PreSettlementPrice
        if SettlementPrice:
            self.SettlementPrice = SettlementPrice
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OpenCost:
            self.OpenCost = OpenCost
        if ExchangeMargin:
            self.ExchangeMargin = ExchangeMargin
        if CombPosition:
            self.CombPosition = CombPosition
        if CombLongFrozen:
            self.CombLongFrozen = CombLongFrozen
        if CombShortFrozen:
            self.CombShortFrozen = CombShortFrozen
        if CloseProfitByDate:
            self.CloseProfitByDate = CloseProfitByDate
        if CloseProfitByTrade:
            self.CloseProfitByTrade = CloseProfitByTrade
        if TodayPosition:
            self.TodayPosition = TodayPosition
        if MarginRateByMoney:
            self.MarginRateByMoney = MarginRateByMoney
        if MarginRateByVolume:
            self.MarginRateByVolume = MarginRateByVolume
        if StrikeFrozen:
            self.StrikeFrozen = StrikeFrozen
        if StrikeFrozenAmount:
            self.StrikeFrozenAmount = StrikeFrozenAmount
        if AbandonFrozen:
            self.AbandonFrozen = AbandonFrozen
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if YdStrikeFrozen:
            self.YdStrikeFrozen = YdStrikeFrozen
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if PositionCostOffset:
            self.PositionCostOffset = PositionCostOffset
        if TasPosition:
            self.TasPosition = TasPosition
        if TasPositionCost:
            self.TasPositionCost = TasPositionCost
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class SyncingInstrumentMarginRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, HedgeFlag=None, LongMarginRatioByMoney=None, LongMarginRatioByVolume=None, ShortMarginRatioByMoney=None, ShortMarginRatioByVolume=None, IsRelative=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume
        if IsRelative:
            self.IsRelative = IsRelative
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class SyncingInstrumentCommissionRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, OpenRatioByMoney=None, OpenRatioByVolume=None, CloseRatioByMoney=None, CloseRatioByVolume=None, CloseTodayRatioByMoney=None, CloseTodayRatioByVolume=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OpenRatioByMoney:
            self.OpenRatioByMoney = OpenRatioByMoney
        if OpenRatioByVolume:
            self.OpenRatioByVolume = OpenRatioByVolume
        if CloseRatioByMoney:
            self.CloseRatioByMoney = CloseRatioByMoney
        if CloseRatioByVolume:
            self.CloseRatioByVolume = CloseRatioByVolume
        if CloseTodayRatioByMoney:
            self.CloseTodayRatioByMoney = CloseTodayRatioByMoney
        if CloseTodayRatioByVolume:
            self.CloseTodayRatioByVolume = CloseTodayRatioByVolume
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class SyncingInstrumentTradingRight(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("TradingRight", c_char),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, TradingRight=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if TradingRight:
            self.TradingRight = TradingRight.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, OrderSysID=None, InsertTimeStart=None, InsertTimeEnd=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if InsertTimeStart:
            self.InsertTimeStart = InsertTimeStart.encode("GBK")
        if InsertTimeEnd:
            self.InsertTimeEnd = InsertTimeEnd.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryTrade(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TradeID", c_char_Array_21),
        ("TradeTimeStart", c_char_Array_9),
        ("TradeTimeEnd", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, TradeID=None, TradeTimeStart=None, TradeTimeEnd=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TradeID:
            self.TradeID = TradeID.encode("GBK")
        if TradeTimeStart:
            self.TradeTimeStart = TradeTimeStart.encode("GBK")
        if TradeTimeEnd:
            self.TradeTimeEnd = TradeTimeEnd.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryInvestorPosition(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryTradingAccount(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("BizType", c_char),
        ("AccountID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, CurrencyID=None, BizType=None, AccountID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if BizType:
            self.BizType = BizType.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")


class QryInvestor(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class QryTradingCode(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ClientID", c_char_Array_11),
        ("ClientIDType", c_char),
        ("InvestUnitID", c_char_Array_17),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExchangeID=None, ClientID=None, ClientIDType=None, InvestUnitID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ClientIDType:
            self.ClientIDType = ClientIDType.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryInvestorGroup(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
    ]

    def __init__(self, BrokerID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")


class QryInstrumentMarginRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, HedgeFlag=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryInstrumentCommissionRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryInstrumentTradingRight(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryBroker(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
    ]

    def __init__(self, BrokerID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")


class QryTrader(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("TraderID", c_char_Array_21),
    ]

    def __init__(self, ExchangeID=None, ParticipantID=None, TraderID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class QrySuperUserFunction(Struct):
    _fields_ = [
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, UserID=None):
        super().__init__()
        if UserID:
            self.UserID = UserID.encode("GBK")


class QryUserSession(Struct):
    _fields_ = [
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, FrontID=None, SessionID=None, BrokerID=None, UserID=None):
        super().__init__()
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class QryPartBroker(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("ParticipantID", c_char_Array_11),
    ]

    def __init__(self, ExchangeID=None, BrokerID=None, ParticipantID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")


class QryFrontStatus(Struct):
    _fields_ = [
        ("FrontID", c_int),
    ]

    def __init__(self, FrontID=None):
        super().__init__()
        if FrontID:
            self.FrontID = FrontID


class QryExchangeOrder(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, ParticipantID=None, ClientID=None, reserve1=None, ExchangeID=None, TraderID=None, ExchangeInstID=None):
        super().__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class QryOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExchangeID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class QryExchangeOrderAction(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

    def __init__(self, ParticipantID=None, ClientID=None, ExchangeID=None, TraderID=None):
        super().__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class QrySuperUser(Struct):
    _fields_ = [
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, UserID=None):
        super().__init__()
        if UserID:
            self.UserID = UserID.encode("GBK")


class QryExchange(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, ExchangeID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class QryProduct(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("ProductClass", c_char),
        ("ExchangeID", c_char_Array_9),
        ("ProductID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, ProductClass=None, ExchangeID=None, ProductID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ProductClass:
            self.ProductClass = ProductClass.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")


class QryInstrument(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("reserve2", c_char_Array_31),
        ("reserve3", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("ProductID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, ExchangeID=None, reserve2=None, reserve3=None, InstrumentID=None, ExchangeInstID=None, ProductID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if reserve3:
            self.reserve3 = reserve3.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")


class QryDepthMarketData(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, ExchangeID=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryBrokerUser(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, BrokerID=None, UserID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class QryBrokerUserFunction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, BrokerID=None, UserID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class QryTraderOffer(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("TraderID", c_char_Array_21),
    ]

    def __init__(self, ExchangeID=None, ParticipantID=None, TraderID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class QrySyncDeposit(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("DepositSeqNo", c_char_Array_15),
    ]

    def __init__(self, BrokerID=None, DepositSeqNo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if DepositSeqNo:
            self.DepositSeqNo = DepositSeqNo.encode("GBK")


class QrySettlementInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, TradingDay=None, AccountID=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class QryExchangeMarginRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, reserve1=None, HedgeFlag=None, ExchangeID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryExchangeMarginRateAdjust(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, reserve1=None, HedgeFlag=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryExchangeRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("FromCurrencyID", c_char_Array_4),
        ("ToCurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, FromCurrencyID=None, ToCurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if FromCurrencyID:
            self.FromCurrencyID = FromCurrencyID.encode("GBK")
        if ToCurrencyID:
            self.ToCurrencyID = ToCurrencyID.encode("GBK")


class QrySyncFundMortgage(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("MortgageSeqNo", c_char_Array_15),
    ]

    def __init__(self, BrokerID=None, MortgageSeqNo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if MortgageSeqNo:
            self.MortgageSeqNo = MortgageSeqNo.encode("GBK")


class QryHisOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, OrderSysID=None, InsertTimeStart=None, InsertTimeEnd=None, TradingDay=None, SettlementID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if InsertTimeStart:
            self.InsertTimeStart = InsertTimeStart.encode("GBK")
        if InsertTimeEnd:
            self.InsertTimeEnd = InsertTimeEnd.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class OptionInstrMiniMargin(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("MinMargin", c_double),
        ("ValueMethod", c_char),
        ("IsRelative", c_int),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, MinMargin=None, ValueMethod=None, IsRelative=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if MinMargin:
            self.MinMargin = MinMargin
        if ValueMethod:
            self.ValueMethod = ValueMethod.encode("GBK")
        if IsRelative:
            self.IsRelative = IsRelative
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class OptionInstrMarginAdjust(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("SShortMarginRatioByMoney", c_double),
        ("SShortMarginRatioByVolume", c_double),
        ("HShortMarginRatioByMoney", c_double),
        ("HShortMarginRatioByVolume", c_double),
        ("AShortMarginRatioByMoney", c_double),
        ("AShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int),
        ("MShortMarginRatioByMoney", c_double),
        ("MShortMarginRatioByVolume", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, SShortMarginRatioByMoney=None, SShortMarginRatioByVolume=None, HShortMarginRatioByMoney=None, HShortMarginRatioByVolume=None, AShortMarginRatioByMoney=None, AShortMarginRatioByVolume=None, IsRelative=None, MShortMarginRatioByMoney=None, MShortMarginRatioByVolume=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if SShortMarginRatioByMoney:
            self.SShortMarginRatioByMoney = SShortMarginRatioByMoney
        if SShortMarginRatioByVolume:
            self.SShortMarginRatioByVolume = SShortMarginRatioByVolume
        if HShortMarginRatioByMoney:
            self.HShortMarginRatioByMoney = HShortMarginRatioByMoney
        if HShortMarginRatioByVolume:
            self.HShortMarginRatioByVolume = HShortMarginRatioByVolume
        if AShortMarginRatioByMoney:
            self.AShortMarginRatioByMoney = AShortMarginRatioByMoney
        if AShortMarginRatioByVolume:
            self.AShortMarginRatioByVolume = AShortMarginRatioByVolume
        if IsRelative:
            self.IsRelative = IsRelative
        if MShortMarginRatioByMoney:
            self.MShortMarginRatioByMoney = MShortMarginRatioByMoney
        if MShortMarginRatioByVolume:
            self.MShortMarginRatioByVolume = MShortMarginRatioByVolume
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class OptionInstrCommRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("StrikeRatioByMoney", c_double),
        ("StrikeRatioByVolume", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, OpenRatioByMoney=None, OpenRatioByVolume=None, CloseRatioByMoney=None, CloseRatioByVolume=None, CloseTodayRatioByMoney=None, CloseTodayRatioByVolume=None, StrikeRatioByMoney=None, StrikeRatioByVolume=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OpenRatioByMoney:
            self.OpenRatioByMoney = OpenRatioByMoney
        if OpenRatioByVolume:
            self.OpenRatioByVolume = OpenRatioByVolume
        if CloseRatioByMoney:
            self.CloseRatioByMoney = CloseRatioByMoney
        if CloseRatioByVolume:
            self.CloseRatioByVolume = CloseRatioByVolume
        if CloseTodayRatioByMoney:
            self.CloseTodayRatioByMoney = CloseTodayRatioByMoney
        if CloseTodayRatioByVolume:
            self.CloseTodayRatioByVolume = CloseTodayRatioByVolume
        if StrikeRatioByMoney:
            self.StrikeRatioByMoney = StrikeRatioByMoney
        if StrikeRatioByVolume:
            self.StrikeRatioByVolume = StrikeRatioByVolume
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class OptionInstrTradeCost(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("FixedMargin", c_double),
        ("MiniMargin", c_double),
        ("Royalty", c_double),
        ("ExchFixedMargin", c_double),
        ("ExchMiniMargin", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, HedgeFlag=None, FixedMargin=None, MiniMargin=None, Royalty=None, ExchFixedMargin=None, ExchMiniMargin=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if FixedMargin:
            self.FixedMargin = FixedMargin
        if MiniMargin:
            self.MiniMargin = MiniMargin
        if Royalty:
            self.Royalty = Royalty
        if ExchFixedMargin:
            self.ExchFixedMargin = ExchFixedMargin
        if ExchMiniMargin:
            self.ExchMiniMargin = ExchMiniMargin
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryOptionInstrTradeCost(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("InputPrice", c_double),
        ("UnderlyingPrice", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, HedgeFlag=None, InputPrice=None, UnderlyingPrice=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if InputPrice:
            self.InputPrice = InputPrice
        if UnderlyingPrice:
            self.UnderlyingPrice = UnderlyingPrice
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryOptionInstrCommRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class IndexPrice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("ClosePrice", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, reserve1=None, ClosePrice=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ClosePrice:
            self.ClosePrice = ClosePrice
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InputExecOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExecOrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("Volume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExecOrderRef=None, UserID=None, Volume=None, RequestID=None, BusinessUnit=None, OffsetFlag=None, HedgeFlag=None, ActionType=None, PosiDirection=None, ReservePositionFlag=None, CloseFlag=None, ExchangeID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, ClientID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExecOrderRef:
            self.ExecOrderRef = ExecOrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Volume:
            self.Volume = Volume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ActionType:
            self.ActionType = ActionType.encode("GBK")
        if PosiDirection:
            self.PosiDirection = PosiDirection.encode("GBK")
        if ReservePositionFlag:
            self.ReservePositionFlag = ReservePositionFlag.encode("GBK")
        if CloseFlag:
            self.CloseFlag = CloseFlag.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class InputExecOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExecOrderActionRef", c_int),
        ("ExecOrderRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("ExecOrderSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExecOrderActionRef=None, ExecOrderRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, ExecOrderSysID=None, ActionFlag=None, UserID=None, reserve1=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExecOrderActionRef:
            self.ExecOrderActionRef = ExecOrderActionRef
        if ExecOrderRef:
            self.ExecOrderRef = ExecOrderRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExecOrderSysID:
            self.ExecOrderSysID = ExecOrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ExecOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExecOrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("Volume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExecOrderLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("ExecOrderSysID", c_char_Array_21),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("CancelTime", c_char_Array_9),
        ("ExecResult", c_char),
        ("ClearingPartID", c_char_Array_11),
        ("SequenceNo", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("UserProductInfo", c_char_Array_11),
        ("StatusMsg", c_char_Array_81),
        ("ActiveUserID", c_char_Array_16),
        ("BrokerExecOrderSeq", c_int),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("reserve3", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExecOrderRef=None, UserID=None, Volume=None, RequestID=None, BusinessUnit=None, OffsetFlag=None, HedgeFlag=None, ActionType=None, PosiDirection=None, ReservePositionFlag=None, CloseFlag=None, ExecOrderLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve2=None, TraderID=None, InstallID=None, OrderSubmitStatus=None, NotifySequence=None, TradingDay=None, SettlementID=None, ExecOrderSysID=None, InsertDate=None, InsertTime=None, CancelTime=None, ExecResult=None, ClearingPartID=None, SequenceNo=None, FrontID=None, SessionID=None, UserProductInfo=None, StatusMsg=None, ActiveUserID=None, BrokerExecOrderSeq=None, BranchID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, reserve3=None, MacAddress=None, InstrumentID=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExecOrderRef:
            self.ExecOrderRef = ExecOrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Volume:
            self.Volume = Volume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ActionType:
            self.ActionType = ActionType.encode("GBK")
        if PosiDirection:
            self.PosiDirection = PosiDirection.encode("GBK")
        if ReservePositionFlag:
            self.ReservePositionFlag = ReservePositionFlag.encode("GBK")
        if CloseFlag:
            self.CloseFlag = CloseFlag.encode("GBK")
        if ExecOrderLocalID:
            self.ExecOrderLocalID = ExecOrderLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus.encode("GBK")
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if ExecOrderSysID:
            self.ExecOrderSysID = ExecOrderSysID.encode("GBK")
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if CancelTime:
            self.CancelTime = CancelTime.encode("GBK")
        if ExecResult:
            self.ExecResult = ExecResult.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if ActiveUserID:
            self.ActiveUserID = ActiveUserID.encode("GBK")
        if BrokerExecOrderSeq:
            self.BrokerExecOrderSeq = BrokerExecOrderSeq
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if reserve3:
            self.reserve3 = reserve3.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ExecOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExecOrderActionRef", c_int),
        ("ExecOrderRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("ExecOrderSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("ExecOrderLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("ActionType", c_char),
        ("StatusMsg", c_char_Array_81),
        ("reserve1", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExecOrderActionRef=None, ExecOrderRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, ExecOrderSysID=None, ActionFlag=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, ExecOrderLocalID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, ActionType=None, StatusMsg=None, reserve1=None, BranchID=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExecOrderActionRef:
            self.ExecOrderActionRef = ExecOrderActionRef
        if ExecOrderRef:
            self.ExecOrderRef = ExecOrderRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExecOrderSysID:
            self.ExecOrderSysID = ExecOrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if ExecOrderLocalID:
            self.ExecOrderLocalID = ExecOrderLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ActionType:
            self.ActionType = ActionType.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryExecOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("ExecOrderSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, ExecOrderSysID=None, InsertTimeStart=None, InsertTimeEnd=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExecOrderSysID:
            self.ExecOrderSysID = ExecOrderSysID.encode("GBK")
        if InsertTimeStart:
            self.InsertTimeStart = InsertTimeStart.encode("GBK")
        if InsertTimeEnd:
            self.InsertTimeEnd = InsertTimeEnd.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ExchangeExecOrder(Struct):
    _fields_ = [
        ("Volume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExecOrderLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("ExecOrderSysID", c_char_Array_21),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("CancelTime", c_char_Array_9),
        ("ExecResult", c_char),
        ("ClearingPartID", c_char_Array_11),
        ("SequenceNo", c_int),
        ("BranchID", c_char_Array_9),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, Volume=None, RequestID=None, BusinessUnit=None, OffsetFlag=None, HedgeFlag=None, ActionType=None, PosiDirection=None, ReservePositionFlag=None, CloseFlag=None, ExecOrderLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve1=None, TraderID=None, InstallID=None, OrderSubmitStatus=None, NotifySequence=None, TradingDay=None, SettlementID=None, ExecOrderSysID=None, InsertDate=None, InsertTime=None, CancelTime=None, ExecResult=None, ClearingPartID=None, SequenceNo=None, BranchID=None, reserve2=None, MacAddress=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if Volume:
            self.Volume = Volume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ActionType:
            self.ActionType = ActionType.encode("GBK")
        if PosiDirection:
            self.PosiDirection = PosiDirection.encode("GBK")
        if ReservePositionFlag:
            self.ReservePositionFlag = ReservePositionFlag.encode("GBK")
        if CloseFlag:
            self.CloseFlag = CloseFlag.encode("GBK")
        if ExecOrderLocalID:
            self.ExecOrderLocalID = ExecOrderLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus.encode("GBK")
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if ExecOrderSysID:
            self.ExecOrderSysID = ExecOrderSysID.encode("GBK")
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if CancelTime:
            self.CancelTime = CancelTime.encode("GBK")
        if ExecResult:
            self.ExecResult = ExecResult.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryExchangeExecOrder(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, ParticipantID=None, ClientID=None, reserve1=None, ExchangeID=None, TraderID=None, ExchangeInstID=None):
        super().__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class QryExecOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExchangeID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class ExchangeExecOrderAction(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ExecOrderSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("ExecOrderLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("ActionType", c_char),
        ("BranchID", c_char_Array_9),
        ("reserve1", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("reserve2", c_char_Array_31),
        ("Volume", c_int),
        ("IPAddress", c_char_Array_33),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, ExecOrderSysID=None, ActionFlag=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, ExecOrderLocalID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, ActionType=None, BranchID=None, reserve1=None, MacAddress=None, reserve2=None, Volume=None, IPAddress=None, ExchangeInstID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExecOrderSysID:
            self.ExecOrderSysID = ExecOrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if ExecOrderLocalID:
            self.ExecOrderLocalID = ExecOrderLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ActionType:
            self.ActionType = ActionType.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if Volume:
            self.Volume = Volume
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class QryExchangeExecOrderAction(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

    def __init__(self, ParticipantID=None, ClientID=None, ExchangeID=None, TraderID=None):
        super().__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class ErrExecOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExecOrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("Volume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExecOrderRef=None, UserID=None, Volume=None, RequestID=None, BusinessUnit=None, OffsetFlag=None, HedgeFlag=None, ActionType=None, PosiDirection=None, ReservePositionFlag=None, CloseFlag=None, ExchangeID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, ClientID=None, reserve2=None, MacAddress=None, ErrorID=None, ErrorMsg=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExecOrderRef:
            self.ExecOrderRef = ExecOrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Volume:
            self.Volume = Volume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ActionType:
            self.ActionType = ActionType.encode("GBK")
        if PosiDirection:
            self.PosiDirection = PosiDirection.encode("GBK")
        if ReservePositionFlag:
            self.ReservePositionFlag = ReservePositionFlag.encode("GBK")
        if CloseFlag:
            self.CloseFlag = CloseFlag.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryErrExecOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class ErrExecOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExecOrderActionRef", c_int),
        ("ExecOrderRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("ExecOrderSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExecOrderActionRef=None, ExecOrderRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, ExecOrderSysID=None, ActionFlag=None, UserID=None, reserve1=None, InvestUnitID=None, reserve2=None, MacAddress=None, ErrorID=None, ErrorMsg=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExecOrderActionRef:
            self.ExecOrderActionRef = ExecOrderActionRef
        if ExecOrderRef:
            self.ExecOrderRef = ExecOrderRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExecOrderSysID:
            self.ExecOrderSysID = ExecOrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryErrExecOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class OptionInstrTradingRight(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Direction", c_char),
        ("TradingRight", c_char),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, Direction=None, TradingRight=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if TradingRight:
            self.TradingRight = TradingRight.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryOptionInstrTradingRight(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("Direction", c_char),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, Direction=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InputForQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ForQuoteRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ForQuoteRef=None, UserID=None, ExchangeID=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ForQuoteRef:
            self.ForQuoteRef = ForQuoteRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ForQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ForQuoteRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("ForQuoteLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("ForQuoteStatus", c_char),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("StatusMsg", c_char_Array_81),
        ("ActiveUserID", c_char_Array_16),
        ("BrokerForQutoSeq", c_int),
        ("InvestUnitID", c_char_Array_17),
        ("reserve3", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ForQuoteRef=None, UserID=None, ForQuoteLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve2=None, TraderID=None, InstallID=None, InsertDate=None, InsertTime=None, ForQuoteStatus=None, FrontID=None, SessionID=None, StatusMsg=None, ActiveUserID=None, BrokerForQutoSeq=None, InvestUnitID=None, reserve3=None, MacAddress=None, InstrumentID=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ForQuoteRef:
            self.ForQuoteRef = ForQuoteRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ForQuoteLocalID:
            self.ForQuoteLocalID = ForQuoteLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if ForQuoteStatus:
            self.ForQuoteStatus = ForQuoteStatus.encode("GBK")
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if ActiveUserID:
            self.ActiveUserID = ActiveUserID.encode("GBK")
        if BrokerForQutoSeq:
            self.BrokerForQutoSeq = BrokerForQutoSeq
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve3:
            self.reserve3 = reserve3.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryForQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, InsertTimeStart=None, InsertTimeEnd=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InsertTimeStart:
            self.InsertTimeStart = InsertTimeStart.encode("GBK")
        if InsertTimeEnd:
            self.InsertTimeEnd = InsertTimeEnd.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ExchangeForQuote(Struct):
    _fields_ = [
        ("ForQuoteLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("ForQuoteStatus", c_char),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, ForQuoteLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve1=None, TraderID=None, InstallID=None, InsertDate=None, InsertTime=None, ForQuoteStatus=None, reserve2=None, MacAddress=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if ForQuoteLocalID:
            self.ForQuoteLocalID = ForQuoteLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if ForQuoteStatus:
            self.ForQuoteStatus = ForQuoteStatus.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryExchangeForQuote(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, ParticipantID=None, ClientID=None, reserve1=None, ExchangeID=None, TraderID=None, ExchangeInstID=None):
        super().__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class InputQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("QuoteRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("AskPrice", c_double),
        ("BidPrice", c_double),
        ("AskVolume", c_int),
        ("BidVolume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("AskOffsetFlag", c_char),
        ("BidOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("AskOrderRef", c_char_Array_13),
        ("BidOrderRef", c_char_Array_13),
        ("ForQuoteSysID", c_char_Array_21),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
        ("ReplaceSysID", c_char_Array_21),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, QuoteRef=None, UserID=None, AskPrice=None, BidPrice=None, AskVolume=None, BidVolume=None, RequestID=None, BusinessUnit=None, AskOffsetFlag=None, BidOffsetFlag=None, AskHedgeFlag=None, BidHedgeFlag=None, AskOrderRef=None, BidOrderRef=None, ForQuoteSysID=None, ExchangeID=None, InvestUnitID=None, ClientID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None, ReplaceSysID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if QuoteRef:
            self.QuoteRef = QuoteRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if AskPrice:
            self.AskPrice = AskPrice
        if BidPrice:
            self.BidPrice = BidPrice
        if AskVolume:
            self.AskVolume = AskVolume
        if BidVolume:
            self.BidVolume = BidVolume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if AskOffsetFlag:
            self.AskOffsetFlag = AskOffsetFlag.encode("GBK")
        if BidOffsetFlag:
            self.BidOffsetFlag = BidOffsetFlag.encode("GBK")
        if AskHedgeFlag:
            self.AskHedgeFlag = AskHedgeFlag.encode("GBK")
        if BidHedgeFlag:
            self.BidHedgeFlag = BidHedgeFlag.encode("GBK")
        if AskOrderRef:
            self.AskOrderRef = AskOrderRef.encode("GBK")
        if BidOrderRef:
            self.BidOrderRef = BidOrderRef.encode("GBK")
        if ForQuoteSysID:
            self.ForQuoteSysID = ForQuoteSysID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if ReplaceSysID:
            self.ReplaceSysID = ReplaceSysID.encode("GBK")


class InputQuoteAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("QuoteActionRef", c_int),
        ("QuoteRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("QuoteSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, QuoteActionRef=None, QuoteRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, QuoteSysID=None, ActionFlag=None, UserID=None, reserve1=None, InvestUnitID=None, ClientID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if QuoteActionRef:
            self.QuoteActionRef = QuoteActionRef
        if QuoteRef:
            self.QuoteRef = QuoteRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if QuoteSysID:
            self.QuoteSysID = QuoteSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class Quote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("QuoteRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("AskPrice", c_double),
        ("BidPrice", c_double),
        ("AskVolume", c_int),
        ("BidVolume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("AskOffsetFlag", c_char),
        ("BidOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("QuoteLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("NotifySequence", c_int),
        ("OrderSubmitStatus", c_char),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("QuoteSysID", c_char_Array_21),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("CancelTime", c_char_Array_9),
        ("QuoteStatus", c_char),
        ("ClearingPartID", c_char_Array_11),
        ("SequenceNo", c_int),
        ("AskOrderSysID", c_char_Array_21),
        ("BidOrderSysID", c_char_Array_21),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("UserProductInfo", c_char_Array_11),
        ("StatusMsg", c_char_Array_81),
        ("ActiveUserID", c_char_Array_16),
        ("BrokerQuoteSeq", c_int),
        ("AskOrderRef", c_char_Array_13),
        ("BidOrderRef", c_char_Array_13),
        ("ForQuoteSysID", c_char_Array_21),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("reserve3", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
        ("ReplaceSysID", c_char_Array_21),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, QuoteRef=None, UserID=None, AskPrice=None, BidPrice=None, AskVolume=None, BidVolume=None, RequestID=None, BusinessUnit=None, AskOffsetFlag=None, BidOffsetFlag=None, AskHedgeFlag=None, BidHedgeFlag=None, QuoteLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve2=None, TraderID=None, InstallID=None, NotifySequence=None, OrderSubmitStatus=None, TradingDay=None, SettlementID=None, QuoteSysID=None, InsertDate=None, InsertTime=None, CancelTime=None, QuoteStatus=None, ClearingPartID=None, SequenceNo=None, AskOrderSysID=None, BidOrderSysID=None, FrontID=None, SessionID=None, UserProductInfo=None, StatusMsg=None, ActiveUserID=None, BrokerQuoteSeq=None, AskOrderRef=None, BidOrderRef=None, ForQuoteSysID=None, BranchID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, reserve3=None, MacAddress=None, InstrumentID=None, ExchangeInstID=None, IPAddress=None, ReplaceSysID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if QuoteRef:
            self.QuoteRef = QuoteRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if AskPrice:
            self.AskPrice = AskPrice
        if BidPrice:
            self.BidPrice = BidPrice
        if AskVolume:
            self.AskVolume = AskVolume
        if BidVolume:
            self.BidVolume = BidVolume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if AskOffsetFlag:
            self.AskOffsetFlag = AskOffsetFlag.encode("GBK")
        if BidOffsetFlag:
            self.BidOffsetFlag = BidOffsetFlag.encode("GBK")
        if AskHedgeFlag:
            self.AskHedgeFlag = AskHedgeFlag.encode("GBK")
        if BidHedgeFlag:
            self.BidHedgeFlag = BidHedgeFlag.encode("GBK")
        if QuoteLocalID:
            self.QuoteLocalID = QuoteLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if QuoteSysID:
            self.QuoteSysID = QuoteSysID.encode("GBK")
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if CancelTime:
            self.CancelTime = CancelTime.encode("GBK")
        if QuoteStatus:
            self.QuoteStatus = QuoteStatus.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if AskOrderSysID:
            self.AskOrderSysID = AskOrderSysID.encode("GBK")
        if BidOrderSysID:
            self.BidOrderSysID = BidOrderSysID.encode("GBK")
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if ActiveUserID:
            self.ActiveUserID = ActiveUserID.encode("GBK")
        if BrokerQuoteSeq:
            self.BrokerQuoteSeq = BrokerQuoteSeq
        if AskOrderRef:
            self.AskOrderRef = AskOrderRef.encode("GBK")
        if BidOrderRef:
            self.BidOrderRef = BidOrderRef.encode("GBK")
        if ForQuoteSysID:
            self.ForQuoteSysID = ForQuoteSysID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if reserve3:
            self.reserve3 = reserve3.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if ReplaceSysID:
            self.ReplaceSysID = ReplaceSysID.encode("GBK")


class QuoteAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("QuoteActionRef", c_int),
        ("QuoteRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("QuoteSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("QuoteLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("StatusMsg", c_char_Array_81),
        ("reserve1", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, QuoteActionRef=None, QuoteRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, QuoteSysID=None, ActionFlag=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, QuoteLocalID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, StatusMsg=None, reserve1=None, BranchID=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if QuoteActionRef:
            self.QuoteActionRef = QuoteActionRef
        if QuoteRef:
            self.QuoteRef = QuoteRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if QuoteSysID:
            self.QuoteSysID = QuoteSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if QuoteLocalID:
            self.QuoteLocalID = QuoteLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("QuoteSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, QuoteSysID=None, InsertTimeStart=None, InsertTimeEnd=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if QuoteSysID:
            self.QuoteSysID = QuoteSysID.encode("GBK")
        if InsertTimeStart:
            self.InsertTimeStart = InsertTimeStart.encode("GBK")
        if InsertTimeEnd:
            self.InsertTimeEnd = InsertTimeEnd.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ExchangeQuote(Struct):
    _fields_ = [
        ("AskPrice", c_double),
        ("BidPrice", c_double),
        ("AskVolume", c_int),
        ("BidVolume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("AskOffsetFlag", c_char),
        ("BidOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("QuoteLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("NotifySequence", c_int),
        ("OrderSubmitStatus", c_char),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("QuoteSysID", c_char_Array_21),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("CancelTime", c_char_Array_9),
        ("QuoteStatus", c_char),
        ("ClearingPartID", c_char_Array_11),
        ("SequenceNo", c_int),
        ("AskOrderSysID", c_char_Array_21),
        ("BidOrderSysID", c_char_Array_21),
        ("ForQuoteSysID", c_char_Array_21),
        ("BranchID", c_char_Array_9),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, AskPrice=None, BidPrice=None, AskVolume=None, BidVolume=None, RequestID=None, BusinessUnit=None, AskOffsetFlag=None, BidOffsetFlag=None, AskHedgeFlag=None, BidHedgeFlag=None, QuoteLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve1=None, TraderID=None, InstallID=None, NotifySequence=None, OrderSubmitStatus=None, TradingDay=None, SettlementID=None, QuoteSysID=None, InsertDate=None, InsertTime=None, CancelTime=None, QuoteStatus=None, ClearingPartID=None, SequenceNo=None, AskOrderSysID=None, BidOrderSysID=None, ForQuoteSysID=None, BranchID=None, reserve2=None, MacAddress=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if AskPrice:
            self.AskPrice = AskPrice
        if BidPrice:
            self.BidPrice = BidPrice
        if AskVolume:
            self.AskVolume = AskVolume
        if BidVolume:
            self.BidVolume = BidVolume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if AskOffsetFlag:
            self.AskOffsetFlag = AskOffsetFlag.encode("GBK")
        if BidOffsetFlag:
            self.BidOffsetFlag = BidOffsetFlag.encode("GBK")
        if AskHedgeFlag:
            self.AskHedgeFlag = AskHedgeFlag.encode("GBK")
        if BidHedgeFlag:
            self.BidHedgeFlag = BidHedgeFlag.encode("GBK")
        if QuoteLocalID:
            self.QuoteLocalID = QuoteLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if QuoteSysID:
            self.QuoteSysID = QuoteSysID.encode("GBK")
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if CancelTime:
            self.CancelTime = CancelTime.encode("GBK")
        if QuoteStatus:
            self.QuoteStatus = QuoteStatus.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if AskOrderSysID:
            self.AskOrderSysID = AskOrderSysID.encode("GBK")
        if BidOrderSysID:
            self.BidOrderSysID = BidOrderSysID.encode("GBK")
        if ForQuoteSysID:
            self.ForQuoteSysID = ForQuoteSysID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryExchangeQuote(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, ParticipantID=None, ClientID=None, reserve1=None, ExchangeID=None, TraderID=None, ExchangeInstID=None):
        super().__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class QryQuoteAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExchangeID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class ExchangeQuoteAction(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("QuoteSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("QuoteLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, ExchangeID=None, QuoteSysID=None, ActionFlag=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, QuoteLocalID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, reserve1=None, MacAddress=None, IPAddress=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if QuoteSysID:
            self.QuoteSysID = QuoteSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if QuoteLocalID:
            self.QuoteLocalID = QuoteLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryExchangeQuoteAction(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

    def __init__(self, ParticipantID=None, ClientID=None, ExchangeID=None, TraderID=None):
        super().__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class OptionInstrDelta(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Delta", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, Delta=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Delta:
            self.Delta = Delta
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ForQuoteRsp(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("reserve1", c_char_Array_31),
        ("ForQuoteSysID", c_char_Array_21),
        ("ForQuoteTime", c_char_Array_9),
        ("ActionDay", c_char_Array_9),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, TradingDay=None, reserve1=None, ForQuoteSysID=None, ForQuoteTime=None, ActionDay=None, ExchangeID=None, InstrumentID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ForQuoteSysID:
            self.ForQuoteSysID = ForQuoteSysID.encode("GBK")
        if ForQuoteTime:
            self.ForQuoteTime = ForQuoteTime.encode("GBK")
        if ActionDay:
            self.ActionDay = ActionDay.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class StrikeOffset(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Offset", c_double),
        ("OffsetType", c_char),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, Offset=None, OffsetType=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Offset:
            self.Offset = Offset
        if OffsetType:
            self.OffsetType = OffsetType.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryStrikeOffset(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InputBatchOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OrderActionRef", c_int),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("UserID", c_char_Array_16),
        ("InvestUnitID", c_char_Array_17),
        ("reserve1", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, OrderActionRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, UserID=None, InvestUnitID=None, reserve1=None, MacAddress=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OrderActionRef:
            self.OrderActionRef = OrderActionRef
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class BatchOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OrderActionRef", c_int),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("StatusMsg", c_char_Array_81),
        ("InvestUnitID", c_char_Array_17),
        ("reserve1", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, OrderActionRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, StatusMsg=None, InvestUnitID=None, reserve1=None, MacAddress=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OrderActionRef:
            self.OrderActionRef = OrderActionRef
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ExchangeBatchOrderAction(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, ExchangeID=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, reserve1=None, MacAddress=None, IPAddress=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryBatchOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExchangeID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class CombInstrumentGuard(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("GuarantRatio", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, reserve1=None, GuarantRatio=None, ExchangeID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if GuarantRatio:
            self.GuarantRatio = GuarantRatio
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryCombInstrumentGuard(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, reserve1=None, ExchangeID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InputCombAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("CombActionRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("Direction", c_char),
        ("Volume", c_int),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InvestUnitID", c_char_Array_17),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, CombActionRef=None, UserID=None, Direction=None, Volume=None, CombDirection=None, HedgeFlag=None, ExchangeID=None, reserve2=None, MacAddress=None, InvestUnitID=None, FrontID=None, SessionID=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if CombActionRef:
            self.CombActionRef = CombActionRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if Volume:
            self.Volume = Volume
        if CombDirection:
            self.CombDirection = CombDirection.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class CombAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("CombActionRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("Direction", c_char),
        ("Volume", c_int),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ActionLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("ActionStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("SequenceNo", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("UserProductInfo", c_char_Array_11),
        ("StatusMsg", c_char_Array_81),
        ("reserve3", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ComTradeID", c_char_Array_21),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, CombActionRef=None, UserID=None, Direction=None, Volume=None, CombDirection=None, HedgeFlag=None, ActionLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve2=None, TraderID=None, InstallID=None, ActionStatus=None, NotifySequence=None, TradingDay=None, SettlementID=None, SequenceNo=None, FrontID=None, SessionID=None, UserProductInfo=None, StatusMsg=None, reserve3=None, MacAddress=None, ComTradeID=None, BranchID=None, InvestUnitID=None, InstrumentID=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if CombActionRef:
            self.CombActionRef = CombActionRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if Volume:
            self.Volume = Volume
        if CombDirection:
            self.CombDirection = CombDirection.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if ActionStatus:
            self.ActionStatus = ActionStatus.encode("GBK")
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if reserve3:
            self.reserve3 = reserve3.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ComTradeID:
            self.ComTradeID = ComTradeID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryCombAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ExchangeCombAction(Struct):
    _fields_ = [
        ("Direction", c_char),
        ("Volume", c_int),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ActionLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("ActionStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("SequenceNo", c_int),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ComTradeID", c_char_Array_21),
        ("BranchID", c_char_Array_9),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, Direction=None, Volume=None, CombDirection=None, HedgeFlag=None, ActionLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve1=None, TraderID=None, InstallID=None, ActionStatus=None, NotifySequence=None, TradingDay=None, SettlementID=None, SequenceNo=None, reserve2=None, MacAddress=None, ComTradeID=None, BranchID=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if Direction:
            self.Direction = Direction.encode("GBK")
        if Volume:
            self.Volume = Volume
        if CombDirection:
            self.CombDirection = CombDirection.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if ActionStatus:
            self.ActionStatus = ActionStatus.encode("GBK")
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ComTradeID:
            self.ComTradeID = ComTradeID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryExchangeCombAction(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, ParticipantID=None, ClientID=None, reserve1=None, ExchangeID=None, TraderID=None, ExchangeInstID=None):
        super().__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class ProductExchRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("QuoteCurrencyID", c_char_Array_4),
        ("ExchangeRate", c_double),
        ("ExchangeID", c_char_Array_9),
        ("ProductID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, QuoteCurrencyID=None, ExchangeRate=None, ExchangeID=None, ProductID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if QuoteCurrencyID:
            self.QuoteCurrencyID = QuoteCurrencyID.encode("GBK")
        if ExchangeRate:
            self.ExchangeRate = ExchangeRate
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")


class QryProductExchRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("ProductID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, ExchangeID=None, ProductID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")


class QryForQuoteParam(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, reserve1=None, ExchangeID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ForQuoteParam(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("LastPrice", c_double),
        ("PriceInterval", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, reserve1=None, ExchangeID=None, LastPrice=None, PriceInterval=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if LastPrice:
            self.LastPrice = LastPrice
        if PriceInterval:
            self.PriceInterval = PriceInterval
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class MMOptionInstrCommRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("StrikeRatioByMoney", c_double),
        ("StrikeRatioByVolume", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, OpenRatioByMoney=None, OpenRatioByVolume=None, CloseRatioByMoney=None, CloseRatioByVolume=None, CloseTodayRatioByMoney=None, CloseTodayRatioByVolume=None, StrikeRatioByMoney=None, StrikeRatioByVolume=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OpenRatioByMoney:
            self.OpenRatioByMoney = OpenRatioByMoney
        if OpenRatioByVolume:
            self.OpenRatioByVolume = OpenRatioByVolume
        if CloseRatioByMoney:
            self.CloseRatioByMoney = CloseRatioByMoney
        if CloseRatioByVolume:
            self.CloseRatioByVolume = CloseRatioByVolume
        if CloseTodayRatioByMoney:
            self.CloseTodayRatioByMoney = CloseTodayRatioByMoney
        if CloseTodayRatioByVolume:
            self.CloseTodayRatioByVolume = CloseTodayRatioByVolume
        if StrikeRatioByMoney:
            self.StrikeRatioByMoney = StrikeRatioByMoney
        if StrikeRatioByVolume:
            self.StrikeRatioByVolume = StrikeRatioByVolume
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryMMOptionInstrCommRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class MMInstrumentCommissionRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, OpenRatioByMoney=None, OpenRatioByVolume=None, CloseRatioByMoney=None, CloseRatioByVolume=None, CloseTodayRatioByMoney=None, CloseTodayRatioByVolume=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OpenRatioByMoney:
            self.OpenRatioByMoney = OpenRatioByMoney
        if OpenRatioByVolume:
            self.OpenRatioByVolume = OpenRatioByVolume
        if CloseRatioByMoney:
            self.CloseRatioByMoney = CloseRatioByMoney
        if CloseRatioByVolume:
            self.CloseRatioByVolume = CloseRatioByVolume
        if CloseTodayRatioByMoney:
            self.CloseTodayRatioByMoney = CloseTodayRatioByMoney
        if CloseTodayRatioByVolume:
            self.CloseTodayRatioByVolume = CloseTodayRatioByVolume
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryMMInstrumentCommissionRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InstrumentOrderCommRate(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("OrderCommByVolume", c_double),
        ("OrderActionCommByVolume", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
        ("OrderCommByTrade", c_double),
        ("OrderActionCommByTrade", c_double),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, HedgeFlag=None, OrderCommByVolume=None, OrderActionCommByVolume=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None, OrderCommByTrade=None, OrderActionCommByTrade=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if OrderCommByVolume:
            self.OrderCommByVolume = OrderCommByVolume
        if OrderActionCommByVolume:
            self.OrderActionCommByVolume = OrderActionCommByVolume
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if OrderCommByTrade:
            self.OrderCommByTrade = OrderCommByTrade
        if OrderActionCommByTrade:
            self.OrderActionCommByTrade = OrderActionCommByTrade


class QryInstrumentOrderCommRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class TradeParam(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("TradeParamID", c_char),
        ("TradeParamValue", c_char_Array_256),
        ("Memo", c_char_Array_161),
    ]

    def __init__(self, BrokerID=None, TradeParamID=None, TradeParamValue=None, Memo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if TradeParamID:
            self.TradeParamID = TradeParamID.encode("GBK")
        if TradeParamValue:
            self.TradeParamValue = TradeParamValue.encode("GBK")
        if Memo:
            self.Memo = Memo.encode("GBK")


class InstrumentMarginRateUL(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InvestorRange=None, BrokerID=None, InvestorID=None, HedgeFlag=None, LongMarginRatioByMoney=None, LongMarginRatioByVolume=None, ShortMarginRatioByMoney=None, ShortMarginRatioByVolume=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class FutureLimitPosiParam(Struct):
    _fields_ = [
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("SpecOpenVolume", c_int),
        ("ArbiOpenVolume", c_int),
        ("OpenVolume", c_int),
        ("ProductID", c_char_Array_81),
    ]

    def __init__(self, InvestorRange=None, BrokerID=None, InvestorID=None, reserve1=None, SpecOpenVolume=None, ArbiOpenVolume=None, OpenVolume=None, ProductID=None):
        super().__init__()
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if SpecOpenVolume:
            self.SpecOpenVolume = SpecOpenVolume
        if ArbiOpenVolume:
            self.ArbiOpenVolume = ArbiOpenVolume
        if OpenVolume:
            self.OpenVolume = OpenVolume
        if ProductID:
            self.ProductID = ProductID.encode("GBK")


class LoginForbiddenIP(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_16),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, reserve1=None, IPAddress=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class IPList(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_16),
        ("IsWhite", c_int),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, reserve1=None, IsWhite=None, IPAddress=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if IsWhite:
            self.IsWhite = IsWhite
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class InputOptionSelfClose(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("OptionSelfCloseRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("Volume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("HedgeFlag", c_char),
        ("OptSelfCloseFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, OptionSelfCloseRef=None, UserID=None, Volume=None, RequestID=None, BusinessUnit=None, HedgeFlag=None, OptSelfCloseFlag=None, ExchangeID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, ClientID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if OptionSelfCloseRef:
            self.OptionSelfCloseRef = OptionSelfCloseRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Volume:
            self.Volume = Volume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if OptSelfCloseFlag:
            self.OptSelfCloseFlag = OptSelfCloseFlag.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class InputOptionSelfCloseAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OptionSelfCloseActionRef", c_int),
        ("OptionSelfCloseRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("OptionSelfCloseSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, OptionSelfCloseActionRef=None, OptionSelfCloseRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, OptionSelfCloseSysID=None, ActionFlag=None, UserID=None, reserve1=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OptionSelfCloseActionRef:
            self.OptionSelfCloseActionRef = OptionSelfCloseActionRef
        if OptionSelfCloseRef:
            self.OptionSelfCloseRef = OptionSelfCloseRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OptionSelfCloseSysID:
            self.OptionSelfCloseSysID = OptionSelfCloseSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class OptionSelfClose(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("OptionSelfCloseRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("Volume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("HedgeFlag", c_char),
        ("OptSelfCloseFlag", c_char),
        ("OptionSelfCloseLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("OptionSelfCloseSysID", c_char_Array_21),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("CancelTime", c_char_Array_9),
        ("ExecResult", c_char),
        ("ClearingPartID", c_char_Array_11),
        ("SequenceNo", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("UserProductInfo", c_char_Array_11),
        ("StatusMsg", c_char_Array_81),
        ("ActiveUserID", c_char_Array_16),
        ("BrokerOptionSelfCloseSeq", c_int),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("reserve3", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, OptionSelfCloseRef=None, UserID=None, Volume=None, RequestID=None, BusinessUnit=None, HedgeFlag=None, OptSelfCloseFlag=None, OptionSelfCloseLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve2=None, TraderID=None, InstallID=None, OrderSubmitStatus=None, NotifySequence=None, TradingDay=None, SettlementID=None, OptionSelfCloseSysID=None, InsertDate=None, InsertTime=None, CancelTime=None, ExecResult=None, ClearingPartID=None, SequenceNo=None, FrontID=None, SessionID=None, UserProductInfo=None, StatusMsg=None, ActiveUserID=None, BrokerOptionSelfCloseSeq=None, BranchID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, reserve3=None, MacAddress=None, InstrumentID=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if OptionSelfCloseRef:
            self.OptionSelfCloseRef = OptionSelfCloseRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Volume:
            self.Volume = Volume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if OptSelfCloseFlag:
            self.OptSelfCloseFlag = OptSelfCloseFlag.encode("GBK")
        if OptionSelfCloseLocalID:
            self.OptionSelfCloseLocalID = OptionSelfCloseLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus.encode("GBK")
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OptionSelfCloseSysID:
            self.OptionSelfCloseSysID = OptionSelfCloseSysID.encode("GBK")
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if CancelTime:
            self.CancelTime = CancelTime.encode("GBK")
        if ExecResult:
            self.ExecResult = ExecResult.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if ActiveUserID:
            self.ActiveUserID = ActiveUserID.encode("GBK")
        if BrokerOptionSelfCloseSeq:
            self.BrokerOptionSelfCloseSeq = BrokerOptionSelfCloseSeq
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if reserve3:
            self.reserve3 = reserve3.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class OptionSelfCloseAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OptionSelfCloseActionRef", c_int),
        ("OptionSelfCloseRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("OptionSelfCloseSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OptionSelfCloseLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("StatusMsg", c_char_Array_81),
        ("reserve1", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, OptionSelfCloseActionRef=None, OptionSelfCloseRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, OptionSelfCloseSysID=None, ActionFlag=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, OptionSelfCloseLocalID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, StatusMsg=None, reserve1=None, BranchID=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OptionSelfCloseActionRef:
            self.OptionSelfCloseActionRef = OptionSelfCloseActionRef
        if OptionSelfCloseRef:
            self.OptionSelfCloseRef = OptionSelfCloseRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OptionSelfCloseSysID:
            self.OptionSelfCloseSysID = OptionSelfCloseSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OptionSelfCloseLocalID:
            self.OptionSelfCloseLocalID = OptionSelfCloseLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryOptionSelfClose(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("OptionSelfCloseSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, OptionSelfCloseSysID=None, InsertTimeStart=None, InsertTimeEnd=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OptionSelfCloseSysID:
            self.OptionSelfCloseSysID = OptionSelfCloseSysID.encode("GBK")
        if InsertTimeStart:
            self.InsertTimeStart = InsertTimeStart.encode("GBK")
        if InsertTimeEnd:
            self.InsertTimeEnd = InsertTimeEnd.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class ExchangeOptionSelfClose(Struct):
    _fields_ = [
        ("Volume", c_int),
        ("RequestID", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("HedgeFlag", c_char),
        ("OptSelfCloseFlag", c_char),
        ("OptionSelfCloseLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve1", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("OptionSelfCloseSysID", c_char_Array_21),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("CancelTime", c_char_Array_9),
        ("ExecResult", c_char),
        ("ClearingPartID", c_char_Array_11),
        ("SequenceNo", c_int),
        ("BranchID", c_char_Array_9),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, Volume=None, RequestID=None, BusinessUnit=None, HedgeFlag=None, OptSelfCloseFlag=None, OptionSelfCloseLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve1=None, TraderID=None, InstallID=None, OrderSubmitStatus=None, NotifySequence=None, TradingDay=None, SettlementID=None, OptionSelfCloseSysID=None, InsertDate=None, InsertTime=None, CancelTime=None, ExecResult=None, ClearingPartID=None, SequenceNo=None, BranchID=None, reserve2=None, MacAddress=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if Volume:
            self.Volume = Volume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if OptSelfCloseFlag:
            self.OptSelfCloseFlag = OptSelfCloseFlag.encode("GBK")
        if OptionSelfCloseLocalID:
            self.OptionSelfCloseLocalID = OptionSelfCloseLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus.encode("GBK")
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OptionSelfCloseSysID:
            self.OptionSelfCloseSysID = OptionSelfCloseSysID.encode("GBK")
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if CancelTime:
            self.CancelTime = CancelTime.encode("GBK")
        if ExecResult:
            self.ExecResult = ExecResult.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryOptionSelfCloseAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExchangeID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class ExchangeOptionSelfCloseAction(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("OptionSelfCloseSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OptionSelfCloseLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("BranchID", c_char_Array_9),
        ("reserve1", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("reserve2", c_char_Array_31),
        ("OptSelfCloseFlag", c_char),
        ("IPAddress", c_char_Array_33),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, OptionSelfCloseSysID=None, ActionFlag=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, OptionSelfCloseLocalID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, BranchID=None, reserve1=None, MacAddress=None, reserve2=None, OptSelfCloseFlag=None, IPAddress=None, ExchangeInstID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OptionSelfCloseSysID:
            self.OptionSelfCloseSysID = OptionSelfCloseSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OptionSelfCloseLocalID:
            self.OptionSelfCloseLocalID = OptionSelfCloseLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if OptSelfCloseFlag:
            self.OptSelfCloseFlag = OptSelfCloseFlag.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class SyncDelaySwap(Struct):
    _fields_ = [
        ("DelaySwapSeqNo", c_char_Array_15),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("FromCurrencyID", c_char_Array_4),
        ("FromAmount", c_double),
        ("FromFrozenSwap", c_double),
        ("FromRemainSwap", c_double),
        ("ToCurrencyID", c_char_Array_4),
        ("ToAmount", c_double),
        ("IsManualSwap", c_int),
        ("IsAllRemainSetZero", c_int),
    ]

    def __init__(self, DelaySwapSeqNo=None, BrokerID=None, InvestorID=None, FromCurrencyID=None, FromAmount=None, FromFrozenSwap=None, FromRemainSwap=None, ToCurrencyID=None, ToAmount=None, IsManualSwap=None, IsAllRemainSetZero=None):
        super().__init__()
        if DelaySwapSeqNo:
            self.DelaySwapSeqNo = DelaySwapSeqNo.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if FromCurrencyID:
            self.FromCurrencyID = FromCurrencyID.encode("GBK")
        if FromAmount:
            self.FromAmount = FromAmount
        if FromFrozenSwap:
            self.FromFrozenSwap = FromFrozenSwap
        if FromRemainSwap:
            self.FromRemainSwap = FromRemainSwap
        if ToCurrencyID:
            self.ToCurrencyID = ToCurrencyID.encode("GBK")
        if ToAmount:
            self.ToAmount = ToAmount
        if IsManualSwap:
            self.IsManualSwap = IsManualSwap
        if IsAllRemainSetZero:
            self.IsAllRemainSetZero = IsAllRemainSetZero


class QrySyncDelaySwap(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("DelaySwapSeqNo", c_char_Array_15),
    ]

    def __init__(self, BrokerID=None, DelaySwapSeqNo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if DelaySwapSeqNo:
            self.DelaySwapSeqNo = DelaySwapSeqNo.encode("GBK")


class InvestUnit(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InvestUnitID", c_char_Array_17),
        ("InvestorUnitName", c_char_Array_81),
        ("InvestorGroupID", c_char_Array_13),
        ("CommModelID", c_char_Array_13),
        ("MarginModelID", c_char_Array_13),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, InvestUnitID=None, InvestorUnitName=None, InvestorGroupID=None, CommModelID=None, MarginModelID=None, AccountID=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InvestorUnitName:
            self.InvestorUnitName = InvestorUnitName.encode("GBK")
        if InvestorGroupID:
            self.InvestorGroupID = InvestorGroupID.encode("GBK")
        if CommModelID:
            self.CommModelID = CommModelID.encode("GBK")
        if MarginModelID:
            self.MarginModelID = MarginModelID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class QryInvestUnit(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InvestUnitID", c_char_Array_17),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, InvestUnitID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class SecAgentCheckMode(Struct):
    _fields_ = [
        ("InvestorID", c_char_Array_13),
        ("BrokerID", c_char_Array_11),
        ("CurrencyID", c_char_Array_4),
        ("BrokerSecAgentID", c_char_Array_13),
        ("CheckSelfAccount", c_int),
    ]

    def __init__(self, InvestorID=None, BrokerID=None, CurrencyID=None, BrokerSecAgentID=None, CheckSelfAccount=None):
        super().__init__()
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if BrokerSecAgentID:
            self.BrokerSecAgentID = BrokerSecAgentID.encode("GBK")
        if CheckSelfAccount:
            self.CheckSelfAccount = CheckSelfAccount


class SecAgentTradeInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("BrokerSecAgentID", c_char_Array_13),
        ("InvestorID", c_char_Array_13),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, BrokerID=None, BrokerSecAgentID=None, InvestorID=None, LongCustomerName=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerSecAgentID:
            self.BrokerSecAgentID = BrokerSecAgentID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class MarketData(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("reserve2", c_char_Array_31),
        ("LastPrice", c_double),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("Volume", c_int),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
        ("ClosePrice", c_double),
        ("SettlementPrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("PreDelta", c_double),
        ("CurrDelta", c_double),
        ("UpdateTime", c_char_Array_9),
        ("UpdateMillisec", c_int),
        ("ActionDay", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, TradingDay=None, reserve1=None, ExchangeID=None, reserve2=None, LastPrice=None, PreSettlementPrice=None, PreClosePrice=None, PreOpenInterest=None, OpenPrice=None, HighestPrice=None, LowestPrice=None, Volume=None, Turnover=None, OpenInterest=None, ClosePrice=None, SettlementPrice=None, UpperLimitPrice=None, LowerLimitPrice=None, PreDelta=None, CurrDelta=None, UpdateTime=None, UpdateMillisec=None, ActionDay=None, InstrumentID=None, ExchangeInstID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if LastPrice:
            self.LastPrice = LastPrice
        if PreSettlementPrice:
            self.PreSettlementPrice = PreSettlementPrice
        if PreClosePrice:
            self.PreClosePrice = PreClosePrice
        if PreOpenInterest:
            self.PreOpenInterest = PreOpenInterest
        if OpenPrice:
            self.OpenPrice = OpenPrice
        if HighestPrice:
            self.HighestPrice = HighestPrice
        if LowestPrice:
            self.LowestPrice = LowestPrice
        if Volume:
            self.Volume = Volume
        if Turnover:
            self.Turnover = Turnover
        if OpenInterest:
            self.OpenInterest = OpenInterest
        if ClosePrice:
            self.ClosePrice = ClosePrice
        if SettlementPrice:
            self.SettlementPrice = SettlementPrice
        if UpperLimitPrice:
            self.UpperLimitPrice = UpperLimitPrice
        if LowerLimitPrice:
            self.LowerLimitPrice = LowerLimitPrice
        if PreDelta:
            self.PreDelta = PreDelta
        if CurrDelta:
            self.CurrDelta = CurrDelta
        if UpdateTime:
            self.UpdateTime = UpdateTime.encode("GBK")
        if UpdateMillisec:
            self.UpdateMillisec = UpdateMillisec
        if ActionDay:
            self.ActionDay = ActionDay.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class MarketDataBase(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("PreDelta", c_double),
    ]

    def __init__(self, TradingDay=None, PreSettlementPrice=None, PreClosePrice=None, PreOpenInterest=None, PreDelta=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PreSettlementPrice:
            self.PreSettlementPrice = PreSettlementPrice
        if PreClosePrice:
            self.PreClosePrice = PreClosePrice
        if PreOpenInterest:
            self.PreOpenInterest = PreOpenInterest
        if PreDelta:
            self.PreDelta = PreDelta


class MarketDataStatic(Struct):
    _fields_ = [
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("ClosePrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("SettlementPrice", c_double),
        ("CurrDelta", c_double),
    ]

    def __init__(self, OpenPrice=None, HighestPrice=None, LowestPrice=None, ClosePrice=None, UpperLimitPrice=None, LowerLimitPrice=None, SettlementPrice=None, CurrDelta=None):
        super().__init__()
        if OpenPrice:
            self.OpenPrice = OpenPrice
        if HighestPrice:
            self.HighestPrice = HighestPrice
        if LowestPrice:
            self.LowestPrice = LowestPrice
        if ClosePrice:
            self.ClosePrice = ClosePrice
        if UpperLimitPrice:
            self.UpperLimitPrice = UpperLimitPrice
        if LowerLimitPrice:
            self.LowerLimitPrice = LowerLimitPrice
        if SettlementPrice:
            self.SettlementPrice = SettlementPrice
        if CurrDelta:
            self.CurrDelta = CurrDelta


class MarketDataLastMatch(Struct):
    _fields_ = [
        ("LastPrice", c_double),
        ("Volume", c_int),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
    ]

    def __init__(self, LastPrice=None, Volume=None, Turnover=None, OpenInterest=None):
        super().__init__()
        if LastPrice:
            self.LastPrice = LastPrice
        if Volume:
            self.Volume = Volume
        if Turnover:
            self.Turnover = Turnover
        if OpenInterest:
            self.OpenInterest = OpenInterest


class MarketDataBestPrice(Struct):
    _fields_ = [
        ("BidPrice1", c_double),
        ("BidVolume1", c_int),
        ("AskPrice1", c_double),
        ("AskVolume1", c_int),
    ]

    def __init__(self, BidPrice1=None, BidVolume1=None, AskPrice1=None, AskVolume1=None):
        super().__init__()
        if BidPrice1:
            self.BidPrice1 = BidPrice1
        if BidVolume1:
            self.BidVolume1 = BidVolume1
        if AskPrice1:
            self.AskPrice1 = AskPrice1
        if AskVolume1:
            self.AskVolume1 = AskVolume1


class MarketDataBid23(Struct):
    _fields_ = [
        ("BidPrice2", c_double),
        ("BidVolume2", c_int),
        ("BidPrice3", c_double),
        ("BidVolume3", c_int),
    ]

    def __init__(self, BidPrice2=None, BidVolume2=None, BidPrice3=None, BidVolume3=None):
        super().__init__()
        if BidPrice2:
            self.BidPrice2 = BidPrice2
        if BidVolume2:
            self.BidVolume2 = BidVolume2
        if BidPrice3:
            self.BidPrice3 = BidPrice3
        if BidVolume3:
            self.BidVolume3 = BidVolume3


class MarketDataAsk23(Struct):
    _fields_ = [
        ("AskPrice2", c_double),
        ("AskVolume2", c_int),
        ("AskPrice3", c_double),
        ("AskVolume3", c_int),
    ]

    def __init__(self, AskPrice2=None, AskVolume2=None, AskPrice3=None, AskVolume3=None):
        super().__init__()
        if AskPrice2:
            self.AskPrice2 = AskPrice2
        if AskVolume2:
            self.AskVolume2 = AskVolume2
        if AskPrice3:
            self.AskPrice3 = AskPrice3
        if AskVolume3:
            self.AskVolume3 = AskVolume3


class MarketDataBid45(Struct):
    _fields_ = [
        ("BidPrice4", c_double),
        ("BidVolume4", c_int),
        ("BidPrice5", c_double),
        ("BidVolume5", c_int),
    ]

    def __init__(self, BidPrice4=None, BidVolume4=None, BidPrice5=None, BidVolume5=None):
        super().__init__()
        if BidPrice4:
            self.BidPrice4 = BidPrice4
        if BidVolume4:
            self.BidVolume4 = BidVolume4
        if BidPrice5:
            self.BidPrice5 = BidPrice5
        if BidVolume5:
            self.BidVolume5 = BidVolume5


class MarketDataAsk45(Struct):
    _fields_ = [
        ("AskPrice4", c_double),
        ("AskVolume4", c_int),
        ("AskPrice5", c_double),
        ("AskVolume5", c_int),
    ]

    def __init__(self, AskPrice4=None, AskVolume4=None, AskPrice5=None, AskVolume5=None):
        super().__init__()
        if AskPrice4:
            self.AskPrice4 = AskPrice4
        if AskVolume4:
            self.AskVolume4 = AskVolume4
        if AskPrice5:
            self.AskPrice5 = AskPrice5
        if AskVolume5:
            self.AskVolume5 = AskVolume5


class MarketDataUpdateTime(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("UpdateTime", c_char_Array_9),
        ("UpdateMillisec", c_int),
        ("ActionDay", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, UpdateTime=None, UpdateMillisec=None, ActionDay=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if UpdateTime:
            self.UpdateTime = UpdateTime.encode("GBK")
        if UpdateMillisec:
            self.UpdateMillisec = UpdateMillisec
        if ActionDay:
            self.ActionDay = ActionDay.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class MarketDataBandingPrice(Struct):
    _fields_ = [
        ("BandingUpperPrice", c_double),
        ("BandingLowerPrice", c_double),
    ]

    def __init__(self, BandingUpperPrice=None, BandingLowerPrice=None):
        super().__init__()
        if BandingUpperPrice:
            self.BandingUpperPrice = BandingUpperPrice
        if BandingLowerPrice:
            self.BandingLowerPrice = BandingLowerPrice


class MarketDataExchange(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, ExchangeID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class SpecificInstrument(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, InstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InstrumentStatus(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("reserve1", c_char_Array_31),
        ("SettlementGroupID", c_char_Array_9),
        ("reserve2", c_char_Array_31),
        ("InstrumentStatus", c_char),
        ("TradingSegmentSN", c_int),
        ("EnterTime", c_char_Array_9),
        ("EnterReason", c_char),
        ("ExchangeInstID", c_char_Array_81),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, reserve1=None, SettlementGroupID=None, reserve2=None, InstrumentStatus=None, TradingSegmentSN=None, EnterTime=None, EnterReason=None, ExchangeInstID=None, InstrumentID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if SettlementGroupID:
            self.SettlementGroupID = SettlementGroupID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if InstrumentStatus:
            self.InstrumentStatus = InstrumentStatus.encode("GBK")
        if TradingSegmentSN:
            self.TradingSegmentSN = TradingSegmentSN
        if EnterTime:
            self.EnterTime = EnterTime.encode("GBK")
        if EnterReason:
            self.EnterReason = EnterReason.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryInstrumentStatus(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("reserve1", c_char_Array_31),
        ("ExchangeInstID", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, reserve1=None, ExchangeInstID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class InvestorAccount(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, AccountID=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class PositionProfitAlgorithm(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("Algorithm", c_char),
        ("Memo", c_char_Array_161),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, AccountID=None, Algorithm=None, Memo=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Algorithm:
            self.Algorithm = Algorithm.encode("GBK")
        if Memo:
            self.Memo = Memo.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class Discount(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorRange", c_char),
        ("InvestorID", c_char_Array_13),
        ("Discount", c_double),
    ]

    def __init__(self, BrokerID=None, InvestorRange=None, InvestorID=None, Discount=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Discount:
            self.Discount = Discount


class QryTransferBank(Struct):
    _fields_ = [
        ("BankID", c_char_Array_4),
        ("BankBrchID", c_char_Array_5),
    ]

    def __init__(self, BankID=None, BankBrchID=None):
        super().__init__()
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBrchID:
            self.BankBrchID = BankBrchID.encode("GBK")


class TransferBank(Struct):
    _fields_ = [
        ("BankID", c_char_Array_4),
        ("BankBrchID", c_char_Array_5),
        ("BankName", c_char_Array_101),
        ("IsActive", c_int),
    ]

    def __init__(self, BankID=None, BankBrchID=None, BankName=None, IsActive=None):
        super().__init__()
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBrchID:
            self.BankBrchID = BankBrchID.encode("GBK")
        if BankName:
            self.BankName = BankName.encode("GBK")
        if IsActive:
            self.IsActive = IsActive


class QryInvestorPositionDetail(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InvestorPositionDetail(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("OpenDate", c_char_Array_9),
        ("TradeID", c_char_Array_21),
        ("Volume", c_int),
        ("OpenPrice", c_double),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("TradeType", c_char),
        ("reserve2", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("CloseProfitByDate", c_double),
        ("CloseProfitByTrade", c_double),
        ("PositionProfitByDate", c_double),
        ("PositionProfitByTrade", c_double),
        ("Margin", c_double),
        ("ExchMargin", c_double),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("LastSettlementPrice", c_double),
        ("SettlementPrice", c_double),
        ("CloseVolume", c_int),
        ("CloseAmount", c_double),
        ("TimeFirstVolume", c_int),
        ("InvestUnitID", c_char_Array_17),
        ("SpecPosiType", c_char),
        ("InstrumentID", c_char_Array_81),
        ("CombInstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, BrokerID=None, InvestorID=None, HedgeFlag=None, Direction=None, OpenDate=None, TradeID=None, Volume=None, OpenPrice=None, TradingDay=None, SettlementID=None, TradeType=None, reserve2=None, ExchangeID=None, CloseProfitByDate=None, CloseProfitByTrade=None, PositionProfitByDate=None, PositionProfitByTrade=None, Margin=None, ExchMargin=None, MarginRateByMoney=None, MarginRateByVolume=None, LastSettlementPrice=None, SettlementPrice=None, CloseVolume=None, CloseAmount=None, TimeFirstVolume=None, InvestUnitID=None, SpecPosiType=None, InstrumentID=None, CombInstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if OpenDate:
            self.OpenDate = OpenDate.encode("GBK")
        if TradeID:
            self.TradeID = TradeID.encode("GBK")
        if Volume:
            self.Volume = Volume
        if OpenPrice:
            self.OpenPrice = OpenPrice
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if TradeType:
            self.TradeType = TradeType.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if CloseProfitByDate:
            self.CloseProfitByDate = CloseProfitByDate
        if CloseProfitByTrade:
            self.CloseProfitByTrade = CloseProfitByTrade
        if PositionProfitByDate:
            self.PositionProfitByDate = PositionProfitByDate
        if PositionProfitByTrade:
            self.PositionProfitByTrade = PositionProfitByTrade
        if Margin:
            self.Margin = Margin
        if ExchMargin:
            self.ExchMargin = ExchMargin
        if MarginRateByMoney:
            self.MarginRateByMoney = MarginRateByMoney
        if MarginRateByVolume:
            self.MarginRateByVolume = MarginRateByVolume
        if LastSettlementPrice:
            self.LastSettlementPrice = LastSettlementPrice
        if SettlementPrice:
            self.SettlementPrice = SettlementPrice
        if CloseVolume:
            self.CloseVolume = CloseVolume
        if CloseAmount:
            self.CloseAmount = CloseAmount
        if TimeFirstVolume:
            self.TimeFirstVolume = TimeFirstVolume
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if SpecPosiType:
            self.SpecPosiType = SpecPosiType.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")


class TradingAccountPassword(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, AccountID=None, Password=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class MDTraderOffer(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("ParticipantID", c_char_Array_11),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("TraderConnectStatus", c_char),
        ("ConnectRequestDate", c_char_Array_9),
        ("ConnectRequestTime", c_char_Array_9),
        ("LastReportDate", c_char_Array_9),
        ("LastReportTime", c_char_Array_9),
        ("ConnectDate", c_char_Array_9),
        ("ConnectTime", c_char_Array_9),
        ("StartDate", c_char_Array_9),
        ("StartTime", c_char_Array_9),
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("MaxTradeID", c_char_Array_21),
        ("MaxOrderMessageReference", c_char_Array_7),
        ("OrderCancelAlg", c_char),
    ]

    def __init__(self, ExchangeID=None, TraderID=None, ParticipantID=None, Password=None, InstallID=None, OrderLocalID=None, TraderConnectStatus=None, ConnectRequestDate=None, ConnectRequestTime=None, LastReportDate=None, LastReportTime=None, ConnectDate=None, ConnectTime=None, StartDate=None, StartTime=None, TradingDay=None, BrokerID=None, MaxTradeID=None, MaxOrderMessageReference=None, OrderCancelAlg=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if TraderConnectStatus:
            self.TraderConnectStatus = TraderConnectStatus.encode("GBK")
        if ConnectRequestDate:
            self.ConnectRequestDate = ConnectRequestDate.encode("GBK")
        if ConnectRequestTime:
            self.ConnectRequestTime = ConnectRequestTime.encode("GBK")
        if LastReportDate:
            self.LastReportDate = LastReportDate.encode("GBK")
        if LastReportTime:
            self.LastReportTime = LastReportTime.encode("GBK")
        if ConnectDate:
            self.ConnectDate = ConnectDate.encode("GBK")
        if ConnectTime:
            self.ConnectTime = ConnectTime.encode("GBK")
        if StartDate:
            self.StartDate = StartDate.encode("GBK")
        if StartTime:
            self.StartTime = StartTime.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if MaxTradeID:
            self.MaxTradeID = MaxTradeID.encode("GBK")
        if MaxOrderMessageReference:
            self.MaxOrderMessageReference = MaxOrderMessageReference.encode("GBK")
        if OrderCancelAlg:
            self.OrderCancelAlg = OrderCancelAlg.encode("GBK")


class QryMDTraderOffer(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("TraderID", c_char_Array_21),
    ]

    def __init__(self, ExchangeID=None, ParticipantID=None, TraderID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class QryNotice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
    ]

    def __init__(self, BrokerID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")


class Notice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("Content", c_char_Array_501),
        ("SequenceLabel", c_char_Array_2),
    ]

    def __init__(self, BrokerID=None, Content=None, SequenceLabel=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if Content:
            self.Content = Content.encode("GBK")
        if SequenceLabel:
            self.SequenceLabel = SequenceLabel.encode("GBK")


class UserRight(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("UserRightType", c_char),
        ("IsForbidden", c_int),
    ]

    def __init__(self, BrokerID=None, UserID=None, UserRightType=None, IsForbidden=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserRightType:
            self.UserRightType = UserRightType.encode("GBK")
        if IsForbidden:
            self.IsForbidden = IsForbidden


class QrySettlementInfoConfirm(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, AccountID=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class LoadSettlementInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
    ]

    def __init__(self, BrokerID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")


class BrokerWithdrawAlgorithm(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("WithdrawAlgorithm", c_char),
        ("UsingRatio", c_double),
        ("IncludeCloseProfit", c_char),
        ("AllWithoutTrade", c_char),
        ("AvailIncludeCloseProfit", c_char),
        ("IsBrokerUserEvent", c_int),
        ("CurrencyID", c_char_Array_4),
        ("FundMortgageRatio", c_double),
        ("BalanceAlgorithm", c_char),
    ]

    def __init__(self, BrokerID=None, WithdrawAlgorithm=None, UsingRatio=None, IncludeCloseProfit=None, AllWithoutTrade=None, AvailIncludeCloseProfit=None, IsBrokerUserEvent=None, CurrencyID=None, FundMortgageRatio=None, BalanceAlgorithm=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if WithdrawAlgorithm:
            self.WithdrawAlgorithm = WithdrawAlgorithm.encode("GBK")
        if UsingRatio:
            self.UsingRatio = UsingRatio
        if IncludeCloseProfit:
            self.IncludeCloseProfit = IncludeCloseProfit.encode("GBK")
        if AllWithoutTrade:
            self.AllWithoutTrade = AllWithoutTrade.encode("GBK")
        if AvailIncludeCloseProfit:
            self.AvailIncludeCloseProfit = AvailIncludeCloseProfit.encode("GBK")
        if IsBrokerUserEvent:
            self.IsBrokerUserEvent = IsBrokerUserEvent
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if FundMortgageRatio:
            self.FundMortgageRatio = FundMortgageRatio
        if BalanceAlgorithm:
            self.BalanceAlgorithm = BalanceAlgorithm.encode("GBK")


class TradingAccountPasswordUpdateV1(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OldPassword", c_char_Array_41),
        ("NewPassword", c_char_Array_41),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, OldPassword=None, NewPassword=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OldPassword:
            self.OldPassword = OldPassword.encode("GBK")
        if NewPassword:
            self.NewPassword = NewPassword.encode("GBK")


class TradingAccountPasswordUpdate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("OldPassword", c_char_Array_41),
        ("NewPassword", c_char_Array_41),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, AccountID=None, OldPassword=None, NewPassword=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if OldPassword:
            self.OldPassword = OldPassword.encode("GBK")
        if NewPassword:
            self.NewPassword = NewPassword.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class QryCombinationLeg(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("LegID", c_int),
        ("reserve2", c_char_Array_31),
        ("CombInstrumentID", c_char_Array_81),
        ("LegInstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, LegID=None, reserve2=None, CombInstrumentID=None, LegInstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if LegID:
            self.LegID = LegID
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")
        if LegInstrumentID:
            self.LegInstrumentID = LegInstrumentID.encode("GBK")


class QrySyncStatus(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
    ]

    def __init__(self, TradingDay=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")


class CombinationLeg(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("LegID", c_int),
        ("reserve2", c_char_Array_31),
        ("Direction", c_char),
        ("LegMultiple", c_int),
        ("ImplyLevel", c_int),
        ("CombInstrumentID", c_char_Array_81),
        ("LegInstrumentID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, LegID=None, reserve2=None, Direction=None, LegMultiple=None, ImplyLevel=None, CombInstrumentID=None, LegInstrumentID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if LegID:
            self.LegID = LegID
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if LegMultiple:
            self.LegMultiple = LegMultiple
        if ImplyLevel:
            self.ImplyLevel = ImplyLevel
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")
        if LegInstrumentID:
            self.LegInstrumentID = LegInstrumentID.encode("GBK")


class SyncStatus(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("DataSyncStatus", c_char),
    ]

    def __init__(self, TradingDay=None, DataSyncStatus=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if DataSyncStatus:
            self.DataSyncStatus = DataSyncStatus.encode("GBK")


class QryLinkMan(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class LinkMan(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("PersonType", c_char),
        ("IdentifiedCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("PersonName", c_char_Array_81),
        ("Telephone", c_char_Array_41),
        ("Address", c_char_Array_101),
        ("ZipCode", c_char_Array_7),
        ("Priority", c_int),
        ("UOAZipCode", c_char_Array_11),
        ("PersonFullName", c_char_Array_101),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, PersonType=None, IdentifiedCardType=None, IdentifiedCardNo=None, PersonName=None, Telephone=None, Address=None, ZipCode=None, Priority=None, UOAZipCode=None, PersonFullName=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if PersonType:
            self.PersonType = PersonType.encode("GBK")
        if IdentifiedCardType:
            self.IdentifiedCardType = IdentifiedCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if PersonName:
            self.PersonName = PersonName.encode("GBK")
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if ZipCode:
            self.ZipCode = ZipCode.encode("GBK")
        if Priority:
            self.Priority = Priority
        if UOAZipCode:
            self.UOAZipCode = UOAZipCode.encode("GBK")
        if PersonFullName:
            self.PersonFullName = PersonFullName.encode("GBK")


class QryBrokerUserEvent(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("UserEventType", c_char),
    ]

    def __init__(self, BrokerID=None, UserID=None, UserEventType=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserEventType:
            self.UserEventType = UserEventType.encode("GBK")


class BrokerUserEvent(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("UserEventType", c_char),
        ("EventSequenceNo", c_int),
        ("EventDate", c_char_Array_9),
        ("EventTime", c_char_Array_9),
        ("UserEventInfo", c_char_Array_1025),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, UserID=None, UserEventType=None, EventSequenceNo=None, EventDate=None, EventTime=None, UserEventInfo=None, InvestorID=None, reserve1=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserEventType:
            self.UserEventType = UserEventType.encode("GBK")
        if EventSequenceNo:
            self.EventSequenceNo = EventSequenceNo
        if EventDate:
            self.EventDate = EventDate.encode("GBK")
        if EventTime:
            self.EventTime = EventTime.encode("GBK")
        if UserEventInfo:
            self.UserEventInfo = UserEventInfo.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryContractBank(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("BankID", c_char_Array_4),
        ("BankBrchID", c_char_Array_5),
    ]

    def __init__(self, BrokerID=None, BankID=None, BankBrchID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBrchID:
            self.BankBrchID = BankBrchID.encode("GBK")


class ContractBank(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("BankID", c_char_Array_4),
        ("BankBrchID", c_char_Array_5),
        ("BankName", c_char_Array_101),
    ]

    def __init__(self, BrokerID=None, BankID=None, BankBrchID=None, BankName=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBrchID:
            self.BankBrchID = BankBrchID.encode("GBK")
        if BankName:
            self.BankName = BankName.encode("GBK")


class InvestorPositionCombineDetail(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("OpenDate", c_char_Array_9),
        ("ExchangeID", c_char_Array_9),
        ("SettlementID", c_int),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ComTradeID", c_char_Array_21),
        ("TradeID", c_char_Array_21),
        ("reserve1", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("TotalAmt", c_int),
        ("Margin", c_double),
        ("ExchMargin", c_double),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("LegID", c_int),
        ("LegMultiple", c_int),
        ("reserve2", c_char_Array_31),
        ("TradeGroupID", c_int),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
        ("CombInstrumentID", c_char_Array_81),
    ]

    def __init__(self, TradingDay=None, OpenDate=None, ExchangeID=None, SettlementID=None, BrokerID=None, InvestorID=None, ComTradeID=None, TradeID=None, reserve1=None, HedgeFlag=None, Direction=None, TotalAmt=None, Margin=None, ExchMargin=None, MarginRateByMoney=None, MarginRateByVolume=None, LegID=None, LegMultiple=None, reserve2=None, TradeGroupID=None, InvestUnitID=None, InstrumentID=None, CombInstrumentID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if OpenDate:
            self.OpenDate = OpenDate.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ComTradeID:
            self.ComTradeID = ComTradeID.encode("GBK")
        if TradeID:
            self.TradeID = TradeID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if TotalAmt:
            self.TotalAmt = TotalAmt
        if Margin:
            self.Margin = Margin
        if ExchMargin:
            self.ExchMargin = ExchMargin
        if MarginRateByMoney:
            self.MarginRateByMoney = MarginRateByMoney
        if MarginRateByVolume:
            self.MarginRateByVolume = MarginRateByVolume
        if LegID:
            self.LegID = LegID
        if LegMultiple:
            self.LegMultiple = LegMultiple
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if TradeGroupID:
            self.TradeGroupID = TradeGroupID
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")


class ParkedOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("OrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char_Array_5),
        ("CombHedgeFlag", c_char_Array_5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int),
        ("TimeCondition", c_char),
        ("GTDDate", c_char_Array_9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("RequestID", c_int),
        ("UserForceClose", c_int),
        ("ExchangeID", c_char_Array_9),
        ("ParkedOrderID", c_char_Array_13),
        ("UserType", c_char),
        ("Status", c_char),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("IsSwapOrder", c_int),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("ClientID", c_char_Array_11),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, OrderRef=None, UserID=None, OrderPriceType=None, Direction=None, CombOffsetFlag=None, CombHedgeFlag=None, LimitPrice=None, VolumeTotalOriginal=None, TimeCondition=None, GTDDate=None, VolumeCondition=None, MinVolume=None, ContingentCondition=None, StopPrice=None, ForceCloseReason=None, IsAutoSuspend=None, BusinessUnit=None, RequestID=None, UserForceClose=None, ExchangeID=None, ParkedOrderID=None, UserType=None, Status=None, ErrorID=None, ErrorMsg=None, IsSwapOrder=None, AccountID=None, CurrencyID=None, ClientID=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition.encode("GBK")
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition.encode("GBK")
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition.encode("GBK")
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason.encode("GBK")
        if IsAutoSuspend:
            self.IsAutoSuspend = IsAutoSuspend
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if UserForceClose:
            self.UserForceClose = UserForceClose
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParkedOrderID:
            self.ParkedOrderID = ParkedOrderID.encode("GBK")
        if UserType:
            self.UserType = UserType.encode("GBK")
        if Status:
            self.Status = Status.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if IsSwapOrder:
            self.IsSwapOrder = IsSwapOrder
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ParkedOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OrderActionRef", c_int),
        ("OrderRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_31),
        ("ParkedOrderActionID", c_char_Array_13),
        ("UserType", c_char),
        ("Status", c_char),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, OrderActionRef=None, OrderRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, OrderSysID=None, ActionFlag=None, LimitPrice=None, VolumeChange=None, UserID=None, reserve1=None, ParkedOrderActionID=None, UserType=None, Status=None, ErrorID=None, ErrorMsg=None, InvestUnitID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OrderActionRef:
            self.OrderActionRef = OrderActionRef
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeChange:
            self.VolumeChange = VolumeChange
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ParkedOrderActionID:
            self.ParkedOrderActionID = ParkedOrderActionID.encode("GBK")
        if UserType:
            self.UserType = UserType.encode("GBK")
        if Status:
            self.Status = Status.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryParkedOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryParkedOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class RemoveParkedOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ParkedOrderID", c_char_Array_13),
        ("InvestUnitID", c_char_Array_17),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ParkedOrderID=None, InvestUnitID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ParkedOrderID:
            self.ParkedOrderID = ParkedOrderID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class RemoveParkedOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ParkedOrderActionID", c_char_Array_13),
        ("InvestUnitID", c_char_Array_17),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ParkedOrderActionID=None, InvestUnitID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ParkedOrderActionID:
            self.ParkedOrderActionID = ParkedOrderActionID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class InvestorWithdrawAlgorithm(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorRange", c_char),
        ("InvestorID", c_char_Array_13),
        ("UsingRatio", c_double),
        ("CurrencyID", c_char_Array_4),
        ("FundMortgageRatio", c_double),
    ]

    def __init__(self, BrokerID=None, InvestorRange=None, InvestorID=None, UsingRatio=None, CurrencyID=None, FundMortgageRatio=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if UsingRatio:
            self.UsingRatio = UsingRatio
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if FundMortgageRatio:
            self.FundMortgageRatio = FundMortgageRatio


class QryInvestorPositionCombineDetail(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("CombInstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, ExchangeID=None, InvestUnitID=None, CombInstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")


class MarketDataAveragePrice(Struct):
    _fields_ = [
        ("AveragePrice", c_double),
    ]

    def __init__(self, AveragePrice=None):
        super().__init__()
        if AveragePrice:
            self.AveragePrice = AveragePrice


class VerifyInvestorPassword(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Password", c_char_Array_41),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, Password=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")


class UserIP(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_16),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("IPAddress", c_char_Array_33),
        ("IPMask", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, UserID=None, reserve1=None, reserve2=None, MacAddress=None, IPAddress=None, IPMask=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if IPMask:
            self.IPMask = IPMask.encode("GBK")


class TradingNoticeInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("SendTime", c_char_Array_9),
        ("FieldContent", c_char_Array_501),
        ("SequenceSeries", c_short),
        ("SequenceNo", c_int),
        ("InvestUnitID", c_char_Array_17),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, SendTime=None, FieldContent=None, SequenceSeries=None, SequenceNo=None, InvestUnitID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if SendTime:
            self.SendTime = SendTime.encode("GBK")
        if FieldContent:
            self.FieldContent = FieldContent.encode("GBK")
        if SequenceSeries:
            self.SequenceSeries = SequenceSeries
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class TradingNotice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorRange", c_char),
        ("InvestorID", c_char_Array_13),
        ("SequenceSeries", c_short),
        ("UserID", c_char_Array_16),
        ("SendTime", c_char_Array_9),
        ("SequenceNo", c_int),
        ("FieldContent", c_char_Array_501),
        ("InvestUnitID", c_char_Array_17),
    ]

    def __init__(self, BrokerID=None, InvestorRange=None, InvestorID=None, SequenceSeries=None, UserID=None, SendTime=None, SequenceNo=None, FieldContent=None, InvestUnitID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if SequenceSeries:
            self.SequenceSeries = SequenceSeries
        if UserID:
            self.UserID = UserID.encode("GBK")
        if SendTime:
            self.SendTime = SendTime.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if FieldContent:
            self.FieldContent = FieldContent.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryTradingNotice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InvestUnitID", c_char_Array_17),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, InvestUnitID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryErrOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class ErrOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("OrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char_Array_5),
        ("CombHedgeFlag", c_char_Array_5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int),
        ("TimeCondition", c_char),
        ("GTDDate", c_char_Array_9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("RequestID", c_int),
        ("UserForceClose", c_int),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("IsSwapOrder", c_int),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, OrderRef=None, UserID=None, OrderPriceType=None, Direction=None, CombOffsetFlag=None, CombHedgeFlag=None, LimitPrice=None, VolumeTotalOriginal=None, TimeCondition=None, GTDDate=None, VolumeCondition=None, MinVolume=None, ContingentCondition=None, StopPrice=None, ForceCloseReason=None, IsAutoSuspend=None, BusinessUnit=None, RequestID=None, UserForceClose=None, ErrorID=None, ErrorMsg=None, IsSwapOrder=None, ExchangeID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, ClientID=None, reserve2=None, MacAddress=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition.encode("GBK")
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition.encode("GBK")
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition.encode("GBK")
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason.encode("GBK")
        if IsAutoSuspend:
            self.IsAutoSuspend = IsAutoSuspend
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if UserForceClose:
            self.UserForceClose = UserForceClose
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if IsSwapOrder:
            self.IsSwapOrder = IsSwapOrder
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class ErrorConditionalOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("OrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char_Array_5),
        ("CombHedgeFlag", c_char_Array_5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int),
        ("TimeCondition", c_char),
        ("GTDDate", c_char_Array_9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int),
        ("BusinessUnit", c_char_Array_21),
        ("RequestID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("reserve2", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("OrderSysID", c_char_Array_21),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("VolumeTraded", c_int),
        ("VolumeTotal", c_int),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("ActiveTime", c_char_Array_9),
        ("SuspendTime", c_char_Array_9),
        ("UpdateTime", c_char_Array_9),
        ("CancelTime", c_char_Array_9),
        ("ActiveTraderID", c_char_Array_21),
        ("ClearingPartID", c_char_Array_11),
        ("SequenceNo", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("UserProductInfo", c_char_Array_11),
        ("StatusMsg", c_char_Array_81),
        ("UserForceClose", c_int),
        ("ActiveUserID", c_char_Array_16),
        ("BrokerOrderSeq", c_int),
        ("RelativeOrderSysID", c_char_Array_21),
        ("ZCETotalTradedVolume", c_int),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("IsSwapOrder", c_int),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("reserve3", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeInstID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, OrderRef=None, UserID=None, OrderPriceType=None, Direction=None, CombOffsetFlag=None, CombHedgeFlag=None, LimitPrice=None, VolumeTotalOriginal=None, TimeCondition=None, GTDDate=None, VolumeCondition=None, MinVolume=None, ContingentCondition=None, StopPrice=None, ForceCloseReason=None, IsAutoSuspend=None, BusinessUnit=None, RequestID=None, OrderLocalID=None, ExchangeID=None, ParticipantID=None, ClientID=None, reserve2=None, TraderID=None, InstallID=None, OrderSubmitStatus=None, NotifySequence=None, TradingDay=None, SettlementID=None, OrderSysID=None, OrderSource=None, OrderStatus=None, OrderType=None, VolumeTraded=None, VolumeTotal=None, InsertDate=None, InsertTime=None, ActiveTime=None, SuspendTime=None, UpdateTime=None, CancelTime=None, ActiveTraderID=None, ClearingPartID=None, SequenceNo=None, FrontID=None, SessionID=None, UserProductInfo=None, StatusMsg=None, UserForceClose=None, ActiveUserID=None, BrokerOrderSeq=None, RelativeOrderSysID=None, ZCETotalTradedVolume=None, ErrorID=None, ErrorMsg=None, IsSwapOrder=None, BranchID=None, InvestUnitID=None, AccountID=None, CurrencyID=None, reserve3=None, MacAddress=None, InstrumentID=None, ExchangeInstID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition.encode("GBK")
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition.encode("GBK")
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition.encode("GBK")
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason.encode("GBK")
        if IsAutoSuspend:
            self.IsAutoSuspend = IsAutoSuspend
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus.encode("GBK")
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if OrderSource:
            self.OrderSource = OrderSource.encode("GBK")
        if OrderStatus:
            self.OrderStatus = OrderStatus.encode("GBK")
        if OrderType:
            self.OrderType = OrderType.encode("GBK")
        if VolumeTraded:
            self.VolumeTraded = VolumeTraded
        if VolumeTotal:
            self.VolumeTotal = VolumeTotal
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if ActiveTime:
            self.ActiveTime = ActiveTime.encode("GBK")
        if SuspendTime:
            self.SuspendTime = SuspendTime.encode("GBK")
        if UpdateTime:
            self.UpdateTime = UpdateTime.encode("GBK")
        if CancelTime:
            self.CancelTime = CancelTime.encode("GBK")
        if ActiveTraderID:
            self.ActiveTraderID = ActiveTraderID.encode("GBK")
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if UserForceClose:
            self.UserForceClose = UserForceClose
        if ActiveUserID:
            self.ActiveUserID = ActiveUserID.encode("GBK")
        if BrokerOrderSeq:
            self.BrokerOrderSeq = BrokerOrderSeq
        if RelativeOrderSysID:
            self.RelativeOrderSysID = RelativeOrderSysID.encode("GBK")
        if ZCETotalTradedVolume:
            self.ZCETotalTradedVolume = ZCETotalTradedVolume
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if IsSwapOrder:
            self.IsSwapOrder = IsSwapOrder
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if reserve3:
            self.reserve3 = reserve3.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryErrOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class ErrOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OrderActionRef", c_int),
        ("OrderRef", c_char_Array_13),
        ("RequestID", c_int),
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int),
        ("ActionDate", c_char_Array_9),
        ("ActionTime", c_char_Array_9),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("OrderLocalID", c_char_Array_13),
        ("ActionLocalID", c_char_Array_13),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("BusinessUnit", c_char_Array_21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char_Array_16),
        ("StatusMsg", c_char_Array_81),
        ("reserve1", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("reserve2", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("InstrumentID", c_char_Array_81),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, OrderActionRef=None, OrderRef=None, RequestID=None, FrontID=None, SessionID=None, ExchangeID=None, OrderSysID=None, ActionFlag=None, LimitPrice=None, VolumeChange=None, ActionDate=None, ActionTime=None, TraderID=None, InstallID=None, OrderLocalID=None, ActionLocalID=None, ParticipantID=None, ClientID=None, BusinessUnit=None, OrderActionStatus=None, UserID=None, StatusMsg=None, reserve1=None, BranchID=None, InvestUnitID=None, reserve2=None, MacAddress=None, ErrorID=None, ErrorMsg=None, InstrumentID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OrderActionRef:
            self.OrderActionRef = OrderActionRef
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if FrontID:
            self.FrontID = FrontID
        if SessionID:
            self.SessionID = SessionID
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeChange:
            self.VolumeChange = VolumeChange
        if ActionDate:
            self.ActionDate = ActionDate.encode("GBK")
        if ActionTime:
            self.ActionTime = ActionTime.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderLocalID:
            self.OrderLocalID = OrderLocalID.encode("GBK")
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OrderActionStatus:
            self.OrderActionStatus = OrderActionStatus.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryExchangeSequence(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, ExchangeID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class ExchangeSequence(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("SequenceNo", c_int),
        ("MarketStatus", c_char),
    ]

    def __init__(self, ExchangeID=None, SequenceNo=None, MarketStatus=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if MarketStatus:
            self.MarketStatus = MarketStatus.encode("GBK")


class QryMaxOrderVolumeWithPrice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("MaxVolume", c_int),
        ("Price", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, Direction=None, OffsetFlag=None, HedgeFlag=None, MaxVolume=None, Price=None, ExchangeID=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if MaxVolume:
            self.MaxVolume = MaxVolume
        if Price:
            self.Price = Price
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryBrokerTradingParams(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("AccountID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, CurrencyID=None, AccountID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")


class BrokerTradingParams(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("MarginPriceType", c_char),
        ("Algorithm", c_char),
        ("AvailIncludeCloseProfit", c_char),
        ("CurrencyID", c_char_Array_4),
        ("OptionRoyaltyPriceType", c_char),
        ("AccountID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, MarginPriceType=None, Algorithm=None, AvailIncludeCloseProfit=None, CurrencyID=None, OptionRoyaltyPriceType=None, AccountID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if MarginPriceType:
            self.MarginPriceType = MarginPriceType.encode("GBK")
        if Algorithm:
            self.Algorithm = Algorithm.encode("GBK")
        if AvailIncludeCloseProfit:
            self.AvailIncludeCloseProfit = AvailIncludeCloseProfit.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if OptionRoyaltyPriceType:
            self.OptionRoyaltyPriceType = OptionRoyaltyPriceType.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")


class QryBrokerTradingAlgos(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("reserve1", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, ExchangeID=None, reserve1=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class BrokerTradingAlgos(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("reserve1", c_char_Array_31),
        ("HandlePositionAlgoID", c_char),
        ("FindMarginRateAlgoID", c_char),
        ("HandleTradingAccountAlgoID", c_char),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, ExchangeID=None, reserve1=None, HandlePositionAlgoID=None, FindMarginRateAlgoID=None, HandleTradingAccountAlgoID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HandlePositionAlgoID:
            self.HandlePositionAlgoID = HandlePositionAlgoID.encode("GBK")
        if FindMarginRateAlgoID:
            self.FindMarginRateAlgoID = FindMarginRateAlgoID.encode("GBK")
        if HandleTradingAccountAlgoID:
            self.HandleTradingAccountAlgoID = HandleTradingAccountAlgoID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QueryBrokerDeposit(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, BrokerID=None, ExchangeID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class BrokerDeposit(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("ParticipantID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("PreBalance", c_double),
        ("CurrMargin", c_double),
        ("CloseProfit", c_double),
        ("Balance", c_double),
        ("Deposit", c_double),
        ("Withdraw", c_double),
        ("Available", c_double),
        ("Reserve", c_double),
        ("FrozenMargin", c_double),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, ParticipantID=None, ExchangeID=None, PreBalance=None, CurrMargin=None, CloseProfit=None, Balance=None, Deposit=None, Withdraw=None, Available=None, Reserve=None, FrozenMargin=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if PreBalance:
            self.PreBalance = PreBalance
        if CurrMargin:
            self.CurrMargin = CurrMargin
        if CloseProfit:
            self.CloseProfit = CloseProfit
        if Balance:
            self.Balance = Balance
        if Deposit:
            self.Deposit = Deposit
        if Withdraw:
            self.Withdraw = Withdraw
        if Available:
            self.Available = Available
        if Reserve:
            self.Reserve = Reserve
        if FrozenMargin:
            self.FrozenMargin = FrozenMargin


class QryCFMMCBrokerKey(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
    ]

    def __init__(self, BrokerID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")


class CFMMCBrokerKey(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ParticipantID", c_char_Array_11),
        ("CreateDate", c_char_Array_9),
        ("CreateTime", c_char_Array_9),
        ("KeyID", c_int),
        ("CurrentKey", c_char_Array_21),
        ("KeyKind", c_char),
    ]

    def __init__(self, BrokerID=None, ParticipantID=None, CreateDate=None, CreateTime=None, KeyID=None, CurrentKey=None, KeyKind=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if CreateDate:
            self.CreateDate = CreateDate.encode("GBK")
        if CreateTime:
            self.CreateTime = CreateTime.encode("GBK")
        if KeyID:
            self.KeyID = KeyID
        if CurrentKey:
            self.CurrentKey = CurrentKey.encode("GBK")
        if KeyKind:
            self.KeyKind = KeyKind.encode("GBK")


class CFMMCTradingAccountKey(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ParticipantID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("KeyID", c_int),
        ("CurrentKey", c_char_Array_21),
    ]

    def __init__(self, BrokerID=None, ParticipantID=None, AccountID=None, KeyID=None, CurrentKey=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if KeyID:
            self.KeyID = KeyID
        if CurrentKey:
            self.CurrentKey = CurrentKey.encode("GBK")


class QryCFMMCTradingAccountKey(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class BrokerUserOTPParam(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("OTPVendorsID", c_char_Array_2),
        ("SerialNumber", c_char_Array_17),
        ("AuthKey", c_char_Array_41),
        ("LastDrift", c_int),
        ("LastSuccess", c_int),
        ("OTPType", c_char),
    ]

    def __init__(self, BrokerID=None, UserID=None, OTPVendorsID=None, SerialNumber=None, AuthKey=None, LastDrift=None, LastSuccess=None, OTPType=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OTPVendorsID:
            self.OTPVendorsID = OTPVendorsID.encode("GBK")
        if SerialNumber:
            self.SerialNumber = SerialNumber.encode("GBK")
        if AuthKey:
            self.AuthKey = AuthKey.encode("GBK")
        if LastDrift:
            self.LastDrift = LastDrift
        if LastSuccess:
            self.LastSuccess = LastSuccess
        if OTPType:
            self.OTPType = OTPType.encode("GBK")


class ManualSyncBrokerUserOTP(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("OTPType", c_char),
        ("FirstOTP", c_char_Array_41),
        ("SecondOTP", c_char_Array_41),
    ]

    def __init__(self, BrokerID=None, UserID=None, OTPType=None, FirstOTP=None, SecondOTP=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OTPType:
            self.OTPType = OTPType.encode("GBK")
        if FirstOTP:
            self.FirstOTP = FirstOTP.encode("GBK")
        if SecondOTP:
            self.SecondOTP = SecondOTP.encode("GBK")


class CommRateModel(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("CommModelID", c_char_Array_13),
        ("CommModelName", c_char_Array_161),
    ]

    def __init__(self, BrokerID=None, CommModelID=None, CommModelName=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if CommModelID:
            self.CommModelID = CommModelID.encode("GBK")
        if CommModelName:
            self.CommModelName = CommModelName.encode("GBK")


class QryCommRateModel(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("CommModelID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, CommModelID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if CommModelID:
            self.CommModelID = CommModelID.encode("GBK")


class MarginModel(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("MarginModelID", c_char_Array_13),
        ("MarginModelName", c_char_Array_161),
    ]

    def __init__(self, BrokerID=None, MarginModelID=None, MarginModelName=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if MarginModelID:
            self.MarginModelID = MarginModelID.encode("GBK")
        if MarginModelName:
            self.MarginModelName = MarginModelName.encode("GBK")


class QryMarginModel(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("MarginModelID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, MarginModelID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if MarginModelID:
            self.MarginModelID = MarginModelID.encode("GBK")


class EWarrantOffset(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("reserve1", c_char_Array_31),
        ("Direction", c_char),
        ("HedgeFlag", c_char),
        ("Volume", c_int),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, InvestorID=None, ExchangeID=None, reserve1=None, Direction=None, HedgeFlag=None, Volume=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if Volume:
            self.Volume = Volume
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryEWarrantOffset(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("reserve1", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExchangeID=None, reserve1=None, InvestUnitID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryInvestorProductGroupMargin(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("reserve1", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("ProductGroupID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, reserve1=None, HedgeFlag=None, ExchangeID=None, InvestUnitID=None, ProductGroupID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if ProductGroupID:
            self.ProductGroupID = ProductGroupID.encode("GBK")


class InvestorProductGroupMargin(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("FrozenMargin", c_double),
        ("LongFrozenMargin", c_double),
        ("ShortFrozenMargin", c_double),
        ("UseMargin", c_double),
        ("LongUseMargin", c_double),
        ("ShortUseMargin", c_double),
        ("ExchMargin", c_double),
        ("LongExchMargin", c_double),
        ("ShortExchMargin", c_double),
        ("CloseProfit", c_double),
        ("FrozenCommission", c_double),
        ("Commission", c_double),
        ("FrozenCash", c_double),
        ("CashIn", c_double),
        ("PositionProfit", c_double),
        ("OffsetAmount", c_double),
        ("LongOffsetAmount", c_double),
        ("ShortOffsetAmount", c_double),
        ("ExchOffsetAmount", c_double),
        ("LongExchOffsetAmount", c_double),
        ("ShortExchOffsetAmount", c_double),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("ProductGroupID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, BrokerID=None, InvestorID=None, TradingDay=None, SettlementID=None, FrozenMargin=None, LongFrozenMargin=None, ShortFrozenMargin=None, UseMargin=None, LongUseMargin=None, ShortUseMargin=None, ExchMargin=None, LongExchMargin=None, ShortExchMargin=None, CloseProfit=None, FrozenCommission=None, Commission=None, FrozenCash=None, CashIn=None, PositionProfit=None, OffsetAmount=None, LongOffsetAmount=None, ShortOffsetAmount=None, ExchOffsetAmount=None, LongExchOffsetAmount=None, ShortExchOffsetAmount=None, HedgeFlag=None, ExchangeID=None, InvestUnitID=None, ProductGroupID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if FrozenMargin:
            self.FrozenMargin = FrozenMargin
        if LongFrozenMargin:
            self.LongFrozenMargin = LongFrozenMargin
        if ShortFrozenMargin:
            self.ShortFrozenMargin = ShortFrozenMargin
        if UseMargin:
            self.UseMargin = UseMargin
        if LongUseMargin:
            self.LongUseMargin = LongUseMargin
        if ShortUseMargin:
            self.ShortUseMargin = ShortUseMargin
        if ExchMargin:
            self.ExchMargin = ExchMargin
        if LongExchMargin:
            self.LongExchMargin = LongExchMargin
        if ShortExchMargin:
            self.ShortExchMargin = ShortExchMargin
        if CloseProfit:
            self.CloseProfit = CloseProfit
        if FrozenCommission:
            self.FrozenCommission = FrozenCommission
        if Commission:
            self.Commission = Commission
        if FrozenCash:
            self.FrozenCash = FrozenCash
        if CashIn:
            self.CashIn = CashIn
        if PositionProfit:
            self.PositionProfit = PositionProfit
        if OffsetAmount:
            self.OffsetAmount = OffsetAmount
        if LongOffsetAmount:
            self.LongOffsetAmount = LongOffsetAmount
        if ShortOffsetAmount:
            self.ShortOffsetAmount = ShortOffsetAmount
        if ExchOffsetAmount:
            self.ExchOffsetAmount = ExchOffsetAmount
        if LongExchOffsetAmount:
            self.LongExchOffsetAmount = LongExchOffsetAmount
        if ShortExchOffsetAmount:
            self.ShortExchOffsetAmount = ShortExchOffsetAmount
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if ProductGroupID:
            self.ProductGroupID = ProductGroupID.encode("GBK")


class QueryCFMMCTradingAccountToken(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InvestUnitID", c_char_Array_17),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, InvestUnitID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class CFMMCTradingAccountToken(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ParticipantID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("KeyID", c_int),
        ("Token", c_char_Array_21),
    ]

    def __init__(self, BrokerID=None, ParticipantID=None, AccountID=None, KeyID=None, Token=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if KeyID:
            self.KeyID = KeyID
        if Token:
            self.Token = Token.encode("GBK")


class QryProductGroup(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("ProductID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, ExchangeID=None, ProductID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")


class ProductGroup(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("reserve2", c_char_Array_31),
        ("ProductID", c_char_Array_81),
        ("ProductGroupID", c_char_Array_81),
    ]

    def __init__(self, reserve1=None, ExchangeID=None, reserve2=None, ProductID=None, ProductGroupID=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if reserve2:
            self.reserve2 = reserve2.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ProductGroupID:
            self.ProductGroupID = ProductGroupID.encode("GBK")


class Bulletin(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("TradingDay", c_char_Array_9),
        ("BulletinID", c_int),
        ("SequenceNo", c_int),
        ("NewsType", c_char_Array_3),
        ("NewsUrgency", c_char),
        ("SendTime", c_char_Array_9),
        ("Abstract", c_char_Array_81),
        ("ComeFrom", c_char_Array_21),
        ("Content", c_char_Array_501),
        ("URLLink", c_char_Array_201),
        ("MarketID", c_char_Array_31),
    ]

    def __init__(self, ExchangeID=None, TradingDay=None, BulletinID=None, SequenceNo=None, NewsType=None, NewsUrgency=None, SendTime=None, Abstract=None, ComeFrom=None, Content=None, URLLink=None, MarketID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BulletinID:
            self.BulletinID = BulletinID
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if NewsType:
            self.NewsType = NewsType.encode("GBK")
        if NewsUrgency:
            self.NewsUrgency = NewsUrgency.encode("GBK")
        if SendTime:
            self.SendTime = SendTime.encode("GBK")
        if Abstract:
            self.Abstract = Abstract.encode("GBK")
        if ComeFrom:
            self.ComeFrom = ComeFrom.encode("GBK")
        if Content:
            self.Content = Content.encode("GBK")
        if URLLink:
            self.URLLink = URLLink.encode("GBK")
        if MarketID:
            self.MarketID = MarketID.encode("GBK")


class QryBulletin(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("BulletinID", c_int),
        ("SequenceNo", c_int),
        ("NewsType", c_char_Array_3),
        ("NewsUrgency", c_char),
    ]

    def __init__(self, ExchangeID=None, BulletinID=None, SequenceNo=None, NewsType=None, NewsUrgency=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if BulletinID:
            self.BulletinID = BulletinID
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if NewsType:
            self.NewsType = NewsType.encode("GBK")
        if NewsUrgency:
            self.NewsUrgency = NewsUrgency.encode("GBK")


class MulticastInstrument(Struct):
    _fields_ = [
        ("TopicID", c_int),
        ("reserve1", c_char_Array_31),
        ("InstrumentNo", c_int),
        ("CodePrice", c_double),
        ("VolumeMultiple", c_int),
        ("PriceTick", c_double),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, TopicID=None, reserve1=None, InstrumentNo=None, CodePrice=None, VolumeMultiple=None, PriceTick=None, InstrumentID=None):
        super().__init__()
        if TopicID:
            self.TopicID = TopicID
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentNo:
            self.InstrumentNo = InstrumentNo
        if CodePrice:
            self.CodePrice = CodePrice
        if VolumeMultiple:
            self.VolumeMultiple = VolumeMultiple
        if PriceTick:
            self.PriceTick = PriceTick
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryMulticastInstrument(Struct):
    _fields_ = [
        ("TopicID", c_int),
        ("reserve1", c_char_Array_31),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, TopicID=None, reserve1=None, InstrumentID=None):
        super().__init__()
        if TopicID:
            self.TopicID = TopicID
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class AppIDAuthAssign(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AppID", c_char_Array_33),
        ("DRIdentityID", c_int),
    ]

    def __init__(self, BrokerID=None, AppID=None, DRIdentityID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AppID:
            self.AppID = AppID.encode("GBK")
        if DRIdentityID:
            self.DRIdentityID = DRIdentityID


class ReqOpenAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("Gender", c_char),
        ("CountryCode", c_char_Array_21),
        ("CustType", c_char),
        ("Address", c_char_Array_101),
        ("ZipCode", c_char_Array_7),
        ("Telephone", c_char_Array_41),
        ("MobilePhone", c_char_Array_21),
        ("Fax", c_char_Array_41),
        ("EMail", c_char_Array_41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("CashExchangeCode", c_char),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("TID", c_int),
        ("UserID", c_char_Array_16),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, Gender=None, CountryCode=None, CustType=None, Address=None, ZipCode=None, Telephone=None, MobilePhone=None, Fax=None, EMail=None, MoneyAccountStatus=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, InstallID=None, VerifyCertNoFlag=None, CurrencyID=None, CashExchangeCode=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, TID=None, UserID=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender.encode("GBK")
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if ZipCode:
            self.ZipCode = ZipCode.encode("GBK")
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if MobilePhone:
            self.MobilePhone = MobilePhone.encode("GBK")
        if Fax:
            self.Fax = Fax.encode("GBK")
        if EMail:
            self.EMail = EMail.encode("GBK")
        if MoneyAccountStatus:
            self.MoneyAccountStatus = MoneyAccountStatus.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if CashExchangeCode:
            self.CashExchangeCode = CashExchangeCode.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if TID:
            self.TID = TID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class ReqCancelAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("Gender", c_char),
        ("CountryCode", c_char_Array_21),
        ("CustType", c_char),
        ("Address", c_char_Array_101),
        ("ZipCode", c_char_Array_7),
        ("Telephone", c_char_Array_41),
        ("MobilePhone", c_char_Array_21),
        ("Fax", c_char_Array_41),
        ("EMail", c_char_Array_41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("CashExchangeCode", c_char),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("TID", c_int),
        ("UserID", c_char_Array_16),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, Gender=None, CountryCode=None, CustType=None, Address=None, ZipCode=None, Telephone=None, MobilePhone=None, Fax=None, EMail=None, MoneyAccountStatus=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, InstallID=None, VerifyCertNoFlag=None, CurrencyID=None, CashExchangeCode=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, TID=None, UserID=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender.encode("GBK")
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if ZipCode:
            self.ZipCode = ZipCode.encode("GBK")
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if MobilePhone:
            self.MobilePhone = MobilePhone.encode("GBK")
        if Fax:
            self.Fax = Fax.encode("GBK")
        if EMail:
            self.EMail = EMail.encode("GBK")
        if MoneyAccountStatus:
            self.MoneyAccountStatus = MoneyAccountStatus.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if CashExchangeCode:
            self.CashExchangeCode = CashExchangeCode.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if TID:
            self.TID = TID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class ReqChangeAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("Gender", c_char),
        ("CountryCode", c_char_Array_21),
        ("CustType", c_char),
        ("Address", c_char_Array_101),
        ("ZipCode", c_char_Array_7),
        ("Telephone", c_char_Array_41),
        ("MobilePhone", c_char_Array_21),
        ("Fax", c_char_Array_41),
        ("EMail", c_char_Array_41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("NewBankAccount", c_char_Array_41),
        ("NewBankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("BankAccType", c_char),
        ("InstallID", c_int),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("TID", c_int),
        ("Digest", c_char_Array_36),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, Gender=None, CountryCode=None, CustType=None, Address=None, ZipCode=None, Telephone=None, MobilePhone=None, Fax=None, EMail=None, MoneyAccountStatus=None, BankAccount=None, BankPassWord=None, NewBankAccount=None, NewBankPassWord=None, AccountID=None, Password=None, BankAccType=None, InstallID=None, VerifyCertNoFlag=None, CurrencyID=None, BrokerIDByBank=None, BankPwdFlag=None, SecuPwdFlag=None, TID=None, Digest=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender.encode("GBK")
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if ZipCode:
            self.ZipCode = ZipCode.encode("GBK")
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if MobilePhone:
            self.MobilePhone = MobilePhone.encode("GBK")
        if Fax:
            self.Fax = Fax.encode("GBK")
        if EMail:
            self.EMail = EMail.encode("GBK")
        if MoneyAccountStatus:
            self.MoneyAccountStatus = MoneyAccountStatus.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if NewBankAccount:
            self.NewBankAccount = NewBankAccount.encode("GBK")
        if NewBankPassWord:
            self.NewBankPassWord = NewBankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if TID:
            self.TID = TID
        if Digest:
            self.Digest = Digest.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class ReqTransfer(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("FutureSerial", c_int),
        ("UserID", c_char_Array_16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("TradeAmount", c_double),
        ("FutureFetchAmount", c_double),
        ("FeePayFlag", c_char),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("Message", c_char_Array_129),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("TransferStatus", c_char),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, InstallID=None, FutureSerial=None, UserID=None, VerifyCertNoFlag=None, CurrencyID=None, TradeAmount=None, FutureFetchAmount=None, FeePayFlag=None, CustFee=None, BrokerFee=None, Message=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, RequestID=None, TID=None, TransferStatus=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if UserID:
            self.UserID = UserID.encode("GBK")
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if FutureFetchAmount:
            self.FutureFetchAmount = FutureFetchAmount
        if FeePayFlag:
            self.FeePayFlag = FeePayFlag.encode("GBK")
        if CustFee:
            self.CustFee = CustFee
        if BrokerFee:
            self.BrokerFee = BrokerFee
        if Message:
            self.Message = Message.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if TransferStatus:
            self.TransferStatus = TransferStatus.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class RspTransfer(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("FutureSerial", c_int),
        ("UserID", c_char_Array_16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("TradeAmount", c_double),
        ("FutureFetchAmount", c_double),
        ("FeePayFlag", c_char),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("Message", c_char_Array_129),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("TransferStatus", c_char),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, InstallID=None, FutureSerial=None, UserID=None, VerifyCertNoFlag=None, CurrencyID=None, TradeAmount=None, FutureFetchAmount=None, FeePayFlag=None, CustFee=None, BrokerFee=None, Message=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, RequestID=None, TID=None, TransferStatus=None, ErrorID=None, ErrorMsg=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if UserID:
            self.UserID = UserID.encode("GBK")
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if FutureFetchAmount:
            self.FutureFetchAmount = FutureFetchAmount
        if FeePayFlag:
            self.FeePayFlag = FeePayFlag.encode("GBK")
        if CustFee:
            self.CustFee = CustFee
        if BrokerFee:
            self.BrokerFee = BrokerFee
        if Message:
            self.Message = Message.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if TransferStatus:
            self.TransferStatus = TransferStatus.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class ReqRepeal(Struct):
    _fields_ = [
        ("RepealTimeInterval", c_int),
        ("RepealedTimes", c_int),
        ("BankRepealFlag", c_char),
        ("BrokerRepealFlag", c_char),
        ("PlateRepealSerial", c_int),
        ("BankRepealSerial", c_char_Array_13),
        ("FutureRepealSerial", c_int),
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("FutureSerial", c_int),
        ("UserID", c_char_Array_16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("TradeAmount", c_double),
        ("FutureFetchAmount", c_double),
        ("FeePayFlag", c_char),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("Message", c_char_Array_129),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("TransferStatus", c_char),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, RepealTimeInterval=None, RepealedTimes=None, BankRepealFlag=None, BrokerRepealFlag=None, PlateRepealSerial=None, BankRepealSerial=None, FutureRepealSerial=None, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, InstallID=None, FutureSerial=None, UserID=None, VerifyCertNoFlag=None, CurrencyID=None, TradeAmount=None, FutureFetchAmount=None, FeePayFlag=None, CustFee=None, BrokerFee=None, Message=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, RequestID=None, TID=None, TransferStatus=None, LongCustomerName=None):
        super().__init__()
        if RepealTimeInterval:
            self.RepealTimeInterval = RepealTimeInterval
        if RepealedTimes:
            self.RepealedTimes = RepealedTimes
        if BankRepealFlag:
            self.BankRepealFlag = BankRepealFlag.encode("GBK")
        if BrokerRepealFlag:
            self.BrokerRepealFlag = BrokerRepealFlag.encode("GBK")
        if PlateRepealSerial:
            self.PlateRepealSerial = PlateRepealSerial
        if BankRepealSerial:
            self.BankRepealSerial = BankRepealSerial.encode("GBK")
        if FutureRepealSerial:
            self.FutureRepealSerial = FutureRepealSerial
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if UserID:
            self.UserID = UserID.encode("GBK")
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if FutureFetchAmount:
            self.FutureFetchAmount = FutureFetchAmount
        if FeePayFlag:
            self.FeePayFlag = FeePayFlag.encode("GBK")
        if CustFee:
            self.CustFee = CustFee
        if BrokerFee:
            self.BrokerFee = BrokerFee
        if Message:
            self.Message = Message.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if TransferStatus:
            self.TransferStatus = TransferStatus.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class RspRepeal(Struct):
    _fields_ = [
        ("RepealTimeInterval", c_int),
        ("RepealedTimes", c_int),
        ("BankRepealFlag", c_char),
        ("BrokerRepealFlag", c_char),
        ("PlateRepealSerial", c_int),
        ("BankRepealSerial", c_char_Array_13),
        ("FutureRepealSerial", c_int),
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("FutureSerial", c_int),
        ("UserID", c_char_Array_16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("TradeAmount", c_double),
        ("FutureFetchAmount", c_double),
        ("FeePayFlag", c_char),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("Message", c_char_Array_129),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("TransferStatus", c_char),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, RepealTimeInterval=None, RepealedTimes=None, BankRepealFlag=None, BrokerRepealFlag=None, PlateRepealSerial=None, BankRepealSerial=None, FutureRepealSerial=None, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, InstallID=None, FutureSerial=None, UserID=None, VerifyCertNoFlag=None, CurrencyID=None, TradeAmount=None, FutureFetchAmount=None, FeePayFlag=None, CustFee=None, BrokerFee=None, Message=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, RequestID=None, TID=None, TransferStatus=None, ErrorID=None, ErrorMsg=None, LongCustomerName=None):
        super().__init__()
        if RepealTimeInterval:
            self.RepealTimeInterval = RepealTimeInterval
        if RepealedTimes:
            self.RepealedTimes = RepealedTimes
        if BankRepealFlag:
            self.BankRepealFlag = BankRepealFlag.encode("GBK")
        if BrokerRepealFlag:
            self.BrokerRepealFlag = BrokerRepealFlag.encode("GBK")
        if PlateRepealSerial:
            self.PlateRepealSerial = PlateRepealSerial
        if BankRepealSerial:
            self.BankRepealSerial = BankRepealSerial.encode("GBK")
        if FutureRepealSerial:
            self.FutureRepealSerial = FutureRepealSerial
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if UserID:
            self.UserID = UserID.encode("GBK")
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if FutureFetchAmount:
            self.FutureFetchAmount = FutureFetchAmount
        if FeePayFlag:
            self.FeePayFlag = FeePayFlag.encode("GBK")
        if CustFee:
            self.CustFee = CustFee
        if BrokerFee:
            self.BrokerFee = BrokerFee
        if Message:
            self.Message = Message.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if TransferStatus:
            self.TransferStatus = TransferStatus.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class ReqQueryAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("FutureSerial", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, FutureSerial=None, InstallID=None, UserID=None, VerifyCertNoFlag=None, CurrencyID=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, RequestID=None, TID=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class RspQueryAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("FutureSerial", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("BankUseAmount", c_double),
        ("BankFetchAmount", c_double),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, FutureSerial=None, InstallID=None, UserID=None, VerifyCertNoFlag=None, CurrencyID=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, RequestID=None, TID=None, BankUseAmount=None, BankFetchAmount=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if BankUseAmount:
            self.BankUseAmount = BankUseAmount
        if BankFetchAmount:
            self.BankFetchAmount = BankFetchAmount
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class FutureSignIO(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("Digest", c_char_Array_36),
        ("CurrencyID", c_char_Array_4),
        ("DeviceID", c_char_Array_3),
        ("BrokerIDByBank", c_char_Array_33),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, InstallID=None, UserID=None, Digest=None, CurrencyID=None, DeviceID=None, BrokerIDByBank=None, OperNo=None, RequestID=None, TID=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID


class RspFutureSignIn(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("Digest", c_char_Array_36),
        ("CurrencyID", c_char_Array_4),
        ("DeviceID", c_char_Array_3),
        ("BrokerIDByBank", c_char_Array_33),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("PinKey", c_char_Array_129),
        ("MacKey", c_char_Array_129),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, InstallID=None, UserID=None, Digest=None, CurrencyID=None, DeviceID=None, BrokerIDByBank=None, OperNo=None, RequestID=None, TID=None, ErrorID=None, ErrorMsg=None, PinKey=None, MacKey=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if PinKey:
            self.PinKey = PinKey.encode("GBK")
        if MacKey:
            self.MacKey = MacKey.encode("GBK")


class ReqFutureSignOut(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("Digest", c_char_Array_36),
        ("CurrencyID", c_char_Array_4),
        ("DeviceID", c_char_Array_3),
        ("BrokerIDByBank", c_char_Array_33),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, InstallID=None, UserID=None, Digest=None, CurrencyID=None, DeviceID=None, BrokerIDByBank=None, OperNo=None, RequestID=None, TID=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID


class RspFutureSignOut(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("Digest", c_char_Array_36),
        ("CurrencyID", c_char_Array_4),
        ("DeviceID", c_char_Array_3),
        ("BrokerIDByBank", c_char_Array_33),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, InstallID=None, UserID=None, Digest=None, CurrencyID=None, DeviceID=None, BrokerIDByBank=None, OperNo=None, RequestID=None, TID=None, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class ReqQueryTradeResultBySerial(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("Reference", c_int),
        ("RefrenceIssureType", c_char),
        ("RefrenceIssure", c_char_Array_36),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("CurrencyID", c_char_Array_4),
        ("TradeAmount", c_double),
        ("Digest", c_char_Array_36),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, Reference=None, RefrenceIssureType=None, RefrenceIssure=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, CurrencyID=None, TradeAmount=None, Digest=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if Reference:
            self.Reference = Reference
        if RefrenceIssureType:
            self.RefrenceIssureType = RefrenceIssureType.encode("GBK")
        if RefrenceIssure:
            self.RefrenceIssure = RefrenceIssure.encode("GBK")
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if Digest:
            self.Digest = Digest.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class RspQueryTradeResultBySerial(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("Reference", c_int),
        ("RefrenceIssureType", c_char),
        ("RefrenceIssure", c_char_Array_36),
        ("OriginReturnCode", c_char_Array_7),
        ("OriginDescrInfoForReturnCode", c_char_Array_129),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("CurrencyID", c_char_Array_4),
        ("TradeAmount", c_double),
        ("Digest", c_char_Array_36),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, ErrorID=None, ErrorMsg=None, Reference=None, RefrenceIssureType=None, RefrenceIssure=None, OriginReturnCode=None, OriginDescrInfoForReturnCode=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, CurrencyID=None, TradeAmount=None, Digest=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if Reference:
            self.Reference = Reference
        if RefrenceIssureType:
            self.RefrenceIssureType = RefrenceIssureType.encode("GBK")
        if RefrenceIssure:
            self.RefrenceIssure = RefrenceIssure.encode("GBK")
        if OriginReturnCode:
            self.OriginReturnCode = OriginReturnCode.encode("GBK")
        if OriginDescrInfoForReturnCode:
            self.OriginDescrInfoForReturnCode = OriginDescrInfoForReturnCode.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if Digest:
            self.Digest = Digest.encode("GBK")


class ReqDayEndFileReady(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("FileBusinessCode", c_char),
        ("Digest", c_char_Array_36),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, FileBusinessCode=None, Digest=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if FileBusinessCode:
            self.FileBusinessCode = FileBusinessCode.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")


class ReturnResult(Struct):
    _fields_ = [
        ("ReturnCode", c_char_Array_7),
        ("DescrInfoForReturnCode", c_char_Array_129),
    ]

    def __init__(self, ReturnCode=None, DescrInfoForReturnCode=None):
        super().__init__()
        if ReturnCode:
            self.ReturnCode = ReturnCode.encode("GBK")
        if DescrInfoForReturnCode:
            self.DescrInfoForReturnCode = DescrInfoForReturnCode.encode("GBK")


class VerifyFuturePassword(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("InstallID", c_int),
        ("TID", c_int),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, AccountID=None, Password=None, BankAccount=None, BankPassWord=None, InstallID=None, TID=None, CurrencyID=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if TID:
            self.TID = TID
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class VerifyCustInfo(Struct):
    _fields_ = [
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, LongCustomerName=None):
        super().__init__()
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class VerifyFuturePasswordAndCustInfo(Struct):
    _fields_ = [
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("CurrencyID", c_char_Array_4),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, AccountID=None, Password=None, CurrencyID=None, LongCustomerName=None):
        super().__init__()
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class DepositResultInform(Struct):
    _fields_ = [
        ("DepositSeqNo", c_char_Array_15),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Deposit", c_double),
        ("RequestID", c_int),
        ("ReturnCode", c_char_Array_7),
        ("DescrInfoForReturnCode", c_char_Array_129),
    ]

    def __init__(self, DepositSeqNo=None, BrokerID=None, InvestorID=None, Deposit=None, RequestID=None, ReturnCode=None, DescrInfoForReturnCode=None):
        super().__init__()
        if DepositSeqNo:
            self.DepositSeqNo = DepositSeqNo.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Deposit:
            self.Deposit = Deposit
        if RequestID:
            self.RequestID = RequestID
        if ReturnCode:
            self.ReturnCode = ReturnCode.encode("GBK")
        if DescrInfoForReturnCode:
            self.DescrInfoForReturnCode = DescrInfoForReturnCode.encode("GBK")


class ReqSyncKey(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("Message", c_char_Array_129),
        ("DeviceID", c_char_Array_3),
        ("BrokerIDByBank", c_char_Array_33),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, InstallID=None, UserID=None, Message=None, DeviceID=None, BrokerIDByBank=None, OperNo=None, RequestID=None, TID=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Message:
            self.Message = Message.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID


class RspSyncKey(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("Message", c_char_Array_129),
        ("DeviceID", c_char_Array_3),
        ("BrokerIDByBank", c_char_Array_33),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, InstallID=None, UserID=None, Message=None, DeviceID=None, BrokerIDByBank=None, OperNo=None, RequestID=None, TID=None, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Message:
            self.Message = Message.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class NotifyQueryAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustType", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("FutureSerial", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("BankUseAmount", c_double),
        ("BankFetchAmount", c_double),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, CustType=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, FutureSerial=None, InstallID=None, UserID=None, VerifyCertNoFlag=None, CurrencyID=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, RequestID=None, TID=None, BankUseAmount=None, BankFetchAmount=None, ErrorID=None, ErrorMsg=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if BankUseAmount:
            self.BankUseAmount = BankUseAmount
        if BankFetchAmount:
            self.BankFetchAmount = BankFetchAmount
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class TransferSerial(Struct):
    _fields_ = [
        ("PlateSerial", c_int),
        ("TradeDate", c_char_Array_9),
        ("TradingDay", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("TradeCode", c_char_Array_7),
        ("SessionID", c_int),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BankAccType", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankSerial", c_char_Array_13),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("FutureAccType", c_char),
        ("AccountID", c_char_Array_13),
        ("InvestorID", c_char_Array_13),
        ("FutureSerial", c_int),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CurrencyID", c_char_Array_4),
        ("TradeAmount", c_double),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("AvailabilityFlag", c_char),
        ("OperatorCode", c_char_Array_17),
        ("BankNewAccount", c_char_Array_41),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, PlateSerial=None, TradeDate=None, TradingDay=None, TradeTime=None, TradeCode=None, SessionID=None, BankID=None, BankBranchID=None, BankAccType=None, BankAccount=None, BankSerial=None, BrokerID=None, BrokerBranchID=None, FutureAccType=None, AccountID=None, InvestorID=None, FutureSerial=None, IdCardType=None, IdentifiedCardNo=None, CurrencyID=None, TradeAmount=None, CustFee=None, BrokerFee=None, AvailabilityFlag=None, OperatorCode=None, BankNewAccount=None, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if FutureAccType:
            self.FutureAccType = FutureAccType.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if CustFee:
            self.CustFee = CustFee
        if BrokerFee:
            self.BrokerFee = BrokerFee
        if AvailabilityFlag:
            self.AvailabilityFlag = AvailabilityFlag.encode("GBK")
        if OperatorCode:
            self.OperatorCode = OperatorCode.encode("GBK")
        if BankNewAccount:
            self.BankNewAccount = BankNewAccount.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class QryTransferSerial(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("BankID", c_char_Array_4),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, AccountID=None, BankID=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class NotifyFutureSignIn(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("Digest", c_char_Array_36),
        ("CurrencyID", c_char_Array_4),
        ("DeviceID", c_char_Array_3),
        ("BrokerIDByBank", c_char_Array_33),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("PinKey", c_char_Array_129),
        ("MacKey", c_char_Array_129),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, InstallID=None, UserID=None, Digest=None, CurrencyID=None, DeviceID=None, BrokerIDByBank=None, OperNo=None, RequestID=None, TID=None, ErrorID=None, ErrorMsg=None, PinKey=None, MacKey=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if PinKey:
            self.PinKey = PinKey.encode("GBK")
        if MacKey:
            self.MacKey = MacKey.encode("GBK")


class NotifyFutureSignOut(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("Digest", c_char_Array_36),
        ("CurrencyID", c_char_Array_4),
        ("DeviceID", c_char_Array_3),
        ("BrokerIDByBank", c_char_Array_33),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, InstallID=None, UserID=None, Digest=None, CurrencyID=None, DeviceID=None, BrokerIDByBank=None, OperNo=None, RequestID=None, TID=None, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class NotifySyncKey(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("InstallID", c_int),
        ("UserID", c_char_Array_16),
        ("Message", c_char_Array_129),
        ("DeviceID", c_char_Array_3),
        ("BrokerIDByBank", c_char_Array_33),
        ("OperNo", c_char_Array_17),
        ("RequestID", c_int),
        ("TID", c_int),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, InstallID=None, UserID=None, Message=None, DeviceID=None, BrokerIDByBank=None, OperNo=None, RequestID=None, TID=None, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if InstallID:
            self.InstallID = InstallID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Message:
            self.Message = Message.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class QryAccountregister(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, AccountID=None, BankID=None, BankBranchID=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class Accountregister(Struct):
    _fields_ = [
        ("TradeDay", c_char_Array_9),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BankAccount", c_char_Array_41),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("AccountID", c_char_Array_13),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("CustomerName", c_char_Array_51),
        ("CurrencyID", c_char_Array_4),
        ("OpenOrDestroy", c_char),
        ("RegDate", c_char_Array_9),
        ("OutDate", c_char_Array_9),
        ("TID", c_int),
        ("CustType", c_char),
        ("BankAccType", c_char),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeDay=None, BankID=None, BankBranchID=None, BankAccount=None, BrokerID=None, BrokerBranchID=None, AccountID=None, IdCardType=None, IdentifiedCardNo=None, CustomerName=None, CurrencyID=None, OpenOrDestroy=None, RegDate=None, OutDate=None, TID=None, CustType=None, BankAccType=None, LongCustomerName=None):
        super().__init__()
        if TradeDay:
            self.TradeDay = TradeDay.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if OpenOrDestroy:
            self.OpenOrDestroy = OpenOrDestroy.encode("GBK")
        if RegDate:
            self.RegDate = RegDate.encode("GBK")
        if OutDate:
            self.OutDate = OutDate.encode("GBK")
        if TID:
            self.TID = TID
        if CustType:
            self.CustType = CustType.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class OpenAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("Gender", c_char),
        ("CountryCode", c_char_Array_21),
        ("CustType", c_char),
        ("Address", c_char_Array_101),
        ("ZipCode", c_char_Array_7),
        ("Telephone", c_char_Array_41),
        ("MobilePhone", c_char_Array_21),
        ("Fax", c_char_Array_41),
        ("EMail", c_char_Array_41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("CashExchangeCode", c_char),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("TID", c_int),
        ("UserID", c_char_Array_16),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, Gender=None, CountryCode=None, CustType=None, Address=None, ZipCode=None, Telephone=None, MobilePhone=None, Fax=None, EMail=None, MoneyAccountStatus=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, InstallID=None, VerifyCertNoFlag=None, CurrencyID=None, CashExchangeCode=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, TID=None, UserID=None, ErrorID=None, ErrorMsg=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender.encode("GBK")
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if ZipCode:
            self.ZipCode = ZipCode.encode("GBK")
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if MobilePhone:
            self.MobilePhone = MobilePhone.encode("GBK")
        if Fax:
            self.Fax = Fax.encode("GBK")
        if EMail:
            self.EMail = EMail.encode("GBK")
        if MoneyAccountStatus:
            self.MoneyAccountStatus = MoneyAccountStatus.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if CashExchangeCode:
            self.CashExchangeCode = CashExchangeCode.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if TID:
            self.TID = TID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class CancelAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("Gender", c_char),
        ("CountryCode", c_char_Array_21),
        ("CustType", c_char),
        ("Address", c_char_Array_101),
        ("ZipCode", c_char_Array_7),
        ("Telephone", c_char_Array_41),
        ("MobilePhone", c_char_Array_21),
        ("Fax", c_char_Array_41),
        ("EMail", c_char_Array_41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("InstallID", c_int),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("CashExchangeCode", c_char),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("DeviceID", c_char_Array_3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankSecuAcc", c_char_Array_41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char_Array_17),
        ("TID", c_int),
        ("UserID", c_char_Array_16),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, Gender=None, CountryCode=None, CustType=None, Address=None, ZipCode=None, Telephone=None, MobilePhone=None, Fax=None, EMail=None, MoneyAccountStatus=None, BankAccount=None, BankPassWord=None, AccountID=None, Password=None, InstallID=None, VerifyCertNoFlag=None, CurrencyID=None, CashExchangeCode=None, Digest=None, BankAccType=None, DeviceID=None, BankSecuAccType=None, BrokerIDByBank=None, BankSecuAcc=None, BankPwdFlag=None, SecuPwdFlag=None, OperNo=None, TID=None, UserID=None, ErrorID=None, ErrorMsg=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender.encode("GBK")
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if ZipCode:
            self.ZipCode = ZipCode.encode("GBK")
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if MobilePhone:
            self.MobilePhone = MobilePhone.encode("GBK")
        if Fax:
            self.Fax = Fax.encode("GBK")
        if EMail:
            self.EMail = EMail.encode("GBK")
        if MoneyAccountStatus:
            self.MoneyAccountStatus = MoneyAccountStatus.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if CashExchangeCode:
            self.CashExchangeCode = CashExchangeCode.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if TID:
            self.TID = TID
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class ChangeAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("Gender", c_char),
        ("CountryCode", c_char_Array_21),
        ("CustType", c_char),
        ("Address", c_char_Array_101),
        ("ZipCode", c_char_Array_7),
        ("Telephone", c_char_Array_41),
        ("MobilePhone", c_char_Array_21),
        ("Fax", c_char_Array_41),
        ("EMail", c_char_Array_41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("NewBankAccount", c_char_Array_41),
        ("NewBankPassWord", c_char_Array_41),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("BankAccType", c_char),
        ("InstallID", c_int),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("BrokerIDByBank", c_char_Array_33),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("TID", c_int),
        ("Digest", c_char_Array_36),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("LongCustomerName", c_char_Array_161),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, Gender=None, CountryCode=None, CustType=None, Address=None, ZipCode=None, Telephone=None, MobilePhone=None, Fax=None, EMail=None, MoneyAccountStatus=None, BankAccount=None, BankPassWord=None, NewBankAccount=None, NewBankPassWord=None, AccountID=None, Password=None, BankAccType=None, InstallID=None, VerifyCertNoFlag=None, CurrencyID=None, BrokerIDByBank=None, BankPwdFlag=None, SecuPwdFlag=None, TID=None, Digest=None, ErrorID=None, ErrorMsg=None, LongCustomerName=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender.encode("GBK")
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if ZipCode:
            self.ZipCode = ZipCode.encode("GBK")
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if MobilePhone:
            self.MobilePhone = MobilePhone.encode("GBK")
        if Fax:
            self.Fax = Fax.encode("GBK")
        if EMail:
            self.EMail = EMail.encode("GBK")
        if MoneyAccountStatus:
            self.MoneyAccountStatus = MoneyAccountStatus.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if NewBankAccount:
            self.NewBankAccount = NewBankAccount.encode("GBK")
        if NewBankPassWord:
            self.NewBankPassWord = NewBankPassWord.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag.encode("GBK")
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag.encode("GBK")
        if TID:
            self.TID = TID
        if Digest:
            self.Digest = Digest.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if LongCustomerName:
            self.LongCustomerName = LongCustomerName.encode("GBK")


class SecAgentACIDMap(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("BrokerSecAgentID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, UserID=None, AccountID=None, CurrencyID=None, BrokerSecAgentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if BrokerSecAgentID:
            self.BrokerSecAgentID = BrokerSecAgentID.encode("GBK")


class QrySecAgentACIDMap(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, UserID=None, AccountID=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class UserRightsAssign(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("DRIdentityID", c_int),
    ]

    def __init__(self, BrokerID=None, UserID=None, DRIdentityID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if DRIdentityID:
            self.DRIdentityID = DRIdentityID


class BrokerUserRightAssign(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("DRIdentityID", c_int),
        ("Tradeable", c_int),
    ]

    def __init__(self, BrokerID=None, DRIdentityID=None, Tradeable=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if DRIdentityID:
            self.DRIdentityID = DRIdentityID
        if Tradeable:
            self.Tradeable = Tradeable


class DRTransfer(Struct):
    _fields_ = [
        ("OrigDRIdentityID", c_int),
        ("DestDRIdentityID", c_int),
        ("OrigBrokerID", c_char_Array_11),
        ("DestBrokerID", c_char_Array_11),
    ]

    def __init__(self, OrigDRIdentityID=None, DestDRIdentityID=None, OrigBrokerID=None, DestBrokerID=None):
        super().__init__()
        if OrigDRIdentityID:
            self.OrigDRIdentityID = OrigDRIdentityID
        if DestDRIdentityID:
            self.DestDRIdentityID = DestDRIdentityID
        if OrigBrokerID:
            self.OrigBrokerID = OrigBrokerID.encode("GBK")
        if DestBrokerID:
            self.DestBrokerID = DestBrokerID.encode("GBK")


class FensUserInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("LoginMode", c_char),
    ]

    def __init__(self, BrokerID=None, UserID=None, LoginMode=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if LoginMode:
            self.LoginMode = LoginMode.encode("GBK")


class CurrTransferIdentity(Struct):
    _fields_ = [
        ("IdentityID", c_int),
    ]

    def __init__(self, IdentityID=None):
        super().__init__()
        if IdentityID:
            self.IdentityID = IdentityID


class LoginForbiddenUser(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("reserve1", c_char_Array_16),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, UserID=None, reserve1=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryLoginForbiddenUser(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, BrokerID=None, UserID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class TradingAccountReserve(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("Reserve", c_double),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, AccountID=None, Reserve=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Reserve:
            self.Reserve = Reserve
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class QryLoginForbiddenIP(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_16),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, reserve1=None, IPAddress=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryIPList(Struct):
    _fields_ = [
        ("reserve1", c_char_Array_16),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, reserve1=None, IPAddress=None):
        super().__init__()
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryUserRightsAssign(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, BrokerID=None, UserID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class ReserveOpenAccountConfirm(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_161),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("Gender", c_char),
        ("CountryCode", c_char_Array_21),
        ("CustType", c_char),
        ("Address", c_char_Array_101),
        ("ZipCode", c_char_Array_7),
        ("Telephone", c_char_Array_41),
        ("MobilePhone", c_char_Array_21),
        ("Fax", c_char_Array_41),
        ("EMail", c_char_Array_41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("InstallID", c_int),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("TID", c_int),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("BankReserveOpenSeq", c_char_Array_13),
        ("BookDate", c_char_Array_9),
        ("BookPsw", c_char_Array_41),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, Gender=None, CountryCode=None, CustType=None, Address=None, ZipCode=None, Telephone=None, MobilePhone=None, Fax=None, EMail=None, MoneyAccountStatus=None, BankAccount=None, BankPassWord=None, InstallID=None, VerifyCertNoFlag=None, CurrencyID=None, Digest=None, BankAccType=None, BrokerIDByBank=None, TID=None, AccountID=None, Password=None, BankReserveOpenSeq=None, BookDate=None, BookPsw=None, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender.encode("GBK")
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if ZipCode:
            self.ZipCode = ZipCode.encode("GBK")
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if MobilePhone:
            self.MobilePhone = MobilePhone.encode("GBK")
        if Fax:
            self.Fax = Fax.encode("GBK")
        if EMail:
            self.EMail = EMail.encode("GBK")
        if MoneyAccountStatus:
            self.MoneyAccountStatus = MoneyAccountStatus.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if TID:
            self.TID = TID
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if BankReserveOpenSeq:
            self.BankReserveOpenSeq = BankReserveOpenSeq.encode("GBK")
        if BookDate:
            self.BookDate = BookDate.encode("GBK")
        if BookPsw:
            self.BookPsw = BookPsw.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class ReserveOpenAccount(Struct):
    _fields_ = [
        ("TradeCode", c_char_Array_7),
        ("BankID", c_char_Array_4),
        ("BankBranchID", c_char_Array_5),
        ("BrokerID", c_char_Array_11),
        ("BrokerBranchID", c_char_Array_31),
        ("TradeDate", c_char_Array_9),
        ("TradeTime", c_char_Array_9),
        ("BankSerial", c_char_Array_13),
        ("TradingDay", c_char_Array_9),
        ("PlateSerial", c_int),
        ("LastFragment", c_char),
        ("SessionID", c_int),
        ("CustomerName", c_char_Array_161),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char_Array_51),
        ("Gender", c_char),
        ("CountryCode", c_char_Array_21),
        ("CustType", c_char),
        ("Address", c_char_Array_101),
        ("ZipCode", c_char_Array_7),
        ("Telephone", c_char_Array_41),
        ("MobilePhone", c_char_Array_21),
        ("Fax", c_char_Array_41),
        ("EMail", c_char_Array_41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char_Array_41),
        ("BankPassWord", c_char_Array_41),
        ("InstallID", c_int),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char_Array_4),
        ("Digest", c_char_Array_36),
        ("BankAccType", c_char),
        ("BrokerIDByBank", c_char_Array_33),
        ("TID", c_int),
        ("ReserveOpenAccStas", c_char),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

    def __init__(self, TradeCode=None, BankID=None, BankBranchID=None, BrokerID=None, BrokerBranchID=None, TradeDate=None, TradeTime=None, BankSerial=None, TradingDay=None, PlateSerial=None, LastFragment=None, SessionID=None, CustomerName=None, IdCardType=None, IdentifiedCardNo=None, Gender=None, CountryCode=None, CustType=None, Address=None, ZipCode=None, Telephone=None, MobilePhone=None, Fax=None, EMail=None, MoneyAccountStatus=None, BankAccount=None, BankPassWord=None, InstallID=None, VerifyCertNoFlag=None, CurrencyID=None, Digest=None, BankAccType=None, BrokerIDByBank=None, TID=None, ReserveOpenAccStas=None, ErrorID=None, ErrorMsg=None):
        super().__init__()
        if TradeCode:
            self.TradeCode = TradeCode.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankBranchID:
            self.BankBranchID = BankBranchID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if PlateSerial:
            self.PlateSerial = PlateSerial
        if LastFragment:
            self.LastFragment = LastFragment.encode("GBK")
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType.encode("GBK")
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender.encode("GBK")
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType.encode("GBK")
        if Address:
            self.Address = Address.encode("GBK")
        if ZipCode:
            self.ZipCode = ZipCode.encode("GBK")
        if Telephone:
            self.Telephone = Telephone.encode("GBK")
        if MobilePhone:
            self.MobilePhone = MobilePhone.encode("GBK")
        if Fax:
            self.Fax = Fax.encode("GBK")
        if EMail:
            self.EMail = EMail.encode("GBK")
        if MoneyAccountStatus:
            self.MoneyAccountStatus = MoneyAccountStatus.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if TID:
            self.TID = TID
        if ReserveOpenAccStas:
            self.ReserveOpenAccStas = ReserveOpenAccStas.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class AccountProperty(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("BankID", c_char_Array_4),
        ("BankAccount", c_char_Array_41),
        ("OpenName", c_char_Array_101),
        ("OpenBank", c_char_Array_101),
        ("IsActive", c_int),
        ("AccountSourceType", c_char),
        ("OpenDate", c_char_Array_9),
        ("CancelDate", c_char_Array_9),
        ("OperatorID", c_char_Array_65),
        ("OperateDate", c_char_Array_9),
        ("OperateTime", c_char_Array_9),
        ("CurrencyID", c_char_Array_4),
    ]

    def __init__(self, BrokerID=None, AccountID=None, BankID=None, BankAccount=None, OpenName=None, OpenBank=None, IsActive=None, AccountSourceType=None, OpenDate=None, CancelDate=None, OperatorID=None, OperateDate=None, OperateTime=None, CurrencyID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if BankID:
            self.BankID = BankID.encode("GBK")
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if OpenName:
            self.OpenName = OpenName.encode("GBK")
        if OpenBank:
            self.OpenBank = OpenBank.encode("GBK")
        if IsActive:
            self.IsActive = IsActive
        if AccountSourceType:
            self.AccountSourceType = AccountSourceType.encode("GBK")
        if OpenDate:
            self.OpenDate = OpenDate.encode("GBK")
        if CancelDate:
            self.CancelDate = CancelDate.encode("GBK")
        if OperatorID:
            self.OperatorID = OperatorID.encode("GBK")
        if OperateDate:
            self.OperateDate = OperateDate.encode("GBK")
        if OperateTime:
            self.OperateTime = OperateTime.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")


class QryCurrDRIdentity(Struct):
    _fields_ = [
        ("DRIdentityID", c_int),
    ]

    def __init__(self, DRIdentityID=None):
        super().__init__()
        if DRIdentityID:
            self.DRIdentityID = DRIdentityID


class CurrDRIdentity(Struct):
    _fields_ = [
        ("DRIdentityID", c_int),
    ]

    def __init__(self, DRIdentityID=None):
        super().__init__()
        if DRIdentityID:
            self.DRIdentityID = DRIdentityID


class QrySecAgentCheckMode(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, InvestorID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class QrySecAgentTradeInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("BrokerSecAgentID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, BrokerSecAgentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerSecAgentID:
            self.BrokerSecAgentID = BrokerSecAgentID.encode("GBK")


class ReqUserAuthMethod(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, UserID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class RspUserAuthMethod(Struct):
    _fields_ = [
        ("UsableAuthMethod", c_int),
    ]

    def __init__(self, UsableAuthMethod=None):
        super().__init__()
        if UsableAuthMethod:
            self.UsableAuthMethod = UsableAuthMethod


class ReqGenUserCaptcha(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, UserID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class RspGenUserCaptcha(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("CaptchaInfoLen", c_int),
        ("CaptchaInfo", c_char_Array_2561),
    ]

    def __init__(self, BrokerID=None, UserID=None, CaptchaInfoLen=None, CaptchaInfo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if CaptchaInfoLen:
            self.CaptchaInfoLen = CaptchaInfoLen
        if CaptchaInfo:
            self.CaptchaInfo = CaptchaInfo.encode("GBK")


class ReqGenUserText(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, UserID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class RspGenUserText(Struct):
    _fields_ = [
        ("UserTextSeq", c_int),
    ]

    def __init__(self, UserTextSeq=None):
        super().__init__()
        if UserTextSeq:
            self.UserTextSeq = UserTextSeq


class ReqUserLoginWithCaptcha(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("Password", c_char_Array_41),
        ("UserProductInfo", c_char_Array_11),
        ("InterfaceProductInfo", c_char_Array_11),
        ("ProtocolInfo", c_char_Array_11),
        ("MacAddress", c_char_Array_21),
        ("reserve1", c_char_Array_16),
        ("LoginRemark", c_char_Array_36),
        ("Captcha", c_char_Array_41),
        ("ClientIPPort", c_int),
        ("ClientIPAddress", c_char_Array_33),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, UserID=None, Password=None, UserProductInfo=None, InterfaceProductInfo=None, ProtocolInfo=None, MacAddress=None, reserve1=None, LoginRemark=None, Captcha=None, ClientIPPort=None, ClientIPAddress=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if InterfaceProductInfo:
            self.InterfaceProductInfo = InterfaceProductInfo.encode("GBK")
        if ProtocolInfo:
            self.ProtocolInfo = ProtocolInfo.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if Captcha:
            self.Captcha = Captcha.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort
        if ClientIPAddress:
            self.ClientIPAddress = ClientIPAddress.encode("GBK")


class ReqUserLoginWithText(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("Password", c_char_Array_41),
        ("UserProductInfo", c_char_Array_11),
        ("InterfaceProductInfo", c_char_Array_11),
        ("ProtocolInfo", c_char_Array_11),
        ("MacAddress", c_char_Array_21),
        ("reserve1", c_char_Array_16),
        ("LoginRemark", c_char_Array_36),
        ("Text", c_char_Array_41),
        ("ClientIPPort", c_int),
        ("ClientIPAddress", c_char_Array_33),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, UserID=None, Password=None, UserProductInfo=None, InterfaceProductInfo=None, ProtocolInfo=None, MacAddress=None, reserve1=None, LoginRemark=None, Text=None, ClientIPPort=None, ClientIPAddress=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if InterfaceProductInfo:
            self.InterfaceProductInfo = InterfaceProductInfo.encode("GBK")
        if ProtocolInfo:
            self.ProtocolInfo = ProtocolInfo.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if Text:
            self.Text = Text.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort
        if ClientIPAddress:
            self.ClientIPAddress = ClientIPAddress.encode("GBK")


class ReqUserLoginWithOTP(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("Password", c_char_Array_41),
        ("UserProductInfo", c_char_Array_11),
        ("InterfaceProductInfo", c_char_Array_11),
        ("ProtocolInfo", c_char_Array_11),
        ("MacAddress", c_char_Array_21),
        ("reserve1", c_char_Array_16),
        ("LoginRemark", c_char_Array_36),
        ("OTPPassword", c_char_Array_41),
        ("ClientIPPort", c_int),
        ("ClientIPAddress", c_char_Array_33),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, UserID=None, Password=None, UserProductInfo=None, InterfaceProductInfo=None, ProtocolInfo=None, MacAddress=None, reserve1=None, LoginRemark=None, OTPPassword=None, ClientIPPort=None, ClientIPAddress=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if InterfaceProductInfo:
            self.InterfaceProductInfo = InterfaceProductInfo.encode("GBK")
        if ProtocolInfo:
            self.ProtocolInfo = ProtocolInfo.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if OTPPassword:
            self.OTPPassword = OTPPassword.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort
        if ClientIPAddress:
            self.ClientIPAddress = ClientIPAddress.encode("GBK")


class ReqApiHandshake(Struct):
    _fields_ = [
        ("CryptoKeyVersion", c_char_Array_31),
    ]

    def __init__(self, CryptoKeyVersion=None):
        super().__init__()
        if CryptoKeyVersion:
            self.CryptoKeyVersion = CryptoKeyVersion.encode("GBK")


class RspApiHandshake(Struct):
    _fields_ = [
        ("FrontHandshakeDataLen", c_int),
        ("FrontHandshakeData", c_char_Array_301),
        ("IsApiAuthEnabled", c_int),
    ]

    def __init__(self, FrontHandshakeDataLen=None, FrontHandshakeData=None, IsApiAuthEnabled=None):
        super().__init__()
        if FrontHandshakeDataLen:
            self.FrontHandshakeDataLen = FrontHandshakeDataLen
        if FrontHandshakeData:
            self.FrontHandshakeData = FrontHandshakeData.encode("GBK")
        if IsApiAuthEnabled:
            self.IsApiAuthEnabled = IsApiAuthEnabled


class ReqVerifyApiKey(Struct):
    _fields_ = [
        ("ApiHandshakeDataLen", c_int),
        ("ApiHandshakeData", c_char_Array_301),
    ]

    def __init__(self, ApiHandshakeDataLen=None, ApiHandshakeData=None):
        super().__init__()
        if ApiHandshakeDataLen:
            self.ApiHandshakeDataLen = ApiHandshakeDataLen
        if ApiHandshakeData:
            self.ApiHandshakeData = ApiHandshakeData.encode("GBK")


class DepartmentUser(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("InvestorRange", c_char),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, BrokerID=None, UserID=None, InvestorRange=None, InvestorID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class QueryFreq(Struct):
    _fields_ = [
        ("QueryFreq", c_int),
    ]

    def __init__(self, QueryFreq=None):
        super().__init__()
        if QueryFreq:
            self.QueryFreq = QueryFreq


class AuthForbiddenIP(Struct):
    _fields_ = [
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, IPAddress=None):
        super().__init__()
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryAuthForbiddenIP(Struct):
    _fields_ = [
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, IPAddress=None):
        super().__init__()
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class SyncDelaySwapFrozen(Struct):
    _fields_ = [
        ("DelaySwapSeqNo", c_char_Array_15),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("FromCurrencyID", c_char_Array_4),
        ("FromRemainSwap", c_double),
        ("IsManualSwap", c_int),
    ]

    def __init__(self, DelaySwapSeqNo=None, BrokerID=None, InvestorID=None, FromCurrencyID=None, FromRemainSwap=None, IsManualSwap=None):
        super().__init__()
        if DelaySwapSeqNo:
            self.DelaySwapSeqNo = DelaySwapSeqNo.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if FromCurrencyID:
            self.FromCurrencyID = FromCurrencyID.encode("GBK")
        if FromRemainSwap:
            self.FromRemainSwap = FromRemainSwap
        if IsManualSwap:
            self.IsManualSwap = IsManualSwap


class UserSystemInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("ClientSystemInfoLen", c_int),
        ("ClientSystemInfo", c_char_Array_273),
        ("reserve1", c_char_Array_16),
        ("ClientIPPort", c_int),
        ("ClientLoginTime", c_char_Array_9),
        ("ClientAppID", c_char_Array_33),
        ("ClientPublicIP", c_char_Array_33),
        ("ClientLoginRemark", c_char_Array_151),
    ]

    def __init__(self, BrokerID=None, UserID=None, ClientSystemInfoLen=None, ClientSystemInfo=None, reserve1=None, ClientIPPort=None, ClientLoginTime=None, ClientAppID=None, ClientPublicIP=None, ClientLoginRemark=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ClientSystemInfoLen:
            self.ClientSystemInfoLen = ClientSystemInfoLen
        if ClientSystemInfo:
            self.ClientSystemInfo = ClientSystemInfo.encode("GBK")
        if reserve1:
            self.reserve1 = reserve1.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort
        if ClientLoginTime:
            self.ClientLoginTime = ClientLoginTime.encode("GBK")
        if ClientAppID:
            self.ClientAppID = ClientAppID.encode("GBK")
        if ClientPublicIP:
            self.ClientPublicIP = ClientPublicIP.encode("GBK")
        if ClientLoginRemark:
            self.ClientLoginRemark = ClientLoginRemark.encode("GBK")


class AuthUserID(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AppID", c_char_Array_33),
        ("UserID", c_char_Array_16),
        ("AuthType", c_char),
    ]

    def __init__(self, BrokerID=None, AppID=None, UserID=None, AuthType=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AppID:
            self.AppID = AppID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if AuthType:
            self.AuthType = AuthType.encode("GBK")


class AuthIP(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AppID", c_char_Array_33),
        ("IPAddress", c_char_Array_33),
    ]

    def __init__(self, BrokerID=None, AppID=None, IPAddress=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AppID:
            self.AppID = AppID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryClassifiedInstrument(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_81),
        ("ExchangeID", c_char_Array_9),
        ("ExchangeInstID", c_char_Array_81),
        ("ProductID", c_char_Array_81),
        ("TradingType", c_char),
        ("ClassType", c_char),
    ]

    def __init__(self, InstrumentID=None, ExchangeID=None, ExchangeInstID=None, ProductID=None, TradingType=None, ClassType=None):
        super().__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if TradingType:
            self.TradingType = TradingType.encode("GBK")
        if ClassType:
            self.ClassType = ClassType.encode("GBK")


class QryCombPromotionParam(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, InstrumentID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class CombPromotionParam(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
        ("CombHedgeFlag", c_char_Array_5),
        ("Xparameter", c_double),
    ]

    def __init__(self, ExchangeID=None, InstrumentID=None, CombHedgeFlag=None, Xparameter=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if Xparameter:
            self.Xparameter = Xparameter


class ReqUserLoginSC(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("Password", c_char_Array_41),
        ("UserProductInfo", c_char_Array_11),
        ("InterfaceProductInfo", c_char_Array_11),
        ("ProtocolInfo", c_char_Array_11),
        ("MacAddress", c_char_Array_21),
        ("OneTimePassword", c_char_Array_41),
        ("ClientIPAddress", c_char_Array_33),
        ("LoginRemark", c_char_Array_36),
        ("ClientIPPort", c_int),
        ("AuthCode", c_char_Array_17),
        ("AppID", c_char_Array_33),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, UserID=None, Password=None, UserProductInfo=None, InterfaceProductInfo=None, ProtocolInfo=None, MacAddress=None, OneTimePassword=None, ClientIPAddress=None, LoginRemark=None, ClientIPPort=None, AuthCode=None, AppID=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Password:
            self.Password = Password.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if InterfaceProductInfo:
            self.InterfaceProductInfo = InterfaceProductInfo.encode("GBK")
        if ProtocolInfo:
            self.ProtocolInfo = ProtocolInfo.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if OneTimePassword:
            self.OneTimePassword = OneTimePassword.encode("GBK")
        if ClientIPAddress:
            self.ClientIPAddress = ClientIPAddress.encode("GBK")
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort
        if AuthCode:
            self.AuthCode = AuthCode.encode("GBK")
        if AppID:
            self.AppID = AppID.encode("GBK")


class QryRiskSettleInvstPosition(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_81),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, InstrumentID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryRiskSettleProductStatus(Struct):
    _fields_ = [
        ("ProductID", c_char_Array_81),
    ]

    def __init__(self, ProductID=None):
        super().__init__()
        if ProductID:
            self.ProductID = ProductID.encode("GBK")


class RiskSettleInvstPosition(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_81),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("PosiDirection", c_char),
        ("HedgeFlag", c_char),
        ("PositionDate", c_char),
        ("YdPosition", c_int),
        ("Position", c_int),
        ("LongFrozen", c_int),
        ("ShortFrozen", c_int),
        ("LongFrozenAmount", c_double),
        ("ShortFrozenAmount", c_double),
        ("OpenVolume", c_int),
        ("CloseVolume", c_int),
        ("OpenAmount", c_double),
        ("CloseAmount", c_double),
        ("PositionCost", c_double),
        ("PreMargin", c_double),
        ("UseMargin", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("PreSettlementPrice", c_double),
        ("SettlementPrice", c_double),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("OpenCost", c_double),
        ("ExchangeMargin", c_double),
        ("CombPosition", c_int),
        ("CombLongFrozen", c_int),
        ("CombShortFrozen", c_int),
        ("CloseProfitByDate", c_double),
        ("CloseProfitByTrade", c_double),
        ("TodayPosition", c_int),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("StrikeFrozen", c_int),
        ("StrikeFrozenAmount", c_double),
        ("AbandonFrozen", c_int),
        ("ExchangeID", c_char_Array_9),
        ("YdStrikeFrozen", c_int),
        ("InvestUnitID", c_char_Array_17),
        ("PositionCostOffset", c_double),
        ("TasPosition", c_int),
        ("TasPositionCost", c_double),
    ]

    def __init__(self, InstrumentID=None, BrokerID=None, InvestorID=None, PosiDirection=None, HedgeFlag=None, PositionDate=None, YdPosition=None, Position=None, LongFrozen=None, ShortFrozen=None, LongFrozenAmount=None, ShortFrozenAmount=None, OpenVolume=None, CloseVolume=None, OpenAmount=None, CloseAmount=None, PositionCost=None, PreMargin=None, UseMargin=None, FrozenMargin=None, FrozenCash=None, FrozenCommission=None, CashIn=None, Commission=None, CloseProfit=None, PositionProfit=None, PreSettlementPrice=None, SettlementPrice=None, TradingDay=None, SettlementID=None, OpenCost=None, ExchangeMargin=None, CombPosition=None, CombLongFrozen=None, CombShortFrozen=None, CloseProfitByDate=None, CloseProfitByTrade=None, TodayPosition=None, MarginRateByMoney=None, MarginRateByVolume=None, StrikeFrozen=None, StrikeFrozenAmount=None, AbandonFrozen=None, ExchangeID=None, YdStrikeFrozen=None, InvestUnitID=None, PositionCostOffset=None, TasPosition=None, TasPositionCost=None):
        super().__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if PosiDirection:
            self.PosiDirection = PosiDirection.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if PositionDate:
            self.PositionDate = PositionDate.encode("GBK")
        if YdPosition:
            self.YdPosition = YdPosition
        if Position:
            self.Position = Position
        if LongFrozen:
            self.LongFrozen = LongFrozen
        if ShortFrozen:
            self.ShortFrozen = ShortFrozen
        if LongFrozenAmount:
            self.LongFrozenAmount = LongFrozenAmount
        if ShortFrozenAmount:
            self.ShortFrozenAmount = ShortFrozenAmount
        if OpenVolume:
            self.OpenVolume = OpenVolume
        if CloseVolume:
            self.CloseVolume = CloseVolume
        if OpenAmount:
            self.OpenAmount = OpenAmount
        if CloseAmount:
            self.CloseAmount = CloseAmount
        if PositionCost:
            self.PositionCost = PositionCost
        if PreMargin:
            self.PreMargin = PreMargin
        if UseMargin:
            self.UseMargin = UseMargin
        if FrozenMargin:
            self.FrozenMargin = FrozenMargin
        if FrozenCash:
            self.FrozenCash = FrozenCash
        if FrozenCommission:
            self.FrozenCommission = FrozenCommission
        if CashIn:
            self.CashIn = CashIn
        if Commission:
            self.Commission = Commission
        if CloseProfit:
            self.CloseProfit = CloseProfit
        if PositionProfit:
            self.PositionProfit = PositionProfit
        if PreSettlementPrice:
            self.PreSettlementPrice = PreSettlementPrice
        if SettlementPrice:
            self.SettlementPrice = SettlementPrice
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OpenCost:
            self.OpenCost = OpenCost
        if ExchangeMargin:
            self.ExchangeMargin = ExchangeMargin
        if CombPosition:
            self.CombPosition = CombPosition
        if CombLongFrozen:
            self.CombLongFrozen = CombLongFrozen
        if CombShortFrozen:
            self.CombShortFrozen = CombShortFrozen
        if CloseProfitByDate:
            self.CloseProfitByDate = CloseProfitByDate
        if CloseProfitByTrade:
            self.CloseProfitByTrade = CloseProfitByTrade
        if TodayPosition:
            self.TodayPosition = TodayPosition
        if MarginRateByMoney:
            self.MarginRateByMoney = MarginRateByMoney
        if MarginRateByVolume:
            self.MarginRateByVolume = MarginRateByVolume
        if StrikeFrozen:
            self.StrikeFrozen = StrikeFrozen
        if StrikeFrozenAmount:
            self.StrikeFrozenAmount = StrikeFrozenAmount
        if AbandonFrozen:
            self.AbandonFrozen = AbandonFrozen
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if YdStrikeFrozen:
            self.YdStrikeFrozen = YdStrikeFrozen
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if PositionCostOffset:
            self.PositionCostOffset = PositionCostOffset
        if TasPosition:
            self.TasPosition = TasPosition
        if TasPositionCost:
            self.TasPositionCost = TasPositionCost


class RiskSettleProductStatus(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ProductID", c_char_Array_81),
        ("ProductStatus", c_char),
    ]

    def __init__(self, ExchangeID=None, ProductID=None, ProductStatus=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ProductStatus:
            self.ProductStatus = ProductStatus.encode("GBK")


class SyncDeltaInfo(Struct):
    _fields_ = [
        ("SyncDeltaSequenceNo", c_int),
        ("SyncDeltaStatus", c_char),
        ("SyncDescription", c_char_Array_257),
        ("IsOnlyTrdDelta", c_int),
    ]

    def __init__(self, SyncDeltaSequenceNo=None, SyncDeltaStatus=None, SyncDescription=None, IsOnlyTrdDelta=None):
        super().__init__()
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo
        if SyncDeltaStatus:
            self.SyncDeltaStatus = SyncDeltaStatus.encode("GBK")
        if SyncDescription:
            self.SyncDescription = SyncDescription.encode("GBK")
        if IsOnlyTrdDelta:
            self.IsOnlyTrdDelta = IsOnlyTrdDelta


class SyncDeltaProductStatus(Struct):
    _fields_ = [
        ("SyncDeltaSequenceNo", c_int),
        ("ExchangeID", c_char_Array_9),
        ("ProductID", c_char_Array_81),
        ("ProductStatus", c_char),
    ]

    def __init__(self, SyncDeltaSequenceNo=None, ExchangeID=None, ProductID=None, ProductStatus=None):
        super().__init__()
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ProductStatus:
            self.ProductStatus = ProductStatus.encode("GBK")


class SyncDeltaInvstPosDtl(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_81),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("OpenDate", c_char_Array_9),
        ("TradeID", c_char_Array_21),
        ("Volume", c_int),
        ("OpenPrice", c_double),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("TradeType", c_char),
        ("CombInstrumentID", c_char_Array_81),
        ("ExchangeID", c_char_Array_9),
        ("CloseProfitByDate", c_double),
        ("CloseProfitByTrade", c_double),
        ("PositionProfitByDate", c_double),
        ("PositionProfitByTrade", c_double),
        ("Margin", c_double),
        ("ExchMargin", c_double),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("LastSettlementPrice", c_double),
        ("SettlementPrice", c_double),
        ("CloseVolume", c_int),
        ("CloseAmount", c_double),
        ("TimeFirstVolume", c_int),
        ("SpecPosiType", c_char),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, InstrumentID=None, BrokerID=None, InvestorID=None, HedgeFlag=None, Direction=None, OpenDate=None, TradeID=None, Volume=None, OpenPrice=None, TradingDay=None, SettlementID=None, TradeType=None, CombInstrumentID=None, ExchangeID=None, CloseProfitByDate=None, CloseProfitByTrade=None, PositionProfitByDate=None, PositionProfitByTrade=None, Margin=None, ExchMargin=None, MarginRateByMoney=None, MarginRateByVolume=None, LastSettlementPrice=None, SettlementPrice=None, CloseVolume=None, CloseAmount=None, TimeFirstVolume=None, SpecPosiType=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if OpenDate:
            self.OpenDate = OpenDate.encode("GBK")
        if TradeID:
            self.TradeID = TradeID.encode("GBK")
        if Volume:
            self.Volume = Volume
        if OpenPrice:
            self.OpenPrice = OpenPrice
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if TradeType:
            self.TradeType = TradeType.encode("GBK")
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if CloseProfitByDate:
            self.CloseProfitByDate = CloseProfitByDate
        if CloseProfitByTrade:
            self.CloseProfitByTrade = CloseProfitByTrade
        if PositionProfitByDate:
            self.PositionProfitByDate = PositionProfitByDate
        if PositionProfitByTrade:
            self.PositionProfitByTrade = PositionProfitByTrade
        if Margin:
            self.Margin = Margin
        if ExchMargin:
            self.ExchMargin = ExchMargin
        if MarginRateByMoney:
            self.MarginRateByMoney = MarginRateByMoney
        if MarginRateByVolume:
            self.MarginRateByVolume = MarginRateByVolume
        if LastSettlementPrice:
            self.LastSettlementPrice = LastSettlementPrice
        if SettlementPrice:
            self.SettlementPrice = SettlementPrice
        if CloseVolume:
            self.CloseVolume = CloseVolume
        if CloseAmount:
            self.CloseAmount = CloseAmount
        if TimeFirstVolume:
            self.TimeFirstVolume = TimeFirstVolume
        if SpecPosiType:
            self.SpecPosiType = SpecPosiType.encode("GBK")
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaInvstPosCombDtl(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("OpenDate", c_char_Array_9),
        ("ExchangeID", c_char_Array_9),
        ("SettlementID", c_int),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ComTradeID", c_char_Array_21),
        ("TradeID", c_char_Array_21),
        ("InstrumentID", c_char_Array_81),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("TotalAmt", c_int),
        ("Margin", c_double),
        ("ExchMargin", c_double),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("LegID", c_int),
        ("LegMultiple", c_int),
        ("TradeGroupID", c_int),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, TradingDay=None, OpenDate=None, ExchangeID=None, SettlementID=None, BrokerID=None, InvestorID=None, ComTradeID=None, TradeID=None, InstrumentID=None, HedgeFlag=None, Direction=None, TotalAmt=None, Margin=None, ExchMargin=None, MarginRateByMoney=None, MarginRateByVolume=None, LegID=None, LegMultiple=None, TradeGroupID=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if OpenDate:
            self.OpenDate = OpenDate.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ComTradeID:
            self.ComTradeID = ComTradeID.encode("GBK")
        if TradeID:
            self.TradeID = TradeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if TotalAmt:
            self.TotalAmt = TotalAmt
        if Margin:
            self.Margin = Margin
        if ExchMargin:
            self.ExchMargin = ExchMargin
        if MarginRateByMoney:
            self.MarginRateByMoney = MarginRateByMoney
        if MarginRateByVolume:
            self.MarginRateByVolume = MarginRateByVolume
        if LegID:
            self.LegID = LegID
        if LegMultiple:
            self.LegMultiple = LegMultiple
        if TradeGroupID:
            self.TradeGroupID = TradeGroupID
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaTradingAccount(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("PreMortgage", c_double),
        ("PreCredit", c_double),
        ("PreDeposit", c_double),
        ("PreBalance", c_double),
        ("PreMargin", c_double),
        ("InterestBase", c_double),
        ("Interest", c_double),
        ("Deposit", c_double),
        ("Withdraw", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CurrMargin", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("Balance", c_double),
        ("Available", c_double),
        ("WithdrawQuota", c_double),
        ("Reserve", c_double),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("Credit", c_double),
        ("Mortgage", c_double),
        ("ExchangeMargin", c_double),
        ("DeliveryMargin", c_double),
        ("ExchangeDeliveryMargin", c_double),
        ("ReserveBalance", c_double),
        ("CurrencyID", c_char_Array_4),
        ("PreFundMortgageIn", c_double),
        ("PreFundMortgageOut", c_double),
        ("FundMortgageIn", c_double),
        ("FundMortgageOut", c_double),
        ("FundMortgageAvailable", c_double),
        ("MortgageableFund", c_double),
        ("SpecProductMargin", c_double),
        ("SpecProductFrozenMargin", c_double),
        ("SpecProductCommission", c_double),
        ("SpecProductFrozenCommission", c_double),
        ("SpecProductPositionProfit", c_double),
        ("SpecProductCloseProfit", c_double),
        ("SpecProductPositionProfitByAlg", c_double),
        ("SpecProductExchangeMargin", c_double),
        ("FrozenSwap", c_double),
        ("RemainSwap", c_double),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, BrokerID=None, AccountID=None, PreMortgage=None, PreCredit=None, PreDeposit=None, PreBalance=None, PreMargin=None, InterestBase=None, Interest=None, Deposit=None, Withdraw=None, FrozenMargin=None, FrozenCash=None, FrozenCommission=None, CurrMargin=None, CashIn=None, Commission=None, CloseProfit=None, PositionProfit=None, Balance=None, Available=None, WithdrawQuota=None, Reserve=None, TradingDay=None, SettlementID=None, Credit=None, Mortgage=None, ExchangeMargin=None, DeliveryMargin=None, ExchangeDeliveryMargin=None, ReserveBalance=None, CurrencyID=None, PreFundMortgageIn=None, PreFundMortgageOut=None, FundMortgageIn=None, FundMortgageOut=None, FundMortgageAvailable=None, MortgageableFund=None, SpecProductMargin=None, SpecProductFrozenMargin=None, SpecProductCommission=None, SpecProductFrozenCommission=None, SpecProductPositionProfit=None, SpecProductCloseProfit=None, SpecProductPositionProfitByAlg=None, SpecProductExchangeMargin=None, FrozenSwap=None, RemainSwap=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if PreMortgage:
            self.PreMortgage = PreMortgage
        if PreCredit:
            self.PreCredit = PreCredit
        if PreDeposit:
            self.PreDeposit = PreDeposit
        if PreBalance:
            self.PreBalance = PreBalance
        if PreMargin:
            self.PreMargin = PreMargin
        if InterestBase:
            self.InterestBase = InterestBase
        if Interest:
            self.Interest = Interest
        if Deposit:
            self.Deposit = Deposit
        if Withdraw:
            self.Withdraw = Withdraw
        if FrozenMargin:
            self.FrozenMargin = FrozenMargin
        if FrozenCash:
            self.FrozenCash = FrozenCash
        if FrozenCommission:
            self.FrozenCommission = FrozenCommission
        if CurrMargin:
            self.CurrMargin = CurrMargin
        if CashIn:
            self.CashIn = CashIn
        if Commission:
            self.Commission = Commission
        if CloseProfit:
            self.CloseProfit = CloseProfit
        if PositionProfit:
            self.PositionProfit = PositionProfit
        if Balance:
            self.Balance = Balance
        if Available:
            self.Available = Available
        if WithdrawQuota:
            self.WithdrawQuota = WithdrawQuota
        if Reserve:
            self.Reserve = Reserve
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if Credit:
            self.Credit = Credit
        if Mortgage:
            self.Mortgage = Mortgage
        if ExchangeMargin:
            self.ExchangeMargin = ExchangeMargin
        if DeliveryMargin:
            self.DeliveryMargin = DeliveryMargin
        if ExchangeDeliveryMargin:
            self.ExchangeDeliveryMargin = ExchangeDeliveryMargin
        if ReserveBalance:
            self.ReserveBalance = ReserveBalance
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if PreFundMortgageIn:
            self.PreFundMortgageIn = PreFundMortgageIn
        if PreFundMortgageOut:
            self.PreFundMortgageOut = PreFundMortgageOut
        if FundMortgageIn:
            self.FundMortgageIn = FundMortgageIn
        if FundMortgageOut:
            self.FundMortgageOut = FundMortgageOut
        if FundMortgageAvailable:
            self.FundMortgageAvailable = FundMortgageAvailable
        if MortgageableFund:
            self.MortgageableFund = MortgageableFund
        if SpecProductMargin:
            self.SpecProductMargin = SpecProductMargin
        if SpecProductFrozenMargin:
            self.SpecProductFrozenMargin = SpecProductFrozenMargin
        if SpecProductCommission:
            self.SpecProductCommission = SpecProductCommission
        if SpecProductFrozenCommission:
            self.SpecProductFrozenCommission = SpecProductFrozenCommission
        if SpecProductPositionProfit:
            self.SpecProductPositionProfit = SpecProductPositionProfit
        if SpecProductCloseProfit:
            self.SpecProductCloseProfit = SpecProductCloseProfit
        if SpecProductPositionProfitByAlg:
            self.SpecProductPositionProfitByAlg = SpecProductPositionProfitByAlg
        if SpecProductExchangeMargin:
            self.SpecProductExchangeMargin = SpecProductExchangeMargin
        if FrozenSwap:
            self.FrozenSwap = FrozenSwap
        if RemainSwap:
            self.RemainSwap = RemainSwap
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaInitInvstMargin(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("LastRiskTotalInvstMargin", c_double),
        ("LastRiskTotalExchMargin", c_double),
        ("ThisSyncInvstMargin", c_double),
        ("ThisSyncExchMargin", c_double),
        ("RemainRiskInvstMargin", c_double),
        ("RemainRiskExchMargin", c_double),
        ("LastRiskSpecTotalInvstMargin", c_double),
        ("LastRiskSpecTotalExchMargin", c_double),
        ("ThisSyncSpecInvstMargin", c_double),
        ("ThisSyncSpecExchMargin", c_double),
        ("RemainRiskSpecInvstMargin", c_double),
        ("RemainRiskSpecExchMargin", c_double),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, LastRiskTotalInvstMargin=None, LastRiskTotalExchMargin=None, ThisSyncInvstMargin=None, ThisSyncExchMargin=None, RemainRiskInvstMargin=None, RemainRiskExchMargin=None, LastRiskSpecTotalInvstMargin=None, LastRiskSpecTotalExchMargin=None, ThisSyncSpecInvstMargin=None, ThisSyncSpecExchMargin=None, RemainRiskSpecInvstMargin=None, RemainRiskSpecExchMargin=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if LastRiskTotalInvstMargin:
            self.LastRiskTotalInvstMargin = LastRiskTotalInvstMargin
        if LastRiskTotalExchMargin:
            self.LastRiskTotalExchMargin = LastRiskTotalExchMargin
        if ThisSyncInvstMargin:
            self.ThisSyncInvstMargin = ThisSyncInvstMargin
        if ThisSyncExchMargin:
            self.ThisSyncExchMargin = ThisSyncExchMargin
        if RemainRiskInvstMargin:
            self.RemainRiskInvstMargin = RemainRiskInvstMargin
        if RemainRiskExchMargin:
            self.RemainRiskExchMargin = RemainRiskExchMargin
        if LastRiskSpecTotalInvstMargin:
            self.LastRiskSpecTotalInvstMargin = LastRiskSpecTotalInvstMargin
        if LastRiskSpecTotalExchMargin:
            self.LastRiskSpecTotalExchMargin = LastRiskSpecTotalExchMargin
        if ThisSyncSpecInvstMargin:
            self.ThisSyncSpecInvstMargin = ThisSyncSpecInvstMargin
        if ThisSyncSpecExchMargin:
            self.ThisSyncSpecExchMargin = ThisSyncSpecExchMargin
        if RemainRiskSpecInvstMargin:
            self.RemainRiskSpecInvstMargin = RemainRiskSpecInvstMargin
        if RemainRiskSpecExchMargin:
            self.RemainRiskSpecExchMargin = RemainRiskSpecExchMargin
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaDceCombInstrument(Struct):
    _fields_ = [
        ("CombInstrumentID", c_char_Array_81),
        ("ExchangeID", c_char_Array_9),
        ("ExchangeInstID", c_char_Array_81),
        ("TradeGroupID", c_int),
        ("CombHedgeFlag", c_char),
        ("CombinationType", c_char),
        ("Direction", c_char),
        ("ProductID", c_char_Array_81),
        ("Xparameter", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, CombInstrumentID=None, ExchangeID=None, ExchangeInstID=None, TradeGroupID=None, CombHedgeFlag=None, CombinationType=None, Direction=None, ProductID=None, Xparameter=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TradeGroupID:
            self.TradeGroupID = TradeGroupID
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if CombinationType:
            self.CombinationType = CombinationType.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if Xparameter:
            self.Xparameter = Xparameter
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaInvstMarginRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_81),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, InstrumentID=None, InvestorRange=None, BrokerID=None, InvestorID=None, HedgeFlag=None, LongMarginRatioByMoney=None, LongMarginRatioByVolume=None, ShortMarginRatioByMoney=None, ShortMarginRatioByVolume=None, IsRelative=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume
        if IsRelative:
            self.IsRelative = IsRelative
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaExchMarginRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_81),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, BrokerID=None, InstrumentID=None, HedgeFlag=None, LongMarginRatioByMoney=None, LongMarginRatioByVolume=None, ShortMarginRatioByMoney=None, ShortMarginRatioByVolume=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaOptExchMargin(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_81),
        ("SShortMarginRatioByMoney", c_double),
        ("SShortMarginRatioByVolume", c_double),
        ("HShortMarginRatioByMoney", c_double),
        ("HShortMarginRatioByVolume", c_double),
        ("AShortMarginRatioByMoney", c_double),
        ("AShortMarginRatioByVolume", c_double),
        ("MShortMarginRatioByMoney", c_double),
        ("MShortMarginRatioByVolume", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, BrokerID=None, InstrumentID=None, SShortMarginRatioByMoney=None, SShortMarginRatioByVolume=None, HShortMarginRatioByMoney=None, HShortMarginRatioByVolume=None, AShortMarginRatioByMoney=None, AShortMarginRatioByVolume=None, MShortMarginRatioByMoney=None, MShortMarginRatioByVolume=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if SShortMarginRatioByMoney:
            self.SShortMarginRatioByMoney = SShortMarginRatioByMoney
        if SShortMarginRatioByVolume:
            self.SShortMarginRatioByVolume = SShortMarginRatioByVolume
        if HShortMarginRatioByMoney:
            self.HShortMarginRatioByMoney = HShortMarginRatioByMoney
        if HShortMarginRatioByVolume:
            self.HShortMarginRatioByVolume = HShortMarginRatioByVolume
        if AShortMarginRatioByMoney:
            self.AShortMarginRatioByMoney = AShortMarginRatioByMoney
        if AShortMarginRatioByVolume:
            self.AShortMarginRatioByVolume = AShortMarginRatioByVolume
        if MShortMarginRatioByMoney:
            self.MShortMarginRatioByMoney = MShortMarginRatioByMoney
        if MShortMarginRatioByVolume:
            self.MShortMarginRatioByVolume = MShortMarginRatioByVolume
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaOptInvstMargin(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_81),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("SShortMarginRatioByMoney", c_double),
        ("SShortMarginRatioByVolume", c_double),
        ("HShortMarginRatioByMoney", c_double),
        ("HShortMarginRatioByVolume", c_double),
        ("AShortMarginRatioByMoney", c_double),
        ("AShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int),
        ("MShortMarginRatioByMoney", c_double),
        ("MShortMarginRatioByVolume", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, InstrumentID=None, InvestorRange=None, BrokerID=None, InvestorID=None, SShortMarginRatioByMoney=None, SShortMarginRatioByVolume=None, HShortMarginRatioByMoney=None, HShortMarginRatioByVolume=None, AShortMarginRatioByMoney=None, AShortMarginRatioByVolume=None, IsRelative=None, MShortMarginRatioByMoney=None, MShortMarginRatioByVolume=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if SShortMarginRatioByMoney:
            self.SShortMarginRatioByMoney = SShortMarginRatioByMoney
        if SShortMarginRatioByVolume:
            self.SShortMarginRatioByVolume = SShortMarginRatioByVolume
        if HShortMarginRatioByMoney:
            self.HShortMarginRatioByMoney = HShortMarginRatioByMoney
        if HShortMarginRatioByVolume:
            self.HShortMarginRatioByVolume = HShortMarginRatioByVolume
        if AShortMarginRatioByMoney:
            self.AShortMarginRatioByMoney = AShortMarginRatioByMoney
        if AShortMarginRatioByVolume:
            self.AShortMarginRatioByVolume = AShortMarginRatioByVolume
        if IsRelative:
            self.IsRelative = IsRelative
        if MShortMarginRatioByMoney:
            self.MShortMarginRatioByMoney = MShortMarginRatioByMoney
        if MShortMarginRatioByVolume:
            self.MShortMarginRatioByVolume = MShortMarginRatioByVolume
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaInvstMarginRateUL(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_81),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, InstrumentID=None, InvestorRange=None, BrokerID=None, InvestorID=None, HedgeFlag=None, LongMarginRatioByMoney=None, LongMarginRatioByVolume=None, ShortMarginRatioByMoney=None, ShortMarginRatioByVolume=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaOptInvstCommRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_81),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("StrikeRatioByMoney", c_double),
        ("StrikeRatioByVolume", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, InstrumentID=None, InvestorRange=None, BrokerID=None, InvestorID=None, OpenRatioByMoney=None, OpenRatioByVolume=None, CloseRatioByMoney=None, CloseRatioByVolume=None, CloseTodayRatioByMoney=None, CloseTodayRatioByVolume=None, StrikeRatioByMoney=None, StrikeRatioByVolume=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OpenRatioByMoney:
            self.OpenRatioByMoney = OpenRatioByMoney
        if OpenRatioByVolume:
            self.OpenRatioByVolume = OpenRatioByVolume
        if CloseRatioByMoney:
            self.CloseRatioByMoney = CloseRatioByMoney
        if CloseRatioByVolume:
            self.CloseRatioByVolume = CloseRatioByVolume
        if CloseTodayRatioByMoney:
            self.CloseTodayRatioByMoney = CloseTodayRatioByMoney
        if CloseTodayRatioByVolume:
            self.CloseTodayRatioByVolume = CloseTodayRatioByVolume
        if StrikeRatioByMoney:
            self.StrikeRatioByMoney = StrikeRatioByMoney
        if StrikeRatioByVolume:
            self.StrikeRatioByVolume = StrikeRatioByVolume
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaInvstCommRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_81),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, InstrumentID=None, InvestorRange=None, BrokerID=None, InvestorID=None, OpenRatioByMoney=None, OpenRatioByVolume=None, CloseRatioByMoney=None, CloseRatioByVolume=None, CloseTodayRatioByMoney=None, CloseTodayRatioByVolume=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if OpenRatioByMoney:
            self.OpenRatioByMoney = OpenRatioByMoney
        if OpenRatioByVolume:
            self.OpenRatioByVolume = OpenRatioByVolume
        if CloseRatioByMoney:
            self.CloseRatioByMoney = CloseRatioByMoney
        if CloseRatioByVolume:
            self.CloseRatioByVolume = CloseRatioByVolume
        if CloseTodayRatioByMoney:
            self.CloseTodayRatioByMoney = CloseTodayRatioByMoney
        if CloseTodayRatioByVolume:
            self.CloseTodayRatioByVolume = CloseTodayRatioByVolume
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaProductExchRate(Struct):
    _fields_ = [
        ("ProductID", c_char_Array_81),
        ("QuoteCurrencyID", c_char_Array_4),
        ("ExchangeRate", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, ProductID=None, QuoteCurrencyID=None, ExchangeRate=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if QuoteCurrencyID:
            self.QuoteCurrencyID = QuoteCurrencyID.encode("GBK")
        if ExchangeRate:
            self.ExchangeRate = ExchangeRate
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaDepthMarketData(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
        ("ExchangeID", c_char_Array_9),
        ("ExchangeInstID", c_char_Array_81),
        ("LastPrice", c_double),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("Volume", c_int),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
        ("ClosePrice", c_double),
        ("SettlementPrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("PreDelta", c_double),
        ("CurrDelta", c_double),
        ("UpdateTime", c_char_Array_9),
        ("UpdateMillisec", c_int),
        ("BidPrice1", c_double),
        ("BidVolume1", c_int),
        ("AskPrice1", c_double),
        ("AskVolume1", c_int),
        ("BidPrice2", c_double),
        ("BidVolume2", c_int),
        ("AskPrice2", c_double),
        ("AskVolume2", c_int),
        ("BidPrice3", c_double),
        ("BidVolume3", c_int),
        ("AskPrice3", c_double),
        ("AskVolume3", c_int),
        ("BidPrice4", c_double),
        ("BidVolume4", c_int),
        ("AskPrice4", c_double),
        ("AskVolume4", c_int),
        ("BidPrice5", c_double),
        ("BidVolume5", c_int),
        ("AskPrice5", c_double),
        ("AskVolume5", c_int),
        ("AveragePrice", c_double),
        ("ActionDay", c_char_Array_9),
        ("BandingUpperPrice", c_double),
        ("BandingLowerPrice", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, TradingDay=None, InstrumentID=None, ExchangeID=None, ExchangeInstID=None, LastPrice=None, PreSettlementPrice=None, PreClosePrice=None, PreOpenInterest=None, OpenPrice=None, HighestPrice=None, LowestPrice=None, Volume=None, Turnover=None, OpenInterest=None, ClosePrice=None, SettlementPrice=None, UpperLimitPrice=None, LowerLimitPrice=None, PreDelta=None, CurrDelta=None, UpdateTime=None, UpdateMillisec=None, BidPrice1=None, BidVolume1=None, AskPrice1=None, AskVolume1=None, BidPrice2=None, BidVolume2=None, AskPrice2=None, AskVolume2=None, BidPrice3=None, BidVolume3=None, AskPrice3=None, AskVolume3=None, BidPrice4=None, BidVolume4=None, AskPrice4=None, AskVolume4=None, BidPrice5=None, BidVolume5=None, AskPrice5=None, AskVolume5=None, AveragePrice=None, ActionDay=None, BandingUpperPrice=None, BandingLowerPrice=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if LastPrice:
            self.LastPrice = LastPrice
        if PreSettlementPrice:
            self.PreSettlementPrice = PreSettlementPrice
        if PreClosePrice:
            self.PreClosePrice = PreClosePrice
        if PreOpenInterest:
            self.PreOpenInterest = PreOpenInterest
        if OpenPrice:
            self.OpenPrice = OpenPrice
        if HighestPrice:
            self.HighestPrice = HighestPrice
        if LowestPrice:
            self.LowestPrice = LowestPrice
        if Volume:
            self.Volume = Volume
        if Turnover:
            self.Turnover = Turnover
        if OpenInterest:
            self.OpenInterest = OpenInterest
        if ClosePrice:
            self.ClosePrice = ClosePrice
        if SettlementPrice:
            self.SettlementPrice = SettlementPrice
        if UpperLimitPrice:
            self.UpperLimitPrice = UpperLimitPrice
        if LowerLimitPrice:
            self.LowerLimitPrice = LowerLimitPrice
        if PreDelta:
            self.PreDelta = PreDelta
        if CurrDelta:
            self.CurrDelta = CurrDelta
        if UpdateTime:
            self.UpdateTime = UpdateTime.encode("GBK")
        if UpdateMillisec:
            self.UpdateMillisec = UpdateMillisec
        if BidPrice1:
            self.BidPrice1 = BidPrice1
        if BidVolume1:
            self.BidVolume1 = BidVolume1
        if AskPrice1:
            self.AskPrice1 = AskPrice1
        if AskVolume1:
            self.AskVolume1 = AskVolume1
        if BidPrice2:
            self.BidPrice2 = BidPrice2
        if BidVolume2:
            self.BidVolume2 = BidVolume2
        if AskPrice2:
            self.AskPrice2 = AskPrice2
        if AskVolume2:
            self.AskVolume2 = AskVolume2
        if BidPrice3:
            self.BidPrice3 = BidPrice3
        if BidVolume3:
            self.BidVolume3 = BidVolume3
        if AskPrice3:
            self.AskPrice3 = AskPrice3
        if AskVolume3:
            self.AskVolume3 = AskVolume3
        if BidPrice4:
            self.BidPrice4 = BidPrice4
        if BidVolume4:
            self.BidVolume4 = BidVolume4
        if AskPrice4:
            self.AskPrice4 = AskPrice4
        if AskVolume4:
            self.AskVolume4 = AskVolume4
        if BidPrice5:
            self.BidPrice5 = BidPrice5
        if BidVolume5:
            self.BidVolume5 = BidVolume5
        if AskPrice5:
            self.AskPrice5 = AskPrice5
        if AskVolume5:
            self.AskVolume5 = AskVolume5
        if AveragePrice:
            self.AveragePrice = AveragePrice
        if ActionDay:
            self.ActionDay = ActionDay.encode("GBK")
        if BandingUpperPrice:
            self.BandingUpperPrice = BandingUpperPrice
        if BandingLowerPrice:
            self.BandingLowerPrice = BandingLowerPrice
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaIndexPrice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_81),
        ("ClosePrice", c_double),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, BrokerID=None, InstrumentID=None, ClosePrice=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ClosePrice:
            self.ClosePrice = ClosePrice
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SyncDeltaEWarrantOffset(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
        ("Direction", c_char),
        ("HedgeFlag", c_char),
        ("Volume", c_int),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", c_int),
    ]

    def __init__(self, TradingDay=None, BrokerID=None, InvestorID=None, ExchangeID=None, InstrumentID=None, Direction=None, HedgeFlag=None, Volume=None, ActionDirection=None, SyncDeltaSequenceNo=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if Direction:
            self.Direction = Direction.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag.encode("GBK")
        if Volume:
            self.Volume = Volume
        if ActionDirection:
            self.ActionDirection = ActionDirection.encode("GBK")
        if SyncDeltaSequenceNo:
            self.SyncDeltaSequenceNo = SyncDeltaSequenceNo


class SPBMFutureParameter(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
        ("ProdFamilyCode", c_char_Array_81),
        ("Cvf", c_int),
        ("TimeRange", c_char),
        ("MarginRate", c_double),
        ("LockRateX", c_double),
        ("AddOnRate", c_double),
        ("PreSettlementPrice", c_double),
    ]

    def __init__(self, TradingDay=None, ExchangeID=None, InstrumentID=None, ProdFamilyCode=None, Cvf=None, TimeRange=None, MarginRate=None, LockRateX=None, AddOnRate=None, PreSettlementPrice=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")
        if Cvf:
            self.Cvf = Cvf
        if TimeRange:
            self.TimeRange = TimeRange.encode("GBK")
        if MarginRate:
            self.MarginRate = MarginRate
        if LockRateX:
            self.LockRateX = LockRateX
        if AddOnRate:
            self.AddOnRate = AddOnRate
        if PreSettlementPrice:
            self.PreSettlementPrice = PreSettlementPrice


class SPBMOptionParameter(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
        ("ProdFamilyCode", c_char_Array_81),
        ("Cvf", c_int),
        ("DownPrice", c_double),
        ("Delta", c_double),
        ("SlimiDelta", c_double),
        ("PreSettlementPrice", c_double),
    ]

    def __init__(self, TradingDay=None, ExchangeID=None, InstrumentID=None, ProdFamilyCode=None, Cvf=None, DownPrice=None, Delta=None, SlimiDelta=None, PreSettlementPrice=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")
        if Cvf:
            self.Cvf = Cvf
        if DownPrice:
            self.DownPrice = DownPrice
        if Delta:
            self.Delta = Delta
        if SlimiDelta:
            self.SlimiDelta = SlimiDelta
        if PreSettlementPrice:
            self.PreSettlementPrice = PreSettlementPrice


class SPBMIntraParameter(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("ExchangeID", c_char_Array_9),
        ("ProdFamilyCode", c_char_Array_81),
        ("IntraRateY", c_double),
    ]

    def __init__(self, TradingDay=None, ExchangeID=None, ProdFamilyCode=None, IntraRateY=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")
        if IntraRateY:
            self.IntraRateY = IntraRateY


class SPBMInterParameter(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("ExchangeID", c_char_Array_9),
        ("SpreadId", c_int),
        ("InterRateZ", c_double),
        ("Leg1ProdFamilyCode", c_char_Array_81),
        ("Leg2ProdFamilyCode", c_char_Array_81),
    ]

    def __init__(self, TradingDay=None, ExchangeID=None, SpreadId=None, InterRateZ=None, Leg1ProdFamilyCode=None, Leg2ProdFamilyCode=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if SpreadId:
            self.SpreadId = SpreadId
        if InterRateZ:
            self.InterRateZ = InterRateZ
        if Leg1ProdFamilyCode:
            self.Leg1ProdFamilyCode = Leg1ProdFamilyCode.encode("GBK")
        if Leg2ProdFamilyCode:
            self.Leg2ProdFamilyCode = Leg2ProdFamilyCode.encode("GBK")


class SyncSPBMParameterEnd(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
    ]

    def __init__(self, TradingDay=None):
        super().__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")


class QrySPBMFutureParameter(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
        ("ProdFamilyCode", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, InstrumentID=None, ProdFamilyCode=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")


class QrySPBMOptionParameter(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_81),
        ("ProdFamilyCode", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, InstrumentID=None, ProdFamilyCode=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")


class QrySPBMIntraParameter(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ProdFamilyCode", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, ProdFamilyCode=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")


class QrySPBMInterParameter(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("Leg1ProdFamilyCode", c_char_Array_81),
        ("Leg2ProdFamilyCode", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, Leg1ProdFamilyCode=None, Leg2ProdFamilyCode=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if Leg1ProdFamilyCode:
            self.Leg1ProdFamilyCode = Leg1ProdFamilyCode.encode("GBK")
        if Leg2ProdFamilyCode:
            self.Leg2ProdFamilyCode = Leg2ProdFamilyCode.encode("GBK")


class SPBMPortfDefinition(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("PortfolioDefID", c_int),
        ("ProdFamilyCode", c_char_Array_81),
        ("IsSPBM", c_int),
    ]

    def __init__(self, ExchangeID=None, PortfolioDefID=None, ProdFamilyCode=None, IsSPBM=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if PortfolioDefID:
            self.PortfolioDefID = PortfolioDefID
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")
        if IsSPBM:
            self.IsSPBM = IsSPBM


class SPBMInvestorPortfDef(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("PortfolioDefID", c_int),
    ]

    def __init__(self, ExchangeID=None, BrokerID=None, InvestorID=None, PortfolioDefID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if PortfolioDefID:
            self.PortfolioDefID = PortfolioDefID


class InvestorPortfMarginRatio(Struct):
    _fields_ = [
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("MarginRatio", c_double),
    ]

    def __init__(self, InvestorRange=None, BrokerID=None, InvestorID=None, ExchangeID=None, MarginRatio=None):
        super().__init__()
        if InvestorRange:
            self.InvestorRange = InvestorRange.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if MarginRatio:
            self.MarginRatio = MarginRatio


class QrySPBMPortfDefinition(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("PortfolioDefID", c_int),
        ("ProdFamilyCode", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, PortfolioDefID=None, ProdFamilyCode=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if PortfolioDefID:
            self.PortfolioDefID = PortfolioDefID
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")


class QrySPBMInvestorPortfDef(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

    def __init__(self, ExchangeID=None, BrokerID=None, InvestorID=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class QryInvestorPortfMarginRatio(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(self, BrokerID=None, InvestorID=None, ExchangeID=None):
        super().__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class InvestorProdSPBMDetail(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ProdFamilyCode", c_char_Array_81),
        ("IntraInstrMargin", c_double),
        ("BCollectingMargin", c_double),
        ("SCollectingMargin", c_double),
        ("IntraProdMargin", c_double),
        ("NetMargin", c_double),
        ("InterProdMargin", c_double),
        ("SingleMargin", c_double),
        ("AddOnMargin", c_double),
        ("DeliveryMargin", c_double),
        ("CallOptionMinRisk", c_double),
        ("PutOptionMinRisk", c_double),
        ("OptionMinRisk", c_double),
        ("OptionValueOffset", c_double),
        ("OptionRoyalty", c_double),
        ("RealOptionValueOffset", c_double),
        ("Margin", c_double),
        ("ExchMargin", c_double),
    ]

    def __init__(self, ExchangeID=None, BrokerID=None, InvestorID=None, ProdFamilyCode=None, IntraInstrMargin=None, BCollectingMargin=None, SCollectingMargin=None, IntraProdMargin=None, NetMargin=None, InterProdMargin=None, SingleMargin=None, AddOnMargin=None, DeliveryMargin=None, CallOptionMinRisk=None, PutOptionMinRisk=None, OptionMinRisk=None, OptionValueOffset=None, OptionRoyalty=None, RealOptionValueOffset=None, Margin=None, ExchMargin=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")
        if IntraInstrMargin:
            self.IntraInstrMargin = IntraInstrMargin
        if BCollectingMargin:
            self.BCollectingMargin = BCollectingMargin
        if SCollectingMargin:
            self.SCollectingMargin = SCollectingMargin
        if IntraProdMargin:
            self.IntraProdMargin = IntraProdMargin
        if NetMargin:
            self.NetMargin = NetMargin
        if InterProdMargin:
            self.InterProdMargin = InterProdMargin
        if SingleMargin:
            self.SingleMargin = SingleMargin
        if AddOnMargin:
            self.AddOnMargin = AddOnMargin
        if DeliveryMargin:
            self.DeliveryMargin = DeliveryMargin
        if CallOptionMinRisk:
            self.CallOptionMinRisk = CallOptionMinRisk
        if PutOptionMinRisk:
            self.PutOptionMinRisk = PutOptionMinRisk
        if OptionMinRisk:
            self.OptionMinRisk = OptionMinRisk
        if OptionValueOffset:
            self.OptionValueOffset = OptionValueOffset
        if OptionRoyalty:
            self.OptionRoyalty = OptionRoyalty
        if RealOptionValueOffset:
            self.RealOptionValueOffset = RealOptionValueOffset
        if Margin:
            self.Margin = Margin
        if ExchMargin:
            self.ExchMargin = ExchMargin


class QryInvestorProdSPBMDetail(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ProdFamilyCode", c_char_Array_81),
    ]

    def __init__(self, ExchangeID=None, BrokerID=None, InvestorID=None, ProdFamilyCode=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ProdFamilyCode:
            self.ProdFamilyCode = ProdFamilyCode.encode("GBK")


class PortfTradeParamSetting(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Portfolio", c_char),
        ("IsActionVerify", c_int),
        ("IsCloseVerify", c_int),
    ]

    def __init__(self, ExchangeID=None, BrokerID=None, InvestorID=None, Portfolio=None, IsActionVerify=None, IsCloseVerify=None):
        super().__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Portfolio:
            self.Portfolio = Portfolio.encode("GBK")
        if IsActionVerify:
            self.IsActionVerify = IsActionVerify
        if IsCloseVerify:
            self.IsCloseVerify = IsCloseVerify

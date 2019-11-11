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


from .utils import Struct


class Dissemination(Struct):
    def __init__(
        self,
        SequenceSeries: int = None,
        SequenceNo: int = None,
    ):
        """
        信息分发
        :param SequenceSeries: 序列系列号
        :param SequenceNo: 序列号
        """
        super().__init__()
        ...


class ReqUserLogin(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        BrokerID: str = None,
        UserID: str = None,
        Password: str = None,
        UserProductInfo: str = None,
        InterfaceProductInfo: str = None,
        ProtocolInfo: str = None,
        MacAddress: str = None,
        OneTimePassword: str = None,
        ClientIPAddress: str = None,
        LoginRemark: str = None,
        ClientIPPort: int = None,
    ):
        """
        用户登录请求
        :param TradingDay: 交易日
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param Password: 密码
        :param UserProductInfo: 用户端产品信息
        :param InterfaceProductInfo: 接口端产品信息
        :param ProtocolInfo: 协议信息
        :param MacAddress: Mac地址
        :param OneTimePassword: 动态密码
        :param ClientIPAddress: 终端IP地址
        :param LoginRemark: 登录备注
        :param ClientIPPort: 终端IP端口
        """
        super().__init__()
        ...


class RspUserLogin(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        LoginTime: str = None,
        BrokerID: str = None,
        UserID: str = None,
        SystemName: str = None,
        FrontID: int = None,
        SessionID: int = None,
        MaxOrderRef: str = None,
        SHFETime: str = None,
        DCETime: str = None,
        CZCETime: str = None,
        FFEXTime: str = None,
        INETime: str = None,
    ):
        """
        用户登录应答
        :param TradingDay: 交易日
        :param LoginTime: 登录成功时间
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param SystemName: 交易系统名称
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param MaxOrderRef: 最大报单引用
        :param SHFETime: 上期所时间
        :param DCETime: 大商所时间
        :param CZCETime: 郑商所时间
        :param FFEXTime: 中金所时间
        :param INETime: 能源中心时间
        """
        super().__init__()
        ...


class UserLogout(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        用户登出请求
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class ForceUserLogout(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        强制交易员退出
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class ReqAuthenticate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        UserProductInfo: str = None,
        AuthCode: str = None,
        AppID: str = None,
    ):
        """
        客户端认证请求
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param UserProductInfo: 用户端产品信息
        :param AuthCode: 认证码
        :param AppID: App代码
        """
        super().__init__()
        ...


class RspAuthenticate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        UserProductInfo: str = None,
        AppID: str = None,
        AppType: bytes = None,
    ):
        """
        客户端认证响应
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param UserProductInfo: 用户端产品信息
        :param AppID: App代码
        :param AppType: App类型
        """
        super().__init__()
        ...


class AuthenticationInfo(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        UserProductInfo: str = None,
        AuthInfo: str = None,
        IsResult: int = None,
        AppID: str = None,
        AppType: bytes = None,
    ):
        """
        客户端认证信息
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param UserProductInfo: 用户端产品信息
        :param AuthInfo: 认证信息
        :param IsResult: 是否为认证结果
        :param AppID: App代码
        :param AppType: App类型
        """
        super().__init__()
        ...


class RspUserLogin2(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        LoginTime: str = None,
        BrokerID: str = None,
        UserID: str = None,
        SystemName: str = None,
        FrontID: int = None,
        SessionID: int = None,
        MaxOrderRef: str = None,
        SHFETime: str = None,
        DCETime: str = None,
        CZCETime: str = None,
        FFEXTime: str = None,
        INETime: str = None,
        RandomString: str = None,
    ):
        """
        用户登录应答2
        :param TradingDay: 交易日
        :param LoginTime: 登录成功时间
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param SystemName: 交易系统名称
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param MaxOrderRef: 最大报单引用
        :param SHFETime: 上期所时间
        :param DCETime: 大商所时间
        :param CZCETime: 郑商所时间
        :param FFEXTime: 中金所时间
        :param INETime: 能源中心时间
        :param RandomString: 随机串
        """
        super().__init__()
        ...


class TransferHeader(Struct):
    def __init__(
        self,
        Version: str = None,
        TradeCode: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        TradeSerial: str = None,
        FutureID: str = None,
        BankID: str = None,
        BankBrchID: str = None,
        OperNo: str = None,
        DeviceID: str = None,
        RecordNum: str = None,
        SessionID: int = None,
        RequestID: int = None,
    ):
        """
        银期转帐报文头
        :param Version: 版本号，常量，1.0
        :param TradeCode: 交易代码，必填
        :param TradeDate: 交易日期，必填，格式：yyyymmdd
        :param TradeTime: 交易时间，必填，格式：hhmmss
        :param TradeSerial: 发起方流水号，NA
        :param FutureID: 期货公司代码，必填
        :param BankID: 银行代码，根据查询银行得到，必填
        :param BankBrchID: 银行分中心代码，根据查询银行得到，必填
        :param OperNo: 操作员，NA
        :param DeviceID: 交易设备类型，NA
        :param RecordNum: 记录数，NA
        :param SessionID: 会话编号，NA
        :param RequestID: 请求编号，NA
        """
        super().__init__()
        ...


class TransferBankToFutureReq(Struct):
    def __init__(
        self,
        FutureAccount: str = None,
        FuturePwdFlag: bytes = None,
        FutureAccPwd: str = None,
        TradeAmt: float = None,
        CustFee: float = None,
        CurrencyCode: str = None,
    ):
        """
        银行资金转期货请求，TradeCode=202001
        :param FutureAccount: 期货资金账户
        :param FuturePwdFlag: 密码标志
        :param FutureAccPwd: 密码
        :param TradeAmt: 转账金额
        :param CustFee: 客户手续费
        :param CurrencyCode: 币种：RMB-人民币 USD-美圆 HKD-港元
        """
        super().__init__()
        ...


class TransferBankToFutureRsp(Struct):
    def __init__(
        self,
        RetCode: str = None,
        RetInfo: str = None,
        FutureAccount: str = None,
        TradeAmt: float = None,
        CustFee: float = None,
        CurrencyCode: str = None,
    ):
        """
        银行资金转期货请求响应
        :param RetCode: 响应代码
        :param RetInfo: 响应信息
        :param FutureAccount: 资金账户
        :param TradeAmt: 转帐金额
        :param CustFee: 应收客户手续费
        :param CurrencyCode: 币种
        """
        super().__init__()
        ...


class TransferFutureToBankReq(Struct):
    def __init__(
        self,
        FutureAccount: str = None,
        FuturePwdFlag: bytes = None,
        FutureAccPwd: str = None,
        TradeAmt: float = None,
        CustFee: float = None,
        CurrencyCode: str = None,
    ):
        """
        期货资金转银行请求，TradeCode=202002
        :param FutureAccount: 期货资金账户
        :param FuturePwdFlag: 密码标志
        :param FutureAccPwd: 密码
        :param TradeAmt: 转账金额
        :param CustFee: 客户手续费
        :param CurrencyCode: 币种：RMB-人民币 USD-美圆 HKD-港元
        """
        super().__init__()
        ...


class TransferFutureToBankRsp(Struct):
    def __init__(
        self,
        RetCode: str = None,
        RetInfo: str = None,
        FutureAccount: str = None,
        TradeAmt: float = None,
        CustFee: float = None,
        CurrencyCode: str = None,
    ):
        """
        期货资金转银行请求响应
        :param RetCode: 响应代码
        :param RetInfo: 响应信息
        :param FutureAccount: 资金账户
        :param TradeAmt: 转帐金额
        :param CustFee: 应收客户手续费
        :param CurrencyCode: 币种
        """
        super().__init__()
        ...


class TransferQryBankReq(Struct):
    def __init__(
        self,
        FutureAccount: str = None,
        FuturePwdFlag: bytes = None,
        FutureAccPwd: str = None,
        CurrencyCode: str = None,
    ):
        """
        查询银行资金请求，TradeCode=204002
        :param FutureAccount: 期货资金账户
        :param FuturePwdFlag: 密码标志
        :param FutureAccPwd: 密码
        :param CurrencyCode: 币种：RMB-人民币 USD-美圆 HKD-港元
        """
        super().__init__()
        ...


class TransferQryBankRsp(Struct):
    def __init__(
        self,
        RetCode: str = None,
        RetInfo: str = None,
        FutureAccount: str = None,
        TradeAmt: float = None,
        UseAmt: float = None,
        FetchAmt: float = None,
        CurrencyCode: str = None,
    ):
        """
        查询银行资金请求响应
        :param RetCode: 响应代码
        :param RetInfo: 响应信息
        :param FutureAccount: 资金账户
        :param TradeAmt: 银行余额
        :param UseAmt: 银行可用余额
        :param FetchAmt: 银行可取余额
        :param CurrencyCode: 币种
        """
        super().__init__()
        ...


class TransferQryDetailReq(Struct):
    def __init__(
        self,
        FutureAccount: str = None,
    ):
        """
        查询银行交易明细请求，TradeCode=204999
        :param FutureAccount: 期货资金账户
        """
        super().__init__()
        ...


class TransferQryDetailRsp(Struct):
    def __init__(
        self,
        TradeDate: str = None,
        TradeTime: str = None,
        TradeCode: str = None,
        FutureSerial: int = None,
        FutureID: str = None,
        FutureAccount: str = None,
        BankSerial: int = None,
        BankID: str = None,
        BankBrchID: str = None,
        BankAccount: str = None,
        CertCode: str = None,
        CurrencyCode: str = None,
        TxAmount: float = None,
        Flag: bytes = None,
    ):
        """
        查询银行交易明细请求响应
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param TradeCode: 交易代码
        :param FutureSerial: 期货流水号
        :param FutureID: 期货公司代码
        :param FutureAccount: 资金帐号
        :param BankSerial: 银行流水号
        :param BankID: 银行代码
        :param BankBrchID: 银行分中心代码
        :param BankAccount: 银行账号
        :param CertCode: 证件号码
        :param CurrencyCode: 货币代码
        :param TxAmount: 发生金额
        :param Flag: 有效标志
        """
        super().__init__()
        ...


class RspInfo(Struct):
    def __init__(
        self,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        响应信息
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class Exchange(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        ExchangeName: str = None,
        ExchangeProperty: bytes = None,
    ):
        """
        交易所
        :param ExchangeID: 交易所代码
        :param ExchangeName: 交易所名称
        :param ExchangeProperty: 交易所属性
        """
        super().__init__()
        ...


class Product(Struct):
    def __init__(
        self,
        ProductID: str = None,
        ProductName: str = None,
        ExchangeID: str = None,
        ProductClass: bytes = None,
        VolumeMultiple: int = None,
        PriceTick: float = None,
        MaxMarketOrderVolume: int = None,
        MinMarketOrderVolume: int = None,
        MaxLimitOrderVolume: int = None,
        MinLimitOrderVolume: int = None,
        PositionType: bytes = None,
        PositionDateType: bytes = None,
        CloseDealType: bytes = None,
        TradeCurrencyID: str = None,
        MortgageFundUseRange: bytes = None,
        ExchangeProductID: str = None,
        UnderlyingMultiple: float = None,
    ):
        """
        产品
        :param ProductID: 产品代码
        :param ProductName: 产品名称
        :param ExchangeID: 交易所代码
        :param ProductClass: 产品类型
        :param VolumeMultiple: 合约数量乘数
        :param PriceTick: 最小变动价位
        :param MaxMarketOrderVolume: 市价单最大下单量
        :param MinMarketOrderVolume: 市价单最小下单量
        :param MaxLimitOrderVolume: 限价单最大下单量
        :param MinLimitOrderVolume: 限价单最小下单量
        :param PositionType: 持仓类型
        :param PositionDateType: 持仓日期类型
        :param CloseDealType: 平仓处理类型
        :param TradeCurrencyID: 交易币种类型
        :param MortgageFundUseRange: 质押资金可用范围
        :param ExchangeProductID: 交易所产品代码
        :param UnderlyingMultiple: 合约基础商品乘数
        """
        super().__init__()
        ...


class Instrument(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        ExchangeID: str = None,
        InstrumentName: str = None,
        ExchangeInstID: str = None,
        ProductID: str = None,
        ProductClass: bytes = None,
        DeliveryYear: int = None,
        DeliveryMonth: int = None,
        MaxMarketOrderVolume: int = None,
        MinMarketOrderVolume: int = None,
        MaxLimitOrderVolume: int = None,
        MinLimitOrderVolume: int = None,
        VolumeMultiple: int = None,
        PriceTick: float = None,
        CreateDate: str = None,
        OpenDate: str = None,
        ExpireDate: str = None,
        StartDelivDate: str = None,
        EndDelivDate: str = None,
        InstLifePhase: bytes = None,
        IsTrading: int = None,
        PositionType: bytes = None,
        PositionDateType: bytes = None,
        LongMarginRatio: float = None,
        ShortMarginRatio: float = None,
        MaxMarginSideAlgorithm: bytes = None,
        UnderlyingInstrID: str = None,
        StrikePrice: float = None,
        OptionsType: bytes = None,
        UnderlyingMultiple: float = None,
        CombinationType: bytes = None,
    ):
        """
        合约
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param InstrumentName: 合约名称
        :param ExchangeInstID: 合约在交易所的代码
        :param ProductID: 产品代码
        :param ProductClass: 产品类型
        :param DeliveryYear: 交割年份
        :param DeliveryMonth: 交割月
        :param MaxMarketOrderVolume: 市价单最大下单量
        :param MinMarketOrderVolume: 市价单最小下单量
        :param MaxLimitOrderVolume: 限价单最大下单量
        :param MinLimitOrderVolume: 限价单最小下单量
        :param VolumeMultiple: 合约数量乘数
        :param PriceTick: 最小变动价位
        :param CreateDate: 创建日
        :param OpenDate: 上市日
        :param ExpireDate: 到期日
        :param StartDelivDate: 开始交割日
        :param EndDelivDate: 结束交割日
        :param InstLifePhase: 合约生命周期状态
        :param IsTrading: 当前是否交易
        :param PositionType: 持仓类型
        :param PositionDateType: 持仓日期类型
        :param LongMarginRatio: 多头保证金率
        :param ShortMarginRatio: 空头保证金率
        :param MaxMarginSideAlgorithm: 是否使用大额单边保证金算法
        :param UnderlyingInstrID: 基础商品代码
        :param StrikePrice: 执行价
        :param OptionsType: 期权类型
        :param UnderlyingMultiple: 合约基础商品乘数
        :param CombinationType: 组合类型
        """
        super().__init__()
        ...


class Broker(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        BrokerAbbr: str = None,
        BrokerName: str = None,
        IsActive: int = None,
    ):
        """
        经纪公司
        :param BrokerID: 经纪公司代码
        :param BrokerAbbr: 经纪公司简称
        :param BrokerName: 经纪公司名称
        :param IsActive: 是否活跃
        """
        super().__init__()
        ...


class Trader(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        TraderID: str = None,
        ParticipantID: str = None,
        Password: str = None,
        InstallCount: int = None,
        BrokerID: str = None,
    ):
        """
        交易所交易员
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        :param ParticipantID: 会员代码
        :param Password: 密码
        :param InstallCount: 安装数量
        :param BrokerID: 经纪公司代码
        """
        super().__init__()
        ...


class Investor(Struct):
    def __init__(
        self,
        InvestorID: str = None,
        BrokerID: str = None,
        InvestorGroupID: str = None,
        InvestorName: str = None,
        IdentifiedCardType: bytes = None,
        IdentifiedCardNo: str = None,
        IsActive: int = None,
        Telephone: str = None,
        Address: str = None,
        OpenDate: str = None,
        Mobile: str = None,
        CommModelID: str = None,
        MarginModelID: str = None,
    ):
        """
        投资者
        :param InvestorID: 投资者代码
        :param BrokerID: 经纪公司代码
        :param InvestorGroupID: 投资者分组代码
        :param InvestorName: 投资者名称
        :param IdentifiedCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param IsActive: 是否活跃
        :param Telephone: 联系电话
        :param Address: 通讯地址
        :param OpenDate: 开户日期
        :param Mobile: 手机
        :param CommModelID: 手续费率模板代码
        :param MarginModelID: 保证金率模板代码
        """
        super().__init__()
        ...


class TradingCode(Struct):
    def __init__(
        self,
        InvestorID: str = None,
        BrokerID: str = None,
        ExchangeID: str = None,
        ClientID: str = None,
        IsActive: int = None,
        ClientIDType: bytes = None,
        BranchID: str = None,
        BizType: bytes = None,
        InvestUnitID: str = None,
    ):
        """
        交易编码
        :param InvestorID: 投资者代码
        :param BrokerID: 经纪公司代码
        :param ExchangeID: 交易所代码
        :param ClientID: 客户代码
        :param IsActive: 是否活跃
        :param ClientIDType: 交易编码类型
        :param BranchID: 营业部编号
        :param BizType: 业务类型
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class PartBroker(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        IsActive: int = None,
    ):
        """
        会员编码和经纪公司编码对照表
        :param BrokerID: 经纪公司代码
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param IsActive: 是否活跃
        """
        super().__init__()
        ...


class SuperUser(Struct):
    def __init__(
        self,
        UserID: str = None,
        UserName: str = None,
        Password: str = None,
        IsActive: int = None,
    ):
        """
        管理用户
        :param UserID: 用户代码
        :param UserName: 用户名称
        :param Password: 密码
        :param IsActive: 是否活跃
        """
        super().__init__()
        ...


class SuperUserFunction(Struct):
    def __init__(
        self,
        UserID: str = None,
        FunctionCode: bytes = None,
    ):
        """
        管理用户功能权限
        :param UserID: 用户代码
        :param FunctionCode: 功能代码
        """
        super().__init__()
        ...


class InvestorGroup(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorGroupID: str = None,
        InvestorGroupName: str = None,
    ):
        """
        投资者组
        :param BrokerID: 经纪公司代码
        :param InvestorGroupID: 投资者分组代码
        :param InvestorGroupName: 投资者分组名称
        """
        super().__init__()
        ...


class TradingAccount(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        AccountID: str = None,
        PreMortgage: float = None,
        PreCredit: float = None,
        PreDeposit: float = None,
        PreBalance: float = None,
        PreMargin: float = None,
        InterestBase: float = None,
        Interest: float = None,
        Deposit: float = None,
        Withdraw: float = None,
        FrozenMargin: float = None,
        FrozenCash: float = None,
        FrozenCommission: float = None,
        CurrMargin: float = None,
        CashIn: float = None,
        Commission: float = None,
        CloseProfit: float = None,
        PositionProfit: float = None,
        Balance: float = None,
        Available: float = None,
        WithdrawQuota: float = None,
        Reserve: float = None,
        TradingDay: str = None,
        SettlementID: int = None,
        Credit: float = None,
        Mortgage: float = None,
        ExchangeMargin: float = None,
        DeliveryMargin: float = None,
        ExchangeDeliveryMargin: float = None,
        ReserveBalance: float = None,
        CurrencyID: str = None,
        PreFundMortgageIn: float = None,
        PreFundMortgageOut: float = None,
        FundMortgageIn: float = None,
        FundMortgageOut: float = None,
        FundMortgageAvailable: float = None,
        MortgageableFund: float = None,
        SpecProductMargin: float = None,
        SpecProductFrozenMargin: float = None,
        SpecProductCommission: float = None,
        SpecProductFrozenCommission: float = None,
        SpecProductPositionProfit: float = None,
        SpecProductCloseProfit: float = None,
        SpecProductPositionProfitByAlg: float = None,
        SpecProductExchangeMargin: float = None,
        BizType: bytes = None,
        FrozenSwap: float = None,
        RemainSwap: float = None,
    ):
        """
        资金账户
        :param BrokerID: 经纪公司代码
        :param AccountID: 投资者帐号
        :param PreMortgage: 上次质押金额
        :param PreCredit: 上次信用额度
        :param PreDeposit: 上次存款额
        :param PreBalance: 上次结算准备金
        :param PreMargin: 上次占用的保证金
        :param InterestBase: 利息基数
        :param Interest: 利息收入
        :param Deposit: 入金金额
        :param Withdraw: 出金金额
        :param FrozenMargin: 冻结的保证金
        :param FrozenCash: 冻结的资金
        :param FrozenCommission: 冻结的手续费
        :param CurrMargin: 当前保证金总额
        :param CashIn: 资金差额
        :param Commission: 手续费
        :param CloseProfit: 平仓盈亏
        :param PositionProfit: 持仓盈亏
        :param Balance: 期货结算准备金
        :param Available: 可用资金
        :param WithdrawQuota: 可取资金
        :param Reserve: 基本准备金
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param Credit: 信用额度
        :param Mortgage: 质押金额
        :param ExchangeMargin: 交易所保证金
        :param DeliveryMargin: 投资者交割保证金
        :param ExchangeDeliveryMargin: 交易所交割保证金
        :param ReserveBalance: 保底期货结算准备金
        :param CurrencyID: 币种代码
        :param PreFundMortgageIn: 上次货币质入金额
        :param PreFundMortgageOut: 上次货币质出金额
        :param FundMortgageIn: 货币质入金额
        :param FundMortgageOut: 货币质出金额
        :param FundMortgageAvailable: 货币质押余额
        :param MortgageableFund: 可质押货币金额
        :param SpecProductMargin: 特殊产品占用保证金
        :param SpecProductFrozenMargin: 特殊产品冻结保证金
        :param SpecProductCommission: 特殊产品手续费
        :param SpecProductFrozenCommission: 特殊产品冻结手续费
        :param SpecProductPositionProfit: 特殊产品持仓盈亏
        :param SpecProductCloseProfit: 特殊产品平仓盈亏
        :param SpecProductPositionProfitByAlg: 根据持仓盈亏算法计算的特殊产品持仓盈亏
        :param SpecProductExchangeMargin: 特殊产品交易所保证金
        :param BizType: 业务类型
        :param FrozenSwap: 延时换汇冻结金额
        :param RemainSwap: 剩余换汇额度
        """
        super().__init__()
        ...


class InvestorPosition(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        BrokerID: str = None,
        InvestorID: str = None,
        PosiDirection: bytes = None,
        HedgeFlag: bytes = None,
        PositionDate: bytes = None,
        YdPosition: int = None,
        Position: int = None,
        LongFrozen: int = None,
        ShortFrozen: int = None,
        LongFrozenAmount: float = None,
        ShortFrozenAmount: float = None,
        OpenVolume: int = None,
        CloseVolume: int = None,
        OpenAmount: float = None,
        CloseAmount: float = None,
        PositionCost: float = None,
        PreMargin: float = None,
        UseMargin: float = None,
        FrozenMargin: float = None,
        FrozenCash: float = None,
        FrozenCommission: float = None,
        CashIn: float = None,
        Commission: float = None,
        CloseProfit: float = None,
        PositionProfit: float = None,
        PreSettlementPrice: float = None,
        SettlementPrice: float = None,
        TradingDay: str = None,
        SettlementID: int = None,
        OpenCost: float = None,
        ExchangeMargin: float = None,
        CombPosition: int = None,
        CombLongFrozen: int = None,
        CombShortFrozen: int = None,
        CloseProfitByDate: float = None,
        CloseProfitByTrade: float = None,
        TodayPosition: int = None,
        MarginRateByMoney: float = None,
        MarginRateByVolume: float = None,
        StrikeFrozen: int = None,
        StrikeFrozenAmount: float = None,
        AbandonFrozen: int = None,
        ExchangeID: str = None,
        YdStrikeFrozen: int = None,
        InvestUnitID: str = None,
        PositionCostOffset: float = None,
    ):
        """
        投资者持仓
        :param InstrumentID: 合约代码
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param PosiDirection: 持仓多空方向
        :param HedgeFlag: 投机套保标志
        :param PositionDate: 持仓日期
        :param YdPosition: 上日持仓
        :param Position: 今日持仓
        :param LongFrozen: 多头冻结
        :param ShortFrozen: 空头冻结
        :param LongFrozenAmount: 开仓冻结金额
        :param ShortFrozenAmount: 开仓冻结金额
        :param OpenVolume: 开仓量
        :param CloseVolume: 平仓量
        :param OpenAmount: 开仓金额
        :param CloseAmount: 平仓金额
        :param PositionCost: 持仓成本
        :param PreMargin: 上次占用的保证金
        :param UseMargin: 占用的保证金
        :param FrozenMargin: 冻结的保证金
        :param FrozenCash: 冻结的资金
        :param FrozenCommission: 冻结的手续费
        :param CashIn: 资金差额
        :param Commission: 手续费
        :param CloseProfit: 平仓盈亏
        :param PositionProfit: 持仓盈亏
        :param PreSettlementPrice: 上次结算价
        :param SettlementPrice: 本次结算价
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param OpenCost: 开仓成本
        :param ExchangeMargin: 交易所保证金
        :param CombPosition: 组合成交形成的持仓
        :param CombLongFrozen: 组合多头冻结
        :param CombShortFrozen: 组合空头冻结
        :param CloseProfitByDate: 逐日盯市平仓盈亏
        :param CloseProfitByTrade: 逐笔对冲平仓盈亏
        :param TodayPosition: 今日持仓
        :param MarginRateByMoney: 保证金率
        :param MarginRateByVolume: 保证金率(按手数)
        :param StrikeFrozen: 执行冻结
        :param StrikeFrozenAmount: 执行冻结金额
        :param AbandonFrozen: 放弃执行冻结
        :param ExchangeID: 交易所代码
        :param YdStrikeFrozen: 执行冻结的昨仓
        :param InvestUnitID: 投资单元代码
        :param PositionCostOffset: 大商所持仓成本差值，只有大商所使用
        """
        super().__init__()
        ...


class InstrumentMarginRate(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        HedgeFlag: bytes = None,
        LongMarginRatioByMoney: float = None,
        LongMarginRatioByVolume: float = None,
        ShortMarginRatioByMoney: float = None,
        ShortMarginRatioByVolume: float = None,
        IsRelative: int = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        合约保证金率
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param HedgeFlag: 投机套保标志
        :param LongMarginRatioByMoney: 多头保证金率
        :param LongMarginRatioByVolume: 多头保证金费
        :param ShortMarginRatioByMoney: 空头保证金率
        :param ShortMarginRatioByVolume: 空头保证金费
        :param IsRelative: 是否相对交易所收取
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class InstrumentCommissionRate(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        OpenRatioByMoney: float = None,
        OpenRatioByVolume: float = None,
        CloseRatioByMoney: float = None,
        CloseRatioByVolume: float = None,
        CloseTodayRatioByMoney: float = None,
        CloseTodayRatioByVolume: float = None,
        ExchangeID: str = None,
        BizType: bytes = None,
        InvestUnitID: str = None,
    ):
        """
        合约手续费率
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OpenRatioByMoney: 开仓手续费率
        :param OpenRatioByVolume: 开仓手续费
        :param CloseRatioByMoney: 平仓手续费率
        :param CloseRatioByVolume: 平仓手续费
        :param CloseTodayRatioByMoney: 平今手续费率
        :param CloseTodayRatioByVolume: 平今手续费
        :param ExchangeID: 交易所代码
        :param BizType: 业务类型
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class DepthMarketData(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        ExchangeInstID: str = None,
        LastPrice: float = None,
        PreSettlementPrice: float = None,
        PreClosePrice: float = None,
        PreOpenInterest: float = None,
        OpenPrice: float = None,
        HighestPrice: float = None,
        LowestPrice: float = None,
        Volume: int = None,
        Turnover: float = None,
        OpenInterest: float = None,
        ClosePrice: float = None,
        SettlementPrice: float = None,
        UpperLimitPrice: float = None,
        LowerLimitPrice: float = None,
        PreDelta: float = None,
        CurrDelta: float = None,
        UpdateTime: str = None,
        UpdateMillisec: int = None,
        BidPrice1: float = None,
        BidVolume1: int = None,
        AskPrice1: float = None,
        AskVolume1: int = None,
        BidPrice2: float = None,
        BidVolume2: int = None,
        AskPrice2: float = None,
        AskVolume2: int = None,
        BidPrice3: float = None,
        BidVolume3: int = None,
        AskPrice3: float = None,
        AskVolume3: int = None,
        BidPrice4: float = None,
        BidVolume4: int = None,
        AskPrice4: float = None,
        AskVolume4: int = None,
        BidPrice5: float = None,
        BidVolume5: int = None,
        AskPrice5: float = None,
        AskVolume5: int = None,
        AveragePrice: float = None,
        ActionDay: str = None,
    ):
        """
        深度行情
        :param TradingDay: 交易日
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param ExchangeInstID: 合约在交易所的代码
        :param LastPrice: 最新价
        :param PreSettlementPrice: 上次结算价
        :param PreClosePrice: 昨收盘
        :param PreOpenInterest: 昨持仓量
        :param OpenPrice: 今开盘
        :param HighestPrice: 最高价
        :param LowestPrice: 最低价
        :param Volume: 数量
        :param Turnover: 成交金额
        :param OpenInterest: 持仓量
        :param ClosePrice: 今收盘
        :param SettlementPrice: 本次结算价
        :param UpperLimitPrice: 涨停板价
        :param LowerLimitPrice: 跌停板价
        :param PreDelta: 昨虚实度
        :param CurrDelta: 今虚实度
        :param UpdateTime: 最后修改时间
        :param UpdateMillisec: 最后修改毫秒
        :param BidPrice1: 申买价一
        :param BidVolume1: 申买量一
        :param AskPrice1: 申卖价一
        :param AskVolume1: 申卖量一
        :param BidPrice2: 申买价二
        :param BidVolume2: 申买量二
        :param AskPrice2: 申卖价二
        :param AskVolume2: 申卖量二
        :param BidPrice3: 申买价三
        :param BidVolume3: 申买量三
        :param AskPrice3: 申卖价三
        :param AskVolume3: 申卖量三
        :param BidPrice4: 申买价四
        :param BidVolume4: 申买量四
        :param AskPrice4: 申卖价四
        :param AskVolume4: 申卖量四
        :param BidPrice5: 申买价五
        :param BidVolume5: 申买量五
        :param AskPrice5: 申卖价五
        :param AskVolume5: 申卖量五
        :param AveragePrice: 当日均价
        :param ActionDay: 业务日期
        """
        super().__init__()
        ...


class InstrumentTradingRight(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        TradingRight: bytes = None,
    ):
        """
        投资者合约交易权限
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param TradingRight: 交易权限
        """
        super().__init__()
        ...


class BrokerUser(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        UserName: str = None,
        UserType: bytes = None,
        IsActive: int = None,
        IsUsingOTP: int = None,
        IsAuthForce: int = None,
    ):
        """
        经纪公司用户
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param UserName: 用户名称
        :param UserType: 用户类型
        :param IsActive: 是否活跃
        :param IsUsingOTP: 是否使用令牌
        :param IsAuthForce: 是否强制终端认证
        """
        super().__init__()
        ...


class BrokerUserPassword(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        Password: str = None,
        LastUpdateTime: str = None,
        LastLoginTime: str = None,
        ExpireDate: str = None,
        WeakExpireDate: str = None,
    ):
        """
        经纪公司用户口令
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param Password: 密码
        :param LastUpdateTime: 上次修改时间
        :param LastLoginTime: 上次登陆时间
        :param ExpireDate: 密码过期时间
        :param WeakExpireDate: 弱密码过期时间
        """
        super().__init__()
        ...


class BrokerUserFunction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        BrokerFunctionCode: bytes = None,
    ):
        """
        经纪公司用户功能权限
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param BrokerFunctionCode: 经纪公司功能代码
        """
        super().__init__()
        ...


class TraderOffer(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        TraderID: str = None,
        ParticipantID: str = None,
        Password: str = None,
        InstallID: int = None,
        OrderLocalID: str = None,
        TraderConnectStatus: bytes = None,
        ConnectRequestDate: str = None,
        ConnectRequestTime: str = None,
        LastReportDate: str = None,
        LastReportTime: str = None,
        ConnectDate: str = None,
        ConnectTime: str = None,
        StartDate: str = None,
        StartTime: str = None,
        TradingDay: str = None,
        BrokerID: str = None,
        MaxTradeID: str = None,
        MaxOrderMessageReference: str = None,
    ):
        """
        交易所交易员报盘机
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        :param ParticipantID: 会员代码
        :param Password: 密码
        :param InstallID: 安装编号
        :param OrderLocalID: 本地报单编号
        :param TraderConnectStatus: 交易所交易员连接状态
        :param ConnectRequestDate: 发出连接请求的日期
        :param ConnectRequestTime: 发出连接请求的时间
        :param LastReportDate: 上次报告日期
        :param LastReportTime: 上次报告时间
        :param ConnectDate: 完成连接日期
        :param ConnectTime: 完成连接时间
        :param StartDate: 启动日期
        :param StartTime: 启动时间
        :param TradingDay: 交易日
        :param BrokerID: 经纪公司代码
        :param MaxTradeID: 本席位最大成交编号
        :param MaxOrderMessageReference: 本席位最大报单备拷
        """
        super().__init__()
        ...


class SettlementInfo(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        SettlementID: int = None,
        BrokerID: str = None,
        InvestorID: str = None,
        SequenceNo: int = None,
        Content: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
    ):
        """
        投资者结算结果
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param SequenceNo: 序号
        :param Content: 消息正文
        :param AccountID: 投资者帐号
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class InstrumentMarginRateAdjust(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        HedgeFlag: bytes = None,
        LongMarginRatioByMoney: float = None,
        LongMarginRatioByVolume: float = None,
        ShortMarginRatioByMoney: float = None,
        ShortMarginRatioByVolume: float = None,
        IsRelative: int = None,
    ):
        """
        合约保证金率调整
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param HedgeFlag: 投机套保标志
        :param LongMarginRatioByMoney: 多头保证金率
        :param LongMarginRatioByVolume: 多头保证金费
        :param ShortMarginRatioByMoney: 空头保证金率
        :param ShortMarginRatioByVolume: 空头保证金费
        :param IsRelative: 是否相对交易所收取
        """
        super().__init__()
        ...


class ExchangeMarginRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InstrumentID: str = None,
        HedgeFlag: bytes = None,
        LongMarginRatioByMoney: float = None,
        LongMarginRatioByVolume: float = None,
        ShortMarginRatioByMoney: float = None,
        ShortMarginRatioByVolume: float = None,
        ExchangeID: str = None,
    ):
        """
        交易所保证金率
        :param BrokerID: 经纪公司代码
        :param InstrumentID: 合约代码
        :param HedgeFlag: 投机套保标志
        :param LongMarginRatioByMoney: 多头保证金率
        :param LongMarginRatioByVolume: 多头保证金费
        :param ShortMarginRatioByMoney: 空头保证金率
        :param ShortMarginRatioByVolume: 空头保证金费
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class ExchangeMarginRateAdjust(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InstrumentID: str = None,
        HedgeFlag: bytes = None,
        LongMarginRatioByMoney: float = None,
        LongMarginRatioByVolume: float = None,
        ShortMarginRatioByMoney: float = None,
        ShortMarginRatioByVolume: float = None,
        ExchLongMarginRatioByMoney: float = None,
        ExchLongMarginRatioByVolume: float = None,
        ExchShortMarginRatioByMoney: float = None,
        ExchShortMarginRatioByVolume: float = None,
        NoLongMarginRatioByMoney: float = None,
        NoLongMarginRatioByVolume: float = None,
        NoShortMarginRatioByMoney: float = None,
        NoShortMarginRatioByVolume: float = None,
    ):
        """
        交易所保证金率调整
        :param BrokerID: 经纪公司代码
        :param InstrumentID: 合约代码
        :param HedgeFlag: 投机套保标志
        :param LongMarginRatioByMoney: 跟随交易所投资者多头保证金率
        :param LongMarginRatioByVolume: 跟随交易所投资者多头保证金费
        :param ShortMarginRatioByMoney: 跟随交易所投资者空头保证金率
        :param ShortMarginRatioByVolume: 跟随交易所投资者空头保证金费
        :param ExchLongMarginRatioByMoney: 交易所多头保证金率
        :param ExchLongMarginRatioByVolume: 交易所多头保证金费
        :param ExchShortMarginRatioByMoney: 交易所空头保证金率
        :param ExchShortMarginRatioByVolume: 交易所空头保证金费
        :param NoLongMarginRatioByMoney: 不跟随交易所投资者多头保证金率
        :param NoLongMarginRatioByVolume: 不跟随交易所投资者多头保证金费
        :param NoShortMarginRatioByMoney: 不跟随交易所投资者空头保证金率
        :param NoShortMarginRatioByVolume: 不跟随交易所投资者空头保证金费
        """
        super().__init__()
        ...


class ExchangeRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        FromCurrencyID: str = None,
        FromCurrencyUnit: float = None,
        ToCurrencyID: str = None,
        ExchangeRate: float = None,
    ):
        """
        汇率
        :param BrokerID: 经纪公司代码
        :param FromCurrencyID: 源币种
        :param FromCurrencyUnit: 源币种单位数量
        :param ToCurrencyID: 目标币种
        :param ExchangeRate: 汇率
        """
        super().__init__()
        ...


class SettlementRef(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        SettlementID: int = None,
    ):
        """
        结算引用
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        """
        super().__init__()
        ...


class CurrentTime(Struct):
    def __init__(
        self,
        CurrDate: str = None,
        CurrTime: str = None,
        CurrMillisec: int = None,
        ActionDay: str = None,
    ):
        """
        当前时间
        :param CurrDate: 当前日期
        :param CurrTime: 当前时间
        :param CurrMillisec: 当前时间（毫秒）
        :param ActionDay: 业务日期
        """
        super().__init__()
        ...


class CommPhase(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        CommPhaseNo: int = None,
        SystemID: str = None,
    ):
        """
        通讯阶段
        :param TradingDay: 交易日
        :param CommPhaseNo: 通讯时段编号
        :param SystemID: 系统编号
        """
        super().__init__()
        ...


class LoginInfo(Struct):
    def __init__(
        self,
        FrontID: int = None,
        SessionID: int = None,
        BrokerID: str = None,
        UserID: str = None,
        LoginDate: str = None,
        LoginTime: str = None,
        IPAddress: str = None,
        UserProductInfo: str = None,
        InterfaceProductInfo: str = None,
        ProtocolInfo: str = None,
        SystemName: str = None,
        PasswordDeprecated: str = None,
        MaxOrderRef: str = None,
        SHFETime: str = None,
        DCETime: str = None,
        CZCETime: str = None,
        FFEXTime: str = None,
        MacAddress: str = None,
        OneTimePassword: str = None,
        INETime: str = None,
        IsQryControl: int = None,
        LoginRemark: str = None,
        Password: str = None,
    ):
        """
        登录信息
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param LoginDate: 登录日期
        :param LoginTime: 登录时间
        :param IPAddress: IP地址
        :param UserProductInfo: 用户端产品信息
        :param InterfaceProductInfo: 接口端产品信息
        :param ProtocolInfo: 协议信息
        :param SystemName: 系统名称
        :param PasswordDeprecated: 密码,已弃用
        :param MaxOrderRef: 最大报单引用
        :param SHFETime: 上期所时间
        :param DCETime: 大商所时间
        :param CZCETime: 郑商所时间
        :param FFEXTime: 中金所时间
        :param MacAddress: Mac地址
        :param OneTimePassword: 动态密码
        :param INETime: 能源中心时间
        :param IsQryControl: 查询时是否需要流控
        :param LoginRemark: 登录备注
        :param Password: 密码
        """
        super().__init__()
        ...


class LogoutAll(Struct):
    def __init__(
        self,
        FrontID: int = None,
        SessionID: int = None,
        SystemName: str = None,
    ):
        """
        登录信息
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param SystemName: 系统名称
        """
        super().__init__()
        ...


class FrontStatus(Struct):
    def __init__(
        self,
        FrontID: int = None,
        LastReportDate: str = None,
        LastReportTime: str = None,
        IsActive: int = None,
    ):
        """
        前置状态
        :param FrontID: 前置编号
        :param LastReportDate: 上次报告日期
        :param LastReportTime: 上次报告时间
        :param IsActive: 是否活跃
        """
        super().__init__()
        ...


class UserPasswordUpdate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        OldPassword: str = None,
        NewPassword: str = None,
    ):
        """
        用户口令变更
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param OldPassword: 原来的口令
        :param NewPassword: 新的口令
        """
        super().__init__()
        ...


class InputOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        OrderRef: str = None,
        UserID: str = None,
        OrderPriceType: bytes = None,
        Direction: bytes = None,
        CombOffsetFlag: str = None,
        CombHedgeFlag: str = None,
        LimitPrice: float = None,
        VolumeTotalOriginal: int = None,
        TimeCondition: bytes = None,
        GTDDate: str = None,
        VolumeCondition: bytes = None,
        MinVolume: int = None,
        ContingentCondition: bytes = None,
        StopPrice: float = None,
        ForceCloseReason: bytes = None,
        IsAutoSuspend: int = None,
        BusinessUnit: str = None,
        RequestID: int = None,
        UserForceClose: int = None,
        IsSwapOrder: int = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        ClientID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入报单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param OrderRef: 报单引用
        :param UserID: 用户代码
        :param OrderPriceType: 报单价格条件
        :param Direction: 买卖方向
        :param CombOffsetFlag: 组合开平标志
        :param CombHedgeFlag: 组合投机套保标志
        :param LimitPrice: 价格
        :param VolumeTotalOriginal: 数量
        :param TimeCondition: 有效期类型
        :param GTDDate: GTD日期
        :param VolumeCondition: 成交量类型
        :param MinVolume: 最小成交量
        :param ContingentCondition: 触发条件
        :param StopPrice: 止损价
        :param ForceCloseReason: 强平原因
        :param IsAutoSuspend: 自动挂起标志
        :param BusinessUnit: 业务单元
        :param RequestID: 请求编号
        :param UserForceClose: 用户强评标志
        :param IsSwapOrder: 互换单标志
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param ClientID: 交易编码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class Order(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        OrderRef: str = None,
        UserID: str = None,
        OrderPriceType: bytes = None,
        Direction: bytes = None,
        CombOffsetFlag: str = None,
        CombHedgeFlag: str = None,
        LimitPrice: float = None,
        VolumeTotalOriginal: int = None,
        TimeCondition: bytes = None,
        GTDDate: str = None,
        VolumeCondition: bytes = None,
        MinVolume: int = None,
        ContingentCondition: bytes = None,
        StopPrice: float = None,
        ForceCloseReason: bytes = None,
        IsAutoSuspend: int = None,
        BusinessUnit: str = None,
        RequestID: int = None,
        OrderLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderSubmitStatus: bytes = None,
        NotifySequence: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        OrderSysID: str = None,
        OrderSource: bytes = None,
        OrderStatus: bytes = None,
        OrderType: bytes = None,
        VolumeTraded: int = None,
        VolumeTotal: int = None,
        InsertDate: str = None,
        InsertTime: str = None,
        ActiveTime: str = None,
        SuspendTime: str = None,
        UpdateTime: str = None,
        CancelTime: str = None,
        ActiveTraderID: str = None,
        ClearingPartID: str = None,
        SequenceNo: int = None,
        FrontID: int = None,
        SessionID: int = None,
        UserProductInfo: str = None,
        StatusMsg: str = None,
        UserForceClose: int = None,
        ActiveUserID: str = None,
        BrokerOrderSeq: int = None,
        RelativeOrderSysID: str = None,
        ZCETotalTradedVolume: int = None,
        IsSwapOrder: int = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        报单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param OrderRef: 报单引用
        :param UserID: 用户代码
        :param OrderPriceType: 报单价格条件
        :param Direction: 买卖方向
        :param CombOffsetFlag: 组合开平标志
        :param CombHedgeFlag: 组合投机套保标志
        :param LimitPrice: 价格
        :param VolumeTotalOriginal: 数量
        :param TimeCondition: 有效期类型
        :param GTDDate: GTD日期
        :param VolumeCondition: 成交量类型
        :param MinVolume: 最小成交量
        :param ContingentCondition: 触发条件
        :param StopPrice: 止损价
        :param ForceCloseReason: 强平原因
        :param IsAutoSuspend: 自动挂起标志
        :param BusinessUnit: 业务单元
        :param RequestID: 请求编号
        :param OrderLocalID: 本地报单编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderSubmitStatus: 报单提交状态
        :param NotifySequence: 报单提示序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param OrderSysID: 报单编号
        :param OrderSource: 报单来源
        :param OrderStatus: 报单状态
        :param OrderType: 报单类型
        :param VolumeTraded: 今成交数量
        :param VolumeTotal: 剩余数量
        :param InsertDate: 报单日期
        :param InsertTime: 委托时间
        :param ActiveTime: 激活时间
        :param SuspendTime: 挂起时间
        :param UpdateTime: 最后修改时间
        :param CancelTime: 撤销时间
        :param ActiveTraderID: 最后修改交易所交易员代码
        :param ClearingPartID: 结算会员编号
        :param SequenceNo: 序号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param UserProductInfo: 用户端产品信息
        :param StatusMsg: 状态信息
        :param UserForceClose: 用户强评标志
        :param ActiveUserID: 操作用户代码
        :param BrokerOrderSeq: 经纪公司报单编号
        :param RelativeOrderSysID: 相关报单
        :param ZCETotalTradedVolume: 郑商所成交数量
        :param IsSwapOrder: 互换单标志
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ExchangeOrder(Struct):
    def __init__(
        self,
        OrderPriceType: bytes = None,
        Direction: bytes = None,
        CombOffsetFlag: str = None,
        CombHedgeFlag: str = None,
        LimitPrice: float = None,
        VolumeTotalOriginal: int = None,
        TimeCondition: bytes = None,
        GTDDate: str = None,
        VolumeCondition: bytes = None,
        MinVolume: int = None,
        ContingentCondition: bytes = None,
        StopPrice: float = None,
        ForceCloseReason: bytes = None,
        IsAutoSuspend: int = None,
        BusinessUnit: str = None,
        RequestID: int = None,
        OrderLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderSubmitStatus: bytes = None,
        NotifySequence: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        OrderSysID: str = None,
        OrderSource: bytes = None,
        OrderStatus: bytes = None,
        OrderType: bytes = None,
        VolumeTraded: int = None,
        VolumeTotal: int = None,
        InsertDate: str = None,
        InsertTime: str = None,
        ActiveTime: str = None,
        SuspendTime: str = None,
        UpdateTime: str = None,
        CancelTime: str = None,
        ActiveTraderID: str = None,
        ClearingPartID: str = None,
        SequenceNo: int = None,
        BranchID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        交易所报单
        :param OrderPriceType: 报单价格条件
        :param Direction: 买卖方向
        :param CombOffsetFlag: 组合开平标志
        :param CombHedgeFlag: 组合投机套保标志
        :param LimitPrice: 价格
        :param VolumeTotalOriginal: 数量
        :param TimeCondition: 有效期类型
        :param GTDDate: GTD日期
        :param VolumeCondition: 成交量类型
        :param MinVolume: 最小成交量
        :param ContingentCondition: 触发条件
        :param StopPrice: 止损价
        :param ForceCloseReason: 强平原因
        :param IsAutoSuspend: 自动挂起标志
        :param BusinessUnit: 业务单元
        :param RequestID: 请求编号
        :param OrderLocalID: 本地报单编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderSubmitStatus: 报单提交状态
        :param NotifySequence: 报单提示序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param OrderSysID: 报单编号
        :param OrderSource: 报单来源
        :param OrderStatus: 报单状态
        :param OrderType: 报单类型
        :param VolumeTraded: 今成交数量
        :param VolumeTotal: 剩余数量
        :param InsertDate: 报单日期
        :param InsertTime: 委托时间
        :param ActiveTime: 激活时间
        :param SuspendTime: 挂起时间
        :param UpdateTime: 最后修改时间
        :param CancelTime: 撤销时间
        :param ActiveTraderID: 最后修改交易所交易员代码
        :param ClearingPartID: 结算会员编号
        :param SequenceNo: 序号
        :param BranchID: 营业部编号
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ExchangeOrderInsertError(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        ParticipantID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderLocalID: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        交易所报单插入失败
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderLocalID: 本地报单编号
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class InputOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        OrderActionRef: int = None,
        OrderRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        OrderSysID: str = None,
        ActionFlag: bytes = None,
        LimitPrice: float = None,
        VolumeChange: int = None,
        UserID: str = None,
        InstrumentID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入报单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OrderActionRef: 报单操作引用
        :param OrderRef: 报单引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param OrderSysID: 报单编号
        :param ActionFlag: 操作标志
        :param LimitPrice: 价格
        :param VolumeChange: 数量变化
        :param UserID: 用户代码
        :param InstrumentID: 合约代码
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class OrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        OrderActionRef: int = None,
        OrderRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        OrderSysID: str = None,
        ActionFlag: bytes = None,
        LimitPrice: float = None,
        VolumeChange: int = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderLocalID: str = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        StatusMsg: str = None,
        InstrumentID: str = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        报单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OrderActionRef: 报单操作引用
        :param OrderRef: 报单引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param OrderSysID: 报单编号
        :param ActionFlag: 操作标志
        :param LimitPrice: 价格
        :param VolumeChange: 数量变化
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderLocalID: 本地报单编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param StatusMsg: 状态信息
        :param InstrumentID: 合约代码
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ExchangeOrderAction(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        OrderSysID: str = None,
        ActionFlag: bytes = None,
        LimitPrice: float = None,
        VolumeChange: int = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderLocalID: str = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        BranchID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        交易所报单操作
        :param ExchangeID: 交易所代码
        :param OrderSysID: 报单编号
        :param ActionFlag: 操作标志
        :param LimitPrice: 价格
        :param VolumeChange: 数量变化
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderLocalID: 本地报单编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param BranchID: 营业部编号
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ExchangeOrderActionError(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        OrderSysID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderLocalID: str = None,
        ActionLocalID: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        交易所报单操作失败
        :param ExchangeID: 交易所代码
        :param OrderSysID: 报单编号
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderLocalID: 本地报单编号
        :param ActionLocalID: 操作本地编号
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class ExchangeTrade(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        TradeID: str = None,
        Direction: bytes = None,
        OrderSysID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        TradingRole: bytes = None,
        ExchangeInstID: str = None,
        OffsetFlag: bytes = None,
        HedgeFlag: bytes = None,
        Price: float = None,
        Volume: int = None,
        TradeDate: str = None,
        TradeTime: str = None,
        TradeType: bytes = None,
        PriceSource: bytes = None,
        TraderID: str = None,
        OrderLocalID: str = None,
        ClearingPartID: str = None,
        BusinessUnit: str = None,
        SequenceNo: int = None,
        TradeSource: bytes = None,
    ):
        """
        交易所成交
        :param ExchangeID: 交易所代码
        :param TradeID: 成交编号
        :param Direction: 买卖方向
        :param OrderSysID: 报单编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param TradingRole: 交易角色
        :param ExchangeInstID: 合约在交易所的代码
        :param OffsetFlag: 开平标志
        :param HedgeFlag: 投机套保标志
        :param Price: 价格
        :param Volume: 数量
        :param TradeDate: 成交时期
        :param TradeTime: 成交时间
        :param TradeType: 成交类型
        :param PriceSource: 成交价来源
        :param TraderID: 交易所交易员代码
        :param OrderLocalID: 本地报单编号
        :param ClearingPartID: 结算会员编号
        :param BusinessUnit: 业务单元
        :param SequenceNo: 序号
        :param TradeSource: 成交来源
        """
        super().__init__()
        ...


class Trade(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        OrderRef: str = None,
        UserID: str = None,
        ExchangeID: str = None,
        TradeID: str = None,
        Direction: bytes = None,
        OrderSysID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        TradingRole: bytes = None,
        ExchangeInstID: str = None,
        OffsetFlag: bytes = None,
        HedgeFlag: bytes = None,
        Price: float = None,
        Volume: int = None,
        TradeDate: str = None,
        TradeTime: str = None,
        TradeType: bytes = None,
        PriceSource: bytes = None,
        TraderID: str = None,
        OrderLocalID: str = None,
        ClearingPartID: str = None,
        BusinessUnit: str = None,
        SequenceNo: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        BrokerOrderSeq: int = None,
        TradeSource: bytes = None,
        InvestUnitID: str = None,
    ):
        """
        成交
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param OrderRef: 报单引用
        :param UserID: 用户代码
        :param ExchangeID: 交易所代码
        :param TradeID: 成交编号
        :param Direction: 买卖方向
        :param OrderSysID: 报单编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param TradingRole: 交易角色
        :param ExchangeInstID: 合约在交易所的代码
        :param OffsetFlag: 开平标志
        :param HedgeFlag: 投机套保标志
        :param Price: 价格
        :param Volume: 数量
        :param TradeDate: 成交时期
        :param TradeTime: 成交时间
        :param TradeType: 成交类型
        :param PriceSource: 成交价来源
        :param TraderID: 交易所交易员代码
        :param OrderLocalID: 本地报单编号
        :param ClearingPartID: 结算会员编号
        :param BusinessUnit: 业务单元
        :param SequenceNo: 序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param BrokerOrderSeq: 经纪公司报单编号
        :param TradeSource: 成交来源
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class UserSession(Struct):
    def __init__(
        self,
        FrontID: int = None,
        SessionID: int = None,
        BrokerID: str = None,
        UserID: str = None,
        LoginDate: str = None,
        LoginTime: str = None,
        IPAddress: str = None,
        UserProductInfo: str = None,
        InterfaceProductInfo: str = None,
        ProtocolInfo: str = None,
        MacAddress: str = None,
        LoginRemark: str = None,
    ):
        """
        用户会话
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param LoginDate: 登录日期
        :param LoginTime: 登录时间
        :param IPAddress: IP地址
        :param UserProductInfo: 用户端产品信息
        :param InterfaceProductInfo: 接口端产品信息
        :param ProtocolInfo: 协议信息
        :param MacAddress: Mac地址
        :param LoginRemark: 登录备注
        """
        super().__init__()
        ...


class QueryMaxOrderVolume(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        Direction: bytes = None,
        OffsetFlag: bytes = None,
        HedgeFlag: bytes = None,
        MaxVolume: int = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询最大报单数量
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param Direction: 买卖方向
        :param OffsetFlag: 开平标志
        :param HedgeFlag: 投机套保标志
        :param MaxVolume: 最大允许报单数量
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class SettlementInfoConfirm(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ConfirmDate: str = None,
        ConfirmTime: str = None,
        SettlementID: int = None,
        AccountID: str = None,
        CurrencyID: str = None,
    ):
        """
        投资者结算结果确认信息
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ConfirmDate: 确认日期
        :param ConfirmTime: 确认时间
        :param SettlementID: 结算编号
        :param AccountID: 投资者帐号
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class SyncDeposit(Struct):
    def __init__(
        self,
        DepositSeqNo: str = None,
        BrokerID: str = None,
        InvestorID: str = None,
        Deposit: float = None,
        IsForce: int = None,
        CurrencyID: str = None,
    ):
        """
        出入金同步
        :param DepositSeqNo: 出入金流水号
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param Deposit: 入金金额
        :param IsForce: 是否强制进行
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class SyncFundMortgage(Struct):
    def __init__(
        self,
        MortgageSeqNo: str = None,
        BrokerID: str = None,
        InvestorID: str = None,
        FromCurrencyID: str = None,
        MortgageAmount: float = None,
        ToCurrencyID: str = None,
    ):
        """
        货币质押同步
        :param MortgageSeqNo: 货币质押流水号
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param FromCurrencyID: 源币种
        :param MortgageAmount: 质押金额
        :param ToCurrencyID: 目标币种
        """
        super().__init__()
        ...


class BrokerSync(Struct):
    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        经纪公司同步
        :param BrokerID: 经纪公司代码
        """
        super().__init__()
        ...


class SyncingInvestor(Struct):
    def __init__(
        self,
        InvestorID: str = None,
        BrokerID: str = None,
        InvestorGroupID: str = None,
        InvestorName: str = None,
        IdentifiedCardType: bytes = None,
        IdentifiedCardNo: str = None,
        IsActive: int = None,
        Telephone: str = None,
        Address: str = None,
        OpenDate: str = None,
        Mobile: str = None,
        CommModelID: str = None,
        MarginModelID: str = None,
    ):
        """
        正在同步中的投资者
        :param InvestorID: 投资者代码
        :param BrokerID: 经纪公司代码
        :param InvestorGroupID: 投资者分组代码
        :param InvestorName: 投资者名称
        :param IdentifiedCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param IsActive: 是否活跃
        :param Telephone: 联系电话
        :param Address: 通讯地址
        :param OpenDate: 开户日期
        :param Mobile: 手机
        :param CommModelID: 手续费率模板代码
        :param MarginModelID: 保证金率模板代码
        """
        super().__init__()
        ...


class SyncingTradingCode(Struct):
    def __init__(
        self,
        InvestorID: str = None,
        BrokerID: str = None,
        ExchangeID: str = None,
        ClientID: str = None,
        IsActive: int = None,
        ClientIDType: bytes = None,
    ):
        """
        正在同步中的交易代码
        :param InvestorID: 投资者代码
        :param BrokerID: 经纪公司代码
        :param ExchangeID: 交易所代码
        :param ClientID: 客户代码
        :param IsActive: 是否活跃
        :param ClientIDType: 交易编码类型
        """
        super().__init__()
        ...


class SyncingInvestorGroup(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorGroupID: str = None,
        InvestorGroupName: str = None,
    ):
        """
        正在同步中的投资者分组
        :param BrokerID: 经纪公司代码
        :param InvestorGroupID: 投资者分组代码
        :param InvestorGroupName: 投资者分组名称
        """
        super().__init__()
        ...


class SyncingTradingAccount(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        AccountID: str = None,
        PreMortgage: float = None,
        PreCredit: float = None,
        PreDeposit: float = None,
        PreBalance: float = None,
        PreMargin: float = None,
        InterestBase: float = None,
        Interest: float = None,
        Deposit: float = None,
        Withdraw: float = None,
        FrozenMargin: float = None,
        FrozenCash: float = None,
        FrozenCommission: float = None,
        CurrMargin: float = None,
        CashIn: float = None,
        Commission: float = None,
        CloseProfit: float = None,
        PositionProfit: float = None,
        Balance: float = None,
        Available: float = None,
        WithdrawQuota: float = None,
        Reserve: float = None,
        TradingDay: str = None,
        SettlementID: int = None,
        Credit: float = None,
        Mortgage: float = None,
        ExchangeMargin: float = None,
        DeliveryMargin: float = None,
        ExchangeDeliveryMargin: float = None,
        ReserveBalance: float = None,
        CurrencyID: str = None,
        PreFundMortgageIn: float = None,
        PreFundMortgageOut: float = None,
        FundMortgageIn: float = None,
        FundMortgageOut: float = None,
        FundMortgageAvailable: float = None,
        MortgageableFund: float = None,
        SpecProductMargin: float = None,
        SpecProductFrozenMargin: float = None,
        SpecProductCommission: float = None,
        SpecProductFrozenCommission: float = None,
        SpecProductPositionProfit: float = None,
        SpecProductCloseProfit: float = None,
        SpecProductPositionProfitByAlg: float = None,
        SpecProductExchangeMargin: float = None,
        FrozenSwap: float = None,
        RemainSwap: float = None,
    ):
        """
        正在同步中的交易账号
        :param BrokerID: 经纪公司代码
        :param AccountID: 投资者帐号
        :param PreMortgage: 上次质押金额
        :param PreCredit: 上次信用额度
        :param PreDeposit: 上次存款额
        :param PreBalance: 上次结算准备金
        :param PreMargin: 上次占用的保证金
        :param InterestBase: 利息基数
        :param Interest: 利息收入
        :param Deposit: 入金金额
        :param Withdraw: 出金金额
        :param FrozenMargin: 冻结的保证金
        :param FrozenCash: 冻结的资金
        :param FrozenCommission: 冻结的手续费
        :param CurrMargin: 当前保证金总额
        :param CashIn: 资金差额
        :param Commission: 手续费
        :param CloseProfit: 平仓盈亏
        :param PositionProfit: 持仓盈亏
        :param Balance: 期货结算准备金
        :param Available: 可用资金
        :param WithdrawQuota: 可取资金
        :param Reserve: 基本准备金
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param Credit: 信用额度
        :param Mortgage: 质押金额
        :param ExchangeMargin: 交易所保证金
        :param DeliveryMargin: 投资者交割保证金
        :param ExchangeDeliveryMargin: 交易所交割保证金
        :param ReserveBalance: 保底期货结算准备金
        :param CurrencyID: 币种代码
        :param PreFundMortgageIn: 上次货币质入金额
        :param PreFundMortgageOut: 上次货币质出金额
        :param FundMortgageIn: 货币质入金额
        :param FundMortgageOut: 货币质出金额
        :param FundMortgageAvailable: 货币质押余额
        :param MortgageableFund: 可质押货币金额
        :param SpecProductMargin: 特殊产品占用保证金
        :param SpecProductFrozenMargin: 特殊产品冻结保证金
        :param SpecProductCommission: 特殊产品手续费
        :param SpecProductFrozenCommission: 特殊产品冻结手续费
        :param SpecProductPositionProfit: 特殊产品持仓盈亏
        :param SpecProductCloseProfit: 特殊产品平仓盈亏
        :param SpecProductPositionProfitByAlg: 根据持仓盈亏算法计算的特殊产品持仓盈亏
        :param SpecProductExchangeMargin: 特殊产品交易所保证金
        :param FrozenSwap: 延时换汇冻结金额
        :param RemainSwap: 剩余换汇额度
        """
        super().__init__()
        ...


class SyncingInvestorPosition(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        BrokerID: str = None,
        InvestorID: str = None,
        PosiDirection: bytes = None,
        HedgeFlag: bytes = None,
        PositionDate: bytes = None,
        YdPosition: int = None,
        Position: int = None,
        LongFrozen: int = None,
        ShortFrozen: int = None,
        LongFrozenAmount: float = None,
        ShortFrozenAmount: float = None,
        OpenVolume: int = None,
        CloseVolume: int = None,
        OpenAmount: float = None,
        CloseAmount: float = None,
        PositionCost: float = None,
        PreMargin: float = None,
        UseMargin: float = None,
        FrozenMargin: float = None,
        FrozenCash: float = None,
        FrozenCommission: float = None,
        CashIn: float = None,
        Commission: float = None,
        CloseProfit: float = None,
        PositionProfit: float = None,
        PreSettlementPrice: float = None,
        SettlementPrice: float = None,
        TradingDay: str = None,
        SettlementID: int = None,
        OpenCost: float = None,
        ExchangeMargin: float = None,
        CombPosition: int = None,
        CombLongFrozen: int = None,
        CombShortFrozen: int = None,
        CloseProfitByDate: float = None,
        CloseProfitByTrade: float = None,
        TodayPosition: int = None,
        MarginRateByMoney: float = None,
        MarginRateByVolume: float = None,
        StrikeFrozen: int = None,
        StrikeFrozenAmount: float = None,
        AbandonFrozen: int = None,
        ExchangeID: str = None,
        YdStrikeFrozen: int = None,
        InvestUnitID: str = None,
        PositionCostOffset: float = None,
    ):
        """
        正在同步中的投资者持仓
        :param InstrumentID: 合约代码
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param PosiDirection: 持仓多空方向
        :param HedgeFlag: 投机套保标志
        :param PositionDate: 持仓日期
        :param YdPosition: 上日持仓
        :param Position: 今日持仓
        :param LongFrozen: 多头冻结
        :param ShortFrozen: 空头冻结
        :param LongFrozenAmount: 开仓冻结金额
        :param ShortFrozenAmount: 开仓冻结金额
        :param OpenVolume: 开仓量
        :param CloseVolume: 平仓量
        :param OpenAmount: 开仓金额
        :param CloseAmount: 平仓金额
        :param PositionCost: 持仓成本
        :param PreMargin: 上次占用的保证金
        :param UseMargin: 占用的保证金
        :param FrozenMargin: 冻结的保证金
        :param FrozenCash: 冻结的资金
        :param FrozenCommission: 冻结的手续费
        :param CashIn: 资金差额
        :param Commission: 手续费
        :param CloseProfit: 平仓盈亏
        :param PositionProfit: 持仓盈亏
        :param PreSettlementPrice: 上次结算价
        :param SettlementPrice: 本次结算价
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param OpenCost: 开仓成本
        :param ExchangeMargin: 交易所保证金
        :param CombPosition: 组合成交形成的持仓
        :param CombLongFrozen: 组合多头冻结
        :param CombShortFrozen: 组合空头冻结
        :param CloseProfitByDate: 逐日盯市平仓盈亏
        :param CloseProfitByTrade: 逐笔对冲平仓盈亏
        :param TodayPosition: 今日持仓
        :param MarginRateByMoney: 保证金率
        :param MarginRateByVolume: 保证金率(按手数)
        :param StrikeFrozen: 执行冻结
        :param StrikeFrozenAmount: 执行冻结金额
        :param AbandonFrozen: 放弃执行冻结
        :param ExchangeID: 交易所代码
        :param YdStrikeFrozen: 执行冻结的昨仓
        :param InvestUnitID: 投资单元代码
        :param PositionCostOffset: 大商所持仓成本差值，只有大商所使用
        """
        super().__init__()
        ...


class SyncingInstrumentMarginRate(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        HedgeFlag: bytes = None,
        LongMarginRatioByMoney: float = None,
        LongMarginRatioByVolume: float = None,
        ShortMarginRatioByMoney: float = None,
        ShortMarginRatioByVolume: float = None,
        IsRelative: int = None,
    ):
        """
        正在同步中的合约保证金率
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param HedgeFlag: 投机套保标志
        :param LongMarginRatioByMoney: 多头保证金率
        :param LongMarginRatioByVolume: 多头保证金费
        :param ShortMarginRatioByMoney: 空头保证金率
        :param ShortMarginRatioByVolume: 空头保证金费
        :param IsRelative: 是否相对交易所收取
        """
        super().__init__()
        ...


class SyncingInstrumentCommissionRate(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        OpenRatioByMoney: float = None,
        OpenRatioByVolume: float = None,
        CloseRatioByMoney: float = None,
        CloseRatioByVolume: float = None,
        CloseTodayRatioByMoney: float = None,
        CloseTodayRatioByVolume: float = None,
    ):
        """
        正在同步中的合约手续费率
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OpenRatioByMoney: 开仓手续费率
        :param OpenRatioByVolume: 开仓手续费
        :param CloseRatioByMoney: 平仓手续费率
        :param CloseRatioByVolume: 平仓手续费
        :param CloseTodayRatioByMoney: 平今手续费率
        :param CloseTodayRatioByVolume: 平今手续费
        """
        super().__init__()
        ...


class SyncingInstrumentTradingRight(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        TradingRight: bytes = None,
    ):
        """
        正在同步中的合约交易权限
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param TradingRight: 交易权限
        """
        super().__init__()
        ...


class QryOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        OrderSysID: str = None,
        InsertTimeStart: str = None,
        InsertTimeEnd: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询报单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param OrderSysID: 报单编号
        :param InsertTimeStart: 开始时间
        :param InsertTimeEnd: 结束时间
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryTrade(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        TradeID: str = None,
        TradeTimeStart: str = None,
        TradeTimeEnd: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询成交
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param TradeID: 成交编号
        :param TradeTimeStart: 开始时间
        :param TradeTimeEnd: 结束时间
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryInvestorPosition(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询投资者持仓
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryTradingAccount(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        CurrencyID: str = None,
        BizType: bytes = None,
        AccountID: str = None,
    ):
        """
        查询资金账户
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param CurrencyID: 币种代码
        :param BizType: 业务类型
        :param AccountID: 投资者帐号
        """
        super().__init__()
        ...


class QryInvestor(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
    ):
        """
        查询投资者
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        """
        super().__init__()
        ...


class QryTradingCode(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExchangeID: str = None,
        ClientID: str = None,
        ClientIDType: bytes = None,
        InvestUnitID: str = None,
    ):
        """
        查询交易编码
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExchangeID: 交易所代码
        :param ClientID: 客户代码
        :param ClientIDType: 交易编码类型
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryInvestorGroup(Struct):
    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        查询投资者组
        :param BrokerID: 经纪公司代码
        """
        super().__init__()
        ...


class QryInstrumentMarginRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        HedgeFlag: bytes = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询合约保证金率
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param HedgeFlag: 投机套保标志
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryInstrumentCommissionRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询手续费率
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryInstrumentTradingRight(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
    ):
        """
        查询合约交易权限
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        """
        super().__init__()
        ...


class QryBroker(Struct):
    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        查询经纪公司
        :param BrokerID: 经纪公司代码
        """
        super().__init__()
        ...


class QryTrader(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        ParticipantID: str = None,
        TraderID: str = None,
    ):
        """
        查询交易员
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class QrySuperUserFunction(Struct):
    def __init__(
        self,
        UserID: str = None,
    ):
        """
        查询管理用户功能权限
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class QryUserSession(Struct):
    def __init__(
        self,
        FrontID: int = None,
        SessionID: int = None,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        查询用户会话
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class QryPartBroker(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        BrokerID: str = None,
        ParticipantID: str = None,
    ):
        """
        查询经纪公司会员代码
        :param ExchangeID: 交易所代码
        :param BrokerID: 经纪公司代码
        :param ParticipantID: 会员代码
        """
        super().__init__()
        ...


class QryFrontStatus(Struct):
    def __init__(
        self,
        FrontID: int = None,
    ):
        """
        查询前置状态
        :param FrontID: 前置编号
        """
        super().__init__()
        ...


class QryExchangeOrder(Struct):
    def __init__(
        self,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        ExchangeID: str = None,
        TraderID: str = None,
    ):
        """
        查询交易所报单
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class QryOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExchangeID: str = None,
    ):
        """
        查询报单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class QryExchangeOrderAction(Struct):
    def __init__(
        self,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeID: str = None,
        TraderID: str = None,
    ):
        """
        查询交易所报单操作
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class QrySuperUser(Struct):
    def __init__(
        self,
        UserID: str = None,
    ):
        """
        查询管理用户
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class QryExchange(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
    ):
        """
        查询交易所
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class QryProduct(Struct):
    def __init__(
        self,
        ProductID: str = None,
        ProductClass: bytes = None,
        ExchangeID: str = None,
    ):
        """
        查询产品
        :param ProductID: 产品代码
        :param ProductClass: 产品类型
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class QryInstrument(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        ExchangeID: str = None,
        ExchangeInstID: str = None,
        ProductID: str = None,
    ):
        """
        查询合约
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param ExchangeInstID: 合约在交易所的代码
        :param ProductID: 产品代码
        """
        super().__init__()
        ...


class QryDepthMarketData(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        ExchangeID: str = None,
    ):
        """
        查询行情
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class QryBrokerUser(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        查询经纪公司用户
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class QryBrokerUserFunction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        查询经纪公司用户权限
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class QryTraderOffer(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        ParticipantID: str = None,
        TraderID: str = None,
    ):
        """
        查询交易员报盘机
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class QrySyncDeposit(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        DepositSeqNo: str = None,
    ):
        """
        查询出入金流水
        :param BrokerID: 经纪公司代码
        :param DepositSeqNo: 出入金流水号
        """
        super().__init__()
        ...


class QrySettlementInfo(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        TradingDay: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
    ):
        """
        查询投资者结算结果
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param TradingDay: 交易日
        :param AccountID: 投资者帐号
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class QryExchangeMarginRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InstrumentID: str = None,
        HedgeFlag: bytes = None,
        ExchangeID: str = None,
    ):
        """
        查询交易所保证金率
        :param BrokerID: 经纪公司代码
        :param InstrumentID: 合约代码
        :param HedgeFlag: 投机套保标志
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class QryExchangeMarginRateAdjust(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InstrumentID: str = None,
        HedgeFlag: bytes = None,
    ):
        """
        查询交易所调整保证金率
        :param BrokerID: 经纪公司代码
        :param InstrumentID: 合约代码
        :param HedgeFlag: 投机套保标志
        """
        super().__init__()
        ...


class QryExchangeRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        FromCurrencyID: str = None,
        ToCurrencyID: str = None,
    ):
        """
        查询汇率
        :param BrokerID: 经纪公司代码
        :param FromCurrencyID: 源币种
        :param ToCurrencyID: 目标币种
        """
        super().__init__()
        ...


class QrySyncFundMortgage(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        MortgageSeqNo: str = None,
    ):
        """
        查询货币质押流水
        :param BrokerID: 经纪公司代码
        :param MortgageSeqNo: 货币质押流水号
        """
        super().__init__()
        ...


class QryHisOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        OrderSysID: str = None,
        InsertTimeStart: str = None,
        InsertTimeEnd: str = None,
        TradingDay: str = None,
        SettlementID: int = None,
    ):
        """
        查询报单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param OrderSysID: 报单编号
        :param InsertTimeStart: 开始时间
        :param InsertTimeEnd: 结束时间
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        """
        super().__init__()
        ...


class OptionInstrMiniMargin(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        MinMargin: float = None,
        ValueMethod: bytes = None,
        IsRelative: int = None,
    ):
        """
        当前期权合约最小保证金
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param MinMargin: 单位（手）期权合约最小保证金
        :param ValueMethod: 取值方式
        :param IsRelative: 是否跟随交易所收取
        """
        super().__init__()
        ...


class OptionInstrMarginAdjust(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        SShortMarginRatioByMoney: float = None,
        SShortMarginRatioByVolume: float = None,
        HShortMarginRatioByMoney: float = None,
        HShortMarginRatioByVolume: float = None,
        AShortMarginRatioByMoney: float = None,
        AShortMarginRatioByVolume: float = None,
        IsRelative: int = None,
        MShortMarginRatioByMoney: float = None,
        MShortMarginRatioByVolume: float = None,
    ):
        """
        当前期权合约保证金调整系数
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param SShortMarginRatioByMoney: 投机空头保证金调整系数
        :param SShortMarginRatioByVolume: 投机空头保证金调整系数
        :param HShortMarginRatioByMoney: 保值空头保证金调整系数
        :param HShortMarginRatioByVolume: 保值空头保证金调整系数
        :param AShortMarginRatioByMoney: 套利空头保证金调整系数
        :param AShortMarginRatioByVolume: 套利空头保证金调整系数
        :param IsRelative: 是否跟随交易所收取
        :param MShortMarginRatioByMoney: 做市商空头保证金调整系数
        :param MShortMarginRatioByVolume: 做市商空头保证金调整系数
        """
        super().__init__()
        ...


class OptionInstrCommRate(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        OpenRatioByMoney: float = None,
        OpenRatioByVolume: float = None,
        CloseRatioByMoney: float = None,
        CloseRatioByVolume: float = None,
        CloseTodayRatioByMoney: float = None,
        CloseTodayRatioByVolume: float = None,
        StrikeRatioByMoney: float = None,
        StrikeRatioByVolume: float = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        当前期权合约手续费的详细内容
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OpenRatioByMoney: 开仓手续费率
        :param OpenRatioByVolume: 开仓手续费
        :param CloseRatioByMoney: 平仓手续费率
        :param CloseRatioByVolume: 平仓手续费
        :param CloseTodayRatioByMoney: 平今手续费率
        :param CloseTodayRatioByVolume: 平今手续费
        :param StrikeRatioByMoney: 执行手续费率
        :param StrikeRatioByVolume: 执行手续费
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class OptionInstrTradeCost(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        HedgeFlag: bytes = None,
        FixedMargin: float = None,
        MiniMargin: float = None,
        Royalty: float = None,
        ExchFixedMargin: float = None,
        ExchMiniMargin: float = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        期权交易成本
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param HedgeFlag: 投机套保标志
        :param FixedMargin: 期权合约保证金不变部分
        :param MiniMargin: 期权合约最小保证金
        :param Royalty: 期权合约权利金
        :param ExchFixedMargin: 交易所期权合约保证金不变部分
        :param ExchMiniMargin: 交易所期权合约最小保证金
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryOptionInstrTradeCost(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        HedgeFlag: bytes = None,
        InputPrice: float = None,
        UnderlyingPrice: float = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        期权交易成本查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param HedgeFlag: 投机套保标志
        :param InputPrice: 期权合约报价
        :param UnderlyingPrice: 标的价格,填0则用昨结算价
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryOptionInstrCommRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        期权手续费率查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class IndexPrice(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InstrumentID: str = None,
        ClosePrice: float = None,
    ):
        """
        股指现货指数
        :param BrokerID: 经纪公司代码
        :param InstrumentID: 合约代码
        :param ClosePrice: 指数现货收盘价
        """
        super().__init__()
        ...


class InputExecOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExecOrderRef: str = None,
        UserID: str = None,
        Volume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        OffsetFlag: bytes = None,
        HedgeFlag: bytes = None,
        ActionType: bytes = None,
        PosiDirection: bytes = None,
        ReservePositionFlag: bytes = None,
        CloseFlag: bytes = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        ClientID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入的执行宣告
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExecOrderRef: 执行宣告引用
        :param UserID: 用户代码
        :param Volume: 数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param OffsetFlag: 开平标志
        :param HedgeFlag: 投机套保标志
        :param ActionType: 执行类型
        :param PosiDirection: 保留头寸申请的持仓方向
        :param ReservePositionFlag: 期权行权后是否保留期货头寸的标记,该字段已废弃
        :param CloseFlag: 期权行权后生成的头寸是否自动平仓
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param ClientID: 交易编码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class InputExecOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExecOrderActionRef: int = None,
        ExecOrderRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        ExecOrderSysID: str = None,
        ActionFlag: bytes = None,
        UserID: str = None,
        InstrumentID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入执行宣告操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExecOrderActionRef: 执行宣告操作引用
        :param ExecOrderRef: 执行宣告引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param ExecOrderSysID: 执行宣告操作编号
        :param ActionFlag: 操作标志
        :param UserID: 用户代码
        :param InstrumentID: 合约代码
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ExecOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExecOrderRef: str = None,
        UserID: str = None,
        Volume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        OffsetFlag: bytes = None,
        HedgeFlag: bytes = None,
        ActionType: bytes = None,
        PosiDirection: bytes = None,
        ReservePositionFlag: bytes = None,
        CloseFlag: bytes = None,
        ExecOrderLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderSubmitStatus: bytes = None,
        NotifySequence: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        ExecOrderSysID: str = None,
        InsertDate: str = None,
        InsertTime: str = None,
        CancelTime: str = None,
        ExecResult: bytes = None,
        ClearingPartID: str = None,
        SequenceNo: int = None,
        FrontID: int = None,
        SessionID: int = None,
        UserProductInfo: str = None,
        StatusMsg: str = None,
        ActiveUserID: str = None,
        BrokerExecOrderSeq: int = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        执行宣告
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExecOrderRef: 执行宣告引用
        :param UserID: 用户代码
        :param Volume: 数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param OffsetFlag: 开平标志
        :param HedgeFlag: 投机套保标志
        :param ActionType: 执行类型
        :param PosiDirection: 保留头寸申请的持仓方向
        :param ReservePositionFlag: 期权行权后是否保留期货头寸的标记,该字段已废弃
        :param CloseFlag: 期权行权后生成的头寸是否自动平仓
        :param ExecOrderLocalID: 本地执行宣告编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderSubmitStatus: 执行宣告提交状态
        :param NotifySequence: 报单提示序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param ExecOrderSysID: 执行宣告编号
        :param InsertDate: 报单日期
        :param InsertTime: 插入时间
        :param CancelTime: 撤销时间
        :param ExecResult: 执行结果
        :param ClearingPartID: 结算会员编号
        :param SequenceNo: 序号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param UserProductInfo: 用户端产品信息
        :param StatusMsg: 状态信息
        :param ActiveUserID: 操作用户代码
        :param BrokerExecOrderSeq: 经纪公司报单编号
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ExecOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExecOrderActionRef: int = None,
        ExecOrderRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        ExecOrderSysID: str = None,
        ActionFlag: bytes = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        ExecOrderLocalID: str = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        ActionType: bytes = None,
        StatusMsg: str = None,
        InstrumentID: str = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        执行宣告操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExecOrderActionRef: 执行宣告操作引用
        :param ExecOrderRef: 执行宣告引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param ExecOrderSysID: 执行宣告操作编号
        :param ActionFlag: 操作标志
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param ExecOrderLocalID: 本地执行宣告编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param ActionType: 执行类型
        :param StatusMsg: 状态信息
        :param InstrumentID: 合约代码
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryExecOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        ExecOrderSysID: str = None,
        InsertTimeStart: str = None,
        InsertTimeEnd: str = None,
    ):
        """
        执行宣告查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param ExecOrderSysID: 执行宣告编号
        :param InsertTimeStart: 开始时间
        :param InsertTimeEnd: 结束时间
        """
        super().__init__()
        ...


class ExchangeExecOrder(Struct):
    def __init__(
        self,
        Volume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        OffsetFlag: bytes = None,
        HedgeFlag: bytes = None,
        ActionType: bytes = None,
        PosiDirection: bytes = None,
        ReservePositionFlag: bytes = None,
        CloseFlag: bytes = None,
        ExecOrderLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderSubmitStatus: bytes = None,
        NotifySequence: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        ExecOrderSysID: str = None,
        InsertDate: str = None,
        InsertTime: str = None,
        CancelTime: str = None,
        ExecResult: bytes = None,
        ClearingPartID: str = None,
        SequenceNo: int = None,
        BranchID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        交易所执行宣告信息
        :param Volume: 数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param OffsetFlag: 开平标志
        :param HedgeFlag: 投机套保标志
        :param ActionType: 执行类型
        :param PosiDirection: 保留头寸申请的持仓方向
        :param ReservePositionFlag: 期权行权后是否保留期货头寸的标记,该字段已废弃
        :param CloseFlag: 期权行权后生成的头寸是否自动平仓
        :param ExecOrderLocalID: 本地执行宣告编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderSubmitStatus: 执行宣告提交状态
        :param NotifySequence: 报单提示序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param ExecOrderSysID: 执行宣告编号
        :param InsertDate: 报单日期
        :param InsertTime: 插入时间
        :param CancelTime: 撤销时间
        :param ExecResult: 执行结果
        :param ClearingPartID: 结算会员编号
        :param SequenceNo: 序号
        :param BranchID: 营业部编号
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryExchangeExecOrder(Struct):
    def __init__(
        self,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        ExchangeID: str = None,
        TraderID: str = None,
    ):
        """
        交易所执行宣告查询
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class QryExecOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExchangeID: str = None,
    ):
        """
        执行宣告操作查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class ExchangeExecOrderAction(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        ExecOrderSysID: str = None,
        ActionFlag: bytes = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        ExecOrderLocalID: str = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        ActionType: bytes = None,
        BranchID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
        ExchangeInstID: str = None,
        Volume: int = None,
    ):
        """
        交易所执行宣告操作
        :param ExchangeID: 交易所代码
        :param ExecOrderSysID: 执行宣告操作编号
        :param ActionFlag: 操作标志
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param ExecOrderLocalID: 本地执行宣告编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param ActionType: 执行类型
        :param BranchID: 营业部编号
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        :param ExchangeInstID: 合约在交易所的代码
        :param Volume: 数量
        """
        super().__init__()
        ...


class QryExchangeExecOrderAction(Struct):
    def __init__(
        self,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeID: str = None,
        TraderID: str = None,
    ):
        """
        交易所执行宣告操作查询
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class ErrExecOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExecOrderRef: str = None,
        UserID: str = None,
        Volume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        OffsetFlag: bytes = None,
        HedgeFlag: bytes = None,
        ActionType: bytes = None,
        PosiDirection: bytes = None,
        ReservePositionFlag: bytes = None,
        CloseFlag: bytes = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        ClientID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        错误执行宣告
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExecOrderRef: 执行宣告引用
        :param UserID: 用户代码
        :param Volume: 数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param OffsetFlag: 开平标志
        :param HedgeFlag: 投机套保标志
        :param ActionType: 执行类型
        :param PosiDirection: 保留头寸申请的持仓方向
        :param ReservePositionFlag: 期权行权后是否保留期货头寸的标记,该字段已废弃
        :param CloseFlag: 期权行权后生成的头寸是否自动平仓
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param ClientID: 交易编码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class QryErrExecOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
    ):
        """
        查询错误执行宣告
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        """
        super().__init__()
        ...


class ErrExecOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExecOrderActionRef: int = None,
        ExecOrderRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        ExecOrderSysID: str = None,
        ActionFlag: bytes = None,
        UserID: str = None,
        InstrumentID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        错误执行宣告操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExecOrderActionRef: 执行宣告操作引用
        :param ExecOrderRef: 执行宣告引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param ExecOrderSysID: 执行宣告操作编号
        :param ActionFlag: 操作标志
        :param UserID: 用户代码
        :param InstrumentID: 合约代码
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class QryErrExecOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
    ):
        """
        查询错误执行宣告操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        """
        super().__init__()
        ...


class OptionInstrTradingRight(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        Direction: bytes = None,
        TradingRight: bytes = None,
    ):
        """
        投资者期权合约交易权限
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param Direction: 买卖方向
        :param TradingRight: 交易权限
        """
        super().__init__()
        ...


class QryOptionInstrTradingRight(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        Direction: bytes = None,
    ):
        """
        查询期权合约交易权限
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param Direction: 买卖方向
        """
        super().__init__()
        ...


class InputForQuote(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ForQuoteRef: str = None,
        UserID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入的询价
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ForQuoteRef: 询价引用
        :param UserID: 用户代码
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ForQuote(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ForQuoteRef: str = None,
        UserID: str = None,
        ForQuoteLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        InsertDate: str = None,
        InsertTime: str = None,
        ForQuoteStatus: bytes = None,
        FrontID: int = None,
        SessionID: int = None,
        StatusMsg: str = None,
        ActiveUserID: str = None,
        BrokerForQutoSeq: int = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        询价
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ForQuoteRef: 询价引用
        :param UserID: 用户代码
        :param ForQuoteLocalID: 本地询价编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param InsertDate: 报单日期
        :param InsertTime: 插入时间
        :param ForQuoteStatus: 询价状态
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param StatusMsg: 状态信息
        :param ActiveUserID: 操作用户代码
        :param BrokerForQutoSeq: 经纪公司询价编号
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryForQuote(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        InsertTimeStart: str = None,
        InsertTimeEnd: str = None,
        InvestUnitID: str = None,
    ):
        """
        询价查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param InsertTimeStart: 开始时间
        :param InsertTimeEnd: 结束时间
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class ExchangeForQuote(Struct):
    def __init__(
        self,
        ForQuoteLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        InsertDate: str = None,
        InsertTime: str = None,
        ForQuoteStatus: bytes = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        交易所询价信息
        :param ForQuoteLocalID: 本地询价编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param InsertDate: 报单日期
        :param InsertTime: 插入时间
        :param ForQuoteStatus: 询价状态
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryExchangeForQuote(Struct):
    def __init__(
        self,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        ExchangeID: str = None,
        TraderID: str = None,
    ):
        """
        交易所询价查询
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class InputQuote(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        QuoteRef: str = None,
        UserID: str = None,
        AskPrice: float = None,
        BidPrice: float = None,
        AskVolume: int = None,
        BidVolume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        AskOffsetFlag: bytes = None,
        BidOffsetFlag: bytes = None,
        AskHedgeFlag: bytes = None,
        BidHedgeFlag: bytes = None,
        AskOrderRef: str = None,
        BidOrderRef: str = None,
        ForQuoteSysID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
        ClientID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入的报价
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param QuoteRef: 报价引用
        :param UserID: 用户代码
        :param AskPrice: 卖价格
        :param BidPrice: 买价格
        :param AskVolume: 卖数量
        :param BidVolume: 买数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param AskOffsetFlag: 卖开平标志
        :param BidOffsetFlag: 买开平标志
        :param AskHedgeFlag: 卖投机套保标志
        :param BidHedgeFlag: 买投机套保标志
        :param AskOrderRef: 衍生卖报单引用
        :param BidOrderRef: 衍生买报单引用
        :param ForQuoteSysID: 应价编号
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        :param ClientID: 交易编码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class InputQuoteAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        QuoteActionRef: int = None,
        QuoteRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        QuoteSysID: str = None,
        ActionFlag: bytes = None,
        UserID: str = None,
        InstrumentID: str = None,
        InvestUnitID: str = None,
        ClientID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入报价操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param QuoteActionRef: 报价操作引用
        :param QuoteRef: 报价引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param QuoteSysID: 报价操作编号
        :param ActionFlag: 操作标志
        :param UserID: 用户代码
        :param InstrumentID: 合约代码
        :param InvestUnitID: 投资单元代码
        :param ClientID: 交易编码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class Quote(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        QuoteRef: str = None,
        UserID: str = None,
        AskPrice: float = None,
        BidPrice: float = None,
        AskVolume: int = None,
        BidVolume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        AskOffsetFlag: bytes = None,
        BidOffsetFlag: bytes = None,
        AskHedgeFlag: bytes = None,
        BidHedgeFlag: bytes = None,
        QuoteLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        NotifySequence: int = None,
        OrderSubmitStatus: bytes = None,
        TradingDay: str = None,
        SettlementID: int = None,
        QuoteSysID: str = None,
        InsertDate: str = None,
        InsertTime: str = None,
        CancelTime: str = None,
        QuoteStatus: bytes = None,
        ClearingPartID: str = None,
        SequenceNo: int = None,
        AskOrderSysID: str = None,
        BidOrderSysID: str = None,
        FrontID: int = None,
        SessionID: int = None,
        UserProductInfo: str = None,
        StatusMsg: str = None,
        ActiveUserID: str = None,
        BrokerQuoteSeq: int = None,
        AskOrderRef: str = None,
        BidOrderRef: str = None,
        ForQuoteSysID: str = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        报价
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param QuoteRef: 报价引用
        :param UserID: 用户代码
        :param AskPrice: 卖价格
        :param BidPrice: 买价格
        :param AskVolume: 卖数量
        :param BidVolume: 买数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param AskOffsetFlag: 卖开平标志
        :param BidOffsetFlag: 买开平标志
        :param AskHedgeFlag: 卖投机套保标志
        :param BidHedgeFlag: 买投机套保标志
        :param QuoteLocalID: 本地报价编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param NotifySequence: 报价提示序号
        :param OrderSubmitStatus: 报价提交状态
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param QuoteSysID: 报价编号
        :param InsertDate: 报单日期
        :param InsertTime: 插入时间
        :param CancelTime: 撤销时间
        :param QuoteStatus: 报价状态
        :param ClearingPartID: 结算会员编号
        :param SequenceNo: 序号
        :param AskOrderSysID: 卖方报单编号
        :param BidOrderSysID: 买方报单编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param UserProductInfo: 用户端产品信息
        :param StatusMsg: 状态信息
        :param ActiveUserID: 操作用户代码
        :param BrokerQuoteSeq: 经纪公司报价编号
        :param AskOrderRef: 衍生卖报单引用
        :param BidOrderRef: 衍生买报单引用
        :param ForQuoteSysID: 应价编号
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QuoteAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        QuoteActionRef: int = None,
        QuoteRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        QuoteSysID: str = None,
        ActionFlag: bytes = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        QuoteLocalID: str = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        StatusMsg: str = None,
        InstrumentID: str = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        报价操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param QuoteActionRef: 报价操作引用
        :param QuoteRef: 报价引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param QuoteSysID: 报价操作编号
        :param ActionFlag: 操作标志
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param QuoteLocalID: 本地报价编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param StatusMsg: 状态信息
        :param InstrumentID: 合约代码
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryQuote(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        QuoteSysID: str = None,
        InsertTimeStart: str = None,
        InsertTimeEnd: str = None,
        InvestUnitID: str = None,
    ):
        """
        报价查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param QuoteSysID: 报价编号
        :param InsertTimeStart: 开始时间
        :param InsertTimeEnd: 结束时间
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class ExchangeQuote(Struct):
    def __init__(
        self,
        AskPrice: float = None,
        BidPrice: float = None,
        AskVolume: int = None,
        BidVolume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        AskOffsetFlag: bytes = None,
        BidOffsetFlag: bytes = None,
        AskHedgeFlag: bytes = None,
        BidHedgeFlag: bytes = None,
        QuoteLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        NotifySequence: int = None,
        OrderSubmitStatus: bytes = None,
        TradingDay: str = None,
        SettlementID: int = None,
        QuoteSysID: str = None,
        InsertDate: str = None,
        InsertTime: str = None,
        CancelTime: str = None,
        QuoteStatus: bytes = None,
        ClearingPartID: str = None,
        SequenceNo: int = None,
        AskOrderSysID: str = None,
        BidOrderSysID: str = None,
        ForQuoteSysID: str = None,
        BranchID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        交易所报价信息
        :param AskPrice: 卖价格
        :param BidPrice: 买价格
        :param AskVolume: 卖数量
        :param BidVolume: 买数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param AskOffsetFlag: 卖开平标志
        :param BidOffsetFlag: 买开平标志
        :param AskHedgeFlag: 卖投机套保标志
        :param BidHedgeFlag: 买投机套保标志
        :param QuoteLocalID: 本地报价编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param NotifySequence: 报价提示序号
        :param OrderSubmitStatus: 报价提交状态
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param QuoteSysID: 报价编号
        :param InsertDate: 报单日期
        :param InsertTime: 插入时间
        :param CancelTime: 撤销时间
        :param QuoteStatus: 报价状态
        :param ClearingPartID: 结算会员编号
        :param SequenceNo: 序号
        :param AskOrderSysID: 卖方报单编号
        :param BidOrderSysID: 买方报单编号
        :param ForQuoteSysID: 应价编号
        :param BranchID: 营业部编号
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryExchangeQuote(Struct):
    def __init__(
        self,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        ExchangeID: str = None,
        TraderID: str = None,
    ):
        """
        交易所报价查询
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class QryQuoteAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExchangeID: str = None,
    ):
        """
        报价操作查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class ExchangeQuoteAction(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        QuoteSysID: str = None,
        ActionFlag: bytes = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        QuoteLocalID: str = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        交易所报价操作
        :param ExchangeID: 交易所代码
        :param QuoteSysID: 报价操作编号
        :param ActionFlag: 操作标志
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param QuoteLocalID: 本地报价编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryExchangeQuoteAction(Struct):
    def __init__(
        self,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeID: str = None,
        TraderID: str = None,
    ):
        """
        交易所报价操作查询
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class OptionInstrDelta(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        Delta: float = None,
    ):
        """
        期权合约delta值
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param Delta: Delta值
        """
        super().__init__()
        ...


class ForQuoteRsp(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        InstrumentID: str = None,
        ForQuoteSysID: str = None,
        ForQuoteTime: str = None,
        ActionDay: str = None,
        ExchangeID: str = None,
    ):
        """
        发给做市商的询价请求
        :param TradingDay: 交易日
        :param InstrumentID: 合约代码
        :param ForQuoteSysID: 询价编号
        :param ForQuoteTime: 询价时间
        :param ActionDay: 业务日期
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class StrikeOffset(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        Offset: float = None,
        OffsetType: bytes = None,
    ):
        """
        当前期权合约执行偏移值的详细内容
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param Offset: 执行偏移值
        :param OffsetType: 执行偏移类型
        """
        super().__init__()
        ...


class QryStrikeOffset(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
    ):
        """
        期权执行偏移值查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        """
        super().__init__()
        ...


class InputBatchOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        OrderActionRef: int = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        UserID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入批量报单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OrderActionRef: 报单操作引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param UserID: 用户代码
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class BatchOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        OrderActionRef: int = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        StatusMsg: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        批量报单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OrderActionRef: 报单操作引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param StatusMsg: 状态信息
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ExchangeBatchOrderAction(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        交易所批量报单操作
        :param ExchangeID: 交易所代码
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryBatchOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExchangeID: str = None,
    ):
        """
        查询批量报单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class CombInstrumentGuard(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InstrumentID: str = None,
        GuarantRatio: float = None,
        ExchangeID: str = None,
    ):
        """
        组合合约安全系数
        :param BrokerID: 经纪公司代码
        :param InstrumentID: 合约代码
        :param GuarantRatio: 合约代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class QryCombInstrumentGuard(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
    ):
        """
        组合合约安全系数查询
        :param BrokerID: 经纪公司代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class InputCombAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        CombActionRef: str = None,
        UserID: str = None,
        Direction: bytes = None,
        Volume: int = None,
        CombDirection: bytes = None,
        HedgeFlag: bytes = None,
        ExchangeID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
        InvestUnitID: str = None,
    ):
        """
        输入的申请组合
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param CombActionRef: 组合引用
        :param UserID: 用户代码
        :param Direction: 买卖方向
        :param Volume: 数量
        :param CombDirection: 组合指令方向
        :param HedgeFlag: 投机套保标志
        :param ExchangeID: 交易所代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class CombAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        CombActionRef: str = None,
        UserID: str = None,
        Direction: bytes = None,
        Volume: int = None,
        CombDirection: bytes = None,
        HedgeFlag: bytes = None,
        ActionLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        ActionStatus: bytes = None,
        NotifySequence: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        SequenceNo: int = None,
        FrontID: int = None,
        SessionID: int = None,
        UserProductInfo: str = None,
        StatusMsg: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
        ComTradeID: str = None,
        BranchID: str = None,
        InvestUnitID: str = None,
    ):
        """
        申请组合
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param CombActionRef: 组合引用
        :param UserID: 用户代码
        :param Direction: 买卖方向
        :param Volume: 数量
        :param CombDirection: 组合指令方向
        :param HedgeFlag: 投机套保标志
        :param ActionLocalID: 本地申请组合编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param ActionStatus: 组合状态
        :param NotifySequence: 报单提示序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param SequenceNo: 序号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param UserProductInfo: 用户端产品信息
        :param StatusMsg: 状态信息
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        :param ComTradeID: 组合编号
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryCombAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        申请组合查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class ExchangeCombAction(Struct):
    def __init__(
        self,
        Direction: bytes = None,
        Volume: int = None,
        CombDirection: bytes = None,
        HedgeFlag: bytes = None,
        ActionLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        ActionStatus: bytes = None,
        NotifySequence: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        SequenceNo: int = None,
        IPAddress: str = None,
        MacAddress: str = None,
        ComTradeID: str = None,
        BranchID: str = None,
    ):
        """
        交易所申请组合信息
        :param Direction: 买卖方向
        :param Volume: 数量
        :param CombDirection: 组合指令方向
        :param HedgeFlag: 投机套保标志
        :param ActionLocalID: 本地申请组合编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param ActionStatus: 组合状态
        :param NotifySequence: 报单提示序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param SequenceNo: 序号
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        :param ComTradeID: 组合编号
        :param BranchID: 营业部编号
        """
        super().__init__()
        ...


class QryExchangeCombAction(Struct):
    def __init__(
        self,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        ExchangeID: str = None,
        TraderID: str = None,
    ):
        """
        交易所申请组合查询
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class ProductExchRate(Struct):
    def __init__(
        self,
        ProductID: str = None,
        QuoteCurrencyID: str = None,
        ExchangeRate: float = None,
        ExchangeID: str = None,
    ):
        """
        产品报价汇率
        :param ProductID: 产品代码
        :param QuoteCurrencyID: 报价币种类型
        :param ExchangeRate: 汇率
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class QryProductExchRate(Struct):
    def __init__(
        self,
        ProductID: str = None,
        ExchangeID: str = None,
    ):
        """
        产品报价汇率查询
        :param ProductID: 产品代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class QryForQuoteParam(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
    ):
        """
        查询询价价差参数
        :param BrokerID: 经纪公司代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class ForQuoteParam(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        LastPrice: float = None,
        PriceInterval: float = None,
    ):
        """
        询价价差参数
        :param BrokerID: 经纪公司代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param LastPrice: 最新价
        :param PriceInterval: 价差
        """
        super().__init__()
        ...


class MMOptionInstrCommRate(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        OpenRatioByMoney: float = None,
        OpenRatioByVolume: float = None,
        CloseRatioByMoney: float = None,
        CloseRatioByVolume: float = None,
        CloseTodayRatioByMoney: float = None,
        CloseTodayRatioByVolume: float = None,
        StrikeRatioByMoney: float = None,
        StrikeRatioByVolume: float = None,
    ):
        """
        当前做市商期权合约手续费的详细内容
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OpenRatioByMoney: 开仓手续费率
        :param OpenRatioByVolume: 开仓手续费
        :param CloseRatioByMoney: 平仓手续费率
        :param CloseRatioByVolume: 平仓手续费
        :param CloseTodayRatioByMoney: 平今手续费率
        :param CloseTodayRatioByVolume: 平今手续费
        :param StrikeRatioByMoney: 执行手续费率
        :param StrikeRatioByVolume: 执行手续费
        """
        super().__init__()
        ...


class QryMMOptionInstrCommRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
    ):
        """
        做市商期权手续费率查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        """
        super().__init__()
        ...


class MMInstrumentCommissionRate(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        OpenRatioByMoney: float = None,
        OpenRatioByVolume: float = None,
        CloseRatioByMoney: float = None,
        CloseRatioByVolume: float = None,
        CloseTodayRatioByMoney: float = None,
        CloseTodayRatioByVolume: float = None,
    ):
        """
        做市商合约手续费率
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OpenRatioByMoney: 开仓手续费率
        :param OpenRatioByVolume: 开仓手续费
        :param CloseRatioByMoney: 平仓手续费率
        :param CloseRatioByVolume: 平仓手续费
        :param CloseTodayRatioByMoney: 平今手续费率
        :param CloseTodayRatioByVolume: 平今手续费
        """
        super().__init__()
        ...


class QryMMInstrumentCommissionRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
    ):
        """
        查询做市商合约手续费率
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        """
        super().__init__()
        ...


class InstrumentOrderCommRate(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        HedgeFlag: bytes = None,
        OrderCommByVolume: float = None,
        OrderActionCommByVolume: float = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        当前报单手续费的详细内容
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param HedgeFlag: 投机套保标志
        :param OrderCommByVolume: 报单手续费
        :param OrderActionCommByVolume: 撤单手续费
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryInstrumentOrderCommRate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
    ):
        """
        报单手续费率查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        """
        super().__init__()
        ...


class TradeParam(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        TradeParamID: bytes = None,
        TradeParamValue: str = None,
        Memo: str = None,
    ):
        """
        交易参数
        :param BrokerID: 经纪公司代码
        :param TradeParamID: 参数代码
        :param TradeParamValue: 参数代码值
        :param Memo: 备注
        """
        super().__init__()
        ...


class InstrumentMarginRateUL(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        HedgeFlag: bytes = None,
        LongMarginRatioByMoney: float = None,
        LongMarginRatioByVolume: float = None,
        ShortMarginRatioByMoney: float = None,
        ShortMarginRatioByVolume: float = None,
    ):
        """
        合约保证金率调整
        :param InstrumentID: 合约代码
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param HedgeFlag: 投机套保标志
        :param LongMarginRatioByMoney: 多头保证金率
        :param LongMarginRatioByVolume: 多头保证金费
        :param ShortMarginRatioByMoney: 空头保证金率
        :param ShortMarginRatioByVolume: 空头保证金费
        """
        super().__init__()
        ...


class FutureLimitPosiParam(Struct):
    def __init__(
        self,
        InvestorRange: bytes = None,
        BrokerID: str = None,
        InvestorID: str = None,
        ProductID: str = None,
        SpecOpenVolume: int = None,
        ArbiOpenVolume: int = None,
        OpenVolume: int = None,
    ):
        """
        期货持仓限制参数
        :param InvestorRange: 投资者范围
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ProductID: 产品代码
        :param SpecOpenVolume: 当日投机开仓数量限制
        :param ArbiOpenVolume: 当日套利开仓数量限制
        :param OpenVolume: 当日投机+套利开仓数量限制
        """
        super().__init__()
        ...


class LoginForbiddenIP(Struct):
    def __init__(
        self,
        IPAddress: str = None,
    ):
        """
        禁止登录IP
        :param IPAddress: IP地址
        """
        super().__init__()
        ...


class IPList(Struct):
    def __init__(
        self,
        IPAddress: str = None,
        IsWhite: int = None,
    ):
        """
        IP列表
        :param IPAddress: IP地址
        :param IsWhite: 是否白名单
        """
        super().__init__()
        ...


class InputOptionSelfClose(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        OptionSelfCloseRef: str = None,
        UserID: str = None,
        Volume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        HedgeFlag: bytes = None,
        OptSelfCloseFlag: bytes = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        ClientID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入的期权自对冲
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param OptionSelfCloseRef: 期权自对冲引用
        :param UserID: 用户代码
        :param Volume: 数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param HedgeFlag: 投机套保标志
        :param OptSelfCloseFlag: 期权行权的头寸是否自对冲
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param ClientID: 交易编码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class InputOptionSelfCloseAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        OptionSelfCloseActionRef: int = None,
        OptionSelfCloseRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        OptionSelfCloseSysID: str = None,
        ActionFlag: bytes = None,
        UserID: str = None,
        InstrumentID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入期权自对冲操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OptionSelfCloseActionRef: 期权自对冲操作引用
        :param OptionSelfCloseRef: 期权自对冲引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param OptionSelfCloseSysID: 期权自对冲操作编号
        :param ActionFlag: 操作标志
        :param UserID: 用户代码
        :param InstrumentID: 合约代码
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class OptionSelfClose(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        OptionSelfCloseRef: str = None,
        UserID: str = None,
        Volume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        HedgeFlag: bytes = None,
        OptSelfCloseFlag: bytes = None,
        OptionSelfCloseLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderSubmitStatus: bytes = None,
        NotifySequence: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        OptionSelfCloseSysID: str = None,
        InsertDate: str = None,
        InsertTime: str = None,
        CancelTime: str = None,
        ExecResult: bytes = None,
        ClearingPartID: str = None,
        SequenceNo: int = None,
        FrontID: int = None,
        SessionID: int = None,
        UserProductInfo: str = None,
        StatusMsg: str = None,
        ActiveUserID: str = None,
        BrokerOptionSelfCloseSeq: int = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        期权自对冲
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param OptionSelfCloseRef: 期权自对冲引用
        :param UserID: 用户代码
        :param Volume: 数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param HedgeFlag: 投机套保标志
        :param OptSelfCloseFlag: 期权行权的头寸是否自对冲
        :param OptionSelfCloseLocalID: 本地期权自对冲编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderSubmitStatus: 期权自对冲提交状态
        :param NotifySequence: 报单提示序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param OptionSelfCloseSysID: 期权自对冲编号
        :param InsertDate: 报单日期
        :param InsertTime: 插入时间
        :param CancelTime: 撤销时间
        :param ExecResult: 自对冲结果
        :param ClearingPartID: 结算会员编号
        :param SequenceNo: 序号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param UserProductInfo: 用户端产品信息
        :param StatusMsg: 状态信息
        :param ActiveUserID: 操作用户代码
        :param BrokerOptionSelfCloseSeq: 经纪公司报单编号
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class OptionSelfCloseAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        OptionSelfCloseActionRef: int = None,
        OptionSelfCloseRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        OptionSelfCloseSysID: str = None,
        ActionFlag: bytes = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OptionSelfCloseLocalID: str = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        StatusMsg: str = None,
        InstrumentID: str = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        期权自对冲操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OptionSelfCloseActionRef: 期权自对冲操作引用
        :param OptionSelfCloseRef: 期权自对冲引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param OptionSelfCloseSysID: 期权自对冲操作编号
        :param ActionFlag: 操作标志
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OptionSelfCloseLocalID: 本地期权自对冲编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param StatusMsg: 状态信息
        :param InstrumentID: 合约代码
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryOptionSelfClose(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        OptionSelfCloseSysID: str = None,
        InsertTimeStart: str = None,
        InsertTimeEnd: str = None,
    ):
        """
        期权自对冲查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param OptionSelfCloseSysID: 期权自对冲编号
        :param InsertTimeStart: 开始时间
        :param InsertTimeEnd: 结束时间
        """
        super().__init__()
        ...


class ExchangeOptionSelfClose(Struct):
    def __init__(
        self,
        Volume: int = None,
        RequestID: int = None,
        BusinessUnit: str = None,
        HedgeFlag: bytes = None,
        OptSelfCloseFlag: bytes = None,
        OptionSelfCloseLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderSubmitStatus: bytes = None,
        NotifySequence: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        OptionSelfCloseSysID: str = None,
        InsertDate: str = None,
        InsertTime: str = None,
        CancelTime: str = None,
        ExecResult: bytes = None,
        ClearingPartID: str = None,
        SequenceNo: int = None,
        BranchID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        交易所期权自对冲信息
        :param Volume: 数量
        :param RequestID: 请求编号
        :param BusinessUnit: 业务单元
        :param HedgeFlag: 投机套保标志
        :param OptSelfCloseFlag: 期权行权的头寸是否自对冲
        :param OptionSelfCloseLocalID: 本地期权自对冲编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderSubmitStatus: 期权自对冲提交状态
        :param NotifySequence: 报单提示序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param OptionSelfCloseSysID: 期权自对冲编号
        :param InsertDate: 报单日期
        :param InsertTime: 插入时间
        :param CancelTime: 撤销时间
        :param ExecResult: 自对冲结果
        :param ClearingPartID: 结算会员编号
        :param SequenceNo: 序号
        :param BranchID: 营业部编号
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryOptionSelfCloseAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExchangeID: str = None,
    ):
        """
        期权自对冲操作查询
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class ExchangeOptionSelfCloseAction(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        OptionSelfCloseSysID: str = None,
        ActionFlag: bytes = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OptionSelfCloseLocalID: str = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        BranchID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
        ExchangeInstID: str = None,
        OptSelfCloseFlag: bytes = None,
    ):
        """
        交易所期权自对冲操作
        :param ExchangeID: 交易所代码
        :param OptionSelfCloseSysID: 期权自对冲操作编号
        :param ActionFlag: 操作标志
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OptionSelfCloseLocalID: 本地期权自对冲编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param BranchID: 营业部编号
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        :param ExchangeInstID: 合约在交易所的代码
        :param OptSelfCloseFlag: 期权行权的头寸是否自对冲
        """
        super().__init__()
        ...


class SyncDelaySwap(Struct):
    def __init__(
        self,
        DelaySwapSeqNo: str = None,
        BrokerID: str = None,
        InvestorID: str = None,
        FromCurrencyID: str = None,
        FromAmount: float = None,
        FromFrozenSwap: float = None,
        FromRemainSwap: float = None,
        ToCurrencyID: str = None,
        ToAmount: float = None,
    ):
        """
        延时换汇同步
        :param DelaySwapSeqNo: 换汇流水号
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param FromCurrencyID: 源币种
        :param FromAmount: 源金额
        :param FromFrozenSwap: 源换汇冻结金额(可用冻结)
        :param FromRemainSwap: 源剩余换汇额度(可提冻结)
        :param ToCurrencyID: 目标币种
        :param ToAmount: 目标金额
        """
        super().__init__()
        ...


class QrySyncDelaySwap(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        DelaySwapSeqNo: str = None,
    ):
        """
        查询延时换汇同步
        :param BrokerID: 经纪公司代码
        :param DelaySwapSeqNo: 延时换汇流水号
        """
        super().__init__()
        ...


class InvestUnit(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InvestUnitID: str = None,
        InvestorUnitName: str = None,
        InvestorGroupID: str = None,
        CommModelID: str = None,
        MarginModelID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
    ):
        """
        投资单元
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InvestUnitID: 投资单元代码
        :param InvestorUnitName: 投资者单元名称
        :param InvestorGroupID: 投资者分组代码
        :param CommModelID: 手续费率模板代码
        :param MarginModelID: 保证金率模板代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class QryInvestUnit(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询投资单元
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class SecAgentCheckMode(Struct):
    def __init__(
        self,
        InvestorID: str = None,
        BrokerID: str = None,
        CurrencyID: str = None,
        BrokerSecAgentID: str = None,
        CheckSelfAccount: int = None,
    ):
        """
        二级代理商资金校验模式
        :param InvestorID: 投资者代码
        :param BrokerID: 经纪公司代码
        :param CurrencyID: 币种
        :param BrokerSecAgentID: 境外中介机构资金帐号
        :param CheckSelfAccount: 是否需要校验自己的资金账户
        """
        super().__init__()
        ...


class SecAgentTradeInfo(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        BrokerSecAgentID: str = None,
        InvestorID: str = None,
        LongCustomerName: str = None,
    ):
        """
        二级代理商信息
        :param BrokerID: 经纪公司代码
        :param BrokerSecAgentID: 境外中介机构资金帐号
        :param InvestorID: 投资者代码
        :param LongCustomerName: 二级代理商姓名
        """
        super().__init__()
        ...


class MarketData(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        ExchangeInstID: str = None,
        LastPrice: float = None,
        PreSettlementPrice: float = None,
        PreClosePrice: float = None,
        PreOpenInterest: float = None,
        OpenPrice: float = None,
        HighestPrice: float = None,
        LowestPrice: float = None,
        Volume: int = None,
        Turnover: float = None,
        OpenInterest: float = None,
        ClosePrice: float = None,
        SettlementPrice: float = None,
        UpperLimitPrice: float = None,
        LowerLimitPrice: float = None,
        PreDelta: float = None,
        CurrDelta: float = None,
        UpdateTime: str = None,
        UpdateMillisec: int = None,
        ActionDay: str = None,
    ):
        """
        市场行情
        :param TradingDay: 交易日
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param ExchangeInstID: 合约在交易所的代码
        :param LastPrice: 最新价
        :param PreSettlementPrice: 上次结算价
        :param PreClosePrice: 昨收盘
        :param PreOpenInterest: 昨持仓量
        :param OpenPrice: 今开盘
        :param HighestPrice: 最高价
        :param LowestPrice: 最低价
        :param Volume: 数量
        :param Turnover: 成交金额
        :param OpenInterest: 持仓量
        :param ClosePrice: 今收盘
        :param SettlementPrice: 本次结算价
        :param UpperLimitPrice: 涨停板价
        :param LowerLimitPrice: 跌停板价
        :param PreDelta: 昨虚实度
        :param CurrDelta: 今虚实度
        :param UpdateTime: 最后修改时间
        :param UpdateMillisec: 最后修改毫秒
        :param ActionDay: 业务日期
        """
        super().__init__()
        ...


class MarketDataBase(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        PreSettlementPrice: float = None,
        PreClosePrice: float = None,
        PreOpenInterest: float = None,
        PreDelta: float = None,
    ):
        """
        行情基础属性
        :param TradingDay: 交易日
        :param PreSettlementPrice: 上次结算价
        :param PreClosePrice: 昨收盘
        :param PreOpenInterest: 昨持仓量
        :param PreDelta: 昨虚实度
        """
        super().__init__()
        ...


class MarketDataStatic(Struct):
    def __init__(
        self,
        OpenPrice: float = None,
        HighestPrice: float = None,
        LowestPrice: float = None,
        ClosePrice: float = None,
        UpperLimitPrice: float = None,
        LowerLimitPrice: float = None,
        SettlementPrice: float = None,
        CurrDelta: float = None,
    ):
        """
        行情静态属性
        :param OpenPrice: 今开盘
        :param HighestPrice: 最高价
        :param LowestPrice: 最低价
        :param ClosePrice: 今收盘
        :param UpperLimitPrice: 涨停板价
        :param LowerLimitPrice: 跌停板价
        :param SettlementPrice: 本次结算价
        :param CurrDelta: 今虚实度
        """
        super().__init__()
        ...


class MarketDataLastMatch(Struct):
    def __init__(
        self,
        LastPrice: float = None,
        Volume: int = None,
        Turnover: float = None,
        OpenInterest: float = None,
    ):
        """
        行情最新成交属性
        :param LastPrice: 最新价
        :param Volume: 数量
        :param Turnover: 成交金额
        :param OpenInterest: 持仓量
        """
        super().__init__()
        ...


class MarketDataBestPrice(Struct):
    def __init__(
        self,
        BidPrice1: float = None,
        BidVolume1: int = None,
        AskPrice1: float = None,
        AskVolume1: int = None,
    ):
        """
        行情最优价属性
        :param BidPrice1: 申买价一
        :param BidVolume1: 申买量一
        :param AskPrice1: 申卖价一
        :param AskVolume1: 申卖量一
        """
        super().__init__()
        ...


class MarketDataBid23(Struct):
    def __init__(
        self,
        BidPrice2: float = None,
        BidVolume2: int = None,
        BidPrice3: float = None,
        BidVolume3: int = None,
    ):
        """
        行情申买二、三属性
        :param BidPrice2: 申买价二
        :param BidVolume2: 申买量二
        :param BidPrice3: 申买价三
        :param BidVolume3: 申买量三
        """
        super().__init__()
        ...


class MarketDataAsk23(Struct):
    def __init__(
        self,
        AskPrice2: float = None,
        AskVolume2: int = None,
        AskPrice3: float = None,
        AskVolume3: int = None,
    ):
        """
        行情申卖二、三属性
        :param AskPrice2: 申卖价二
        :param AskVolume2: 申卖量二
        :param AskPrice3: 申卖价三
        :param AskVolume3: 申卖量三
        """
        super().__init__()
        ...


class MarketDataBid45(Struct):
    def __init__(
        self,
        BidPrice4: float = None,
        BidVolume4: int = None,
        BidPrice5: float = None,
        BidVolume5: int = None,
    ):
        """
        行情申买四、五属性
        :param BidPrice4: 申买价四
        :param BidVolume4: 申买量四
        :param BidPrice5: 申买价五
        :param BidVolume5: 申买量五
        """
        super().__init__()
        ...


class MarketDataAsk45(Struct):
    def __init__(
        self,
        AskPrice4: float = None,
        AskVolume4: int = None,
        AskPrice5: float = None,
        AskVolume5: int = None,
    ):
        """
        行情申卖四、五属性
        :param AskPrice4: 申卖价四
        :param AskVolume4: 申卖量四
        :param AskPrice5: 申卖价五
        :param AskVolume5: 申卖量五
        """
        super().__init__()
        ...


class MarketDataUpdateTime(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        UpdateTime: str = None,
        UpdateMillisec: int = None,
        ActionDay: str = None,
    ):
        """
        行情更新时间属性
        :param InstrumentID: 合约代码
        :param UpdateTime: 最后修改时间
        :param UpdateMillisec: 最后修改毫秒
        :param ActionDay: 业务日期
        """
        super().__init__()
        ...


class MarketDataExchange(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
    ):
        """
        行情交易所代码属性
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class SpecificInstrument(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
    ):
        """
        指定的合约
        :param InstrumentID: 合约代码
        """
        super().__init__()
        ...


class InstrumentStatus(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        ExchangeInstID: str = None,
        SettlementGroupID: str = None,
        InstrumentID: str = None,
        InstrumentStatus: bytes = None,
        TradingSegmentSN: int = None,
        EnterTime: str = None,
        EnterReason: bytes = None,
    ):
        """
        合约状态
        :param ExchangeID: 交易所代码
        :param ExchangeInstID: 合约在交易所的代码
        :param SettlementGroupID: 结算组代码
        :param InstrumentID: 合约代码
        :param InstrumentStatus: 合约交易状态
        :param TradingSegmentSN: 交易阶段编号
        :param EnterTime: 进入本状态时间
        :param EnterReason: 进入本状态原因
        """
        super().__init__()
        ...


class QryInstrumentStatus(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        ExchangeInstID: str = None,
    ):
        """
        查询合约状态
        :param ExchangeID: 交易所代码
        :param ExchangeInstID: 合约在交易所的代码
        """
        super().__init__()
        ...


class InvestorAccount(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
    ):
        """
        投资者账户
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param AccountID: 投资者帐号
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class PositionProfitAlgorithm(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        AccountID: str = None,
        Algorithm: bytes = None,
        Memo: str = None,
        CurrencyID: str = None,
    ):
        """
        浮动盈亏算法
        :param BrokerID: 经纪公司代码
        :param AccountID: 投资者帐号
        :param Algorithm: 盈亏算法
        :param Memo: 备注
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class Discount(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorRange: bytes = None,
        InvestorID: str = None,
        Discount: float = None,
    ):
        """
        会员资金折扣
        :param BrokerID: 经纪公司代码
        :param InvestorRange: 投资者范围
        :param InvestorID: 投资者代码
        :param Discount: 资金折扣比例
        """
        super().__init__()
        ...


class QryTransferBank(Struct):
    def __init__(
        self,
        BankID: str = None,
        BankBrchID: str = None,
    ):
        """
        查询转帐银行
        :param BankID: 银行代码
        :param BankBrchID: 银行分中心代码
        """
        super().__init__()
        ...


class TransferBank(Struct):
    def __init__(
        self,
        BankID: str = None,
        BankBrchID: str = None,
        BankName: str = None,
        IsActive: int = None,
    ):
        """
        转帐银行
        :param BankID: 银行代码
        :param BankBrchID: 银行分中心代码
        :param BankName: 银行名称
        :param IsActive: 是否活跃
        """
        super().__init__()
        ...


class QryInvestorPositionDetail(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询投资者持仓明细
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class InvestorPositionDetail(Struct):
    def __init__(
        self,
        InstrumentID: str = None,
        BrokerID: str = None,
        InvestorID: str = None,
        HedgeFlag: bytes = None,
        Direction: bytes = None,
        OpenDate: str = None,
        TradeID: str = None,
        Volume: int = None,
        OpenPrice: float = None,
        TradingDay: str = None,
        SettlementID: int = None,
        TradeType: bytes = None,
        CombInstrumentID: str = None,
        ExchangeID: str = None,
        CloseProfitByDate: float = None,
        CloseProfitByTrade: float = None,
        PositionProfitByDate: float = None,
        PositionProfitByTrade: float = None,
        Margin: float = None,
        ExchMargin: float = None,
        MarginRateByMoney: float = None,
        MarginRateByVolume: float = None,
        LastSettlementPrice: float = None,
        SettlementPrice: float = None,
        CloseVolume: int = None,
        CloseAmount: float = None,
        TimeFirstVolume: int = None,
        InvestUnitID: str = None,
    ):
        """
        投资者持仓明细
        :param InstrumentID: 合约代码
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param HedgeFlag: 投机套保标志
        :param Direction: 买卖
        :param OpenDate: 开仓日期
        :param TradeID: 成交编号
        :param Volume: 数量
        :param OpenPrice: 开仓价
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param TradeType: 成交类型
        :param CombInstrumentID: 组合合约代码
        :param ExchangeID: 交易所代码
        :param CloseProfitByDate: 逐日盯市平仓盈亏
        :param CloseProfitByTrade: 逐笔对冲平仓盈亏
        :param PositionProfitByDate: 逐日盯市持仓盈亏
        :param PositionProfitByTrade: 逐笔对冲持仓盈亏
        :param Margin: 投资者保证金
        :param ExchMargin: 交易所保证金
        :param MarginRateByMoney: 保证金率
        :param MarginRateByVolume: 保证金率(按手数)
        :param LastSettlementPrice: 昨结算价
        :param SettlementPrice: 结算价
        :param CloseVolume: 平仓量
        :param CloseAmount: 平仓金额
        :param TimeFirstVolume: 按照时间顺序平仓的笔数,大商所专用
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class TradingAccountPassword(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        AccountID: str = None,
        Password: str = None,
        CurrencyID: str = None,
    ):
        """
        资金账户口令域
        :param BrokerID: 经纪公司代码
        :param AccountID: 投资者帐号
        :param Password: 密码
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class MDTraderOffer(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        TraderID: str = None,
        ParticipantID: str = None,
        Password: str = None,
        InstallID: int = None,
        OrderLocalID: str = None,
        TraderConnectStatus: bytes = None,
        ConnectRequestDate: str = None,
        ConnectRequestTime: str = None,
        LastReportDate: str = None,
        LastReportTime: str = None,
        ConnectDate: str = None,
        ConnectTime: str = None,
        StartDate: str = None,
        StartTime: str = None,
        TradingDay: str = None,
        BrokerID: str = None,
        MaxTradeID: str = None,
        MaxOrderMessageReference: str = None,
    ):
        """
        交易所行情报盘机
        :param ExchangeID: 交易所代码
        :param TraderID: 交易所交易员代码
        :param ParticipantID: 会员代码
        :param Password: 密码
        :param InstallID: 安装编号
        :param OrderLocalID: 本地报单编号
        :param TraderConnectStatus: 交易所交易员连接状态
        :param ConnectRequestDate: 发出连接请求的日期
        :param ConnectRequestTime: 发出连接请求的时间
        :param LastReportDate: 上次报告日期
        :param LastReportTime: 上次报告时间
        :param ConnectDate: 完成连接日期
        :param ConnectTime: 完成连接时间
        :param StartDate: 启动日期
        :param StartTime: 启动时间
        :param TradingDay: 交易日
        :param BrokerID: 经纪公司代码
        :param MaxTradeID: 本席位最大成交编号
        :param MaxOrderMessageReference: 本席位最大报单备拷
        """
        super().__init__()
        ...


class QryMDTraderOffer(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        ParticipantID: str = None,
        TraderID: str = None,
    ):
        """
        查询行情报盘机
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param TraderID: 交易所交易员代码
        """
        super().__init__()
        ...


class QryNotice(Struct):
    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        查询客户通知
        :param BrokerID: 经纪公司代码
        """
        super().__init__()
        ...


class Notice(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        Content: str = None,
        SequenceLabel: str = None,
    ):
        """
        客户通知
        :param BrokerID: 经纪公司代码
        :param Content: 消息正文
        :param SequenceLabel: 经纪公司通知内容序列号
        """
        super().__init__()
        ...


class UserRight(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        UserRightType: bytes = None,
        IsForbidden: int = None,
    ):
        """
        用户权限
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param UserRightType: 客户权限类型
        :param IsForbidden: 是否禁止
        """
        super().__init__()
        ...


class QrySettlementInfoConfirm(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
    ):
        """
        查询结算信息确认域
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param AccountID: 投资者帐号
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class LoadSettlementInfo(Struct):
    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        装载结算信息
        :param BrokerID: 经纪公司代码
        """
        super().__init__()
        ...


class BrokerWithdrawAlgorithm(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        WithdrawAlgorithm: bytes = None,
        UsingRatio: float = None,
        IncludeCloseProfit: bytes = None,
        AllWithoutTrade: bytes = None,
        AvailIncludeCloseProfit: bytes = None,
        IsBrokerUserEvent: int = None,
        CurrencyID: str = None,
        FundMortgageRatio: float = None,
        BalanceAlgorithm: bytes = None,
    ):
        """
        经纪公司可提资金算法表
        :param BrokerID: 经纪公司代码
        :param WithdrawAlgorithm: 可提资金算法
        :param UsingRatio: 资金使用率
        :param IncludeCloseProfit: 可提是否包含平仓盈利
        :param AllWithoutTrade: 本日无仓且无成交客户是否受可提比例限制
        :param AvailIncludeCloseProfit: 可用是否包含平仓盈利
        :param IsBrokerUserEvent: 是否启用用户事件
        :param CurrencyID: 币种代码
        :param FundMortgageRatio: 货币质押比率
        :param BalanceAlgorithm: 权益算法
        """
        super().__init__()
        ...


class TradingAccountPasswordUpdateV1(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        OldPassword: str = None,
        NewPassword: str = None,
    ):
        """
        资金账户口令变更域
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OldPassword: 原来的口令
        :param NewPassword: 新的口令
        """
        super().__init__()
        ...


class TradingAccountPasswordUpdate(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        AccountID: str = None,
        OldPassword: str = None,
        NewPassword: str = None,
        CurrencyID: str = None,
    ):
        """
        资金账户口令变更域
        :param BrokerID: 经纪公司代码
        :param AccountID: 投资者帐号
        :param OldPassword: 原来的口令
        :param NewPassword: 新的口令
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class QryCombinationLeg(Struct):
    def __init__(
        self,
        CombInstrumentID: str = None,
        LegID: int = None,
        LegInstrumentID: str = None,
    ):
        """
        查询组合合约分腿
        :param CombInstrumentID: 组合合约代码
        :param LegID: 单腿编号
        :param LegInstrumentID: 单腿合约代码
        """
        super().__init__()
        ...


class QrySyncStatus(Struct):
    def __init__(
        self,
        TradingDay: str = None,
    ):
        """
        查询组合合约分腿
        :param TradingDay: 交易日
        """
        super().__init__()
        ...


class CombinationLeg(Struct):
    def __init__(
        self,
        CombInstrumentID: str = None,
        LegID: int = None,
        LegInstrumentID: str = None,
        Direction: bytes = None,
        LegMultiple: int = None,
        ImplyLevel: int = None,
    ):
        """
        组合交易合约的单腿
        :param CombInstrumentID: 组合合约代码
        :param LegID: 单腿编号
        :param LegInstrumentID: 单腿合约代码
        :param Direction: 买卖方向
        :param LegMultiple: 单腿乘数
        :param ImplyLevel: 派生层数
        """
        super().__init__()
        ...


class SyncStatus(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        DataSyncStatus: bytes = None,
    ):
        """
        数据同步状态
        :param TradingDay: 交易日
        :param DataSyncStatus: 数据同步状态
        """
        super().__init__()
        ...


class QryLinkMan(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
    ):
        """
        查询联系人
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        """
        super().__init__()
        ...


class LinkMan(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        PersonType: bytes = None,
        IdentifiedCardType: bytes = None,
        IdentifiedCardNo: str = None,
        PersonName: str = None,
        Telephone: str = None,
        Address: str = None,
        ZipCode: str = None,
        Priority: int = None,
        UOAZipCode: str = None,
        PersonFullName: str = None,
    ):
        """
        联系人
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param PersonType: 联系人类型
        :param IdentifiedCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param PersonName: 名称
        :param Telephone: 联系电话
        :param Address: 通讯地址
        :param ZipCode: 邮政编码
        :param Priority: 优先级
        :param UOAZipCode: 开户邮政编码
        :param PersonFullName: 全称
        """
        super().__init__()
        ...


class QryBrokerUserEvent(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        UserEventType: bytes = None,
    ):
        """
        查询经纪公司用户事件
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param UserEventType: 用户事件类型
        """
        super().__init__()
        ...


class BrokerUserEvent(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        UserEventType: bytes = None,
        EventSequenceNo: int = None,
        EventDate: str = None,
        EventTime: str = None,
        UserEventInfo: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
    ):
        """
        查询经纪公司用户事件
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param UserEventType: 用户事件类型
        :param EventSequenceNo: 用户事件序号
        :param EventDate: 事件发生日期
        :param EventTime: 事件发生时间
        :param UserEventInfo: 用户事件信息
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        """
        super().__init__()
        ...


class QryContractBank(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        BankID: str = None,
        BankBrchID: str = None,
    ):
        """
        查询签约银行请求
        :param BrokerID: 经纪公司代码
        :param BankID: 银行代码
        :param BankBrchID: 银行分中心代码
        """
        super().__init__()
        ...


class ContractBank(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        BankID: str = None,
        BankBrchID: str = None,
        BankName: str = None,
    ):
        """
        查询签约银行响应
        :param BrokerID: 经纪公司代码
        :param BankID: 银行代码
        :param BankBrchID: 银行分中心代码
        :param BankName: 银行名称
        """
        super().__init__()
        ...


class InvestorPositionCombineDetail(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        OpenDate: str = None,
        ExchangeID: str = None,
        SettlementID: int = None,
        BrokerID: str = None,
        InvestorID: str = None,
        ComTradeID: str = None,
        TradeID: str = None,
        InstrumentID: str = None,
        HedgeFlag: bytes = None,
        Direction: bytes = None,
        TotalAmt: int = None,
        Margin: float = None,
        ExchMargin: float = None,
        MarginRateByMoney: float = None,
        MarginRateByVolume: float = None,
        LegID: int = None,
        LegMultiple: int = None,
        CombInstrumentID: str = None,
        TradeGroupID: int = None,
        InvestUnitID: str = None,
    ):
        """
        投资者组合持仓明细
        :param TradingDay: 交易日
        :param OpenDate: 开仓日期
        :param ExchangeID: 交易所代码
        :param SettlementID: 结算编号
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ComTradeID: 组合编号
        :param TradeID: 撮合编号
        :param InstrumentID: 合约代码
        :param HedgeFlag: 投机套保标志
        :param Direction: 买卖
        :param TotalAmt: 持仓量
        :param Margin: 投资者保证金
        :param ExchMargin: 交易所保证金
        :param MarginRateByMoney: 保证金率
        :param MarginRateByVolume: 保证金率(按手数)
        :param LegID: 单腿编号
        :param LegMultiple: 单腿乘数
        :param CombInstrumentID: 组合持仓合约编码
        :param TradeGroupID: 成交组号
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class ParkedOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        OrderRef: str = None,
        UserID: str = None,
        OrderPriceType: bytes = None,
        Direction: bytes = None,
        CombOffsetFlag: str = None,
        CombHedgeFlag: str = None,
        LimitPrice: float = None,
        VolumeTotalOriginal: int = None,
        TimeCondition: bytes = None,
        GTDDate: str = None,
        VolumeCondition: bytes = None,
        MinVolume: int = None,
        ContingentCondition: bytes = None,
        StopPrice: float = None,
        ForceCloseReason: bytes = None,
        IsAutoSuspend: int = None,
        BusinessUnit: str = None,
        RequestID: int = None,
        UserForceClose: int = None,
        ExchangeID: str = None,
        ParkedOrderID: str = None,
        UserType: bytes = None,
        Status: bytes = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        IsSwapOrder: int = None,
        AccountID: str = None,
        CurrencyID: str = None,
        ClientID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        预埋单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param OrderRef: 报单引用
        :param UserID: 用户代码
        :param OrderPriceType: 报单价格条件
        :param Direction: 买卖方向
        :param CombOffsetFlag: 组合开平标志
        :param CombHedgeFlag: 组合投机套保标志
        :param LimitPrice: 价格
        :param VolumeTotalOriginal: 数量
        :param TimeCondition: 有效期类型
        :param GTDDate: GTD日期
        :param VolumeCondition: 成交量类型
        :param MinVolume: 最小成交量
        :param ContingentCondition: 触发条件
        :param StopPrice: 止损价
        :param ForceCloseReason: 强平原因
        :param IsAutoSuspend: 自动挂起标志
        :param BusinessUnit: 业务单元
        :param RequestID: 请求编号
        :param UserForceClose: 用户强评标志
        :param ExchangeID: 交易所代码
        :param ParkedOrderID: 预埋报单编号
        :param UserType: 用户类型
        :param Status: 预埋单状态
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param IsSwapOrder: 互换单标志
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param ClientID: 交易编码
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ParkedOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        OrderActionRef: int = None,
        OrderRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        OrderSysID: str = None,
        ActionFlag: bytes = None,
        LimitPrice: float = None,
        VolumeChange: int = None,
        UserID: str = None,
        InstrumentID: str = None,
        ParkedOrderActionID: str = None,
        UserType: bytes = None,
        Status: bytes = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        输入预埋单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OrderActionRef: 报单操作引用
        :param OrderRef: 报单引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param OrderSysID: 报单编号
        :param ActionFlag: 操作标志
        :param LimitPrice: 价格
        :param VolumeChange: 数量变化
        :param UserID: 用户代码
        :param InstrumentID: 合约代码
        :param ParkedOrderActionID: 预埋撤单单编号
        :param UserType: 用户类型
        :param Status: 预埋撤单状态
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryParkedOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询预埋单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryParkedOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询预埋撤单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class RemoveParkedOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ParkedOrderID: str = None,
        InvestUnitID: str = None,
    ):
        """
        删除预埋单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ParkedOrderID: 预埋报单编号
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class RemoveParkedOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ParkedOrderActionID: str = None,
        InvestUnitID: str = None,
    ):
        """
        删除预埋撤单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ParkedOrderActionID: 预埋撤单编号
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class InvestorWithdrawAlgorithm(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorRange: bytes = None,
        InvestorID: str = None,
        UsingRatio: float = None,
        CurrencyID: str = None,
        FundMortgageRatio: float = None,
    ):
        """
        经纪公司可提资金算法表
        :param BrokerID: 经纪公司代码
        :param InvestorRange: 投资者范围
        :param InvestorID: 投资者代码
        :param UsingRatio: 可提资金比例
        :param CurrencyID: 币种代码
        :param FundMortgageRatio: 货币质押比率
        """
        super().__init__()
        ...


class QryInvestorPositionCombineDetail(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        CombInstrumentID: str = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询组合持仓明细
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param CombInstrumentID: 组合持仓合约编码
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class MarketDataAveragePrice(Struct):
    def __init__(
        self,
        AveragePrice: float = None,
    ):
        """
        成交均价
        :param AveragePrice: 当日均价
        """
        super().__init__()
        ...


class VerifyInvestorPassword(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        Password: str = None,
    ):
        """
        校验投资者密码
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param Password: 密码
        """
        super().__init__()
        ...


class UserIP(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        IPAddress: str = None,
        IPMask: str = None,
        MacAddress: str = None,
    ):
        """
        用户IP
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param IPAddress: IP地址
        :param IPMask: IP地址掩码
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class TradingNoticeInfo(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        SendTime: str = None,
        FieldContent: str = None,
        SequenceSeries: int = None,
        SequenceNo: int = None,
        InvestUnitID: str = None,
    ):
        """
        用户事件通知信息
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param SendTime: 发送时间
        :param FieldContent: 消息正文
        :param SequenceSeries: 序列系列号
        :param SequenceNo: 序列号
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class TradingNotice(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorRange: bytes = None,
        InvestorID: str = None,
        SequenceSeries: int = None,
        UserID: str = None,
        SendTime: str = None,
        SequenceNo: int = None,
        FieldContent: str = None,
        InvestUnitID: str = None,
    ):
        """
        用户事件通知
        :param BrokerID: 经纪公司代码
        :param InvestorRange: 投资者范围
        :param InvestorID: 投资者代码
        :param SequenceSeries: 序列系列号
        :param UserID: 用户代码
        :param SendTime: 发送时间
        :param SequenceNo: 序列号
        :param FieldContent: 消息正文
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryTradingNotice(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询交易事件通知
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryErrOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
    ):
        """
        查询错误报单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        """
        super().__init__()
        ...


class ErrOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        OrderRef: str = None,
        UserID: str = None,
        OrderPriceType: bytes = None,
        Direction: bytes = None,
        CombOffsetFlag: str = None,
        CombHedgeFlag: str = None,
        LimitPrice: float = None,
        VolumeTotalOriginal: int = None,
        TimeCondition: bytes = None,
        GTDDate: str = None,
        VolumeCondition: bytes = None,
        MinVolume: int = None,
        ContingentCondition: bytes = None,
        StopPrice: float = None,
        ForceCloseReason: bytes = None,
        IsAutoSuspend: int = None,
        BusinessUnit: str = None,
        RequestID: int = None,
        UserForceClose: int = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        IsSwapOrder: int = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        ClientID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        错误报单
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param OrderRef: 报单引用
        :param UserID: 用户代码
        :param OrderPriceType: 报单价格条件
        :param Direction: 买卖方向
        :param CombOffsetFlag: 组合开平标志
        :param CombHedgeFlag: 组合投机套保标志
        :param LimitPrice: 价格
        :param VolumeTotalOriginal: 数量
        :param TimeCondition: 有效期类型
        :param GTDDate: GTD日期
        :param VolumeCondition: 成交量类型
        :param MinVolume: 最小成交量
        :param ContingentCondition: 触发条件
        :param StopPrice: 止损价
        :param ForceCloseReason: 强平原因
        :param IsAutoSuspend: 自动挂起标志
        :param BusinessUnit: 业务单元
        :param RequestID: 请求编号
        :param UserForceClose: 用户强评标志
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param IsSwapOrder: 互换单标志
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param ClientID: 交易编码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class ErrorConditionalOrder(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        OrderRef: str = None,
        UserID: str = None,
        OrderPriceType: bytes = None,
        Direction: bytes = None,
        CombOffsetFlag: str = None,
        CombHedgeFlag: str = None,
        LimitPrice: float = None,
        VolumeTotalOriginal: int = None,
        TimeCondition: bytes = None,
        GTDDate: str = None,
        VolumeCondition: bytes = None,
        MinVolume: int = None,
        ContingentCondition: bytes = None,
        StopPrice: float = None,
        ForceCloseReason: bytes = None,
        IsAutoSuspend: int = None,
        BusinessUnit: str = None,
        RequestID: int = None,
        OrderLocalID: str = None,
        ExchangeID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        ExchangeInstID: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderSubmitStatus: bytes = None,
        NotifySequence: int = None,
        TradingDay: str = None,
        SettlementID: int = None,
        OrderSysID: str = None,
        OrderSource: bytes = None,
        OrderStatus: bytes = None,
        OrderType: bytes = None,
        VolumeTraded: int = None,
        VolumeTotal: int = None,
        InsertDate: str = None,
        InsertTime: str = None,
        ActiveTime: str = None,
        SuspendTime: str = None,
        UpdateTime: str = None,
        CancelTime: str = None,
        ActiveTraderID: str = None,
        ClearingPartID: str = None,
        SequenceNo: int = None,
        FrontID: int = None,
        SessionID: int = None,
        UserProductInfo: str = None,
        StatusMsg: str = None,
        UserForceClose: int = None,
        ActiveUserID: str = None,
        BrokerOrderSeq: int = None,
        RelativeOrderSysID: str = None,
        ZCETotalTradedVolume: int = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        IsSwapOrder: int = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
    ):
        """
        查询错误报单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param OrderRef: 报单引用
        :param UserID: 用户代码
        :param OrderPriceType: 报单价格条件
        :param Direction: 买卖方向
        :param CombOffsetFlag: 组合开平标志
        :param CombHedgeFlag: 组合投机套保标志
        :param LimitPrice: 价格
        :param VolumeTotalOriginal: 数量
        :param TimeCondition: 有效期类型
        :param GTDDate: GTD日期
        :param VolumeCondition: 成交量类型
        :param MinVolume: 最小成交量
        :param ContingentCondition: 触发条件
        :param StopPrice: 止损价
        :param ForceCloseReason: 强平原因
        :param IsAutoSuspend: 自动挂起标志
        :param BusinessUnit: 业务单元
        :param RequestID: 请求编号
        :param OrderLocalID: 本地报单编号
        :param ExchangeID: 交易所代码
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param ExchangeInstID: 合约在交易所的代码
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderSubmitStatus: 报单提交状态
        :param NotifySequence: 报单提示序号
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param OrderSysID: 报单编号
        :param OrderSource: 报单来源
        :param OrderStatus: 报单状态
        :param OrderType: 报单类型
        :param VolumeTraded: 今成交数量
        :param VolumeTotal: 剩余数量
        :param InsertDate: 报单日期
        :param InsertTime: 委托时间
        :param ActiveTime: 激活时间
        :param SuspendTime: 挂起时间
        :param UpdateTime: 最后修改时间
        :param CancelTime: 撤销时间
        :param ActiveTraderID: 最后修改交易所交易员代码
        :param ClearingPartID: 结算会员编号
        :param SequenceNo: 序号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param UserProductInfo: 用户端产品信息
        :param StatusMsg: 状态信息
        :param UserForceClose: 用户强评标志
        :param ActiveUserID: 操作用户代码
        :param BrokerOrderSeq: 经纪公司报单编号
        :param RelativeOrderSysID: 相关报单
        :param ZCETotalTradedVolume: 郑商所成交数量
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param IsSwapOrder: 互换单标志
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param AccountID: 资金账号
        :param CurrencyID: 币种代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        """
        super().__init__()
        ...


class QryErrOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
    ):
        """
        查询错误报单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        """
        super().__init__()
        ...


class ErrOrderAction(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        OrderActionRef: int = None,
        OrderRef: str = None,
        RequestID: int = None,
        FrontID: int = None,
        SessionID: int = None,
        ExchangeID: str = None,
        OrderSysID: str = None,
        ActionFlag: bytes = None,
        LimitPrice: float = None,
        VolumeChange: int = None,
        ActionDate: str = None,
        ActionTime: str = None,
        TraderID: str = None,
        InstallID: int = None,
        OrderLocalID: str = None,
        ActionLocalID: str = None,
        ParticipantID: str = None,
        ClientID: str = None,
        BusinessUnit: str = None,
        OrderActionStatus: bytes = None,
        UserID: str = None,
        StatusMsg: str = None,
        InstrumentID: str = None,
        BranchID: str = None,
        InvestUnitID: str = None,
        IPAddress: str = None,
        MacAddress: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        错误报单操作
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param OrderActionRef: 报单操作引用
        :param OrderRef: 报单引用
        :param RequestID: 请求编号
        :param FrontID: 前置编号
        :param SessionID: 会话编号
        :param ExchangeID: 交易所代码
        :param OrderSysID: 报单编号
        :param ActionFlag: 操作标志
        :param LimitPrice: 价格
        :param VolumeChange: 数量变化
        :param ActionDate: 操作日期
        :param ActionTime: 操作时间
        :param TraderID: 交易所交易员代码
        :param InstallID: 安装编号
        :param OrderLocalID: 本地报单编号
        :param ActionLocalID: 操作本地编号
        :param ParticipantID: 会员代码
        :param ClientID: 客户代码
        :param BusinessUnit: 业务单元
        :param OrderActionStatus: 报单操作状态
        :param UserID: 用户代码
        :param StatusMsg: 状态信息
        :param InstrumentID: 合约代码
        :param BranchID: 营业部编号
        :param InvestUnitID: 投资单元代码
        :param IPAddress: IP地址
        :param MacAddress: Mac地址
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class QryExchangeSequence(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
    ):
        """
        查询交易所状态
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class ExchangeSequence(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        SequenceNo: int = None,
        MarketStatus: bytes = None,
    ):
        """
        交易所状态
        :param ExchangeID: 交易所代码
        :param SequenceNo: 序号
        :param MarketStatus: 合约交易状态
        """
        super().__init__()
        ...


class QueryMaxOrderVolumeWithPrice(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InstrumentID: str = None,
        Direction: bytes = None,
        OffsetFlag: bytes = None,
        HedgeFlag: bytes = None,
        MaxVolume: int = None,
        Price: float = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        根据价格查询最大报单数量
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InstrumentID: 合约代码
        :param Direction: 买卖方向
        :param OffsetFlag: 开平标志
        :param HedgeFlag: 投机套保标志
        :param MaxVolume: 最大允许报单数量
        :param Price: 报单价格
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryBrokerTradingParams(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        CurrencyID: str = None,
        AccountID: str = None,
    ):
        """
        查询经纪公司交易参数
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param CurrencyID: 币种代码
        :param AccountID: 投资者帐号
        """
        super().__init__()
        ...


class BrokerTradingParams(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        MarginPriceType: bytes = None,
        Algorithm: bytes = None,
        AvailIncludeCloseProfit: bytes = None,
        CurrencyID: str = None,
        OptionRoyaltyPriceType: bytes = None,
        AccountID: str = None,
    ):
        """
        经纪公司交易参数
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param MarginPriceType: 保证金价格类型
        :param Algorithm: 盈亏算法
        :param AvailIncludeCloseProfit: 可用是否包含平仓盈利
        :param CurrencyID: 币种代码
        :param OptionRoyaltyPriceType: 期权权利金价格类型
        :param AccountID: 投资者帐号
        """
        super().__init__()
        ...


class QryBrokerTradingAlgos(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        ExchangeID: str = None,
        InstrumentID: str = None,
    ):
        """
        查询经纪公司交易算法
        :param BrokerID: 经纪公司代码
        :param ExchangeID: 交易所代码
        :param InstrumentID: 合约代码
        """
        super().__init__()
        ...


class BrokerTradingAlgos(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        ExchangeID: str = None,
        InstrumentID: str = None,
        HandlePositionAlgoID: bytes = None,
        FindMarginRateAlgoID: bytes = None,
        HandleTradingAccountAlgoID: bytes = None,
    ):
        """
        经纪公司交易算法
        :param BrokerID: 经纪公司代码
        :param ExchangeID: 交易所代码
        :param InstrumentID: 合约代码
        :param HandlePositionAlgoID: 持仓处理算法编号
        :param FindMarginRateAlgoID: 寻找保证金率算法编号
        :param HandleTradingAccountAlgoID: 资金处理算法编号
        """
        super().__init__()
        ...


class QueryBrokerDeposit(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        ExchangeID: str = None,
    ):
        """
        查询经纪公司资金
        :param BrokerID: 经纪公司代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class BrokerDeposit(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        BrokerID: str = None,
        ParticipantID: str = None,
        ExchangeID: str = None,
        PreBalance: float = None,
        CurrMargin: float = None,
        CloseProfit: float = None,
        Balance: float = None,
        Deposit: float = None,
        Withdraw: float = None,
        Available: float = None,
        Reserve: float = None,
        FrozenMargin: float = None,
    ):
        """
        经纪公司资金
        :param TradingDay: 交易日期
        :param BrokerID: 经纪公司代码
        :param ParticipantID: 会员代码
        :param ExchangeID: 交易所代码
        :param PreBalance: 上次结算准备金
        :param CurrMargin: 当前保证金总额
        :param CloseProfit: 平仓盈亏
        :param Balance: 期货结算准备金
        :param Deposit: 入金金额
        :param Withdraw: 出金金额
        :param Available: 可提资金
        :param Reserve: 基本准备金
        :param FrozenMargin: 冻结的保证金
        """
        super().__init__()
        ...


class QryCFMMCBrokerKey(Struct):
    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        查询保证金监管系统经纪公司密钥
        :param BrokerID: 经纪公司代码
        """
        super().__init__()
        ...


class CFMMCBrokerKey(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        ParticipantID: str = None,
        CreateDate: str = None,
        CreateTime: str = None,
        KeyID: int = None,
        CurrentKey: str = None,
        KeyKind: bytes = None,
    ):
        """
        保证金监管系统经纪公司密钥
        :param BrokerID: 经纪公司代码
        :param ParticipantID: 经纪公司统一编码
        :param CreateDate: 密钥生成日期
        :param CreateTime: 密钥生成时间
        :param KeyID: 密钥编号
        :param CurrentKey: 动态密钥
        :param KeyKind: 动态密钥类型
        """
        super().__init__()
        ...


class CFMMCTradingAccountKey(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        ParticipantID: str = None,
        AccountID: str = None,
        KeyID: int = None,
        CurrentKey: str = None,
    ):
        """
        保证金监管系统经纪公司资金账户密钥
        :param BrokerID: 经纪公司代码
        :param ParticipantID: 经纪公司统一编码
        :param AccountID: 投资者帐号
        :param KeyID: 密钥编号
        :param CurrentKey: 动态密钥
        """
        super().__init__()
        ...


class QryCFMMCTradingAccountKey(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
    ):
        """
        请求查询保证金监管系统经纪公司资金账户密钥
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        """
        super().__init__()
        ...


class BrokerUserOTPParam(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        OTPVendorsID: str = None,
        SerialNumber: str = None,
        AuthKey: str = None,
        LastDrift: int = None,
        LastSuccess: int = None,
        OTPType: bytes = None,
    ):
        """
        用户动态令牌参数
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param OTPVendorsID: 动态令牌提供商
        :param SerialNumber: 动态令牌序列号
        :param AuthKey: 令牌密钥
        :param LastDrift: 漂移值
        :param LastSuccess: 成功值
        :param OTPType: 动态令牌类型
        """
        super().__init__()
        ...


class ManualSyncBrokerUserOTP(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        OTPType: bytes = None,
        FirstOTP: str = None,
        SecondOTP: str = None,
    ):
        """
        手工同步用户动态令牌
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param OTPType: 动态令牌类型
        :param FirstOTP: 第一个动态密码
        :param SecondOTP: 第二个动态密码
        """
        super().__init__()
        ...


class CommRateModel(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        CommModelID: str = None,
        CommModelName: str = None,
    ):
        """
        投资者手续费率模板
        :param BrokerID: 经纪公司代码
        :param CommModelID: 手续费率模板代码
        :param CommModelName: 模板名称
        """
        super().__init__()
        ...


class QryCommRateModel(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        CommModelID: str = None,
    ):
        """
        请求查询投资者手续费率模板
        :param BrokerID: 经纪公司代码
        :param CommModelID: 手续费率模板代码
        """
        super().__init__()
        ...


class MarginModel(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        MarginModelID: str = None,
        MarginModelName: str = None,
    ):
        """
        投资者保证金率模板
        :param BrokerID: 经纪公司代码
        :param MarginModelID: 保证金率模板代码
        :param MarginModelName: 模板名称
        """
        super().__init__()
        ...


class QryMarginModel(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        MarginModelID: str = None,
    ):
        """
        请求查询投资者保证金率模板
        :param BrokerID: 经纪公司代码
        :param MarginModelID: 保证金率模板代码
        """
        super().__init__()
        ...


class EWarrantOffset(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        BrokerID: str = None,
        InvestorID: str = None,
        ExchangeID: str = None,
        InstrumentID: str = None,
        Direction: bytes = None,
        HedgeFlag: bytes = None,
        Volume: int = None,
        InvestUnitID: str = None,
    ):
        """
        仓单折抵信息
        :param TradingDay: 交易日期
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExchangeID: 交易所代码
        :param InstrumentID: 合约代码
        :param Direction: 买卖方向
        :param HedgeFlag: 投机套保标志
        :param Volume: 数量
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryEWarrantOffset(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ExchangeID: str = None,
        InstrumentID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询仓单折抵信息
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ExchangeID: 交易所代码
        :param InstrumentID: 合约代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QryInvestorProductGroupMargin(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        ProductGroupID: str = None,
        HedgeFlag: bytes = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询投资者品种跨品种保证金
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param ProductGroupID: 品种跨品种标示
        :param HedgeFlag: 投机套保标志
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class InvestorProductGroupMargin(Struct):
    def __init__(
        self,
        ProductGroupID: str = None,
        BrokerID: str = None,
        InvestorID: str = None,
        TradingDay: str = None,
        SettlementID: int = None,
        FrozenMargin: float = None,
        LongFrozenMargin: float = None,
        ShortFrozenMargin: float = None,
        UseMargin: float = None,
        LongUseMargin: float = None,
        ShortUseMargin: float = None,
        ExchMargin: float = None,
        LongExchMargin: float = None,
        ShortExchMargin: float = None,
        CloseProfit: float = None,
        FrozenCommission: float = None,
        Commission: float = None,
        FrozenCash: float = None,
        CashIn: float = None,
        PositionProfit: float = None,
        OffsetAmount: float = None,
        LongOffsetAmount: float = None,
        ShortOffsetAmount: float = None,
        ExchOffsetAmount: float = None,
        LongExchOffsetAmount: float = None,
        ShortExchOffsetAmount: float = None,
        HedgeFlag: bytes = None,
        ExchangeID: str = None,
        InvestUnitID: str = None,
    ):
        """
        投资者品种跨品种保证金
        :param ProductGroupID: 品种跨品种标示
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param TradingDay: 交易日
        :param SettlementID: 结算编号
        :param FrozenMargin: 冻结的保证金
        :param LongFrozenMargin: 多头冻结的保证金
        :param ShortFrozenMargin: 空头冻结的保证金
        :param UseMargin: 占用的保证金
        :param LongUseMargin: 多头保证金
        :param ShortUseMargin: 空头保证金
        :param ExchMargin: 交易所保证金
        :param LongExchMargin: 交易所多头保证金
        :param ShortExchMargin: 交易所空头保证金
        :param CloseProfit: 平仓盈亏
        :param FrozenCommission: 冻结的手续费
        :param Commission: 手续费
        :param FrozenCash: 冻结的资金
        :param CashIn: 资金差额
        :param PositionProfit: 持仓盈亏
        :param OffsetAmount: 折抵总金额
        :param LongOffsetAmount: 多头折抵总金额
        :param ShortOffsetAmount: 空头折抵总金额
        :param ExchOffsetAmount: 交易所折抵总金额
        :param LongExchOffsetAmount: 交易所多头折抵总金额
        :param ShortExchOffsetAmount: 交易所空头折抵总金额
        :param HedgeFlag: 投机套保标志
        :param ExchangeID: 交易所代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class QueryCFMMCTradingAccountToken(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
        InvestUnitID: str = None,
    ):
        """
        查询监控中心用户令牌
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param InvestUnitID: 投资单元代码
        """
        super().__init__()
        ...


class CFMMCTradingAccountToken(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        ParticipantID: str = None,
        AccountID: str = None,
        KeyID: int = None,
        Token: str = None,
    ):
        """
        监控中心用户令牌
        :param BrokerID: 经纪公司代码
        :param ParticipantID: 经纪公司统一编码
        :param AccountID: 投资者帐号
        :param KeyID: 密钥编号
        :param Token: 动态令牌
        """
        super().__init__()
        ...


class QryProductGroup(Struct):
    def __init__(
        self,
        ProductID: str = None,
        ExchangeID: str = None,
    ):
        """
        查询产品组
        :param ProductID: 产品代码
        :param ExchangeID: 交易所代码
        """
        super().__init__()
        ...


class ProductGroup(Struct):
    def __init__(
        self,
        ProductID: str = None,
        ExchangeID: str = None,
        ProductGroupID: str = None,
    ):
        """
        投资者品种跨品种保证金产品组
        :param ProductID: 产品代码
        :param ExchangeID: 交易所代码
        :param ProductGroupID: 产品组代码
        """
        super().__init__()
        ...


class Bulletin(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        TradingDay: str = None,
        BulletinID: int = None,
        SequenceNo: int = None,
        NewsType: str = None,
        NewsUrgency: str = None,
        SendTime: str = None,
        Abstract: str = None,
        ComeFrom: str = None,
        Content: str = None,
        URLLink: str = None,
        MarketID: str = None,
    ):
        """
        交易所公告
        :param ExchangeID: 交易所代码
        :param TradingDay: 交易日
        :param BulletinID: 公告编号
        :param SequenceNo: 序列号
        :param NewsType: 公告类型
        :param NewsUrgency: 紧急程度
        :param SendTime: 发送时间
        :param Abstract: 消息摘要
        :param ComeFrom: 消息来源
        :param Content: 消息正文
        :param URLLink: WEB地址
        :param MarketID: 市场代码
        """
        super().__init__()
        ...


class QryBulletin(Struct):
    def __init__(
        self,
        ExchangeID: str = None,
        BulletinID: int = None,
        SequenceNo: int = None,
        NewsType: str = None,
        NewsUrgency: str = None,
    ):
        """
        查询交易所公告
        :param ExchangeID: 交易所代码
        :param BulletinID: 公告编号
        :param SequenceNo: 序列号
        :param NewsType: 公告类型
        :param NewsUrgency: 紧急程度
        """
        super().__init__()
        ...


class ReqOpenAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        Gender: bytes = None,
        CountryCode: str = None,
        CustType: bytes = None,
        Address: str = None,
        ZipCode: str = None,
        Telephone: str = None,
        MobilePhone: str = None,
        Fax: str = None,
        EMail: str = None,
        MoneyAccountStatus: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        InstallID: int = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        CashExchangeCode: bytes = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        TID: int = None,
        UserID: str = None,
        LongCustomerName: str = None,
    ):
        """
        转帐开户请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param Gender: 性别
        :param CountryCode: 国家代码
        :param CustType: 客户类型
        :param Address: 地址
        :param ZipCode: 邮编
        :param Telephone: 电话号码
        :param MobilePhone: 手机
        :param Fax: 传真
        :param EMail: 电子邮件
        :param MoneyAccountStatus: 资金账户状态
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param InstallID: 安装编号
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param CashExchangeCode: 汇钞标志
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param TID: 交易ID
        :param UserID: 用户标识
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class ReqCancelAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        Gender: bytes = None,
        CountryCode: str = None,
        CustType: bytes = None,
        Address: str = None,
        ZipCode: str = None,
        Telephone: str = None,
        MobilePhone: str = None,
        Fax: str = None,
        EMail: str = None,
        MoneyAccountStatus: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        InstallID: int = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        CashExchangeCode: bytes = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        TID: int = None,
        UserID: str = None,
        LongCustomerName: str = None,
    ):
        """
        转帐销户请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param Gender: 性别
        :param CountryCode: 国家代码
        :param CustType: 客户类型
        :param Address: 地址
        :param ZipCode: 邮编
        :param Telephone: 电话号码
        :param MobilePhone: 手机
        :param Fax: 传真
        :param EMail: 电子邮件
        :param MoneyAccountStatus: 资金账户状态
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param InstallID: 安装编号
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param CashExchangeCode: 汇钞标志
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param TID: 交易ID
        :param UserID: 用户标识
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class ReqChangeAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        Gender: bytes = None,
        CountryCode: str = None,
        CustType: bytes = None,
        Address: str = None,
        ZipCode: str = None,
        Telephone: str = None,
        MobilePhone: str = None,
        Fax: str = None,
        EMail: str = None,
        MoneyAccountStatus: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        NewBankAccount: str = None,
        NewBankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        BankAccType: bytes = None,
        InstallID: int = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        BrokerIDByBank: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        TID: int = None,
        Digest: str = None,
        LongCustomerName: str = None,
    ):
        """
        变更银行账户请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param Gender: 性别
        :param CountryCode: 国家代码
        :param CustType: 客户类型
        :param Address: 地址
        :param ZipCode: 邮编
        :param Telephone: 电话号码
        :param MobilePhone: 手机
        :param Fax: 传真
        :param EMail: 电子邮件
        :param MoneyAccountStatus: 资金账户状态
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param NewBankAccount: 新银行帐号
        :param NewBankPassWord: 新银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param BankAccType: 银行帐号类型
        :param InstallID: 安装编号
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param BrokerIDByBank: 期货公司银行编码
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param TID: 交易ID
        :param Digest: 摘要
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class ReqTransfer(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        InstallID: int = None,
        FutureSerial: int = None,
        UserID: str = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        TradeAmount: float = None,
        FutureFetchAmount: float = None,
        FeePayFlag: bytes = None,
        CustFee: float = None,
        BrokerFee: float = None,
        Message: str = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        TransferStatus: bytes = None,
        LongCustomerName: str = None,
    ):
        """
        转账请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param InstallID: 安装编号
        :param FutureSerial: 期货公司流水号
        :param UserID: 用户标识
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param TradeAmount: 转帐金额
        :param FutureFetchAmount: 期货可取金额
        :param FeePayFlag: 费用支付标志
        :param CustFee: 应收客户费用
        :param BrokerFee: 应收期货公司费用
        :param Message: 发送方给接收方的消息
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param TransferStatus: 转账交易状态
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class RspTransfer(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        InstallID: int = None,
        FutureSerial: int = None,
        UserID: str = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        TradeAmount: float = None,
        FutureFetchAmount: float = None,
        FeePayFlag: bytes = None,
        CustFee: float = None,
        BrokerFee: float = None,
        Message: str = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        TransferStatus: bytes = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        LongCustomerName: str = None,
    ):
        """
        银行发起银行资金转期货响应
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param InstallID: 安装编号
        :param FutureSerial: 期货公司流水号
        :param UserID: 用户标识
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param TradeAmount: 转帐金额
        :param FutureFetchAmount: 期货可取金额
        :param FeePayFlag: 费用支付标志
        :param CustFee: 应收客户费用
        :param BrokerFee: 应收期货公司费用
        :param Message: 发送方给接收方的消息
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param TransferStatus: 转账交易状态
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class ReqRepeal(Struct):
    def __init__(
        self,
        RepealTimeInterval: int = None,
        RepealedTimes: int = None,
        BankRepealFlag: bytes = None,
        BrokerRepealFlag: bytes = None,
        PlateRepealSerial: int = None,
        BankRepealSerial: str = None,
        FutureRepealSerial: int = None,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        InstallID: int = None,
        FutureSerial: int = None,
        UserID: str = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        TradeAmount: float = None,
        FutureFetchAmount: float = None,
        FeePayFlag: bytes = None,
        CustFee: float = None,
        BrokerFee: float = None,
        Message: str = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        TransferStatus: bytes = None,
        LongCustomerName: str = None,
    ):
        """
        冲正请求
        :param RepealTimeInterval: 冲正时间间隔
        :param RepealedTimes: 已经冲正次数
        :param BankRepealFlag: 银行冲正标志
        :param BrokerRepealFlag: 期商冲正标志
        :param PlateRepealSerial: 被冲正平台流水号
        :param BankRepealSerial: 被冲正银行流水号
        :param FutureRepealSerial: 被冲正期货流水号
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param InstallID: 安装编号
        :param FutureSerial: 期货公司流水号
        :param UserID: 用户标识
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param TradeAmount: 转帐金额
        :param FutureFetchAmount: 期货可取金额
        :param FeePayFlag: 费用支付标志
        :param CustFee: 应收客户费用
        :param BrokerFee: 应收期货公司费用
        :param Message: 发送方给接收方的消息
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param TransferStatus: 转账交易状态
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class RspRepeal(Struct):
    def __init__(
        self,
        RepealTimeInterval: int = None,
        RepealedTimes: int = None,
        BankRepealFlag: bytes = None,
        BrokerRepealFlag: bytes = None,
        PlateRepealSerial: int = None,
        BankRepealSerial: str = None,
        FutureRepealSerial: int = None,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        InstallID: int = None,
        FutureSerial: int = None,
        UserID: str = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        TradeAmount: float = None,
        FutureFetchAmount: float = None,
        FeePayFlag: bytes = None,
        CustFee: float = None,
        BrokerFee: float = None,
        Message: str = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        TransferStatus: bytes = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        LongCustomerName: str = None,
    ):
        """
        冲正响应
        :param RepealTimeInterval: 冲正时间间隔
        :param RepealedTimes: 已经冲正次数
        :param BankRepealFlag: 银行冲正标志
        :param BrokerRepealFlag: 期商冲正标志
        :param PlateRepealSerial: 被冲正平台流水号
        :param BankRepealSerial: 被冲正银行流水号
        :param FutureRepealSerial: 被冲正期货流水号
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param InstallID: 安装编号
        :param FutureSerial: 期货公司流水号
        :param UserID: 用户标识
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param TradeAmount: 转帐金额
        :param FutureFetchAmount: 期货可取金额
        :param FeePayFlag: 费用支付标志
        :param CustFee: 应收客户费用
        :param BrokerFee: 应收期货公司费用
        :param Message: 发送方给接收方的消息
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param TransferStatus: 转账交易状态
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class ReqQueryAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        FutureSerial: int = None,
        InstallID: int = None,
        UserID: str = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        LongCustomerName: str = None,
    ):
        """
        查询账户信息请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param FutureSerial: 期货公司流水号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class RspQueryAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        FutureSerial: int = None,
        InstallID: int = None,
        UserID: str = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        BankUseAmount: float = None,
        BankFetchAmount: float = None,
        LongCustomerName: str = None,
    ):
        """
        查询账户信息响应
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param FutureSerial: 期货公司流水号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param BankUseAmount: 银行可用金额
        :param BankFetchAmount: 银行可取金额
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class FutureSignIO(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        InstallID: int = None,
        UserID: str = None,
        Digest: str = None,
        CurrencyID: str = None,
        DeviceID: str = None,
        BrokerIDByBank: str = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
    ):
        """
        期商签到签退
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param Digest: 摘要
        :param CurrencyID: 币种代码
        :param DeviceID: 渠道标志
        :param BrokerIDByBank: 期货公司银行编码
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        """
        super().__init__()
        ...


class RspFutureSignIn(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        InstallID: int = None,
        UserID: str = None,
        Digest: str = None,
        CurrencyID: str = None,
        DeviceID: str = None,
        BrokerIDByBank: str = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        PinKey: str = None,
        MacKey: str = None,
    ):
        """
        期商签到响应
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param Digest: 摘要
        :param CurrencyID: 币种代码
        :param DeviceID: 渠道标志
        :param BrokerIDByBank: 期货公司银行编码
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param PinKey: PIN密钥
        :param MacKey: MAC密钥
        """
        super().__init__()
        ...


class ReqFutureSignOut(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        InstallID: int = None,
        UserID: str = None,
        Digest: str = None,
        CurrencyID: str = None,
        DeviceID: str = None,
        BrokerIDByBank: str = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
    ):
        """
        期商签退请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param Digest: 摘要
        :param CurrencyID: 币种代码
        :param DeviceID: 渠道标志
        :param BrokerIDByBank: 期货公司银行编码
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        """
        super().__init__()
        ...


class RspFutureSignOut(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        InstallID: int = None,
        UserID: str = None,
        Digest: str = None,
        CurrencyID: str = None,
        DeviceID: str = None,
        BrokerIDByBank: str = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        期商签退响应
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param Digest: 摘要
        :param CurrencyID: 币种代码
        :param DeviceID: 渠道标志
        :param BrokerIDByBank: 期货公司银行编码
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class ReqQueryTradeResultBySerial(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        Reference: int = None,
        RefrenceIssureType: bytes = None,
        RefrenceIssure: str = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        CurrencyID: str = None,
        TradeAmount: float = None,
        Digest: str = None,
        LongCustomerName: str = None,
    ):
        """
        查询指定流水号的交易结果请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param Reference: 流水号
        :param RefrenceIssureType: 本流水号发布者的机构类型
        :param RefrenceIssure: 本流水号发布者机构编码
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param CurrencyID: 币种代码
        :param TradeAmount: 转帐金额
        :param Digest: 摘要
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class RspQueryTradeResultBySerial(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        Reference: int = None,
        RefrenceIssureType: bytes = None,
        RefrenceIssure: str = None,
        OriginReturnCode: str = None,
        OriginDescrInfoForReturnCode: str = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        CurrencyID: str = None,
        TradeAmount: float = None,
        Digest: str = None,
    ):
        """
        查询指定流水号的交易结果响应
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param Reference: 流水号
        :param RefrenceIssureType: 本流水号发布者的机构类型
        :param RefrenceIssure: 本流水号发布者机构编码
        :param OriginReturnCode: 原始返回代码
        :param OriginDescrInfoForReturnCode: 原始返回码描述
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param CurrencyID: 币种代码
        :param TradeAmount: 转帐金额
        :param Digest: 摘要
        """
        super().__init__()
        ...


class ReqDayEndFileReady(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        FileBusinessCode: bytes = None,
        Digest: str = None,
    ):
        """
        日终文件就绪请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param FileBusinessCode: 文件业务功能
        :param Digest: 摘要
        """
        super().__init__()
        ...


class ReturnResult(Struct):
    def __init__(
        self,
        ReturnCode: str = None,
        DescrInfoForReturnCode: str = None,
    ):
        """
        返回结果
        :param ReturnCode: 返回代码
        :param DescrInfoForReturnCode: 返回码描述
        """
        super().__init__()
        ...


class VerifyFuturePassword(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        AccountID: str = None,
        Password: str = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        InstallID: int = None,
        TID: int = None,
        CurrencyID: str = None,
    ):
        """
        验证期货资金密码
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param InstallID: 安装编号
        :param TID: 交易ID
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class VerifyCustInfo(Struct):
    def __init__(
        self,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        LongCustomerName: str = None,
    ):
        """
        验证客户信息
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class VerifyFuturePasswordAndCustInfo(Struct):
    def __init__(
        self,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        AccountID: str = None,
        Password: str = None,
        CurrencyID: str = None,
        LongCustomerName: str = None,
    ):
        """
        验证期货资金密码和客户信息
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param CurrencyID: 币种代码
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class DepositResultInform(Struct):
    def __init__(
        self,
        DepositSeqNo: str = None,
        BrokerID: str = None,
        InvestorID: str = None,
        Deposit: float = None,
        RequestID: int = None,
        ReturnCode: str = None,
        DescrInfoForReturnCode: str = None,
    ):
        """
        验证期货资金密码和客户信息
        :param DepositSeqNo: 出入金流水号，该流水号为银期报盘返回的流水号
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        :param Deposit: 入金金额
        :param RequestID: 请求编号
        :param ReturnCode: 返回代码
        :param DescrInfoForReturnCode: 返回码描述
        """
        super().__init__()
        ...


class ReqSyncKey(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        InstallID: int = None,
        UserID: str = None,
        Message: str = None,
        DeviceID: str = None,
        BrokerIDByBank: str = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
    ):
        """
        交易核心向银期报盘发出密钥同步请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param Message: 交易核心给银期报盘的消息
        :param DeviceID: 渠道标志
        :param BrokerIDByBank: 期货公司银行编码
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        """
        super().__init__()
        ...


class RspSyncKey(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        InstallID: int = None,
        UserID: str = None,
        Message: str = None,
        DeviceID: str = None,
        BrokerIDByBank: str = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        交易核心向银期报盘发出密钥同步响应
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param Message: 交易核心给银期报盘的消息
        :param DeviceID: 渠道标志
        :param BrokerIDByBank: 期货公司银行编码
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class NotifyQueryAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustType: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        FutureSerial: int = None,
        InstallID: int = None,
        UserID: str = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        BankUseAmount: float = None,
        BankFetchAmount: float = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        LongCustomerName: str = None,
    ):
        """
        查询账户信息通知
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustType: 客户类型
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param FutureSerial: 期货公司流水号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param BankUseAmount: 银行可用金额
        :param BankFetchAmount: 银行可取金额
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class TransferSerial(Struct):
    def __init__(
        self,
        PlateSerial: int = None,
        TradeDate: str = None,
        TradingDay: str = None,
        TradeTime: str = None,
        TradeCode: str = None,
        SessionID: int = None,
        BankID: str = None,
        BankBranchID: str = None,
        BankAccType: bytes = None,
        BankAccount: str = None,
        BankSerial: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        FutureAccType: bytes = None,
        AccountID: str = None,
        InvestorID: str = None,
        FutureSerial: int = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CurrencyID: str = None,
        TradeAmount: float = None,
        CustFee: float = None,
        BrokerFee: float = None,
        AvailabilityFlag: bytes = None,
        OperatorCode: str = None,
        BankNewAccount: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        银期转账交易流水表
        :param PlateSerial: 平台流水号
        :param TradeDate: 交易发起方日期
        :param TradingDay: 交易日期
        :param TradeTime: 交易时间
        :param TradeCode: 交易代码
        :param SessionID: 会话编号
        :param BankID: 银行编码
        :param BankBranchID: 银行分支机构编码
        :param BankAccType: 银行帐号类型
        :param BankAccount: 银行帐号
        :param BankSerial: 银行流水号
        :param BrokerID: 期货公司编码
        :param BrokerBranchID: 期商分支机构代码
        :param FutureAccType: 期货公司帐号类型
        :param AccountID: 投资者帐号
        :param InvestorID: 投资者代码
        :param FutureSerial: 期货公司流水号
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CurrencyID: 币种代码
        :param TradeAmount: 交易金额
        :param CustFee: 应收客户费用
        :param BrokerFee: 应收期货公司费用
        :param AvailabilityFlag: 有效标志
        :param OperatorCode: 操作员
        :param BankNewAccount: 新银行帐号
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class QryTransferSerial(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        AccountID: str = None,
        BankID: str = None,
        CurrencyID: str = None,
    ):
        """
        请求查询转帐流水
        :param BrokerID: 经纪公司代码
        :param AccountID: 投资者帐号
        :param BankID: 银行编码
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class NotifyFutureSignIn(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        InstallID: int = None,
        UserID: str = None,
        Digest: str = None,
        CurrencyID: str = None,
        DeviceID: str = None,
        BrokerIDByBank: str = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        PinKey: str = None,
        MacKey: str = None,
    ):
        """
        期商签到通知
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param Digest: 摘要
        :param CurrencyID: 币种代码
        :param DeviceID: 渠道标志
        :param BrokerIDByBank: 期货公司银行编码
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param PinKey: PIN密钥
        :param MacKey: MAC密钥
        """
        super().__init__()
        ...


class NotifyFutureSignOut(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        InstallID: int = None,
        UserID: str = None,
        Digest: str = None,
        CurrencyID: str = None,
        DeviceID: str = None,
        BrokerIDByBank: str = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        期商签退通知
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param Digest: 摘要
        :param CurrencyID: 币种代码
        :param DeviceID: 渠道标志
        :param BrokerIDByBank: 期货公司银行编码
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class NotifySyncKey(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        InstallID: int = None,
        UserID: str = None,
        Message: str = None,
        DeviceID: str = None,
        BrokerIDByBank: str = None,
        OperNo: str = None,
        RequestID: int = None,
        TID: int = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        交易核心向银期报盘发出密钥同步处理结果的通知
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param InstallID: 安装编号
        :param UserID: 用户标识
        :param Message: 交易核心给银期报盘的消息
        :param DeviceID: 渠道标志
        :param BrokerIDByBank: 期货公司银行编码
        :param OperNo: 交易柜员
        :param RequestID: 请求编号
        :param TID: 交易ID
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class QryAccountregister(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        AccountID: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        CurrencyID: str = None,
    ):
        """
        请求查询银期签约关系
        :param BrokerID: 经纪公司代码
        :param AccountID: 投资者帐号
        :param BankID: 银行编码
        :param BankBranchID: 银行分支机构编码
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class Accountregister(Struct):
    def __init__(
        self,
        TradeDay: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BankAccount: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        AccountID: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        CustomerName: str = None,
        CurrencyID: str = None,
        OpenOrDestroy: bytes = None,
        RegDate: str = None,
        OutDate: str = None,
        TID: int = None,
        CustType: bytes = None,
        BankAccType: bytes = None,
        LongCustomerName: str = None,
    ):
        """
        客户开销户信息表
        :param TradeDay: 交易日期
        :param BankID: 银行编码
        :param BankBranchID: 银行分支机构编码
        :param BankAccount: 银行帐号
        :param BrokerID: 期货公司编码
        :param BrokerBranchID: 期货公司分支机构编码
        :param AccountID: 投资者帐号
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param CustomerName: 客户姓名
        :param CurrencyID: 币种代码
        :param OpenOrDestroy: 开销户类别
        :param RegDate: 签约日期
        :param OutDate: 解约日期
        :param TID: 交易ID
        :param CustType: 客户类型
        :param BankAccType: 银行帐号类型
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class OpenAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        Gender: bytes = None,
        CountryCode: str = None,
        CustType: bytes = None,
        Address: str = None,
        ZipCode: str = None,
        Telephone: str = None,
        MobilePhone: str = None,
        Fax: str = None,
        EMail: str = None,
        MoneyAccountStatus: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        InstallID: int = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        CashExchangeCode: bytes = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        TID: int = None,
        UserID: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        LongCustomerName: str = None,
    ):
        """
        银期开户信息
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param Gender: 性别
        :param CountryCode: 国家代码
        :param CustType: 客户类型
        :param Address: 地址
        :param ZipCode: 邮编
        :param Telephone: 电话号码
        :param MobilePhone: 手机
        :param Fax: 传真
        :param EMail: 电子邮件
        :param MoneyAccountStatus: 资金账户状态
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param InstallID: 安装编号
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param CashExchangeCode: 汇钞标志
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param TID: 交易ID
        :param UserID: 用户标识
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class CancelAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        Gender: bytes = None,
        CountryCode: str = None,
        CustType: bytes = None,
        Address: str = None,
        ZipCode: str = None,
        Telephone: str = None,
        MobilePhone: str = None,
        Fax: str = None,
        EMail: str = None,
        MoneyAccountStatus: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        InstallID: int = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        CashExchangeCode: bytes = None,
        Digest: str = None,
        BankAccType: bytes = None,
        DeviceID: str = None,
        BankSecuAccType: bytes = None,
        BrokerIDByBank: str = None,
        BankSecuAcc: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        OperNo: str = None,
        TID: int = None,
        UserID: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        LongCustomerName: str = None,
    ):
        """
        银期销户信息
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param Gender: 性别
        :param CountryCode: 国家代码
        :param CustType: 客户类型
        :param Address: 地址
        :param ZipCode: 邮编
        :param Telephone: 电话号码
        :param MobilePhone: 手机
        :param Fax: 传真
        :param EMail: 电子邮件
        :param MoneyAccountStatus: 资金账户状态
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param InstallID: 安装编号
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param CashExchangeCode: 汇钞标志
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param DeviceID: 渠道标志
        :param BankSecuAccType: 期货单位帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param BankSecuAcc: 期货单位帐号
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param OperNo: 交易柜员
        :param TID: 交易ID
        :param UserID: 用户标识
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class ChangeAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        Gender: bytes = None,
        CountryCode: str = None,
        CustType: bytes = None,
        Address: str = None,
        ZipCode: str = None,
        Telephone: str = None,
        MobilePhone: str = None,
        Fax: str = None,
        EMail: str = None,
        MoneyAccountStatus: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        NewBankAccount: str = None,
        NewBankPassWord: str = None,
        AccountID: str = None,
        Password: str = None,
        BankAccType: bytes = None,
        InstallID: int = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        BrokerIDByBank: str = None,
        BankPwdFlag: bytes = None,
        SecuPwdFlag: bytes = None,
        TID: int = None,
        Digest: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
        LongCustomerName: str = None,
    ):
        """
        银期变更银行账号信息
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param Gender: 性别
        :param CountryCode: 国家代码
        :param CustType: 客户类型
        :param Address: 地址
        :param ZipCode: 邮编
        :param Telephone: 电话号码
        :param MobilePhone: 手机
        :param Fax: 传真
        :param EMail: 电子邮件
        :param MoneyAccountStatus: 资金账户状态
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param NewBankAccount: 新银行帐号
        :param NewBankPassWord: 新银行密码
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param BankAccType: 银行帐号类型
        :param InstallID: 安装编号
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param BrokerIDByBank: 期货公司银行编码
        :param BankPwdFlag: 银行密码标志
        :param SecuPwdFlag: 期货资金密码核对标志
        :param TID: 交易ID
        :param Digest: 摘要
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        :param LongCustomerName: 长客户姓名
        """
        super().__init__()
        ...


class SecAgentACIDMap(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
        BrokerSecAgentID: str = None,
    ):
        """
        二级代理操作员银期权限
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param AccountID: 资金账户
        :param CurrencyID: 币种
        :param BrokerSecAgentID: 境外中介机构资金帐号
        """
        super().__init__()
        ...


class QrySecAgentACIDMap(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        AccountID: str = None,
        CurrencyID: str = None,
    ):
        """
        二级代理操作员银期权限查询
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param AccountID: 资金账户
        :param CurrencyID: 币种
        """
        super().__init__()
        ...


class UserRightsAssign(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        DRIdentityID: int = None,
    ):
        """
        灾备中心交易权限
        :param BrokerID: 应用单元代码
        :param UserID: 用户代码
        :param DRIdentityID: 交易中心代码
        """
        super().__init__()
        ...


class BrokerUserRightAssign(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        DRIdentityID: int = None,
        Tradeable: int = None,
    ):
        """
        经济公司是否有在本标示的交易权限
        :param BrokerID: 应用单元代码
        :param DRIdentityID: 交易中心代码
        :param Tradeable: 能否交易
        """
        super().__init__()
        ...


class DRTransfer(Struct):
    def __init__(
        self,
        OrigDRIdentityID: int = None,
        DestDRIdentityID: int = None,
        OrigBrokerID: str = None,
        DestBrokerID: str = None,
    ):
        """
        灾备交易转换报文
        :param OrigDRIdentityID: 原交易中心代码
        :param DestDRIdentityID: 目标交易中心代码
        :param OrigBrokerID: 原应用单元代码
        :param DestBrokerID: 目标易用单元代码
        """
        super().__init__()
        ...


class FensUserInfo(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        LoginMode: bytes = None,
    ):
        """
        Fens用户信息
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param LoginMode: 登录模式
        """
        super().__init__()
        ...


class CurrTransferIdentity(Struct):
    def __init__(
        self,
        IdentityID: int = None,
    ):
        """
        当前银期所属交易中心
        :param IdentityID: 交易中心代码
        """
        super().__init__()
        ...


class LoginForbiddenUser(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        IPAddress: str = None,
    ):
        """
        禁止登录用户
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param IPAddress: IP地址
        """
        super().__init__()
        ...


class QryLoginForbiddenUser(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        查询禁止登录用户
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class MulticastGroupInfo(Struct):
    def __init__(
        self,
        GroupIP: str = None,
        GroupPort: int = None,
        SourceIP: str = None,
    ):
        """
        UDP组播组信息
        :param GroupIP: 组播组IP地址
        :param GroupPort: 组播组IP端口
        :param SourceIP: 源地址
        """
        super().__init__()
        ...


class TradingAccountReserve(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        AccountID: str = None,
        Reserve: float = None,
        CurrencyID: str = None,
    ):
        """
        资金账户基本准备金
        :param BrokerID: 经纪公司代码
        :param AccountID: 投资者帐号
        :param Reserve: 基本准备金
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class QryLoginForbiddenIP(Struct):
    def __init__(
        self,
        IPAddress: str = None,
    ):
        """
        查询禁止登录IP
        :param IPAddress: IP地址
        """
        super().__init__()
        ...


class QryIPList(Struct):
    def __init__(
        self,
        IPAddress: str = None,
    ):
        """
        查询IP列表
        :param IPAddress: IP地址
        """
        super().__init__()
        ...


class QryUserRightsAssign(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        查询用户下单权限分配表
        :param BrokerID: 应用单元代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class ReserveOpenAccountConfirm(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        Gender: bytes = None,
        CountryCode: str = None,
        CustType: bytes = None,
        Address: str = None,
        ZipCode: str = None,
        Telephone: str = None,
        MobilePhone: str = None,
        Fax: str = None,
        EMail: str = None,
        MoneyAccountStatus: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        InstallID: int = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        Digest: str = None,
        BankAccType: bytes = None,
        BrokerIDByBank: str = None,
        TID: int = None,
        AccountID: str = None,
        Password: str = None,
        BankReserveOpenSeq: str = None,
        BookDate: str = None,
        BookPsw: str = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        银期预约开户确认请求
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param Gender: 性别
        :param CountryCode: 国家代码
        :param CustType: 客户类型
        :param Address: 地址
        :param ZipCode: 邮编
        :param Telephone: 电话号码
        :param MobilePhone: 手机
        :param Fax: 传真
        :param EMail: 电子邮件
        :param MoneyAccountStatus: 资金账户状态
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param InstallID: 安装编号
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param TID: 交易ID
        :param AccountID: 投资者帐号
        :param Password: 期货密码
        :param BankReserveOpenSeq: 预约开户银行流水号
        :param BookDate: 预约开户日期
        :param BookPsw: 预约开户验证密码
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class ReserveOpenAccount(Struct):
    def __init__(
        self,
        TradeCode: str = None,
        BankID: str = None,
        BankBranchID: str = None,
        BrokerID: str = None,
        BrokerBranchID: str = None,
        TradeDate: str = None,
        TradeTime: str = None,
        BankSerial: str = None,
        TradingDay: str = None,
        PlateSerial: int = None,
        LastFragment: bytes = None,
        SessionID: int = None,
        CustomerName: str = None,
        IdCardType: bytes = None,
        IdentifiedCardNo: str = None,
        Gender: bytes = None,
        CountryCode: str = None,
        CustType: bytes = None,
        Address: str = None,
        ZipCode: str = None,
        Telephone: str = None,
        MobilePhone: str = None,
        Fax: str = None,
        EMail: str = None,
        MoneyAccountStatus: bytes = None,
        BankAccount: str = None,
        BankPassWord: str = None,
        InstallID: int = None,
        VerifyCertNoFlag: bytes = None,
        CurrencyID: str = None,
        Digest: str = None,
        BankAccType: bytes = None,
        BrokerIDByBank: str = None,
        TID: int = None,
        ReserveOpenAccStas: bytes = None,
        ErrorID: int = None,
        ErrorMsg: str = None,
    ):
        """
        银期预约开户
        :param TradeCode: 业务功能码
        :param BankID: 银行代码
        :param BankBranchID: 银行分支机构代码
        :param BrokerID: 期商代码
        :param BrokerBranchID: 期商分支机构代码
        :param TradeDate: 交易日期
        :param TradeTime: 交易时间
        :param BankSerial: 银行流水号
        :param TradingDay: 交易系统日期
        :param PlateSerial: 银期平台消息流水号
        :param LastFragment: 最后分片标志
        :param SessionID: 会话号
        :param CustomerName: 客户姓名
        :param IdCardType: 证件类型
        :param IdentifiedCardNo: 证件号码
        :param Gender: 性别
        :param CountryCode: 国家代码
        :param CustType: 客户类型
        :param Address: 地址
        :param ZipCode: 邮编
        :param Telephone: 电话号码
        :param MobilePhone: 手机
        :param Fax: 传真
        :param EMail: 电子邮件
        :param MoneyAccountStatus: 资金账户状态
        :param BankAccount: 银行帐号
        :param BankPassWord: 银行密码
        :param InstallID: 安装编号
        :param VerifyCertNoFlag: 验证客户证件号码标志
        :param CurrencyID: 币种代码
        :param Digest: 摘要
        :param BankAccType: 银行帐号类型
        :param BrokerIDByBank: 期货公司银行编码
        :param TID: 交易ID
        :param ReserveOpenAccStas: 预约开户状态
        :param ErrorID: 错误代码
        :param ErrorMsg: 错误信息
        """
        super().__init__()
        ...


class AccountProperty(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        AccountID: str = None,
        BankID: str = None,
        BankAccount: str = None,
        OpenName: str = None,
        OpenBank: str = None,
        IsActive: int = None,
        AccountSourceType: bytes = None,
        OpenDate: str = None,
        CancelDate: str = None,
        OperatorID: str = None,
        OperateDate: str = None,
        OperateTime: str = None,
        CurrencyID: str = None,
    ):
        """
        银行账户属性
        :param BrokerID: 经纪公司代码
        :param AccountID: 投资者帐号
        :param BankID: 银行统一标识类型
        :param BankAccount: 银行账户
        :param OpenName: 银行账户的开户人名称
        :param OpenBank: 银行账户的开户行
        :param IsActive: 是否活跃
        :param AccountSourceType: 账户来源
        :param OpenDate: 开户日期
        :param CancelDate: 注销日期
        :param OperatorID: 录入员代码
        :param OperateDate: 录入日期
        :param OperateTime: 录入时间
        :param CurrencyID: 币种代码
        """
        super().__init__()
        ...


class QryCurrDRIdentity(Struct):
    def __init__(
        self,
        DRIdentityID: int = None,
    ):
        """
        查询当前交易中心
        :param DRIdentityID: 交易中心代码
        """
        super().__init__()
        ...


class CurrDRIdentity(Struct):
    def __init__(
        self,
        DRIdentityID: int = None,
    ):
        """
        当前交易中心
        :param DRIdentityID: 交易中心代码
        """
        super().__init__()
        ...


class QrySecAgentCheckMode(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        InvestorID: str = None,
    ):
        """
        查询二级代理商资金校验模式
        :param BrokerID: 经纪公司代码
        :param InvestorID: 投资者代码
        """
        super().__init__()
        ...


class QrySecAgentTradeInfo(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        BrokerSecAgentID: str = None,
    ):
        """
        查询二级代理商信息
        :param BrokerID: 经纪公司代码
        :param BrokerSecAgentID: 境外中介机构资金帐号
        """
        super().__init__()
        ...


class UserSystemInfo(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        ClientSystemInfoLen: int = None,
        ClientSystemInfo: str = None,
        ClientPublicIP: str = None,
        ClientIPPort: int = None,
        ClientLoginTime: str = None,
        ClientAppID: str = None,
    ):
        """
        用户系统信息
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param ClientSystemInfoLen: 用户端系统内部信息长度
        :param ClientSystemInfo: 用户端系统内部信息
        :param ClientPublicIP: 用户公网IP
        :param ClientIPPort: 终端IP端口
        :param ClientLoginTime: 登录成功时间
        :param ClientAppID: App代码
        """
        super().__init__()
        ...


class ReqUserAuthMethod(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        用户发出获取安全安全登陆方法请求
        :param TradingDay: 交易日
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class RspUserAuthMethod(Struct):
    def __init__(
        self,
        UsableAuthMethod: int = None,
    ):
        """
        用户发出获取安全安全登陆方法回复
        :param UsableAuthMethod: 当前可以用的认证模式
        """
        super().__init__()
        ...


class ReqGenUserCaptcha(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        用户发出获取安全安全登陆方法请求
        :param TradingDay: 交易日
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class RspGenUserCaptcha(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        CaptchaInfoLen: int = None,
        CaptchaInfo: str = None,
    ):
        """
        生成的图片验证码信息
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param CaptchaInfoLen: 图片信息长度
        :param CaptchaInfo: 图片信息
        """
        super().__init__()
        ...


class ReqGenUserText(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        BrokerID: str = None,
        UserID: str = None,
    ):
        """
        用户发出获取安全安全登陆方法请求
        :param TradingDay: 交易日
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        """
        super().__init__()
        ...


class RspGenUserText(Struct):
    def __init__(
        self,
        UserTextSeq: int = None,
    ):
        """
        短信验证码生成的回复
        :param UserTextSeq: 短信验证码序号
        """
        super().__init__()
        ...


class ReqUserLoginWithCaptcha(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        BrokerID: str = None,
        UserID: str = None,
        Password: str = None,
        UserProductInfo: str = None,
        InterfaceProductInfo: str = None,
        ProtocolInfo: str = None,
        MacAddress: str = None,
        ClientIPAddress: str = None,
        LoginRemark: str = None,
        Captcha: str = None,
        ClientIPPort: int = None,
    ):
        """
        用户发出带图形验证码的登录请求请求
        :param TradingDay: 交易日
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param Password: 密码
        :param UserProductInfo: 用户端产品信息
        :param InterfaceProductInfo: 接口端产品信息
        :param ProtocolInfo: 协议信息
        :param MacAddress: Mac地址
        :param ClientIPAddress: 终端IP地址
        :param LoginRemark: 登录备注
        :param Captcha: 图形验证码的文字内容
        :param ClientIPPort: 终端IP端口
        """
        super().__init__()
        ...


class ReqUserLoginWithText(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        BrokerID: str = None,
        UserID: str = None,
        Password: str = None,
        UserProductInfo: str = None,
        InterfaceProductInfo: str = None,
        ProtocolInfo: str = None,
        MacAddress: str = None,
        ClientIPAddress: str = None,
        LoginRemark: str = None,
        Text: str = None,
        ClientIPPort: int = None,
    ):
        """
        用户发出带短信验证码的登录请求请求
        :param TradingDay: 交易日
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param Password: 密码
        :param UserProductInfo: 用户端产品信息
        :param InterfaceProductInfo: 接口端产品信息
        :param ProtocolInfo: 协议信息
        :param MacAddress: Mac地址
        :param ClientIPAddress: 终端IP地址
        :param LoginRemark: 登录备注
        :param Text: 短信验证码文字内容
        :param ClientIPPort: 终端IP端口
        """
        super().__init__()
        ...


class ReqUserLoginWithOTP(Struct):
    def __init__(
        self,
        TradingDay: str = None,
        BrokerID: str = None,
        UserID: str = None,
        Password: str = None,
        UserProductInfo: str = None,
        InterfaceProductInfo: str = None,
        ProtocolInfo: str = None,
        MacAddress: str = None,
        ClientIPAddress: str = None,
        LoginRemark: str = None,
        OTPPassword: str = None,
        ClientIPPort: int = None,
    ):
        """
        用户发出带动态验证码的登录请求请求
        :param TradingDay: 交易日
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param Password: 密码
        :param UserProductInfo: 用户端产品信息
        :param InterfaceProductInfo: 接口端产品信息
        :param ProtocolInfo: 协议信息
        :param MacAddress: Mac地址
        :param ClientIPAddress: 终端IP地址
        :param LoginRemark: 登录备注
        :param OTPPassword: OTP密码
        :param ClientIPPort: 终端IP端口
        """
        super().__init__()
        ...


class ReqApiHandshake(Struct):
    def __init__(
        self,
        CryptoKeyVersion: str = None,
    ):
        """
        api握手请求
        :param CryptoKeyVersion: api与front通信密钥版本号
        """
        super().__init__()
        ...


class RspApiHandshake(Struct):
    def __init__(
        self,
        FrontHandshakeDataLen: int = None,
        FrontHandshakeData: str = None,
        IsApiAuthEnabled: int = None,
    ):
        """
        front发给api的握手回复
        :param FrontHandshakeDataLen: 握手回复数据长度
        :param FrontHandshakeData: 握手回复数据
        :param IsApiAuthEnabled: API认证是否开启
        """
        super().__init__()
        ...


class ReqVerifyApiKey(Struct):
    def __init__(
        self,
        ApiHandshakeDataLen: int = None,
        ApiHandshakeData: str = None,
    ):
        """
        api给front的验证key的请求
        :param ApiHandshakeDataLen: 握手回复数据长度
        :param ApiHandshakeData: 握手回复数据
        """
        super().__init__()
        ...


class DepartmentUser(Struct):
    def __init__(
        self,
        BrokerID: str = None,
        UserID: str = None,
        InvestorRange: bytes = None,
        InvestorID: str = None,
    ):
        """
        操作员组织架构关系
        :param BrokerID: 经纪公司代码
        :param UserID: 用户代码
        :param InvestorRange: 投资者范围
        :param InvestorID: 投资者代码
        """
        super().__init__()
        ...


class QueryFreq(Struct):
    def __init__(
        self,
        QueryFreq: int = None,
    ):
        """
        查询频率，每秒查询比数
        :param QueryFreq: 查询频率
        """
        super().__init__()
        ...

from ctypes import c_char, c_short, c_double, c_int

from .utils import Struct

c_char_Array_2 = c_char * 2
c_char_Array_3 = c_char * 3
c_char_Array_4 = c_char * 4
c_char_Array_5 = c_char * 5
c_char_Array_7 = c_char * 7
c_char_Array_9 = c_char * 9
c_char_Array_11 = c_char * 11
c_char_Array_13 = c_char * 13
c_char_Array_15 = c_char * 15
c_char_Array_16 = c_char * 16
c_char_Array_17 = c_char * 17
c_char_Array_21 = c_char * 21
c_char_Array_22 = c_char * 22
c_char_Array_31 = c_char * 31
c_char_Array_33 = c_char * 33
c_char_Array_36 = c_char * 36
c_char_Array_41 = c_char * 41
c_char_Array_51 = c_char * 51
c_char_Array_61 = c_char * 61
c_char_Array_65 = c_char * 65
c_char_Array_81 = c_char * 81
c_char_Array_101 = c_char * 101
c_char_Array_129 = c_char * 129
c_char_Array_161 = c_char * 161
c_char_Array_201 = c_char * 201
c_char_Array_256 = c_char * 256
c_char_Array_273 = c_char * 273
c_char_Array_301 = c_char * 301
c_char_Array_501 = c_char * 501
c_char_Array_1025 = c_char * 1025
c_char_Array_2561 = c_char * 2561


class Dissemination(Struct):
    _fields_ = [
        ("SequenceSeries", c_short),
        ("SequenceNo", c_int),
    ]

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
        super(Dissemination, self).__init__()
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
        ("ClientIPAddress", c_char_Array_16),
        ("LoginRemark", c_char_Array_36),
        ("ClientIPPort", c_int),
    ]

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
        super(ReqUserLogin, self).__init__()
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
    ]

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
        super(RspUserLogin, self).__init__()
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


class UserLogout(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

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
        super(UserLogout, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class ForceUserLogout(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

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
        super(ForceUserLogout, self).__init__()
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
        super(ReqAuthenticate, self).__init__()
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
        super(RspAuthenticate, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserProductInfo:
            self.UserProductInfo = UserProductInfo.encode("GBK")
        if AppID:
            self.AppID = AppID.encode("GBK")
        if AppType:
            self.AppType = AppType


class AuthenticationInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("UserProductInfo", c_char_Array_11),
        ("AuthInfo", c_char_Array_129),
        ("IsResult", c_int),
        ("AppID", c_char_Array_33),
        ("AppType", c_char),
    ]

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
        super(AuthenticationInfo, self).__init__()
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
            self.AppType = AppType


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
        super(RspUserLogin2, self).__init__()
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
        super(TransferHeader, self).__init__()
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
        super(TransferBankToFutureReq, self).__init__()
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if FuturePwdFlag:
            self.FuturePwdFlag = FuturePwdFlag
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
        super(TransferBankToFutureRsp, self).__init__()
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
        super(TransferFutureToBankReq, self).__init__()
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if FuturePwdFlag:
            self.FuturePwdFlag = FuturePwdFlag
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
        super(TransferFutureToBankRsp, self).__init__()
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
        super(TransferQryBankReq, self).__init__()
        if FutureAccount:
            self.FutureAccount = FutureAccount.encode("GBK")
        if FuturePwdFlag:
            self.FuturePwdFlag = FuturePwdFlag
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
        super(TransferQryBankRsp, self).__init__()
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

    def __init__(
        self,
        FutureAccount: str = None,
    ):
        """
        查询银行交易明细请求，TradeCode=204999
        :param FutureAccount: 期货资金账户
        """
        super(TransferQryDetailReq, self).__init__()
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
        super(TransferQryDetailRsp, self).__init__()
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
            self.Flag = Flag


class RspInfo(Struct):
    _fields_ = [
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

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
        super(RspInfo, self).__init__()
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
        super(Exchange, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExchangeName:
            self.ExchangeName = ExchangeName.encode("GBK")
        if ExchangeProperty:
            self.ExchangeProperty = ExchangeProperty


class Product(Struct):
    _fields_ = [
        ("ProductID", c_char_Array_31),
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
        ("ExchangeProductID", c_char_Array_31),
        ("UnderlyingMultiple", c_double),
    ]

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
        super(Product, self).__init__()
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ProductName:
            self.ProductName = ProductName.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ProductClass:
            self.ProductClass = ProductClass
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
            self.PositionType = PositionType
        if PositionDateType:
            self.PositionDateType = PositionDateType
        if CloseDealType:
            self.CloseDealType = CloseDealType
        if TradeCurrencyID:
            self.TradeCurrencyID = TradeCurrencyID.encode("GBK")
        if MortgageFundUseRange:
            self.MortgageFundUseRange = MortgageFundUseRange
        if ExchangeProductID:
            self.ExchangeProductID = ExchangeProductID.encode("GBK")
        if UnderlyingMultiple:
            self.UnderlyingMultiple = UnderlyingMultiple


class Instrument(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentName", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_31),
        ("ProductID", c_char_Array_31),
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
        ("UnderlyingInstrID", c_char_Array_31),
        ("StrikePrice", c_double),
        ("OptionsType", c_char),
        ("UnderlyingMultiple", c_double),
        ("CombinationType", c_char),
    ]

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
        super(Instrument, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentName:
            self.InstrumentName = InstrumentName.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ProductClass:
            self.ProductClass = ProductClass
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
            self.InstLifePhase = InstLifePhase
        if IsTrading:
            self.IsTrading = IsTrading
        if PositionType:
            self.PositionType = PositionType
        if PositionDateType:
            self.PositionDateType = PositionDateType
        if LongMarginRatio:
            self.LongMarginRatio = LongMarginRatio
        if ShortMarginRatio:
            self.ShortMarginRatio = ShortMarginRatio
        if MaxMarginSideAlgorithm:
            self.MaxMarginSideAlgorithm = MaxMarginSideAlgorithm
        if UnderlyingInstrID:
            self.UnderlyingInstrID = UnderlyingInstrID.encode("GBK")
        if StrikePrice:
            self.StrikePrice = StrikePrice
        if OptionsType:
            self.OptionsType = OptionsType
        if UnderlyingMultiple:
            self.UnderlyingMultiple = UnderlyingMultiple
        if CombinationType:
            self.CombinationType = CombinationType


class Broker(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("BrokerAbbr", c_char_Array_9),
        ("BrokerName", c_char_Array_81),
        ("IsActive", c_int),
    ]

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
        super(Broker, self).__init__()
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
    ]

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
        super(Trader, self).__init__()
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
    ]

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
        super(Investor, self).__init__()
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorGroupID:
            self.InvestorGroupID = InvestorGroupID.encode("GBK")
        if InvestorName:
            self.InvestorName = InvestorName.encode("GBK")
        if IdentifiedCardType:
            self.IdentifiedCardType = IdentifiedCardType
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
        super(TradingCode, self).__init__()
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
            self.ClientIDType = ClientIDType
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if BizType:
            self.BizType = BizType
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class PartBroker(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("IsActive", c_int),
    ]

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
        super(PartBroker, self).__init__()
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
        super(SuperUser, self).__init__()
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
        super(SuperUserFunction, self).__init__()
        if UserID:
            self.UserID = UserID.encode("GBK")
        if FunctionCode:
            self.FunctionCode = FunctionCode


class InvestorGroup(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorGroupID", c_char_Array_13),
        ("InvestorGroupName", c_char_Array_41),
    ]

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
        super(InvestorGroup, self).__init__()
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
        super(TradingAccount, self).__init__()
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
            self.BizType = BizType
        if FrozenSwap:
            self.FrozenSwap = FrozenSwap
        if RemainSwap:
            self.RemainSwap = RemainSwap


class InvestorPosition(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
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
    ]

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
        super(InvestorPosition, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if PosiDirection:
            self.PosiDirection = PosiDirection
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if PositionDate:
            self.PositionDate = PositionDate
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


class InstrumentMarginRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
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
    ]

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
        super(InstrumentMarginRate, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
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


class InstrumentCommissionRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
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
    ]

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
        super(InstrumentCommissionRate, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
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
            self.BizType = BizType
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class DepthMarketData(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("ExchangeInstID", c_char_Array_31),
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
    ]

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
        super(DepthMarketData, self).__init__()
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


class InstrumentTradingRight(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("TradingRight", c_char),
    ]

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
        super(InstrumentTradingRight, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if TradingRight:
            self.TradingRight = TradingRight


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
        super(BrokerUser, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserName:
            self.UserName = UserName.encode("GBK")
        if UserType:
            self.UserType = UserType
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
        super(BrokerUserPassword, self).__init__()
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
        super(BrokerUserFunction, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if BrokerFunctionCode:
            self.BrokerFunctionCode = BrokerFunctionCode


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
    ]

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
        super(TraderOffer, self).__init__()
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
            self.TraderConnectStatus = TraderConnectStatus
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
        super(SettlementInfo, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int),
    ]

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
        super(InstrumentMarginRateAdjust, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
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


class ExchangeMarginRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(ExchangeMarginRate, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
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


class ExchangeMarginRateAdjust(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_31),
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
    ]

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
        super(ExchangeMarginRateAdjust, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
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


class ExchangeRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("FromCurrencyID", c_char_Array_4),
        ("FromCurrencyUnit", c_double),
        ("ToCurrencyID", c_char_Array_4),
        ("ExchangeRate", c_double),
    ]

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
        super(ExchangeRate, self).__init__()
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
        super(SettlementRef, self).__init__()
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
        super(CurrentTime, self).__init__()
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
        super(CommPhase, self).__init__()
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
        ("IPAddress", c_char_Array_16),
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
    ]

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
        super(LoginInfo, self).__init__()
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
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


class LogoutAll(Struct):
    _fields_ = [
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("SystemName", c_char_Array_41),
    ]

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
        super(LogoutAll, self).__init__()
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
        super(FrontStatus, self).__init__()
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
        super(UserPasswordUpdate, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType
        if Direction:
            self.Direction = Direction
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class Order(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(Order, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType
        if Direction:
            self.Direction = Direction
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason
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
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if OrderSource:
            self.OrderSource = OrderSource
        if OrderStatus:
            self.OrderStatus = OrderStatus
        if OrderType:
            self.OrderType = OrderType
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExchangeOrder, self).__init__()
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType
        if Direction:
            self.Direction = Direction
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason
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
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if OrderSource:
            self.OrderSource = OrderSource
        if OrderStatus:
            self.OrderStatus = OrderStatus
        if OrderType:
            self.OrderType = OrderType
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        super(ExchangeOrderInsertError, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputOrderAction, self).__init__()
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
            self.ActionFlag = ActionFlag
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeChange:
            self.VolumeChange = VolumeChange
        if UserID:
            self.UserID = UserID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("InstrumentID", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(OrderAction, self).__init__()
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
            self.ActionFlag = ActionFlag
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExchangeOrderAction, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        super(ExchangeOrderActionError, self).__init__()
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
        ("ExchangeInstID", c_char_Array_31),
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
    ]

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
        super(ExchangeTrade, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TradeID:
            self.TradeID = TradeID.encode("GBK")
        if Direction:
            self.Direction = Direction
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if TradingRole:
            self.TradingRole = TradingRole
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if Price:
            self.Price = Price
        if Volume:
            self.Volume = Volume
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if TradeType:
            self.TradeType = TradeType
        if PriceSource:
            self.PriceSource = PriceSource
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
            self.TradeSource = TradeSource


class Trade(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("OrderRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("ExchangeID", c_char_Array_9),
        ("TradeID", c_char_Array_21),
        ("Direction", c_char),
        ("OrderSysID", c_char_Array_21),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("TradingRole", c_char),
        ("ExchangeInstID", c_char_Array_31),
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
    ]

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
        super(Trade, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TradeID:
            self.TradeID = TradeID.encode("GBK")
        if Direction:
            self.Direction = Direction
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if TradingRole:
            self.TradingRole = TradingRole
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if Price:
            self.Price = Price
        if Volume:
            self.Volume = Volume
        if TradeDate:
            self.TradeDate = TradeDate.encode("GBK")
        if TradeTime:
            self.TradeTime = TradeTime.encode("GBK")
        if TradeType:
            self.TradeType = TradeType
        if PriceSource:
            self.PriceSource = PriceSource
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
            self.TradeSource = TradeSource
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class UserSession(Struct):
    _fields_ = [
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("LoginDate", c_char_Array_9),
        ("LoginTime", c_char_Array_9),
        ("IPAddress", c_char_Array_16),
        ("UserProductInfo", c_char_Array_11),
        ("InterfaceProductInfo", c_char_Array_11),
        ("ProtocolInfo", c_char_Array_11),
        ("MacAddress", c_char_Array_21),
        ("LoginRemark", c_char_Array_36),
    ]

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
        super(UserSession, self).__init__()
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
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


class QueryMaxOrderVolume(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("MaxVolume", c_int),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QueryMaxOrderVolume, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if Direction:
            self.Direction = Direction
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if MaxVolume:
            self.MaxVolume = MaxVolume
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


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
        super(SettlementInfoConfirm, self).__init__()
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
    ]

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
        super(SyncDeposit, self).__init__()
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


class SyncFundMortgage(Struct):
    _fields_ = [
        ("MortgageSeqNo", c_char_Array_15),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("FromCurrencyID", c_char_Array_4),
        ("MortgageAmount", c_double),
        ("ToCurrencyID", c_char_Array_4),
    ]

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
        super(SyncFundMortgage, self).__init__()
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

    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        经纪公司同步
        :param BrokerID: 经纪公司代码
        """
        super(BrokerSync, self).__init__()
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
    ]

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
        super(SyncingInvestor, self).__init__()
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorGroupID:
            self.InvestorGroupID = InvestorGroupID.encode("GBK")
        if InvestorName:
            self.InvestorName = InvestorName.encode("GBK")
        if IdentifiedCardType:
            self.IdentifiedCardType = IdentifiedCardType
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


class SyncingTradingCode(Struct):
    _fields_ = [
        ("InvestorID", c_char_Array_13),
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("ClientID", c_char_Array_11),
        ("IsActive", c_int),
        ("ClientIDType", c_char),
    ]

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
        super(SyncingTradingCode, self).__init__()
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
            self.ClientIDType = ClientIDType


class SyncingInvestorGroup(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorGroupID", c_char_Array_13),
        ("InvestorGroupName", c_char_Array_41),
    ]

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
        super(SyncingInvestorGroup, self).__init__()
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
        super(SyncingTradingAccount, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
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
    ]

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
        super(SyncingInvestorPosition, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if PosiDirection:
            self.PosiDirection = PosiDirection
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if PositionDate:
            self.PositionDate = PositionDate
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


class SyncingInstrumentMarginRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int),
    ]

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
        super(SyncingInstrumentMarginRate, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
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


class SyncingInstrumentCommissionRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
    ]

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
        super(SyncingInstrumentCommissionRate, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
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


class SyncingInstrumentTradingRight(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("TradingRight", c_char),
    ]

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
        super(SyncingInstrumentTradingRight, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if TradingRight:
            self.TradingRight = TradingRight


class QryOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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


class QryTrade(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TradeID", c_char_Array_21),
        ("TradeTimeStart", c_char_Array_9),
        ("TradeTimeEnd", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryTrade, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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


class QryInvestorPosition(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryInvestorPosition, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryTradingAccount(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("BizType", c_char),
        ("AccountID", c_char_Array_13),
    ]

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
        super(QryTradingAccount, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if BizType:
            self.BizType = BizType
        if AccountID:
            self.AccountID = AccountID.encode("GBK")


class QryInvestor(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

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
        super(QryInvestor, self).__init__()
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
        super(QryTradingCode, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ClientIDType:
            self.ClientIDType = ClientIDType
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryInvestorGroup(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
    ]

    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        查询投资者组
        :param BrokerID: 经纪公司代码
        """
        super(QryInvestorGroup, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")


class QryInstrumentMarginRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryInstrumentMarginRate, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryInstrumentCommissionRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryInstrumentCommissionRate, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryInstrumentTradingRight(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
    ]

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
        super(QryInstrumentTradingRight, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryBroker(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
    ]

    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        查询经纪公司
        :param BrokerID: 经纪公司代码
        """
        super(QryBroker, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")


class QryTrader(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("TraderID", c_char_Array_21),
    ]

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
        super(QryTrader, self).__init__()
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

    def __init__(
        self,
        UserID: str = None,
    ):
        """
        查询管理用户功能权限
        :param UserID: 用户代码
        """
        super(QrySuperUserFunction, self).__init__()
        if UserID:
            self.UserID = UserID.encode("GBK")


class QryUserSession(Struct):
    _fields_ = [
        ("FrontID", c_int),
        ("SessionID", c_int),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

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
        super(QryUserSession, self).__init__()
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
        super(QryPartBroker, self).__init__()
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

    def __init__(
        self,
        FrontID: int = None,
    ):
        """
        查询前置状态
        :param FrontID: 前置编号
        """
        super(QryFrontStatus, self).__init__()
        if FrontID:
            self.FrontID = FrontID


class QryExchangeOrder(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeInstID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

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
        super(QryExchangeOrder, self).__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class QryOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryOrderAction, self).__init__()
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
        super(QryExchangeOrderAction, self).__init__()
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

    def __init__(
        self,
        UserID: str = None,
    ):
        """
        查询管理用户
        :param UserID: 用户代码
        """
        super(QrySuperUser, self).__init__()
        if UserID:
            self.UserID = UserID.encode("GBK")


class QryExchange(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(
        self,
        ExchangeID: str = None,
    ):
        """
        查询交易所
        :param ExchangeID: 交易所代码
        """
        super(QryExchange, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class QryProduct(Struct):
    _fields_ = [
        ("ProductID", c_char_Array_31),
        ("ProductClass", c_char),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryProduct, self).__init__()
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ProductClass:
            self.ProductClass = ProductClass
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class QryInstrument(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("ExchangeInstID", c_char_Array_31),
        ("ProductID", c_char_Array_31),
    ]

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
        super(QryInstrument, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")


class QryDepthMarketData(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryDepthMarketData, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class QryBrokerUser(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

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
        super(QryBrokerUser, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class QryBrokerUserFunction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

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
        super(QryBrokerUserFunction, self).__init__()
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
        super(QryTraderOffer, self).__init__()
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
        super(QrySyncDeposit, self).__init__()
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
        super(QrySettlementInfo, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryExchangeMarginRate, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class QryExchangeMarginRateAdjust(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_31),
        ("HedgeFlag", c_char),
    ]

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
        super(QryExchangeMarginRateAdjust, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag


class QryExchangeRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("FromCurrencyID", c_char_Array_4),
        ("ToCurrencyID", c_char_Array_4),
    ]

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
        super(QryExchangeRate, self).__init__()
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
        super(QrySyncFundMortgage, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if MortgageSeqNo:
            self.MortgageSeqNo = MortgageSeqNo.encode("GBK")


class QryHisOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("OrderSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
    ]

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
        super(QryHisOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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


class OptionInstrMiniMargin(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("MinMargin", c_double),
        ("ValueMethod", c_char),
        ("IsRelative", c_int),
    ]

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
        super(OptionInstrMiniMargin, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if MinMargin:
            self.MinMargin = MinMargin
        if ValueMethod:
            self.ValueMethod = ValueMethod
        if IsRelative:
            self.IsRelative = IsRelative


class OptionInstrMarginAdjust(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
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
    ]

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
        super(OptionInstrMarginAdjust, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
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


class OptionInstrCommRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
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
    ]

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
        super(OptionInstrCommRate, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
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


class OptionInstrTradeCost(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("FixedMargin", c_double),
        ("MiniMargin", c_double),
        ("Royalty", c_double),
        ("ExchFixedMargin", c_double),
        ("ExchMiniMargin", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(OptionInstrTradeCost, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
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


class QryOptionInstrTradeCost(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("InputPrice", c_double),
        ("UnderlyingPrice", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryOptionInstrTradeCost, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if InputPrice:
            self.InputPrice = InputPrice
        if UnderlyingPrice:
            self.UnderlyingPrice = UnderlyingPrice
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryOptionInstrCommRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryOptionInstrCommRate, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class IndexPrice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_31),
        ("ClosePrice", c_double),
    ]

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
        super(IndexPrice, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ClosePrice:
            self.ClosePrice = ClosePrice


class InputExecOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputExecOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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
            self.OffsetFlag = OffsetFlag
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ActionType:
            self.ActionType = ActionType
        if PosiDirection:
            self.PosiDirection = PosiDirection
        if ReservePositionFlag:
            self.ReservePositionFlag = ReservePositionFlag
        if CloseFlag:
            self.CloseFlag = CloseFlag
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("InstrumentID", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputExecOrderAction, self).__init__()
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
            self.ActionFlag = ActionFlag
        if UserID:
            self.UserID = UserID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class ExecOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExecOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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
            self.OffsetFlag = OffsetFlag
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ActionType:
            self.ActionType = ActionType
        if PosiDirection:
            self.PosiDirection = PosiDirection
        if ReservePositionFlag:
            self.ReservePositionFlag = ReservePositionFlag
        if CloseFlag:
            self.CloseFlag = CloseFlag
        if ExecOrderLocalID:
            self.ExecOrderLocalID = ExecOrderLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus
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
            self.ExecResult = ExecResult
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("InstrumentID", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExecOrderAction, self).__init__()
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
            self.ActionFlag = ActionFlag
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ActionType:
            self.ActionType = ActionType
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryExecOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("ExecOrderSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
    ]

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
        super(QryExecOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExecOrderSysID:
            self.ExecOrderSysID = ExecOrderSysID.encode("GBK")
        if InsertTimeStart:
            self.InsertTimeStart = InsertTimeStart.encode("GBK")
        if InsertTimeEnd:
            self.InsertTimeEnd = InsertTimeEnd.encode("GBK")


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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExchangeExecOrder, self).__init__()
        if Volume:
            self.Volume = Volume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ActionType:
            self.ActionType = ActionType
        if PosiDirection:
            self.PosiDirection = PosiDirection
        if ReservePositionFlag:
            self.ReservePositionFlag = ReservePositionFlag
        if CloseFlag:
            self.CloseFlag = CloseFlag
        if ExecOrderLocalID:
            self.ExecOrderLocalID = ExecOrderLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus
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
            self.ExecResult = ExecResult
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryExchangeExecOrder(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeInstID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

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
        super(QryExchangeExecOrder, self).__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class QryExecOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryExecOrderAction, self).__init__()
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_31),
        ("Volume", c_int),
    ]

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
        super(ExchangeExecOrderAction, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExecOrderSysID:
            self.ExecOrderSysID = ExecOrderSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ActionType:
            self.ActionType = ActionType
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if Volume:
            self.Volume = Volume


class QryExchangeExecOrderAction(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

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
        super(QryExchangeExecOrderAction, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

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
        super(ErrExecOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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
            self.OffsetFlag = OffsetFlag
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ActionType:
            self.ActionType = ActionType
        if PosiDirection:
            self.PosiDirection = PosiDirection
        if ReservePositionFlag:
            self.ReservePositionFlag = ReservePositionFlag
        if CloseFlag:
            self.CloseFlag = CloseFlag
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class QryErrExecOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

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
        super(QryErrExecOrder, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

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
        super(ErrExecOrderAction, self).__init__()
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
            self.ActionFlag = ActionFlag
        if UserID:
            self.UserID = UserID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class QryErrExecOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

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
        super(QryErrExecOrderAction, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class OptionInstrTradingRight(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Direction", c_char),
        ("TradingRight", c_char),
    ]

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
        super(OptionInstrTradingRight, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Direction:
            self.Direction = Direction
        if TradingRight:
            self.TradingRight = TradingRight


class QryOptionInstrTradingRight(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("Direction", c_char),
    ]

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
        super(QryOptionInstrTradingRight, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if Direction:
            self.Direction = Direction


class InputForQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ForQuoteRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputForQuote, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ForQuoteRef:
            self.ForQuoteRef = ForQuoteRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class ForQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ForQuoteRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("ForQuoteLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ForQuote, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if ForQuoteStatus:
            self.ForQuoteStatus = ForQuoteStatus
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryForQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryForQuote, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InsertTimeStart:
            self.InsertTimeStart = InsertTimeStart.encode("GBK")
        if InsertTimeEnd:
            self.InsertTimeEnd = InsertTimeEnd.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class ExchangeForQuote(Struct):
    _fields_ = [
        ("ForQuoteLocalID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeInstID", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("InsertDate", c_char_Array_9),
        ("InsertTime", c_char_Array_9),
        ("ForQuoteStatus", c_char),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExchangeForQuote, self).__init__()
        if ForQuoteLocalID:
            self.ForQuoteLocalID = ForQuoteLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if InsertDate:
            self.InsertDate = InsertDate.encode("GBK")
        if InsertTime:
            self.InsertTime = InsertTime.encode("GBK")
        if ForQuoteStatus:
            self.ForQuoteStatus = ForQuoteStatus
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryExchangeForQuote(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeInstID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

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
        super(QryExchangeForQuote, self).__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class InputQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputQuote, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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
            self.AskOffsetFlag = AskOffsetFlag
        if BidOffsetFlag:
            self.BidOffsetFlag = BidOffsetFlag
        if AskHedgeFlag:
            self.AskHedgeFlag = AskHedgeFlag
        if BidHedgeFlag:
            self.BidHedgeFlag = BidHedgeFlag
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("InstrumentID", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("ClientID", c_char_Array_11),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputQuoteAction, self).__init__()
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
            self.ActionFlag = ActionFlag
        if UserID:
            self.UserID = UserID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class Quote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(Quote, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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
            self.AskOffsetFlag = AskOffsetFlag
        if BidOffsetFlag:
            self.BidOffsetFlag = BidOffsetFlag
        if AskHedgeFlag:
            self.AskHedgeFlag = AskHedgeFlag
        if BidHedgeFlag:
            self.BidHedgeFlag = BidHedgeFlag
        if QuoteLocalID:
            self.QuoteLocalID = QuoteLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus
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
            self.QuoteStatus = QuoteStatus
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("InstrumentID", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(QuoteAction, self).__init__()
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
            self.ActionFlag = ActionFlag
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryQuote(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("QuoteSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryQuote, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExchangeQuote, self).__init__()
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
            self.AskOffsetFlag = AskOffsetFlag
        if BidOffsetFlag:
            self.BidOffsetFlag = BidOffsetFlag
        if AskHedgeFlag:
            self.AskHedgeFlag = AskHedgeFlag
        if BidHedgeFlag:
            self.BidHedgeFlag = BidHedgeFlag
        if QuoteLocalID:
            self.QuoteLocalID = QuoteLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus
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
            self.QuoteStatus = QuoteStatus
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryExchangeQuote(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeInstID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

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
        super(QryExchangeQuote, self).__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class QryQuoteAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryQuoteAction, self).__init__()
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExchangeQuoteAction, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if QuoteSysID:
            self.QuoteSysID = QuoteSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryExchangeQuoteAction(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

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
        super(QryExchangeQuoteAction, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Delta", c_double),
    ]

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
        super(OptionInstrDelta, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Delta:
            self.Delta = Delta


class ForQuoteRsp(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("InstrumentID", c_char_Array_31),
        ("ForQuoteSysID", c_char_Array_21),
        ("ForQuoteTime", c_char_Array_9),
        ("ActionDay", c_char_Array_9),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(ForQuoteRsp, self).__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ForQuoteSysID:
            self.ForQuoteSysID = ForQuoteSysID.encode("GBK")
        if ForQuoteTime:
            self.ForQuoteTime = ForQuoteTime.encode("GBK")
        if ActionDay:
            self.ActionDay = ActionDay.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class StrikeOffset(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Offset", c_double),
        ("OffsetType", c_char),
    ]

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
        super(StrikeOffset, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Offset:
            self.Offset = Offset
        if OffsetType:
            self.OffsetType = OffsetType


class QryStrikeOffset(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
    ]

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
        super(QryStrikeOffset, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputBatchOrderAction, self).__init__()
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(BatchOrderAction, self).__init__()
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExchangeBatchOrderAction, self).__init__()
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryBatchOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryBatchOrderAction, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class CombInstrumentGuard(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_31),
        ("GuarantRatio", c_double),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(CombInstrumentGuard, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if GuarantRatio:
            self.GuarantRatio = GuarantRatio
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class QryCombInstrumentGuard(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryCombInstrumentGuard, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class InputCombAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("CombActionRef", c_char_Array_13),
        ("UserID", c_char_Array_16),
        ("Direction", c_char),
        ("Volume", c_int),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(InputCombAction, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if CombActionRef:
            self.CombActionRef = CombActionRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Direction:
            self.Direction = Direction
        if Volume:
            self.Volume = Volume
        if CombDirection:
            self.CombDirection = CombDirection
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class CombAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ComTradeID", c_char_Array_21),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(CombAction, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if CombActionRef:
            self.CombActionRef = CombActionRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if Direction:
            self.Direction = Direction
        if Volume:
            self.Volume = Volume
        if CombDirection:
            self.CombDirection = CombDirection
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if ActionStatus:
            self.ActionStatus = ActionStatus
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ComTradeID:
            self.ComTradeID = ComTradeID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryCombAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryCombAction, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


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
        ("ExchangeInstID", c_char_Array_31),
        ("TraderID", c_char_Array_21),
        ("InstallID", c_int),
        ("ActionStatus", c_char),
        ("NotifySequence", c_int),
        ("TradingDay", c_char_Array_9),
        ("SettlementID", c_int),
        ("SequenceNo", c_int),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ComTradeID", c_char_Array_21),
        ("BranchID", c_char_Array_9),
    ]

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
        super(ExchangeCombAction, self).__init__()
        if Direction:
            self.Direction = Direction
        if Volume:
            self.Volume = Volume
        if CombDirection:
            self.CombDirection = CombDirection
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ActionLocalID:
            self.ActionLocalID = ActionLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if ActionStatus:
            self.ActionStatus = ActionStatus
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ComTradeID:
            self.ComTradeID = ComTradeID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")


class QryExchangeCombAction(Struct):
    _fields_ = [
        ("ParticipantID", c_char_Array_11),
        ("ClientID", c_char_Array_11),
        ("ExchangeInstID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("TraderID", c_char_Array_21),
    ]

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
        super(QryExchangeCombAction, self).__init__()
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")


class ProductExchRate(Struct):
    _fields_ = [
        ("ProductID", c_char_Array_31),
        ("QuoteCurrencyID", c_char_Array_4),
        ("ExchangeRate", c_double),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(ProductExchRate, self).__init__()
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if QuoteCurrencyID:
            self.QuoteCurrencyID = QuoteCurrencyID.encode("GBK")
        if ExchangeRate:
            self.ExchangeRate = ExchangeRate
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class QryProductExchRate(Struct):
    _fields_ = [
        ("ProductID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryProductExchRate, self).__init__()
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class QryForQuoteParam(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryForQuoteParam, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class ForQuoteParam(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("LastPrice", c_double),
        ("PriceInterval", c_double),
    ]

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
        super(ForQuoteParam, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if LastPrice:
            self.LastPrice = LastPrice
        if PriceInterval:
            self.PriceInterval = PriceInterval


class MMOptionInstrCommRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
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
    ]

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
        super(MMOptionInstrCommRate, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
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


class QryMMOptionInstrCommRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
    ]

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
        super(QryMMOptionInstrCommRate, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class MMInstrumentCommissionRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
    ]

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
        super(MMInstrumentCommissionRate, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
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


class QryMMInstrumentCommissionRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
    ]

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
        super(QryMMInstrumentCommissionRate, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InstrumentOrderCommRate(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("OrderCommByVolume", c_double),
        ("OrderActionCommByVolume", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(InstrumentOrderCommRate, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if OrderCommByVolume:
            self.OrderCommByVolume = OrderCommByVolume
        if OrderActionCommByVolume:
            self.OrderActionCommByVolume = OrderActionCommByVolume
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryInstrumentOrderCommRate(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
    ]

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
        super(QryInstrumentOrderCommRate, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class TradeParam(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("TradeParamID", c_char),
        ("TradeParamValue", c_char_Array_256),
        ("Memo", c_char_Array_161),
    ]

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
        super(TradeParam, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if TradeParamID:
            self.TradeParamID = TradeParamID
        if TradeParamValue:
            self.TradeParamValue = TradeParamValue.encode("GBK")
        if Memo:
            self.Memo = Memo.encode("GBK")


class InstrumentMarginRateUL(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
    ]

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
        super(InstrumentMarginRateUL, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if LongMarginRatioByMoney:
            self.LongMarginRatioByMoney = LongMarginRatioByMoney
        if LongMarginRatioByVolume:
            self.LongMarginRatioByVolume = LongMarginRatioByVolume
        if ShortMarginRatioByMoney:
            self.ShortMarginRatioByMoney = ShortMarginRatioByMoney
        if ShortMarginRatioByVolume:
            self.ShortMarginRatioByVolume = ShortMarginRatioByVolume


class FutureLimitPosiParam(Struct):
    _fields_ = [
        ("InvestorRange", c_char),
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ProductID", c_char_Array_31),
        ("SpecOpenVolume", c_int),
        ("ArbiOpenVolume", c_int),
        ("OpenVolume", c_int),
    ]

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
        super(FutureLimitPosiParam, self).__init__()
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if SpecOpenVolume:
            self.SpecOpenVolume = SpecOpenVolume
        if ArbiOpenVolume:
            self.ArbiOpenVolume = ArbiOpenVolume
        if OpenVolume:
            self.OpenVolume = OpenVolume


class LoginForbiddenIP(Struct):
    _fields_ = [
        ("IPAddress", c_char_Array_16),
    ]

    def __init__(
        self,
        IPAddress: str = None,
    ):
        """
        禁止登录IP
        :param IPAddress: IP地址
        """
        super(LoginForbiddenIP, self).__init__()
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class IPList(Struct):
    _fields_ = [
        ("IPAddress", c_char_Array_16),
        ("IsWhite", c_int),
    ]

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
        super(IPList, self).__init__()
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if IsWhite:
            self.IsWhite = IsWhite


class InputOptionSelfClose(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputOptionSelfClose, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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
            self.HedgeFlag = HedgeFlag
        if OptSelfCloseFlag:
            self.OptSelfCloseFlag = OptSelfCloseFlag
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("InstrumentID", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(InputOptionSelfCloseAction, self).__init__()
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
            self.ActionFlag = ActionFlag
        if UserID:
            self.UserID = UserID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class OptionSelfClose(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(OptionSelfClose, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
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
            self.HedgeFlag = HedgeFlag
        if OptSelfCloseFlag:
            self.OptSelfCloseFlag = OptSelfCloseFlag
        if OptionSelfCloseLocalID:
            self.OptionSelfCloseLocalID = OptionSelfCloseLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus
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
            self.ExecResult = ExecResult
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("InstrumentID", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(OptionSelfCloseAction, self).__init__()
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
            self.ActionFlag = ActionFlag
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryOptionSelfClose(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("OptionSelfCloseSysID", c_char_Array_21),
        ("InsertTimeStart", c_char_Array_9),
        ("InsertTimeEnd", c_char_Array_9),
    ]

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
        super(QryOptionSelfClose, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OptionSelfCloseSysID:
            self.OptionSelfCloseSysID = OptionSelfCloseSysID.encode("GBK")
        if InsertTimeStart:
            self.InsertTimeStart = InsertTimeStart.encode("GBK")
        if InsertTimeEnd:
            self.InsertTimeEnd = InsertTimeEnd.encode("GBK")


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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ExchangeOptionSelfClose, self).__init__()
        if Volume:
            self.Volume = Volume
        if RequestID:
            self.RequestID = RequestID
        if BusinessUnit:
            self.BusinessUnit = BusinessUnit.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if OptSelfCloseFlag:
            self.OptSelfCloseFlag = OptSelfCloseFlag
        if OptionSelfCloseLocalID:
            self.OptionSelfCloseLocalID = OptionSelfCloseLocalID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ParticipantID:
            self.ParticipantID = ParticipantID.encode("GBK")
        if ClientID:
            self.ClientID = ClientID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus
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
            self.ExecResult = ExecResult
        if ClearingPartID:
            self.ClearingPartID = ClearingPartID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryOptionSelfCloseAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryOptionSelfCloseAction, self).__init__()
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ExchangeInstID", c_char_Array_31),
        ("OptSelfCloseFlag", c_char),
    ]

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
        super(ExchangeOptionSelfCloseAction, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if OptionSelfCloseSysID:
            self.OptionSelfCloseSysID = OptionSelfCloseSysID.encode("GBK")
        if ActionFlag:
            self.ActionFlag = ActionFlag
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if OptSelfCloseFlag:
            self.OptSelfCloseFlag = OptSelfCloseFlag


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
    ]

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
        super(SyncDelaySwap, self).__init__()
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


class QrySyncDelaySwap(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("DelaySwapSeqNo", c_char_Array_15),
    ]

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
        super(QrySyncDelaySwap, self).__init__()
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
        super(InvestUnit, self).__init__()
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
        super(QryInvestUnit, self).__init__()
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
        super(SecAgentCheckMode, self).__init__()
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
        super(SecAgentTradeInfo, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("ExchangeInstID", c_char_Array_31),
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
    ]

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
        super(MarketData, self).__init__()
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
        if ActionDay:
            self.ActionDay = ActionDay.encode("GBK")


class MarketDataBase(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("PreDelta", c_double),
    ]

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
        super(MarketDataBase, self).__init__()
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
        super(MarketDataStatic, self).__init__()
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
        super(MarketDataLastMatch, self).__init__()
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
        super(MarketDataBestPrice, self).__init__()
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
        super(MarketDataBid23, self).__init__()
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
        super(MarketDataAsk23, self).__init__()
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
        super(MarketDataBid45, self).__init__()
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
        super(MarketDataAsk45, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("UpdateTime", c_char_Array_9),
        ("UpdateMillisec", c_int),
        ("ActionDay", c_char_Array_9),
    ]

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
        super(MarketDataUpdateTime, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if UpdateTime:
            self.UpdateTime = UpdateTime.encode("GBK")
        if UpdateMillisec:
            self.UpdateMillisec = UpdateMillisec
        if ActionDay:
            self.ActionDay = ActionDay.encode("GBK")


class MarketDataExchange(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(
        self,
        ExchangeID: str = None,
    ):
        """
        行情交易所代码属性
        :param ExchangeID: 交易所代码
        """
        super(MarketDataExchange, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class SpecificInstrument(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
    ]

    def __init__(
        self,
        InstrumentID: str = None,
    ):
        """
        指定的合约
        :param InstrumentID: 合约代码
        """
        super(SpecificInstrument, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class InstrumentStatus(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ExchangeInstID", c_char_Array_31),
        ("SettlementGroupID", c_char_Array_9),
        ("InstrumentID", c_char_Array_31),
        ("InstrumentStatus", c_char),
        ("TradingSegmentSN", c_int),
        ("EnterTime", c_char_Array_9),
        ("EnterReason", c_char),
    ]

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
        super(InstrumentStatus, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if SettlementGroupID:
            self.SettlementGroupID = SettlementGroupID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InstrumentStatus:
            self.InstrumentStatus = InstrumentStatus
        if TradingSegmentSN:
            self.TradingSegmentSN = TradingSegmentSN
        if EnterTime:
            self.EnterTime = EnterTime.encode("GBK")
        if EnterReason:
            self.EnterReason = EnterReason


class QryInstrumentStatus(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ExchangeInstID", c_char_Array_31),
    ]

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
        super(QryInstrumentStatus, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")


class InvestorAccount(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
    ]

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
        super(InvestorAccount, self).__init__()
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
        super(PositionProfitAlgorithm, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if Algorithm:
            self.Algorithm = Algorithm
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
        super(Discount, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if Discount:
            self.Discount = Discount


class QryTransferBank(Struct):
    _fields_ = [
        ("BankID", c_char_Array_4),
        ("BankBrchID", c_char_Array_5),
    ]

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
        super(QryTransferBank, self).__init__()
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
        super(TransferBank, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryInvestorPositionDetail, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class InvestorPositionDetail(Struct):
    _fields_ = [
        ("InstrumentID", c_char_Array_31),
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
        ("CombInstrumentID", c_char_Array_31),
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
    ]

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
        super(InvestorPositionDetail, self).__init__()
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if Direction:
            self.Direction = Direction
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
            self.TradeType = TradeType
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
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class TradingAccountPassword(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("Password", c_char_Array_41),
        ("CurrencyID", c_char_Array_4),
    ]

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
        super(TradingAccountPassword, self).__init__()
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
    ]

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
        super(MDTraderOffer, self).__init__()
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
            self.TraderConnectStatus = TraderConnectStatus
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


class QryMDTraderOffer(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("ParticipantID", c_char_Array_11),
        ("TraderID", c_char_Array_21),
    ]

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
        super(QryMDTraderOffer, self).__init__()
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

    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        查询客户通知
        :param BrokerID: 经纪公司代码
        """
        super(QryNotice, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")


class Notice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("Content", c_char_Array_501),
        ("SequenceLabel", c_char_Array_2),
    ]

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
        super(Notice, self).__init__()
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
        super(UserRight, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserRightType:
            self.UserRightType = UserRightType
        if IsForbidden:
            self.IsForbidden = IsForbidden


class QrySettlementInfoConfirm(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("AccountID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
    ]

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
        super(QrySettlementInfoConfirm, self).__init__()
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

    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        装载结算信息
        :param BrokerID: 经纪公司代码
        """
        super(LoadSettlementInfo, self).__init__()
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
        super(BrokerWithdrawAlgorithm, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if WithdrawAlgorithm:
            self.WithdrawAlgorithm = WithdrawAlgorithm
        if UsingRatio:
            self.UsingRatio = UsingRatio
        if IncludeCloseProfit:
            self.IncludeCloseProfit = IncludeCloseProfit
        if AllWithoutTrade:
            self.AllWithoutTrade = AllWithoutTrade
        if AvailIncludeCloseProfit:
            self.AvailIncludeCloseProfit = AvailIncludeCloseProfit
        if IsBrokerUserEvent:
            self.IsBrokerUserEvent = IsBrokerUserEvent
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if FundMortgageRatio:
            self.FundMortgageRatio = FundMortgageRatio
        if BalanceAlgorithm:
            self.BalanceAlgorithm = BalanceAlgorithm


class TradingAccountPasswordUpdateV1(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("OldPassword", c_char_Array_41),
        ("NewPassword", c_char_Array_41),
    ]

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
        super(TradingAccountPasswordUpdateV1, self).__init__()
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
        super(TradingAccountPasswordUpdate, self).__init__()
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
        ("CombInstrumentID", c_char_Array_31),
        ("LegID", c_int),
        ("LegInstrumentID", c_char_Array_31),
    ]

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
        super(QryCombinationLeg, self).__init__()
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")
        if LegID:
            self.LegID = LegID
        if LegInstrumentID:
            self.LegInstrumentID = LegInstrumentID.encode("GBK")


class QrySyncStatus(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
    ]

    def __init__(
        self,
        TradingDay: str = None,
    ):
        """
        查询组合合约分腿
        :param TradingDay: 交易日
        """
        super(QrySyncStatus, self).__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")


class CombinationLeg(Struct):
    _fields_ = [
        ("CombInstrumentID", c_char_Array_31),
        ("LegID", c_int),
        ("LegInstrumentID", c_char_Array_31),
        ("Direction", c_char),
        ("LegMultiple", c_int),
        ("ImplyLevel", c_int),
    ]

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
        super(CombinationLeg, self).__init__()
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")
        if LegID:
            self.LegID = LegID
        if LegInstrumentID:
            self.LegInstrumentID = LegInstrumentID.encode("GBK")
        if Direction:
            self.Direction = Direction
        if LegMultiple:
            self.LegMultiple = LegMultiple
        if ImplyLevel:
            self.ImplyLevel = ImplyLevel


class SyncStatus(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("DataSyncStatus", c_char),
    ]

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
        super(SyncStatus, self).__init__()
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if DataSyncStatus:
            self.DataSyncStatus = DataSyncStatus


class QryLinkMan(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

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
        super(QryLinkMan, self).__init__()
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
        super(LinkMan, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if PersonType:
            self.PersonType = PersonType
        if IdentifiedCardType:
            self.IdentifiedCardType = IdentifiedCardType
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
        super(QryBrokerUserEvent, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserEventType:
            self.UserEventType = UserEventType


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
        ("InstrumentID", c_char_Array_31),
    ]

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
        super(BrokerUserEvent, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if UserEventType:
            self.UserEventType = UserEventType
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
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class QryContractBank(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("BankID", c_char_Array_4),
        ("BankBrchID", c_char_Array_5),
    ]

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
        super(QryContractBank, self).__init__()
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
        super(ContractBank, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("TotalAmt", c_int),
        ("Margin", c_double),
        ("ExchMargin", c_double),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("LegID", c_int),
        ("LegMultiple", c_int),
        ("CombInstrumentID", c_char_Array_31),
        ("TradeGroupID", c_int),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(InvestorPositionCombineDetail, self).__init__()
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
            self.HedgeFlag = HedgeFlag
        if Direction:
            self.Direction = Direction
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
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")
        if TradeGroupID:
            self.TradeGroupID = TradeGroupID
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class ParkedOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ParkedOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType
        if Direction:
            self.Direction = Direction
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason
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
            self.UserType = UserType
        if Status:
            self.Status = Status
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        ("InstrumentID", c_char_Array_31),
        ("ParkedOrderActionID", c_char_Array_13),
        ("UserType", c_char),
        ("Status", c_char),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ParkedOrderAction, self).__init__()
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
            self.ActionFlag = ActionFlag
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeChange:
            self.VolumeChange = VolumeChange
        if UserID:
            self.UserID = UserID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ParkedOrderActionID:
            self.ParkedOrderActionID = ParkedOrderActionID.encode("GBK")
        if UserType:
            self.UserType = UserType
        if Status:
            self.Status = Status
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryParkedOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryParkedOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryParkedOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryParkedOrderAction, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class RemoveParkedOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ParkedOrderID", c_char_Array_13),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(RemoveParkedOrder, self).__init__()
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
        super(RemoveParkedOrderAction, self).__init__()
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
        super(InvestorWithdrawAlgorithm, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
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
        ("CombInstrumentID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryInvestorPositionCombineDetail, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if CombInstrumentID:
            self.CombInstrumentID = CombInstrumentID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class MarketDataAveragePrice(Struct):
    _fields_ = [
        ("AveragePrice", c_double),
    ]

    def __init__(
        self,
        AveragePrice: float = None,
    ):
        """
        成交均价
        :param AveragePrice: 当日均价
        """
        super(MarketDataAveragePrice, self).__init__()
        if AveragePrice:
            self.AveragePrice = AveragePrice


class VerifyInvestorPassword(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("Password", c_char_Array_41),
    ]

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
        super(VerifyInvestorPassword, self).__init__()
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
        ("IPAddress", c_char_Array_16),
        ("IPMask", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(UserIP, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if IPMask:
            self.IPMask = IPMask.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


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
        super(TradingNoticeInfo, self).__init__()
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
        super(TradingNotice, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
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
        super(QryTradingNotice, self).__init__()
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
        super(QryErrOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class ErrOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ErrOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType
        if Direction:
            self.Direction = Direction
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class ErrorConditionalOrder(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
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
        ("ExchangeInstID", c_char_Array_31),
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
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
    ]

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
        super(ErrorConditionalOrder, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if OrderRef:
            self.OrderRef = OrderRef.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OrderPriceType:
            self.OrderPriceType = OrderPriceType
        if Direction:
            self.Direction = Direction
        if CombOffsetFlag:
            self.CombOffsetFlag = CombOffsetFlag.encode("GBK")
        if CombHedgeFlag:
            self.CombHedgeFlag = CombHedgeFlag.encode("GBK")
        if LimitPrice:
            self.LimitPrice = LimitPrice
        if VolumeTotalOriginal:
            self.VolumeTotalOriginal = VolumeTotalOriginal
        if TimeCondition:
            self.TimeCondition = TimeCondition
        if GTDDate:
            self.GTDDate = GTDDate.encode("GBK")
        if VolumeCondition:
            self.VolumeCondition = VolumeCondition
        if MinVolume:
            self.MinVolume = MinVolume
        if ContingentCondition:
            self.ContingentCondition = ContingentCondition
        if StopPrice:
            self.StopPrice = StopPrice
        if ForceCloseReason:
            self.ForceCloseReason = ForceCloseReason
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
        if ExchangeInstID:
            self.ExchangeInstID = ExchangeInstID.encode("GBK")
        if TraderID:
            self.TraderID = TraderID.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if OrderSubmitStatus:
            self.OrderSubmitStatus = OrderSubmitStatus
        if NotifySequence:
            self.NotifySequence = NotifySequence
        if TradingDay:
            self.TradingDay = TradingDay.encode("GBK")
        if SettlementID:
            self.SettlementID = SettlementID
        if OrderSysID:
            self.OrderSysID = OrderSysID.encode("GBK")
        if OrderSource:
            self.OrderSource = OrderSource
        if OrderStatus:
            self.OrderStatus = OrderStatus
        if OrderType:
            self.OrderType = OrderType
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
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")


class QryErrOrderAction(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

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
        super(QryErrOrderAction, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("BranchID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
        ("IPAddress", c_char_Array_16),
        ("MacAddress", c_char_Array_21),
        ("ErrorID", c_int),
        ("ErrorMsg", c_char_Array_81),
    ]

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
        super(ErrOrderAction, self).__init__()
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
            self.ActionFlag = ActionFlag
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
            self.OrderActionStatus = OrderActionStatus
        if UserID:
            self.UserID = UserID.encode("GBK")
        if StatusMsg:
            self.StatusMsg = StatusMsg.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if BranchID:
            self.BranchID = BranchID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")
        if MacAddress:
            self.MacAddress = MacAddress.encode("GBK")
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")


class QryExchangeSequence(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
    ]

    def __init__(
        self,
        ExchangeID: str = None,
    ):
        """
        查询交易所状态
        :param ExchangeID: 交易所代码
        """
        super(QryExchangeSequence, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class ExchangeSequence(Struct):
    _fields_ = [
        ("ExchangeID", c_char_Array_9),
        ("SequenceNo", c_int),
        ("MarketStatus", c_char),
    ]

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
        super(ExchangeSequence, self).__init__()
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if SequenceNo:
            self.SequenceNo = SequenceNo
        if MarketStatus:
            self.MarketStatus = MarketStatus


class QueryMaxOrderVolumeWithPrice(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InstrumentID", c_char_Array_31),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("MaxVolume", c_int),
        ("Price", c_double),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QueryMaxOrderVolumeWithPrice, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if Direction:
            self.Direction = Direction
        if OffsetFlag:
            self.OffsetFlag = OffsetFlag
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if MaxVolume:
            self.MaxVolume = MaxVolume
        if Price:
            self.Price = Price
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryBrokerTradingParams(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("CurrencyID", c_char_Array_4),
        ("AccountID", c_char_Array_13),
    ]

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
        super(QryBrokerTradingParams, self).__init__()
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
        super(BrokerTradingParams, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if MarginPriceType:
            self.MarginPriceType = MarginPriceType
        if Algorithm:
            self.Algorithm = Algorithm
        if AvailIncludeCloseProfit:
            self.AvailIncludeCloseProfit = AvailIncludeCloseProfit
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if OptionRoyaltyPriceType:
            self.OptionRoyaltyPriceType = OptionRoyaltyPriceType
        if AccountID:
            self.AccountID = AccountID.encode("GBK")


class QryBrokerTradingAlgos(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_31),
    ]

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
        super(QryBrokerTradingAlgos, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")


class BrokerTradingAlgos(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_31),
        ("HandlePositionAlgoID", c_char),
        ("FindMarginRateAlgoID", c_char),
        ("HandleTradingAccountAlgoID", c_char),
    ]

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
        super(BrokerTradingAlgos, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if HandlePositionAlgoID:
            self.HandlePositionAlgoID = HandlePositionAlgoID
        if FindMarginRateAlgoID:
            self.FindMarginRateAlgoID = FindMarginRateAlgoID
        if HandleTradingAccountAlgoID:
            self.HandleTradingAccountAlgoID = HandleTradingAccountAlgoID


class QueryBrokerDeposit(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QueryBrokerDeposit, self).__init__()
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
        super(BrokerDeposit, self).__init__()
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

    def __init__(
        self,
        BrokerID: str = None,
    ):
        """
        查询保证金监管系统经纪公司密钥
        :param BrokerID: 经纪公司代码
        """
        super(QryCFMMCBrokerKey, self).__init__()
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
        super(CFMMCBrokerKey, self).__init__()
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
            self.KeyKind = KeyKind


class CFMMCTradingAccountKey(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("ParticipantID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("KeyID", c_int),
        ("CurrentKey", c_char_Array_21),
    ]

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
        super(CFMMCTradingAccountKey, self).__init__()
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
        super(QryCFMMCTradingAccountKey, self).__init__()
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
        super(BrokerUserOTPParam, self).__init__()
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
            self.OTPType = OTPType


class ManualSyncBrokerUserOTP(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("OTPType", c_char),
        ("FirstOTP", c_char_Array_41),
        ("SecondOTP", c_char_Array_41),
    ]

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
        super(ManualSyncBrokerUserOTP, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if OTPType:
            self.OTPType = OTPType
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
        super(CommRateModel, self).__init__()
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
        super(QryCommRateModel, self).__init__()
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
        super(MarginModel, self).__init__()
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
        super(QryMarginModel, self).__init__()
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
        ("InstrumentID", c_char_Array_31),
        ("Direction", c_char),
        ("HedgeFlag", c_char),
        ("Volume", c_int),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(EWarrantOffset, self).__init__()
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
            self.Direction = Direction
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if Volume:
            self.Volume = Volume
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryEWarrantOffset(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ExchangeID", c_char_Array_9),
        ("InstrumentID", c_char_Array_31),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryEWarrantOffset, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InstrumentID:
            self.InstrumentID = InstrumentID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QryInvestorProductGroupMargin(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("ProductGroupID", c_char_Array_31),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char_Array_9),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QryInvestorProductGroupMargin, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if ProductGroupID:
            self.ProductGroupID = ProductGroupID.encode("GBK")
        if HedgeFlag:
            self.HedgeFlag = HedgeFlag
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class InvestorProductGroupMargin(Struct):
    _fields_ = [
        ("ProductGroupID", c_char_Array_31),
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
    ]

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
        super(InvestorProductGroupMargin, self).__init__()
        if ProductGroupID:
            self.ProductGroupID = ProductGroupID.encode("GBK")
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
            self.HedgeFlag = HedgeFlag
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
        if InvestUnitID:
            self.InvestUnitID = InvestUnitID.encode("GBK")


class QueryCFMMCTradingAccountToken(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
        ("InvestUnitID", c_char_Array_17),
    ]

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
        super(QueryCFMMCTradingAccountToken, self).__init__()
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
        super(CFMMCTradingAccountToken, self).__init__()
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
        ("ProductID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
    ]

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
        super(QryProductGroup, self).__init__()
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")


class ProductGroup(Struct):
    _fields_ = [
        ("ProductID", c_char_Array_31),
        ("ExchangeID", c_char_Array_9),
        ("ProductGroupID", c_char_Array_31),
    ]

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
        super(ProductGroup, self).__init__()
        if ProductID:
            self.ProductID = ProductID.encode("GBK")
        if ExchangeID:
            self.ExchangeID = ExchangeID.encode("GBK")
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
        super(Bulletin, self).__init__()
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
        super(QryBulletin, self).__init__()
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
        super(ReqOpenAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.MoneyAccountStatus = MoneyAccountStatus
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if CashExchangeCode:
            self.CashExchangeCode = CashExchangeCode
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
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
        super(ReqCancelAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.MoneyAccountStatus = MoneyAccountStatus
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if CashExchangeCode:
            self.CashExchangeCode = CashExchangeCode
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
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
        super(ReqChangeAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.MoneyAccountStatus = MoneyAccountStatus
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
            self.BankAccType = BankAccType
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
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
        super(ReqTransfer, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if FutureFetchAmount:
            self.FutureFetchAmount = FutureFetchAmount
        if FeePayFlag:
            self.FeePayFlag = FeePayFlag
        if CustFee:
            self.CustFee = CustFee
        if BrokerFee:
            self.BrokerFee = BrokerFee
        if Message:
            self.Message = Message.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if TransferStatus:
            self.TransferStatus = TransferStatus
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
        super(RspTransfer, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if FutureFetchAmount:
            self.FutureFetchAmount = FutureFetchAmount
        if FeePayFlag:
            self.FeePayFlag = FeePayFlag
        if CustFee:
            self.CustFee = CustFee
        if BrokerFee:
            self.BrokerFee = BrokerFee
        if Message:
            self.Message = Message.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if TransferStatus:
            self.TransferStatus = TransferStatus
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
        super(ReqRepeal, self).__init__()
        if RepealTimeInterval:
            self.RepealTimeInterval = RepealTimeInterval
        if RepealedTimes:
            self.RepealedTimes = RepealedTimes
        if BankRepealFlag:
            self.BankRepealFlag = BankRepealFlag
        if BrokerRepealFlag:
            self.BrokerRepealFlag = BrokerRepealFlag
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if FutureFetchAmount:
            self.FutureFetchAmount = FutureFetchAmount
        if FeePayFlag:
            self.FeePayFlag = FeePayFlag
        if CustFee:
            self.CustFee = CustFee
        if BrokerFee:
            self.BrokerFee = BrokerFee
        if Message:
            self.Message = Message.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if TransferStatus:
            self.TransferStatus = TransferStatus
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
        super(RspRepeal, self).__init__()
        if RepealTimeInterval:
            self.RepealTimeInterval = RepealTimeInterval
        if RepealedTimes:
            self.RepealedTimes = RepealedTimes
        if BankRepealFlag:
            self.BankRepealFlag = BankRepealFlag
        if BrokerRepealFlag:
            self.BrokerRepealFlag = BrokerRepealFlag
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if TradeAmount:
            self.TradeAmount = TradeAmount
        if FutureFetchAmount:
            self.FutureFetchAmount = FutureFetchAmount
        if FeePayFlag:
            self.FeePayFlag = FeePayFlag
        if CustFee:
            self.CustFee = CustFee
        if BrokerFee:
            self.BrokerFee = BrokerFee
        if Message:
            self.Message = Message.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
        if OperNo:
            self.OperNo = OperNo.encode("GBK")
        if RequestID:
            self.RequestID = RequestID
        if TID:
            self.TID = TID
        if TransferStatus:
            self.TransferStatus = TransferStatus
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
        super(ReqQueryAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
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
        super(RspQueryAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
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
        super(FutureSignIO, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(RspFutureSignIn, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(ReqFutureSignOut, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(RspFutureSignOut, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(ReqQueryTradeResultBySerial, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if Reference:
            self.Reference = Reference
        if RefrenceIssureType:
            self.RefrenceIssureType = RefrenceIssureType
        if RefrenceIssure:
            self.RefrenceIssure = RefrenceIssure.encode("GBK")
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
        super(RspQueryTradeResultBySerial, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if ErrorID:
            self.ErrorID = ErrorID
        if ErrorMsg:
            self.ErrorMsg = ErrorMsg.encode("GBK")
        if Reference:
            self.Reference = Reference
        if RefrenceIssureType:
            self.RefrenceIssureType = RefrenceIssureType
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
        super(ReqDayEndFileReady, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if FileBusinessCode:
            self.FileBusinessCode = FileBusinessCode
        if Digest:
            self.Digest = Digest.encode("GBK")


class ReturnResult(Struct):
    _fields_ = [
        ("ReturnCode", c_char_Array_7),
        ("DescrInfoForReturnCode", c_char_Array_129),
    ]

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
        super(ReturnResult, self).__init__()
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
        super(VerifyFuturePassword, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(VerifyCustInfo, self).__init__()
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
        super(VerifyFuturePasswordAndCustInfo, self).__init__()
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
        super(DepositResultInform, self).__init__()
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
        super(ReqSyncKey, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(RspSyncKey, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(NotifyQueryAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
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
        super(TransferSerial, self).__init__()
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
            self.BankAccType = BankAccType
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankSerial:
            self.BankSerial = BankSerial.encode("GBK")
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerBranchID:
            self.BrokerBranchID = BrokerBranchID.encode("GBK")
        if FutureAccType:
            self.FutureAccType = FutureAccType
        if AccountID:
            self.AccountID = AccountID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")
        if FutureSerial:
            self.FutureSerial = FutureSerial
        if IdCardType:
            self.IdCardType = IdCardType
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
            self.AvailabilityFlag = AvailabilityFlag
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
        super(QryTransferSerial, self).__init__()
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
        super(NotifyFutureSignIn, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(NotifyFutureSignOut, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(NotifySyncKey, self).__init__()
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
            self.LastFragment = LastFragment
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
        super(QryAccountregister, self).__init__()
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
        super(Accountregister, self).__init__()
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
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if OpenOrDestroy:
            self.OpenOrDestroy = OpenOrDestroy
        if RegDate:
            self.RegDate = RegDate.encode("GBK")
        if OutDate:
            self.OutDate = OutDate.encode("GBK")
        if TID:
            self.TID = TID
        if CustType:
            self.CustType = CustType
        if BankAccType:
            self.BankAccType = BankAccType
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
        super(OpenAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.MoneyAccountStatus = MoneyAccountStatus
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if CashExchangeCode:
            self.CashExchangeCode = CashExchangeCode
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
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
        super(CancelAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.MoneyAccountStatus = MoneyAccountStatus
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
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if CashExchangeCode:
            self.CashExchangeCode = CashExchangeCode
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if DeviceID:
            self.DeviceID = DeviceID.encode("GBK")
        if BankSecuAccType:
            self.BankSecuAccType = BankSecuAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankSecuAcc:
            self.BankSecuAcc = BankSecuAcc.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
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
        super(ChangeAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.MoneyAccountStatus = MoneyAccountStatus
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
            self.BankAccType = BankAccType
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if BankPwdFlag:
            self.BankPwdFlag = BankPwdFlag
        if SecuPwdFlag:
            self.SecuPwdFlag = SecuPwdFlag
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
        super(SecAgentACIDMap, self).__init__()
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
        super(QrySecAgentACIDMap, self).__init__()
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
        super(UserRightsAssign, self).__init__()
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
        super(BrokerUserRightAssign, self).__init__()
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
        super(DRTransfer, self).__init__()
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
        super(FensUserInfo, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if LoginMode:
            self.LoginMode = LoginMode


class CurrTransferIdentity(Struct):
    _fields_ = [
        ("IdentityID", c_int),
    ]

    def __init__(
        self,
        IdentityID: int = None,
    ):
        """
        当前银期所属交易中心
        :param IdentityID: 交易中心代码
        """
        super(CurrTransferIdentity, self).__init__()
        if IdentityID:
            self.IdentityID = IdentityID


class LoginForbiddenUser(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("IPAddress", c_char_Array_16),
    ]

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
        super(LoginForbiddenUser, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryLoginForbiddenUser(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

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
        super(QryLoginForbiddenUser, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")


class MulticastGroupInfo(Struct):
    _fields_ = [
        ("GroupIP", c_char_Array_16),
        ("GroupPort", c_int),
        ("SourceIP", c_char_Array_16),
    ]

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
        super(MulticastGroupInfo, self).__init__()
        if GroupIP:
            self.GroupIP = GroupIP.encode("GBK")
        if GroupPort:
            self.GroupPort = GroupPort
        if SourceIP:
            self.SourceIP = SourceIP.encode("GBK")


class TradingAccountReserve(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("AccountID", c_char_Array_13),
        ("Reserve", c_double),
        ("CurrencyID", c_char_Array_4),
    ]

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
        super(TradingAccountReserve, self).__init__()
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
        ("IPAddress", c_char_Array_16),
    ]

    def __init__(
        self,
        IPAddress: str = None,
    ):
        """
        查询禁止登录IP
        :param IPAddress: IP地址
        """
        super(QryLoginForbiddenIP, self).__init__()
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryIPList(Struct):
    _fields_ = [
        ("IPAddress", c_char_Array_16),
    ]

    def __init__(
        self,
        IPAddress: str = None,
    ):
        """
        查询IP列表
        :param IPAddress: IP地址
        """
        super(QryIPList, self).__init__()
        if IPAddress:
            self.IPAddress = IPAddress.encode("GBK")


class QryUserRightsAssign(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

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
        super(QryUserRightsAssign, self).__init__()
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
        super(ReserveOpenAccountConfirm, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.MoneyAccountStatus = MoneyAccountStatus
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
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
        super(ReserveOpenAccount, self).__init__()
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
            self.LastFragment = LastFragment
        if SessionID:
            self.SessionID = SessionID
        if CustomerName:
            self.CustomerName = CustomerName.encode("GBK")
        if IdCardType:
            self.IdCardType = IdCardType
        if IdentifiedCardNo:
            self.IdentifiedCardNo = IdentifiedCardNo.encode("GBK")
        if Gender:
            self.Gender = Gender
        if CountryCode:
            self.CountryCode = CountryCode.encode("GBK")
        if CustType:
            self.CustType = CustType
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
            self.MoneyAccountStatus = MoneyAccountStatus
        if BankAccount:
            self.BankAccount = BankAccount.encode("GBK")
        if BankPassWord:
            self.BankPassWord = BankPassWord.encode("GBK")
        if InstallID:
            self.InstallID = InstallID
        if VerifyCertNoFlag:
            self.VerifyCertNoFlag = VerifyCertNoFlag
        if CurrencyID:
            self.CurrencyID = CurrencyID.encode("GBK")
        if Digest:
            self.Digest = Digest.encode("GBK")
        if BankAccType:
            self.BankAccType = BankAccType
        if BrokerIDByBank:
            self.BrokerIDByBank = BrokerIDByBank.encode("GBK")
        if TID:
            self.TID = TID
        if ReserveOpenAccStas:
            self.ReserveOpenAccStas = ReserveOpenAccStas
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
        super(AccountProperty, self).__init__()
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
            self.AccountSourceType = AccountSourceType
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

    def __init__(
        self,
        DRIdentityID: int = None,
    ):
        """
        查询当前交易中心
        :param DRIdentityID: 交易中心代码
        """
        super(QryCurrDRIdentity, self).__init__()
        if DRIdentityID:
            self.DRIdentityID = DRIdentityID


class CurrDRIdentity(Struct):
    _fields_ = [
        ("DRIdentityID", c_int),
    ]

    def __init__(
        self,
        DRIdentityID: int = None,
    ):
        """
        当前交易中心
        :param DRIdentityID: 交易中心代码
        """
        super(CurrDRIdentity, self).__init__()
        if DRIdentityID:
            self.DRIdentityID = DRIdentityID


class QrySecAgentCheckMode(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("InvestorID", c_char_Array_13),
    ]

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
        super(QrySecAgentCheckMode, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class QrySecAgentTradeInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("BrokerSecAgentID", c_char_Array_13),
    ]

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
        super(QrySecAgentTradeInfo, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if BrokerSecAgentID:
            self.BrokerSecAgentID = BrokerSecAgentID.encode("GBK")


class UserSystemInfo(Struct):
    _fields_ = [
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
        ("ClientSystemInfoLen", c_int),
        ("ClientSystemInfo", c_char_Array_273),
        ("ClientPublicIP", c_char_Array_16),
        ("ClientIPPort", c_int),
        ("ClientLoginTime", c_char_Array_9),
        ("ClientAppID", c_char_Array_33),
    ]

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
        super(UserSystemInfo, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if ClientSystemInfoLen:
            self.ClientSystemInfoLen = ClientSystemInfoLen
        if ClientSystemInfo:
            self.ClientSystemInfo = ClientSystemInfo.encode("GBK")
        if ClientPublicIP:
            self.ClientPublicIP = ClientPublicIP.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort
        if ClientLoginTime:
            self.ClientLoginTime = ClientLoginTime.encode("GBK")
        if ClientAppID:
            self.ClientAppID = ClientAppID.encode("GBK")


class ReqUserAuthMethod(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

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
        super(ReqUserAuthMethod, self).__init__()
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

    def __init__(
        self,
        UsableAuthMethod: int = None,
    ):
        """
        用户发出获取安全安全登陆方法回复
        :param UsableAuthMethod: 当前可以用的认证模式
        """
        super(RspUserAuthMethod, self).__init__()
        if UsableAuthMethod:
            self.UsableAuthMethod = UsableAuthMethod


class ReqGenUserCaptcha(Struct):
    _fields_ = [
        ("TradingDay", c_char_Array_9),
        ("BrokerID", c_char_Array_11),
        ("UserID", c_char_Array_16),
    ]

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
        super(ReqGenUserCaptcha, self).__init__()
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
        super(RspGenUserCaptcha, self).__init__()
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
        super(ReqGenUserText, self).__init__()
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

    def __init__(
        self,
        UserTextSeq: int = None,
    ):
        """
        短信验证码生成的回复
        :param UserTextSeq: 短信验证码序号
        """
        super(RspGenUserText, self).__init__()
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
        ("ClientIPAddress", c_char_Array_16),
        ("LoginRemark", c_char_Array_36),
        ("Captcha", c_char_Array_41),
        ("ClientIPPort", c_int),
    ]

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
        super(ReqUserLoginWithCaptcha, self).__init__()
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
        if ClientIPAddress:
            self.ClientIPAddress = ClientIPAddress.encode("GBK")
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if Captcha:
            self.Captcha = Captcha.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort


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
        ("ClientIPAddress", c_char_Array_16),
        ("LoginRemark", c_char_Array_36),
        ("Text", c_char_Array_41),
        ("ClientIPPort", c_int),
    ]

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
        super(ReqUserLoginWithText, self).__init__()
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
        if ClientIPAddress:
            self.ClientIPAddress = ClientIPAddress.encode("GBK")
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if Text:
            self.Text = Text.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort


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
        ("ClientIPAddress", c_char_Array_16),
        ("LoginRemark", c_char_Array_36),
        ("OTPPassword", c_char_Array_41),
        ("ClientIPPort", c_int),
    ]

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
        super(ReqUserLoginWithOTP, self).__init__()
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
        if ClientIPAddress:
            self.ClientIPAddress = ClientIPAddress.encode("GBK")
        if LoginRemark:
            self.LoginRemark = LoginRemark.encode("GBK")
        if OTPPassword:
            self.OTPPassword = OTPPassword.encode("GBK")
        if ClientIPPort:
            self.ClientIPPort = ClientIPPort


class ReqApiHandshake(Struct):
    _fields_ = [
        ("CryptoKeyVersion", c_char_Array_31),
    ]

    def __init__(
        self,
        CryptoKeyVersion: str = None,
    ):
        """
        api握手请求
        :param CryptoKeyVersion: api与front通信密钥版本号
        """
        super(ReqApiHandshake, self).__init__()
        if CryptoKeyVersion:
            self.CryptoKeyVersion = CryptoKeyVersion.encode("GBK")


class RspApiHandshake(Struct):
    _fields_ = [
        ("FrontHandshakeDataLen", c_int),
        ("FrontHandshakeData", c_char_Array_301),
        ("IsApiAuthEnabled", c_int),
    ]

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
        super(RspApiHandshake, self).__init__()
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
        super(ReqVerifyApiKey, self).__init__()
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
        super(DepartmentUser, self).__init__()
        if BrokerID:
            self.BrokerID = BrokerID.encode("GBK")
        if UserID:
            self.UserID = UserID.encode("GBK")
        if InvestorRange:
            self.InvestorRange = InvestorRange
        if InvestorID:
            self.InvestorID = InvestorID.encode("GBK")


class QueryFreq(Struct):
    _fields_ = [
        ("QueryFreq", c_int),
    ]

    def __init__(
        self,
        QueryFreq: int = None,
    ):
        """
        查询频率，每秒查询比数
        :param QueryFreq: 查询频率
        """
        super(QueryFreq, self).__init__()
        if QueryFreq:
            self.QueryFreq = QueryFreq

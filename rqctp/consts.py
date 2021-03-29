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


class RESUME_TYPE:
    RESTART = 0
    RESUME = 1
    QUICK = 2


class ExchangeProperty:  # 交易所属性
    Normal = '0'  # 正常
    GenOrderByTrade = '1'  # 根据成交生成报单


class IdCardType:  # 证件类型
    EID = '0'  # 组织机构代码
    IDCard = '1'  # 中国公民身份证
    OfficerIDCard = '2'  # 军官证
    PoliceIDCard = '3'  # 警官证
    SoldierIDCard = '4'  # 士兵证
    HouseholdRegister = '5'  # 户口簿
    Passport = '6'  # 护照
    TaiwanCompatriotIDCard = '7'  # 台胞证
    HomeComingCard = '8'  # 回乡证
    LicenseNo = '9'  # 营业执照号
    TaxNo = 'A'  # 税务登记号当地纳税ID
    HMMainlandTravelPermit = 'B'  # 港澳居民来往内地通行证
    TwMainlandTravelPermit = 'C'  # 台湾居民来往大陆通行证
    DrivingLicense = 'D'  # 驾照
    SocialID = 'F'  # 当地社保ID
    LocalID = 'G'  # 当地身份证
    BusinessRegistration = 'H'  # 商业登记证
    HKMCIDCard = 'I'  # 港澳永久性居民身份证
    AccountsPermits = 'J'  # 人行开户许可证
    FrgPrmtRdCard = 'K'  # 外国人永久居留证
    CptMngPrdLetter = 'L'  # 资管产品备案函
    OtherCard = 'x'  # 其他证件


class InvestorRange:  # 投资者范围
    All = '1'  # 所有
    Group = '2'  # 投资者组
    Single = '3'  # 单一投资者


class DepartmentRange:  # 投资者范围
    All = '1'  # 所有
    Group = '2'  # 组织架构
    Single = '3'  # 单一投资者


class DataSyncStatus:  # 数据同步状态
    Asynchronous = '1'  # 未同步
    Synchronizing = '2'  # 同步中
    Synchronized = '3'  # 已同步


class BrokerDataSyncStatus:  # 经纪公司数据同步状态
    Synchronized = '1'  # 已同步
    Synchronizing = '2'  # 同步中


class ExchangeConnectStatus:  # 交易所连接状态
    NoConnection = '1'  # 没有任何连接
    QryInstrumentSent = '2'  # 已经发出合约查询请求
    GotInformation = '9'  # 已经获取信息


class TraderConnectStatus:  # 交易所交易员连接状态
    NotConnected = '1'  # 没有任何连接
    Connected = '2'  # 已经连接
    QryInstrumentSent = '3'  # 已经发出合约查询请求
    SubPrivateFlow = '4'  # 订阅私有流


class FunctionCode:  # 功能代码
    DataAsync = '1'  # 数据异步化
    ForceUserLogout = '2'  # 强制用户登出
    UserPasswordUpdate = '3'  # 变更管理用户口令
    BrokerPasswordUpdate = '4'  # 变更经纪公司口令
    InvestorPasswordUpdate = '5'  # 变更投资者口令
    OrderInsert = '6'  # 报单插入
    OrderAction = '7'  # 报单操作
    SyncSystemData = '8'  # 同步系统数据
    SyncBrokerData = '9'  # 同步经纪公司数据
    BachSyncBrokerData = 'A'  # 批量同步经纪公司数据
    SuperQuery = 'B'  # 超级查询
    ParkedOrderInsert = 'C'  # 预埋报单插入
    ParkedOrderAction = 'D'  # 预埋报单操作
    SyncOTP = 'E'  # 同步动态令牌
    DeleteOrder = 'F'  # 删除未知单


class BrokerFunctionCode:  # 经纪公司功能代码
    ForceUserLogout = '1'  # 强制用户登出
    UserPasswordUpdate = '2'  # 变更用户口令
    SyncBrokerData = '3'  # 同步经纪公司数据
    BachSyncBrokerData = '4'  # 批量同步经纪公司数据
    OrderInsert = '5'  # 报单插入
    OrderAction = '6'  # 报单操作
    AllQuery = '7'  # 全部查询
    log = 'a'  # 系统功能：登入登出修改密码等
    BaseQry = 'b'  # 基本查询：查询基础数据，如合约，交易所等常量
    TradeQry = 'c'  # 交易查询：如查成交，委托
    Trade = 'd'  # 交易功能：报单，撤单
    Virement = 'e'  # 银期转账
    Risk = 'f'  # 风险监控
    Session = 'g'  # 查询管理：查询会话，踢人等
    RiskNoticeCtl = 'h'  # 风控通知控制
    RiskNotice = 'i'  # 风控通知发送
    BrokerDeposit = 'j'  # 察看经纪公司资金权限
    QueryFund = 'k'  # 资金查询
    QueryOrder = 'l'  # 报单查询
    QueryTrade = 'm'  # 成交查询
    QueryPosition = 'n'  # 持仓查询
    QueryMarketData = 'o'  # 行情查询
    QueryUserEvent = 'p'  # 用户事件查询
    QueryRiskNotify = 'q'  # 风险通知查询
    QueryFundChange = 'r'  # 出入金查询
    QueryInvestor = 's'  # 投资者信息查询
    QueryTradingCode = 't'  # 交易编码查询
    ForceClose = 'u'  # 强平
    PressTest = 'v'  # 压力测试
    RemainCalc = 'w'  # 权益反算
    NetPositionInd = 'x'  # 净持仓保证金指标
    RiskPredict = 'y'  # 风险预算
    DataExport = 'z'  # 数据导出
    RiskTargetSetup = 'A'  # 风控指标设置
    MarketDataWarn = 'B'  # 行情预警
    QryBizNotice = 'C'  # 业务通知查询
    CfgBizNotice = 'D'  # 业务通知模板设置
    SyncOTP = 'E'  # 同步动态令牌
    SendBizNotice = 'F'  # 发送业务通知
    CfgRiskLevelStd = 'G'  # 风险级别标准设置
    TbCommand = 'H'  # 交易终端应急功能
    DeleteOrder = 'J'  # 删除未知单
    ParkedOrderInsert = 'K'  # 预埋报单插入
    ParkedOrderAction = 'L'  # 预埋报单操作
    ExecOrderNoCheck = 'M'  # 资金不够仍允许行权
    Designate = 'N'  # 指定
    StockDisposal = 'O'  # 证券处置
    BrokerDepositWarn = 'Q'  # 席位资金预警
    CoverWarn = 'S'  # 备兑不足预警
    PreExecOrder = 'T'  # 行权试算
    ExecOrderRisk = 'P'  # 行权交收风险
    PosiLimitWarn = 'U'  # 持仓限额预警
    QryPosiLimit = 'V'  # 持仓限额查询
    FBSign = 'W'  # 银期签到签退
    FBAccount = 'X'  # 银期签约解约


class OrderActionStatus:  # 报单操作状态
    Submitted = 'a'  # 已经提交
    Accepted = 'b'  # 已经接受
    Rejected = 'c'  # 已经被拒绝


class OrderStatus:  # 报单状态
    AllTraded = '0'  # 全部成交
    PartTradedQueueing = '1'  # 部分成交还在队列中
    PartTradedNotQueueing = '2'  # 部分成交不在队列中
    NoTradeQueueing = '3'  # 未成交还在队列中
    NoTradeNotQueueing = '4'  # 未成交不在队列中
    Canceled = '5'  # 撤单
    Unknown = 'a'  # 未知
    NotTouched = 'b'  # 尚未触发
    Touched = 'c'  # 已触发


class OrderSubmitStatus:  # 报单提交状态
    InsertSubmitted = '0'  # 已经提交
    CancelSubmitted = '1'  # 撤单已经提交
    ModifySubmitted = '2'  # 修改已经提交
    Accepted = '3'  # 已经接受
    InsertRejected = '4'  # 报单已经被拒绝
    CancelRejected = '5'  # 撤单已经被拒绝
    ModifyRejected = '6'  # 改单已经被拒绝


class PositionDate:  # 持仓日期
    Today = '1'  # 今日持仓
    History = '2'  # 历史持仓


class PositionDateType:  # 持仓日期类型
    UseHistory = '1'  # 使用历史持仓
    NoUseHistory = '2'  # 不使用历史持仓


class TradingRole:  # 交易角色
    Broker = '1'  # 代理
    Host = '2'  # 自营
    Maker = '3'  # 做市商


class ProductClass:  # 产品类型
    Futures = '1'  # 期货
    Options = '2'  # 期货期权
    Combination = '3'  # 组合
    Spot = '4'  # 即期
    EFP = '5'  # 期转现
    SpotOption = '6'  # 现货期权


class InstLifePhase:  # 合约生命周期状态
    NotStart = '0'  # 未上市
    Started = '1'  # 上市
    Pause = '2'  # 停牌
    Expired = '3'  # 到期


class Direction:  # 买卖方向
    Buy = '0'  # 买
    Sell = '1'  # 卖


class PositionType:  # 持仓类型
    Net = '1'  # 净持仓
    Gross = '2'  # 综合持仓


class PosiDirection:  # 持仓多空方向
    Net = '1'  # 净
    Long = '2'  # 多头
    Short = '3'  # 空头


class SysSettlementStatus:  # 系统结算状态
    NonActive = '1'  # 不活跃
    Startup = '2'  # 启动
    Operating = '3'  # 操作
    Settlement = '4'  # 结算
    SettlementFinished = '5'  # 结算完成


class RatioAttr:  # 费率属性
    Trade = '0'  # 交易费率
    Settlement = '1'  # 结算费率


class HedgeFlag:  # 投机套保标志
    Speculation = '1'  # 投机
    Arbitrage = '2'  # 套利
    Hedge = '3'  # 套保
    MarketMaker = '5'  # 做市商
    SpecHedge = '6'  # 第一腿投机第二腿套保 大商所专用
    HedgeSpec = '7'  # 第一腿套保第二腿投机  大商所专用


class BillHedgeFlag:  # 投机套保标志
    Speculation = '1'  # 投机
    Arbitrage = '2'  # 套利
    Hedge = '3'  # 套保


class ClientIDType:  # 交易编码类型
    Speculation = '1'  # 投机
    Arbitrage = '2'  # 套利
    Hedge = '3'  # 套保
    MarketMaker = '5'  # 做市商


class OrderPriceType:  # 报单价格条件
    AnyPrice = '1'  # 任意价
    LimitPrice = '2'  # 限价
    BestPrice = '3'  # 最优价
    LastPrice = '4'  # 最新价
    LastPricePlusOneTicks = '5'  # 最新价浮动上浮1个ticks
    LastPricePlusTwoTicks = '6'  # 最新价浮动上浮2个ticks
    LastPricePlusThreeTicks = '7'  # 最新价浮动上浮3个ticks
    AskPrice1 = '8'  # 卖一价
    AskPrice1PlusOneTicks = '9'  # 卖一价浮动上浮1个ticks
    AskPrice1PlusTwoTicks = 'A'  # 卖一价浮动上浮2个ticks
    AskPrice1PlusThreeTicks = 'B'  # 卖一价浮动上浮3个ticks
    BidPrice1 = 'C'  # 买一价
    BidPrice1PlusOneTicks = 'D'  # 买一价浮动上浮1个ticks
    BidPrice1PlusTwoTicks = 'E'  # 买一价浮动上浮2个ticks
    BidPrice1PlusThreeTicks = 'F'  # 买一价浮动上浮3个ticks
    FiveLevelPrice = 'G'  # 五档价


class OffsetFlag:  # 开平标志
    Open = '0'  # 开仓
    Close = '1'  # 平仓
    ForceClose = '2'  # 强平
    CloseToday = '3'  # 平今
    CloseYesterday = '4'  # 平昨
    ForceOff = '5'  # 强减
    LocalForceClose = '6'  # 本地强平


class ForceCloseReason:  # 强平原因
    NotForceClose = '0'  # 非强平
    LackDeposit = '1'  # 资金不足
    ClientOverPositionLimit = '2'  # 客户超仓
    MemberOverPositionLimit = '3'  # 会员超仓
    NotMultiple = '4'  # 持仓非整数倍
    Violation = '5'  # 违规
    Other = '6'  # 其它
    PersonDeliv = '7'  # 自然人临近交割


class OrderType:  # 报单类型
    Normal = '0'  # 正常
    DeriveFromQuote = '1'  # 报价衍生
    DeriveFromCombination = '2'  # 组合衍生
    Combination = '3'  # 组合报单
    ConditionalOrder = '4'  # 条件单
    Swap = '5'  # 互换单
    DeriveFromBlockTrade = '6'  # 大宗交易成交衍生
    DeriveFromEFPTrade = '7'  # 期转现成交衍生


class TimeCondition:  # 有效期类型
    IOC = '1'  # 立即完成，否则撤销
    GFS = '2'  # 本节有效
    GFD = '3'  # 当日有效
    GTD = '4'  # 指定日期前有效
    GTC = '5'  # 撤销前有效
    GFA = '6'  # 集合竞价有效


class VolumeCondition:  # 成交量类型
    AV = '1'  # 任何数量
    MV = '2'  # 最小数量
    CV = '3'  # 全部数量


class ContingentCondition:  # 触发条件
    Immediately = '1'  # 立即
    Touch = '2'  # 止损
    TouchProfit = '3'  # 止赢
    ParkedOrder = '4'  # 预埋单
    LastPriceGreaterThanStopPrice = '5'  # 最新价大于条件价
    LastPriceGreaterEqualStopPrice = '6'  # 最新价大于等于条件价
    LastPriceLesserThanStopPrice = '7'  # 最新价小于条件价
    LastPriceLesserEqualStopPrice = '8'  # 最新价小于等于条件价
    AskPriceGreaterThanStopPrice = '9'  # 卖一价大于条件价
    AskPriceGreaterEqualStopPrice = 'A'  # 卖一价大于等于条件价
    AskPriceLesserThanStopPrice = 'B'  # 卖一价小于条件价
    AskPriceLesserEqualStopPrice = 'C'  # 卖一价小于等于条件价
    BidPriceGreaterThanStopPrice = 'D'  # 买一价大于条件价
    BidPriceGreaterEqualStopPrice = 'E'  # 买一价大于等于条件价
    BidPriceLesserThanStopPrice = 'F'  # 买一价小于条件价
    BidPriceLesserEqualStopPrice = 'H'  # 买一价小于等于条件价


class ActionFlag:  # 操作标志
    Delete = '0'  # 删除
    Modify = '3'  # 修改


class TradingRight:  # 交易权限
    Allow = '0'  # 可以交易
    CloseOnly = '1'  # 只能平仓
    Forbidden = '2'  # 不能交易


class OrderSource:  # 报单来源
    Participant = '0'  # 来自参与者
    Administrator = '1'  # 来自管理员


class TradeType:  # 成交类型
    SplitCombination = '#'  # 组合持仓拆分为单一持仓,初始化不应包含该类型的持仓
    Common = '0'  # 普通成交
    OptionsExecution = '1'  # 期权执行
    OTC = '2'  # OTC成交
    EFPDerived = '3'  # 期转现衍生成交
    CombinationDerived = '4'  # 组合衍生成交
    BlockTrade = '5'  # 大宗交易成交


class PriceSource:  # 成交价来源
    LastPrice = '0'  # 前成交价
    Buy = '1'  # 买委托价
    Sell = '2'  # 卖委托价
    OTC = '3'  # 场外成交价


class InstrumentStatus:  # 合约交易状态
    BeforeTrading = '0'  # 开盘前
    NoTrading = '1'  # 非交易
    Continous = '2'  # 连续交易
    AuctionOrdering = '3'  # 集合竞价报单
    AuctionBalance = '4'  # 集合竞价价格平衡
    AuctionMatch = '5'  # 集合竞价撮合
    Closed = '6'  # 收盘


class InstStatusEnterReason:  # 品种进入交易状态原因
    Automatic = '1'  # 自动切换
    Manual = '2'  # 手动切换
    Fuse = '3'  # 熔断


class BatchStatus:  # 处理状态
    NoUpload = '1'  # 未上传
    Uploaded = '2'  # 已上传
    Failed = '3'  # 审核失败


class ReturnStyle:  # 按品种返还方式
    All = '1'  # 按所有品种
    ByProduct = '2'  # 按品种


class ReturnPattern:  # 返还模式
    ByVolume = '1'  # 按成交手数
    ByFeeOnHand = '2'  # 按留存手续费


class ReturnLevel:  # 返还级别
    Level1 = '1'  # 级别1
    Level2 = '2'  # 级别2
    Level3 = '3'  # 级别3
    Level4 = '4'  # 级别4
    Level5 = '5'  # 级别5
    Level6 = '6'  # 级别6
    Level7 = '7'  # 级别7
    Level8 = '8'  # 级别8
    Level9 = '9'  # 级别9


class ReturnStandard:  # 返还标准
    ByPeriod = '1'  # 分阶段返还
    ByStandard = '2'  # 按某一标准


class MortgageType:  # 质押类型
    Out = '0'  # 质出
    In = '1'  # 质入


class InvestorSettlementParamID:  # 投资者结算参数代码
    MortgageRatio = '4'  # 质押比例
    MarginWay = '5'  # 保证金算法
    BillDeposit = '9'  # 结算单结存是否包含质押


class ExchangeSettlementParamID:  # 交易所结算参数代码
    MortgageRatio = '1'  # 质押比例
    OtherFundItem = '2'  # 分项资金导入项
    OtherFundImport = '3'  # 分项资金入交易所出入金
    CFFEXMinPrepa = '6'  # 中金所开户最低可用金额
    CZCESettlementType = '7'  # 郑商所结算方式
    ExchDelivFeeMode = '9'  # 交易所交割手续费收取方式
    DelivFeeMode = '0'  # 投资者交割手续费收取方式
    CZCEComMarginType = 'A'  # 郑商所组合持仓保证金收取方式
    DceComMarginType = 'B'  # 大商所套利保证金是否优惠
    OptOutDisCountRate = 'a'  # 虚值期权保证金优惠比率
    OptMiniGuarantee = 'b'  # 最低保障系数


class SystemParamID:  # 系统参数代码
    InvestorIDMinLength = '1'  # 投资者代码最小长度
    AccountIDMinLength = '2'  # 投资者帐号代码最小长度
    UserRightLogon = '3'  # 投资者开户默认登录权限
    SettlementBillTrade = '4'  # 投资者交易结算单成交汇总方式
    TradingCode = '5'  # 统一开户更新交易编码方式
    CheckFund = '6'  # 结算是否判断存在未复核的出入金和分项资金
    CommModelRight = '7'  # 是否启用手续费模板数据权限
    MarginModelRight = '9'  # 是否启用保证金率模板数据权限
    IsStandardActive = '8'  # 是否规范用户才能激活
    UploadSettlementFile = 'U'  # 上传的交易所结算文件路径
    DownloadCSRCFile = 'D'  # 上报保证金监控中心文件路径
    SettlementBillFile = 'S'  # 生成的结算单文件路径
    CSRCOthersFile = 'C'  # 证监会文件标识
    InvestorPhoto = 'P'  # 投资者照片路径
    CSRCData = 'R'  # 全结经纪公司上传文件路径
    InvestorPwdModel = 'I'  # 开户密码录入方式
    CFFEXInvestorSettleFile = 'F'  # 投资者中金所结算文件下载路径
    InvestorIDType = 'a'  # 投资者代码编码方式
    FreezeMaxReMain = 'r'  # 休眠户最高权益
    IsSync = 'A'  # 手续费相关操作实时上场开关
    RelieveOpenLimit = 'O'  # 解除开仓权限限制
    IsStandardFreeze = 'X'  # 是否规范用户才能休眠
    CZCENormalProductHedge = 'B'  # 郑商所是否开放所有品种套保交易


class TradeParamID:  # 交易系统参数代码
    EncryptionStandard = 'E'  # 系统加密算法
    RiskMode = 'R'  # 系统风险算法
    RiskModeGlobal = 'G'  # 系统风险算法是否全局 0-否 1-是
    modeEncode = 'P'  # 密码加密算法
    tickMode = 'T'  # 价格小数位数参数
    SingleUserSessionMaxNum = 'S'  # 用户最大会话数
    LoginFailMaxNum = 'L'  # 最大连续登录失败数
    IsAuthForce = 'A'  # 是否强制认证
    IsPosiFreeze = 'F'  # 是否冻结证券持仓
    IsPosiLimit = 'M'  # 是否限仓
    ForQuoteTimeInterval = 'Q'  # 郑商所询价时间间隔
    IsFuturePosiLimit = 'B'  # 是否期货限仓
    IsFutureOrderFreq = 'C'  # 是否期货下单频率限制
    IsExecOrderProfit = 'H'  # 行权冻结是否计算盈利
    IsCheckBankAcc = 'I'  # 银期开户是否验证开户银行卡号是否是预留银行账户
    PasswordDeadLine = 'J'  # 弱密码最后修改日期
    IsStrongPassword = 'K'  # 强密码校验
    BalanceMorgage = 'a'  # 自有资金质押比
    MinPwdLen = 'O'  # 最小密码长度
    LoginFailMaxNumForIP = 'U'  # IP当日最大登陆失败次数
    PasswordPeriod = 'V'  # 密码有效期


class FileID:  # 文件标识
    SettlementFund = 'F'  # 资金数据
    Trade = 'T'  # 成交数据
    InvestorPosition = 'P'  # 投资者持仓数据
    SubEntryFund = 'O'  # 投资者分项资金数据
    CZCECombinationPos = 'C'  # 组合持仓数据
    CSRCData = 'R'  # 上报保证金监控中心数据
    CZCEClose = 'L'  # 郑商所平仓了结数据
    CZCENoClose = 'N'  # 郑商所非平仓了结数据
    PositionDtl = 'D'  # 持仓明细数据
    OptionStrike = 'S'  # 期权执行文件
    SettlementPriceComparison = 'M'  # 结算价比对文件
    NonTradePosChange = 'B'  # 上期所非持仓变动明细


class FileType:  # 文件上传类型
    Settlement = '0'  # 结算
    Check = '1'  # 核对


class FileFormat:  # 文件格式
    Txt = '0'  # 文本文件(.txt)
    Zip = '1'  # 压缩文件(.zip)
    DBF = '2'  # DBF文件(.dbf)


class FileUploadStatus:  # 文件状态
    SucceedUpload = '1'  # 上传成功
    FailedUpload = '2'  # 上传失败
    SucceedLoad = '3'  # 导入成功
    PartSucceedLoad = '4'  # 导入部分成功
    FailedLoad = '5'  # 导入失败


class TransferDirection:  # 移仓方向
    Out = '0'  # 移出
    In = '1'  # 移入


class SpecialCreateRule:  # 特殊的创建规则
    NoSpecialRule = '0'  # 没有特殊创建规则
    NoSpringFestival = '1'  # 不包含春节


class BasisPriceType:  # 挂牌基准价类型
    LastSettlement = '1'  # 上一合约结算价
    LaseClose = '2'  # 上一合约收盘价


class ProductLifePhase:  # 产品生命周期状态
    Active = '1'  # 活跃
    NonActive = '2'  # 不活跃
    Canceled = '3'  # 注销


class DeliveryMode:  # 交割方式
    CashDeliv = '1'  # 现金交割
    CommodityDeliv = '2'  # 实物交割


class FundIOType:  # 出入金类型
    FundIO = '1'  # 出入金
    Transfer = '2'  # 银期转帐
    SwapCurrency = '3'  # 银期换汇


class FundType:  # 资金类型
    Deposite = '1'  # 银行存款
    ItemFund = '2'  # 分项资金
    Company = '3'  # 公司调整
    InnerTransfer = '4'  # 资金内转


class FundDirection:  # 出入金方向
    In = '1'  # 入金
    Out = '2'  # 出金


class FundStatus:  # 资金状态
    Record = '1'  # 已录入
    Check = '2'  # 已复核
    Charge = '3'  # 已冲销


class PublishStatus:  # 发布状态
    _None = '1'  # 未发布
    Publishing = '2'  # 正在发布
    Published = '3'  # 已发布


class SystemStatus:  # 系统状态
    NonActive = '1'  # 不活跃
    Startup = '2'  # 启动
    Initialize = '3'  # 交易开始初始化
    Initialized = '4'  # 交易完成初始化
    Close = '5'  # 收市开始
    Closed = '6'  # 收市完成
    Settlement = '7'  # 结算


class SettlementStatus:  # 结算状态
    Initialize = '0'  # 初始
    Settlementing = '1'  # 结算中
    Settlemented = '2'  # 已结算
    Finished = '3'  # 结算完成


class InvestorType:  # 投资者类型
    Person = '0'  # 自然人
    Company = '1'  # 法人
    Fund = '2'  # 投资基金
    SpecialOrgan = '3'  # 特殊法人
    Asset = '4'  # 资管户


class BrokerType:  # 经纪公司类型
    Trade = '0'  # 交易会员
    TradeSettle = '1'  # 交易结算会员


class RiskLevel:  # 风险等级
    Low = '1'  # 低风险客户
    Normal = '2'  # 普通客户
    Focus = '3'  # 关注客户
    Risk = '4'  # 风险客户


class FeeAcceptStyle:  # 手续费收取方式
    ByTrade = '1'  # 按交易收取
    ByDeliv = '2'  # 按交割收取
    _None = '3'  # 不收
    FixFee = '4'  # 按指定手续费收取


class PasswordType:  # 密码类型
    Trade = '1'  # 交易密码
    Account = '2'  # 资金密码


class Algorithm:  # 盈亏算法
    All = '1'  # 浮盈浮亏都计算
    OnlyLost = '2'  # 浮盈不计，浮亏计
    OnlyGain = '3'  # 浮盈计，浮亏不计
    _None = '4'  # 浮盈浮亏都不计算


class IncludeCloseProfit:  # 是否包含平仓盈利
    Include = '0'  # 包含平仓盈利
    NotInclude = '2'  # 不包含平仓盈利


class AllWithoutTrade:  # 是否受可提比例限制
    Enable = '0'  # 无仓无成交不受可提比例限制
    Disable = '2'  # 受可提比例限制
    NoHoldEnable = '3'  # 无仓不受可提比例限制


class FuturePwdFlag:  # 资金密码核对标志
    UnCheck = '0'  # 不核对
    Check = '1'  # 核对


class TransferType:  # 银期转账类型
    BankToFuture = '0'  # 银行转期货
    FutureToBank = '1'  # 期货转银行


class TransferValidFlag:  # 转账有效标志
    Invalid = '0'  # 无效或失败
    Valid = '1'  # 有效
    Reverse = '2'  # 冲正


class Reason:  # 事由
    CD = '0'  # 错单
    ZT = '1'  # 资金在途
    QT = '2'  # 其它


class Sex:  # 性别
    _None = '0'  # 未知
    Man = '1'  # 男
    Woman = '2'  # 女


class UserType:  # 用户类型
    Investor = '0'  # 投资者
    Operator = '1'  # 操作员
    SuperUser = '2'  # 管理员


class RateType:  # 费率类型
    MarginRate = '2'  # 保证金率


class NoteType:  # 通知类型
    TradeSettleBill = '1'  # 交易结算单
    TradeSettleMonth = '2'  # 交易结算月报
    CallMarginNotes = '3'  # 追加保证金通知书
    ForceCloseNotes = '4'  # 强行平仓通知书
    TradeNotes = '5'  # 成交通知书
    DelivNotes = '6'  # 交割通知书


class SettlementStyle:  # 结算单方式
    Day = '1'  # 逐日盯市
    Volume = '2'  # 逐笔对冲


class SettlementBillType:  # 结算单类型
    Day = '0'  # 日报
    Month = '1'  # 月报


class UserRightType:  # 客户权限类型
    Logon = '1'  # 登录
    Transfer = '2'  # 银期转帐
    EMail = '3'  # 邮寄结算单
    Fax = '4'  # 传真结算单
    ConditionOrder = '5'  # 条件单


class MarginPriceType:  # 保证金价格类型
    PreSettlementPrice = '1'  # 昨结算价
    SettlementPrice = '2'  # 最新价
    AveragePrice = '3'  # 成交均价
    OpenPrice = '4'  # 开仓价


class BillGenStatus:  # 结算单生成状态
    _None = '0'  # 未生成
    NoGenerated = '1'  # 生成中
    Generated = '2'  # 已生成


class AlgoType:  # 算法类型
    HandlePositionAlgo = '1'  # 持仓处理算法
    FindMarginRateAlgo = '2'  # 寻找保证金率算法


class HandlePositionAlgoID:  # 持仓处理算法编号
    Base = '1'  # 基本
    DCE = '2'  # 大连商品交易所
    CZCE = '3'  # 郑州商品交易所


class FindMarginRateAlgoID:  # 寻找保证金率算法编号
    Base = '1'  # 基本
    DCE = '2'  # 大连商品交易所
    CZCE = '3'  # 郑州商品交易所


class HandleTradingAccountAlgoID:  # 资金处理算法编号
    Base = '1'  # 基本
    DCE = '2'  # 大连商品交易所
    CZCE = '3'  # 郑州商品交易所


class PersonType:  # 联系人类型
    Order = '1'  # 指定下单人
    Open = '2'  # 开户授权人
    Fund = '3'  # 资金调拨人
    Settlement = '4'  # 结算单确认人
    Company = '5'  # 法人
    Corporation = '6'  # 法人代表
    LinkMan = '7'  # 投资者联系人
    Ledger = '8'  # 分户管理资产负责人
    Trustee = '9'  # 托（保）管人
    TrusteeCorporation = 'A'  # 托（保）管机构法人代表
    TrusteeOpen = 'B'  # 托（保）管机构开户授权人
    TrusteeContact = 'C'  # 托（保）管机构联系人
    ForeignerRefer = 'D'  # 境外自然人参考证件
    CorporationRefer = 'E'  # 法人代表参考证件


class QueryInvestorRange:  # 查询范围
    All = '1'  # 所有
    Group = '2'  # 查询分类
    Single = '3'  # 单一投资者


class InvestorRiskStatus:  # 投资者风险状态
    Normal = '1'  # 正常
    Warn = '2'  # 警告
    Call = '3'  # 追保
    Force = '4'  # 强平
    Exception = '5'  # 异常


class UserEventType:  # 用户事件类型
    Login = '1'  # 登录
    Logout = '2'  # 登出
    Trading = '3'  # 交易成功
    TradingError = '4'  # 交易失败
    UpdatePassword = '5'  # 修改密码
    Authenticate = '6'  # 客户端认证
    Other = '9'  # 其他


class CloseStyle:  # 平仓方式
    Close = '0'  # 先开先平
    CloseToday = '1'  # 先平今再平昨


class StatMode:  # 统计方式
    Non = '0'  # ----
    Instrument = '1'  # 按合约统计
    Product = '2'  # 按产品统计
    Investor = '3'  # 按投资者统计


class ParkedOrderStatus:  # 预埋单状态
    NotSend = '1'  # 未发送
    Send = '2'  # 已发送
    Deleted = '3'  # 已删除


class VirDealStatus:  # 处理状态
    Dealing = '1'  # 正在处理
    DeaclSucceed = '2'  # 处理成功


class OrgSystemID:  # 原有系统代码
    Standard = '0'  # 综合交易平台
    ESunny = '1'  # 易盛系统
    KingStarV6 = '2'  # 金仕达V6系统


class VirTradeStatus:  # 交易状态
    NaturalDeal = '0'  # 正常处理中
    SucceedEnd = '1'  # 成功结束
    FailedEND = '2'  # 失败结束
    Exception = '3'  # 异常中
    ManualDeal = '4'  # 已人工异常处理
    MesException = '5'  # 通讯异常 ，请人工处理
    SysException = '6'  # 系统出错，请人工处理


class VirBankAccType:  # 银行帐户类型
    BankBook = '1'  # 存折
    BankCard = '2'  # 储蓄卡
    CreditCard = '3'  # 信用卡


class VirementStatus:  # 银行帐户类型
    Natural = '0'  # 正常
    Canceled = '9'  # 销户


class VirementAvailAbility:  # 有效标志
    NoAvailAbility = '0'  # 未确认
    AvailAbility = '1'  # 有效
    Repeal = '2'  # 冲正


class VirementTradeCode:  # 交易代码
    BankBankToFuture = '102001'  # 银行发起银行资金转期货
    BankFutureToBank = '102002'  # 银行发起期货资金转银行
    FutureBankToFuture = '202001'  # 期货发起银行资金转期货
    FutureFutureToBank = '202002'  # 期货发起期货资金转银行


class AMLGenStatus:  # Aml生成方式
    Program = '0'  # 程序生成
    HandWork = '1'  # 人工生成


class CFMMCKeyKind:  # 动态密钥类别(保证金监管)
    REQUEST = 'R'  # 主动请求更新
    AUTO = 'A'  # CFMMC自动更新
    MANUAL = 'M'  # CFMMC手动更新


class CertificationType:  # 证件类型
    IDCard = '0'  # 身份证
    Passport = '1'  # 护照
    OfficerIDCard = '2'  # 军官证
    SoldierIDCard = '3'  # 士兵证
    HomeComingCard = '4'  # 回乡证
    HouseholdRegister = '5'  # 户口簿
    LicenseNo = '6'  # 营业执照号
    InstitutionCodeCard = '7'  # 组织机构代码证
    TempLicenseNo = '8'  # 临时营业执照号
    NoEnterpriseLicenseNo = '9'  # 民办非企业登记证书
    OtherCard = 'x'  # 其他证件
    SuperDepAgree = 'a'  # 主管部门批文


class FileBusinessCode:  # 文件业务功能
    Others = '0'  # 其他
    TransferDetails = '1'  # 转账交易明细对账
    CustAccStatus = '2'  # 客户账户状态对账
    AccountTradeDetails = '3'  # 账户类交易明细对账
    FutureAccountChangeInfoDetails = '4'  # 期货账户信息变更明细对账
    CustMoneyDetail = '5'  # 客户资金台账余额明细对账
    CustCancelAccountInfo = '6'  # 客户销户结息明细对账
    CustMoneyResult = '7'  # 客户资金余额对账结果
    OthersExceptionResult = '8'  # 其它对账异常结果文件
    CustInterestNetMoneyDetails = '9'  # 客户结息净额明细
    CustMoneySendAndReceiveDetails = 'a'  # 客户资金交收明细
    CorporationMoneyTotal = 'b'  # 法人存管银行资金交收汇总
    MainbodyMoneyTotal = 'c'  # 主体间资金交收汇总
    MainPartMonitorData = 'd'  # 总分平衡监管数据
    PreparationMoney = 'e'  # 存管银行备付金余额
    BankMoneyMonitorData = 'f'  # 协办存管银行资金监管数据


class CashExchangeCode:  # 汇钞标志
    Exchange = '1'  # 汇
    Cash = '2'  # 钞


class YesNoIndicator:  # 是或否标识
    Yes = '0'  # 是
    No = '1'  # 否


class BanlanceType:  # 余额类型
    CurrentMoney = '0'  # 当前余额
    UsableMoney = '1'  # 可用余额
    FetchableMoney = '2'  # 可取余额
    FreezeMoney = '3'  # 冻结余额


class Gender:  # 性别
    Unknown = '0'  # 未知状态
    Male = '1'  # 男
    Female = '2'  # 女


class FeePayFlag:  # 费用支付标志
    BEN = '0'  # 由受益方支付费用
    OUR = '1'  # 由发送方支付费用
    SHA = '2'  # 由发送方支付发起的费用，受益方支付接受的费用


class PassWordKeyType:  # 密钥类型
    ExchangeKey = '0'  # 交换密钥
    PassWordKey = '1'  # 密码密钥
    MACKey = '2'  # MAC密钥
    MessageKey = '3'  # 报文密钥


class FBTPassWordType:  # 密码类型
    Query = '0'  # 查询
    Fetch = '1'  # 取款
    Transfer = '2'  # 转帐
    Trade = '3'  # 交易


class FBTEncryMode:  # 加密方式
    NoEncry = '0'  # 不加密
    DES = '1'  # DES
    _3DES = '2'  # 3DES


class BankRepealFlag:  # 银行冲正标志
    BankNotNeedRepeal = '0'  # 银行无需自动冲正
    BankWaitingRepeal = '1'  # 银行待自动冲正
    BankBeenRepealed = '2'  # 银行已自动冲正


class BrokerRepealFlag:  # 期商冲正标志
    BrokerNotNeedRepeal = '0'  # 期商无需自动冲正
    BrokerWaitingRepeal = '1'  # 期商待自动冲正
    BrokerBeenRepealed = '2'  # 期商已自动冲正


class InstitutionType:  # 机构类别
    Bank = '0'  # 银行
    Future = '1'  # 期商
    Store = '2'  # 券商


class LastFragment:  # 最后分片标志
    Yes = '0'  # 是最后分片
    No = '1'  # 不是最后分片


class BankAccStatus:  # 银行账户状态
    Normal = '0'  # 正常
    Freeze = '1'  # 冻结
    ReportLoss = '2'  # 挂失


class MoneyAccountStatus:  # 资金账户状态
    Normal = '0'  # 正常
    Cancel = '1'  # 销户


class ManageStatus:  # 存管状态
    Point = '0'  # 指定存管
    PrePoint = '1'  # 预指定
    CancelPoint = '2'  # 撤销指定


class SystemType:  # 应用系统类型
    FutureBankTransfer = '0'  # 银期转帐
    StockBankTransfer = '1'  # 银证转帐
    TheThirdPartStore = '2'  # 第三方存管


class TxnEndFlag:  # 银期转帐划转结果标志
    NormalProcessing = '0'  # 正常处理中
    Success = '1'  # 成功结束
    Failed = '2'  # 失败结束
    Abnormal = '3'  # 异常中
    ManualProcessedForException = '4'  # 已人工异常处理
    CommuFailedNeedManualProcess = '5'  # 通讯异常 ，请人工处理
    SysErrorNeedManualProcess = '6'  # 系统出错，请人工处理


class ProcessStatus:  # 银期转帐服务处理状态
    NotProcess = '0'  # 未处理
    StartProcess = '1'  # 开始处理
    Finished = '2'  # 处理完成


class CustType:  # 客户类型
    Person = '0'  # 自然人
    Institution = '1'  # 机构户


class FBTTransferDirection:  # 银期转帐方向
    FromBankToFuture = '1'  # 入金，银行转期货
    FromFutureToBank = '2'  # 出金，期货转银行


class OpenOrDestroy:  # 开销户类别
    Open = '1'  # 开户
    Destroy = '0'  # 销户


class AvailabilityFlag:  # 有效标志
    Invalid = '0'  # 未确认
    Valid = '1'  # 有效
    Repeal = '2'  # 冲正


class OrganType:  # 机构类型
    Bank = '1'  # 银行代理
    Future = '2'  # 交易前置
    PlateForm = '9'  # 银期转帐平台管理


class OrganLevel:  # 机构级别
    HeadQuarters = '1'  # 银行总行或期商总部
    Branch = '2'  # 银行分中心或期货公司营业部


class ProtocalID:  # 协议类型
    FutureProtocal = '0'  # 期商协议
    ICBCProtocal = '1'  # 工行协议
    ABCProtocal = '2'  # 农行协议
    CBCProtocal = '3'  # 中国银行协议
    CCBProtocal = '4'  # 建行协议
    BOCOMProtocal = '5'  # 交行协议
    FBTPlateFormProtocal = 'X'  # 银期转帐平台协议


class ConnectMode:  # 套接字连接方式
    ShortConnect = '0'  # 短连接
    LongConnect = '1'  # 长连接


class SyncMode:  # 套接字通信方式
    ASync = '0'  # 异步
    Sync = '1'  # 同步


class BankAccType:  # 银行帐号类型
    BankBook = '1'  # 银行存折
    SavingCard = '2'  # 储蓄卡
    CreditCard = '3'  # 信用卡


class FutureAccType:  # 期货公司帐号类型
    BankBook = '1'  # 银行存折
    SavingCard = '2'  # 储蓄卡
    CreditCard = '3'  # 信用卡


class OrganStatus:  # 接入机构状态
    Ready = '0'  # 启用
    CheckIn = '1'  # 签到
    CheckOut = '2'  # 签退
    CheckFileArrived = '3'  # 对帐文件到达
    CheckDetail = '4'  # 对帐
    DayEndClean = '5'  # 日终清理
    Invalid = '9'  # 注销


class CCBFeeMode:  # 建行收费模式
    ByAmount = '1'  # 按金额扣收
    ByMonth = '2'  # 按月扣收


class CommApiType:  # 通讯API类型
    Client = '1'  # 客户端
    Server = '2'  # 服务端
    UserApi = '3'  # 交易系统的UserApi


class LinkStatus:  # 连接状态
    Connected = '1'  # 已经连接
    Disconnected = '2'  # 没有连接


class PwdFlag:  # 密码核对标志
    NoCheck = '0'  # 不核对
    BlankCheck = '1'  # 明文核对
    EncryptCheck = '2'  # 密文核对


class SecuAccType:  # 期货帐号类型
    AccountID = '1'  # 资金帐号
    CardID = '2'  # 资金卡号
    SHStockholderID = '3'  # 上海股东帐号
    SZStockholderID = '4'  # 深圳股东帐号


class TransferStatus:  # 转账交易状态
    Normal = '0'  # 正常
    Repealed = '1'  # 被冲正


class SponsorType:  # 发起方
    Broker = '0'  # 期商
    Bank = '1'  # 银行


class ReqRspType:  # 请求响应类别
    Request = '0'  # 请求
    Response = '1'  # 响应


class FBTUserEventType:  # 银期转帐用户事件类型
    SignIn = '0'  # 签到
    FromBankToFuture = '1'  # 银行转期货
    FromFutureToBank = '2'  # 期货转银行
    OpenAccount = '3'  # 开户
    CancelAccount = '4'  # 销户
    ChangeAccount = '5'  # 变更银行账户
    RepealFromBankToFuture = '6'  # 冲正银行转期货
    RepealFromFutureToBank = '7'  # 冲正期货转银行
    QueryBankAccount = '8'  # 查询银行账户
    QueryFutureAccount = '9'  # 查询期货账户
    SignOut = 'A'  # 签退
    SyncKey = 'B'  # 密钥同步
    ReserveOpenAccount = 'C'  # 预约开户
    CancelReserveOpenAccount = 'D'  # 撤销预约开户
    ReserveOpenAccountConfirm = 'E'  # 预约开户确认
    Other = 'Z'  # 其他


class DBOperation:  # 记录操作类型
    Insert = '0'  # 插入
    Update = '1'  # 更新
    Delete = '2'  # 删除


class SyncFlag:  # 同步标记
    Yes = '0'  # 已同步
    No = '1'  # 未同步


class SyncType:  # 同步类型
    OneOffSync = '0'  # 一次同步
    TimerSync = '1'  # 定时同步
    TimerFullSync = '2'  # 定时完全同步


class ExDirection:  # 换汇方向
    Settlement = '0'  # 结汇
    Sale = '1'  # 售汇


class FBEResultFlag:  # 换汇成功标志
    Success = '0'  # 成功
    InsufficientBalance = '1'  # 账户余额不足
    UnknownTrading = '8'  # 交易结果未知
    Fail = 'x'  # 失败


class FBEExchStatus:  # 换汇交易状态
    Normal = '0'  # 正常
    ReExchange = '1'  # 交易重发


class FBEFileFlag:  # 换汇文件标志
    DataPackage = '0'  # 数据包
    File = '1'  # 文件


class FBEAlreadyTrade:  # 换汇已交易标志
    NotTrade = '0'  # 未交易
    Trade = '1'  # 已交易


class FBEUserEventType:  # 银期换汇用户事件类型
    SignIn = '0'  # 签到
    Exchange = '1'  # 换汇
    ReExchange = '2'  # 换汇重发
    QueryBankAccount = '3'  # 银行账户查询
    QueryExchDetial = '4'  # 换汇明细查询
    QueryExchSummary = '5'  # 换汇汇总查询
    QueryExchRate = '6'  # 换汇汇率查询
    CheckBankAccount = '7'  # 对账文件通知
    SignOut = '8'  # 签退
    Other = 'Z'  # 其他


class FBEReqFlag:  # 换汇发送标志
    UnProcessed = '0'  # 未处理
    WaitSend = '1'  # 等待发送
    SendSuccess = '2'  # 发送成功
    SendFailed = '3'  # 发送失败
    WaitReSend = '4'  # 等待重发


class NotifyClass:  # 风险通知类型
    NOERROR = '0'  # 正常
    Warn = '1'  # 警示
    Call = '2'  # 追保
    Force = '3'  # 强平
    CHUANCANG = '4'  # 穿仓
    Exception = '5'  # 异常


class ForceCloseType:  # 强平单类型
    Manual = '0'  # 手工强平
    Single = '1'  # 单一投资者辅助强平
    Group = '2'  # 批量投资者辅助强平


class RiskNotifyMethod:  # 风险通知途径
    System = '0'  # 系统通知
    SMS = '1'  # 短信通知
    EMail = '2'  # 邮件通知
    Manual = '3'  # 人工通知


class RiskNotifyStatus:  # 风险通知状态
    NotGen = '0'  # 未生成
    Generated = '1'  # 已生成未发送
    SendError = '2'  # 发送失败
    SendOk = '3'  # 已发送未接收
    Received = '4'  # 已接收未确认
    Confirmed = '5'  # 已确认


class RiskUserEvent:  # 风控用户操作事件
    ExportData = '0'  # 导出数据


class ConditionalOrderSortType:  # 条件单索引条件
    LastPriceAsc = '0'  # 使用最新价升序
    LastPriceDesc = '1'  # 使用最新价降序
    AskPriceAsc = '2'  # 使用卖价升序
    AskPriceDesc = '3'  # 使用卖价降序
    BidPriceAsc = '4'  # 使用买价升序
    BidPriceDesc = '5'  # 使用买价降序


class SendType:  # 报送状态
    NoSend = '0'  # 未发送
    Sended = '1'  # 已发送
    Generated = '2'  # 已生成
    SendFail = '3'  # 报送失败
    Success = '4'  # 接收成功
    Fail = '5'  # 接收失败
    Cancel = '6'  # 取消报送


class ClientIDStatus:  # 交易编码状态
    NoApply = '1'  # 未申请
    Submited = '2'  # 已提交申请
    Sended = '3'  # 已发送申请
    Success = '4'  # 完成
    Refuse = '5'  # 拒绝
    Cancel = '6'  # 已撤销编码


class QuestionType:  # 特有信息类型
    Radio = '1'  # 单选
    Option = '2'  # 多选
    Blank = '3'  # 填空


class BusinessType:  # 业务类型
    Request = '1'  # 请求
    Response = '2'  # 应答
    Notice = '3'  # 通知


class CfmmcReturnCode:  # 监控中心返回码
    Success = '0'  # 成功
    Working = '1'  # 该客户已经有流程在处理中
    InfoFail = '2'  # 监控中客户资料检查失败
    IDCardFail = '3'  # 监控中实名制检查失败
    OtherFail = '4'  # 其他错误


class ClientType:  # 客户类型
    All = '0'  # 所有
    Person = '1'  # 个人
    Company = '2'  # 单位
    Other = '3'  # 其他
    SpecialOrgan = '4'  # 特殊法人
    Asset = '5'  # 资管户


class ExchangeIDType:  # 交易所编号
    SHFE = 'S'  # 上海期货交易所
    CZCE = 'Z'  # 郑州商品交易所
    DCE = 'D'  # 大连商品交易所
    CFFEX = 'J'  # 中国金融期货交易所
    INE = 'N'  # 上海国际能源交易中心股份有限公司


class ExClientIDType:  # 交易编码类型
    Hedge = '1'  # 套保
    Arbitrage = '2'  # 套利
    Speculation = '3'  # 投机


class UpdateFlag:  # 更新状态
    NoUpdate = '0'  # 未更新
    Success = '1'  # 更新全部信息成功
    Fail = '2'  # 更新全部信息失败
    TCSuccess = '3'  # 更新交易编码成功
    TCFail = '4'  # 更新交易编码失败
    Cancel = '5'  # 已丢弃


class ApplyOperateID:  # 申请动作
    OpenInvestor = '1'  # 开户
    ModifyIDCard = '2'  # 修改身份信息
    ModifyNoIDCard = '3'  # 修改一般信息
    ApplyTradingCode = '4'  # 申请交易编码
    CancelTradingCode = '5'  # 撤销交易编码
    CancelInvestor = '6'  # 销户
    FreezeAccount = '8'  # 账户休眠
    ActiveFreezeAccount = '9'  # 激活休眠账户


class ApplyStatusID:  # 申请状态
    NoComplete = '1'  # 未补全
    Submited = '2'  # 已提交
    Checked = '3'  # 已审核
    Refused = '4'  # 已拒绝
    Deleted = '5'  # 已删除


class SendMethod:  # 发送方式
    ByAPI = '1'  # 文件发送
    ByFile = '2'  # 电子发送


class EventMode:  # 操作方法
    ADD = '1'  # 增加
    UPDATE = '2'  # 修改
    DELETE = '3'  # 删除
    CHECK = '4'  # 复核
    COPY = '5'  # 复制
    CANCEL = '6'  # 注销
    Reverse = '7'  # 冲销


class UOAAutoSend:  # 统一开户申请自动发送
    ASR = '1'  # 自动发送并接收
    ASNR = '2'  # 自动发送，不自动接收
    NSAR = '3'  # 不自动发送，自动接收
    NSR = '4'  # 不自动发送，也不自动接收


class FlowID:  # 流程ID
    InvestorGroupFlow = '1'  # 投资者对应投资者组设置
    InvestorRate = '2'  # 投资者手续费率设置
    InvestorCommRateModel = '3'  # 投资者手续费率模板关系设置


class CheckLevel:  # 复核级别
    Zero = '0'  # 零级复核
    One = '1'  # 一级复核
    Two = '2'  # 二级复核


class CheckStatus:  # 复核级别
    Init = '0'  # 未复核
    Checking = '1'  # 复核中
    Checked = '2'  # 已复核
    Refuse = '3'  # 拒绝
    Cancel = '4'  # 作废


class UsedStatus:  # 生效状态
    Unused = '0'  # 未生效
    Used = '1'  # 已生效
    Fail = '2'  # 生效失败


class BankAcountOrigin:  # 账户来源
    ByAccProperty = '0'  # 手工录入
    ByFBTransfer = '1'  # 银期转账


class MonthBillTradeSum:  # 结算单月报成交汇总方式
    ByInstrument = '0'  # 同日同合约
    ByDayInsPrc = '1'  # 同日同合约同价格
    ByDayIns = '2'  # 同合约


class FBTTradeCodeEnum:  # 银期交易代码枚举
    BankLaunchBankToBroker = '102001'  # 银行发起银行转期货
    BrokerLaunchBankToBroker = '202001'  # 期货发起银行转期货
    BankLaunchBrokerToBank = '102002'  # 银行发起期货转银行
    BrokerLaunchBrokerToBank = '202002'  # 期货发起期货转银行


class OTPType:  # 动态令牌类型
    NONE = '0'  # 无动态令牌
    TOTP = '1'  # 时间令牌


class OTPStatus:  # 动态令牌状态
    Unused = '0'  # 未使用
    Used = '1'  # 已使用
    Disuse = '2'  # 注销


class BrokerUserType:  # 经济公司用户类型
    Investor = '1'  # 投资者
    BrokerUser = '2'  # 操作员


class FutureType:  # 期货类型
    Commodity = '1'  # 商品期货
    Financial = '2'  # 金融期货


class FundEventType:  # 资金管理操作类型
    Restriction = '0'  # 转账限额
    TodayRestriction = '1'  # 当日转账限额
    Transfer = '2'  # 期商流水
    Credit = '3'  # 资金冻结
    InvestorWithdrawAlm = '4'  # 投资者可提资金比例
    BankRestriction = '5'  # 单个银行帐户转账限额
    Accountregister = '6'  # 银期签约账户
    ExchangeFundIO = '7'  # 交易所出入金
    InvestorFundIO = '8'  # 投资者出入金


class AccountSourceType:  # 资金账户来源
    FBTransfer = '0'  # 银期同步
    ManualEntry = '1'  # 手工录入


class CodeSourceType:  # 交易编码来源
    UnifyAccount = '0'  # 统一开户(已规范)
    ManualEntry = '1'  # 手工录入(未规范)


class UserRange:  # 操作员范围
    All = '0'  # 所有
    Single = '1'  # 单一操作员


class ByGroup:  # 交易统计表按客户统计方式
    Investor = '2'  # 按投资者统计
    Group = '1'  # 按类统计


class TradeSumStatMode:  # 交易统计表按范围统计方式
    Instrument = '1'  # 按合约统计
    Product = '2'  # 按产品统计
    Exchange = '3'  # 按交易所统计


class ExprSetMode:  # 日期表达式设置类型
    Relative = '1'  # 相对已有规则设置
    Typical = '2'  # 典型设置


class RateInvestorRange:  # 投资者范围
    All = '1'  # 公司标准
    Model = '2'  # 模板
    Single = '3'  # 单一投资者


class SyncDataStatus:  # 主次用系统数据同步状态
    Initialize = '0'  # 未同步
    Settlementing = '1'  # 同步中
    Settlemented = '2'  # 已同步


class TradeSource:  # 成交来源
    NORMAL = '0'  # 来自交易所普通回报
    QUERY = '1'  # 来自查询


class FlexStatMode:  # 产品合约统计方式
    Product = '1'  # 产品统计
    Exchange = '2'  # 交易所统计
    All = '3'  # 统计所有


class ByInvestorRange:  # 投资者范围统计方式
    Property = '1'  # 属性统计
    All = '2'  # 统计所有


class PropertyInvestorRange:  # 投资者范围
    All = '1'  # 所有
    Property = '2'  # 投资者属性
    Single = '3'  # 单一投资者


class FileStatus:  # 文件状态
    NoCreate = '0'  # 未生成
    Created = '1'  # 已生成
    Failed = '2'  # 生成失败


class FileGenStyle:  # 文件生成方式
    FileTransmit = '0'  # 下发
    FileGen = '1'  # 生成


class SysOperMode:  # 系统日志操作方法
    Add = '1'  # 增加
    Update = '2'  # 修改
    Delete = '3'  # 删除
    Copy = '4'  # 复制
    AcTive = '5'  # 激活
    CanCel = '6'  # 注销
    ReSet = '7'  # 重置


class SysOperType:  # 系统日志操作类型
    UpdatePassword = '0'  # 修改操作员密码
    UserDepartment = '1'  # 操作员组织架构关系
    RoleManager = '2'  # 角色管理
    RoleFunction = '3'  # 角色功能设置
    BaseParam = '4'  # 基础参数设置
    SetUserID = '5'  # 设置操作员
    SetUserRole = '6'  # 用户角色设置
    UserIpRestriction = '7'  # 用户IP限制
    DepartmentManager = '8'  # 组织架构管理
    DepartmentCopy = '9'  # 组织架构向查询分类复制
    Tradingcode = 'A'  # 交易编码管理
    InvestorStatus = 'B'  # 投资者状态维护
    InvestorAuthority = 'C'  # 投资者权限管理
    PropertySet = 'D'  # 属性设置
    ReSetInvestorPasswd = 'E'  # 重置投资者密码
    InvestorPersonalityInfo = 'F'  # 投资者个性信息维护


class CSRCDataQueyType:  # 上报数据查询类型
    Current = '0'  # 查询当前交易日报送的数据
    History = '1'  # 查询历史报送的代理经纪公司的数据


class FreezeStatus:  # 休眠状态
    Normal = '1'  # 活跃
    Freeze = '0'  # 休眠


class StandardStatus:  # 规范状态
    Standard = '0'  # 已规范
    NonStandard = '1'  # 未规范


class RightParamType:  # 配置类型
    Freeze = '1'  # 休眠户
    FreezeActive = '2'  # 激活休眠户
    OpenLimit = '3'  # 开仓权限限制
    RelieveOpenLimit = '4'  # 解除开仓权限限制


class DataStatus:  # 反洗钱审核表数据状态
    Normal = '0'  # 正常
    Deleted = '1'  # 已删除


class AMLCheckStatus:  # 审核状态
    Init = '0'  # 未复核
    Checking = '1'  # 复核中
    Checked = '2'  # 已复核
    RefuseReport = '3'  # 拒绝上报


class AmlDateType:  # 日期类型
    DrawDay = '0'  # 检查日期
    TouchDay = '1'  # 发生日期


class AmlCheckLevel:  # 审核级别
    CheckLevel0 = '0'  # 零级审核
    CheckLevel1 = '1'  # 一级审核
    CheckLevel2 = '2'  # 二级审核
    CheckLevel3 = '3'  # 三级审核


class ExportFileType:  # 导出文件类型
    CSV = '0'  # CSV
    EXCEL = '1'  # Excel
    DBF = '2'  # DBF


class SettleManagerType:  # 结算配置类型
    Before = '1'  # 结算前准备
    Settlement = '2'  # 结算
    After = '3'  # 结算后核对
    Settlemented = '4'  # 结算后处理


class SettleManagerLevel:  # 结算配置等级
    Must = '1'  # 必要
    Alarm = '2'  # 警告
    Prompt = '3'  # 提示
    Ignore = '4'  # 不检查


class SettleManagerGroup:  # 模块分组
    Exhcange = '1'  # 交易所核对
    ASP = '2'  # 内部核对
    CSRC = '3'  # 上报数据核对


class LimitUseType:  # 保值额度使用类型
    Repeatable = '1'  # 可重复使用
    Unrepeatable = '2'  # 不可重复使用


class DataResource:  # 数据来源
    Settle = '1'  # 本系统
    Exchange = '2'  # 交易所
    CSRC = '3'  # 报送数据


class MarginType:  # 保证金类型
    ExchMarginRate = '0'  # 交易所保证金率
    InstrMarginRate = '1'  # 投资者保证金率
    InstrMarginRateTrade = '2'  # 投资者交易保证金率


class ActiveType:  # 生效类型
    Intraday = '1'  # 仅当日生效
    Long = '2'  # 长期生效


class MarginRateType:  # 冲突保证金率类型
    Exchange = '1'  # 交易所保证金率
    Investor = '2'  # 投资者保证金率
    InvestorTrade = '3'  # 投资者交易保证金率


class BackUpStatus:  # 备份数据状态
    UnBak = '0'  # 未生成备份数据
    BakUp = '1'  # 备份数据生成中
    BakUped = '2'  # 已生成备份数据
    BakFail = '3'  # 备份数据失败


class InitSettlement:  # 结算初始化状态
    UnInitialize = '0'  # 结算初始化未开始
    Initialize = '1'  # 结算初始化中
    Initialized = '2'  # 结算初始化完成


class ReportStatus:  # 报表数据生成状态
    NoCreate = '0'  # 未生成报表数据
    Create = '1'  # 报表数据生成中
    Created = '2'  # 已生成报表数据
    CreateFail = '3'  # 生成报表数据失败


class SaveStatus:  # 数据归档状态
    UnSaveData = '0'  # 归档未完成
    SaveDatad = '1'  # 归档完成


class SettArchiveStatus:  # 结算确认数据归档状态
    UnArchived = '0'  # 未归档数据
    Archiving = '1'  # 数据归档中
    Archived = '2'  # 已归档数据
    ArchiveFail = '3'  # 归档数据失败


class CTPType:  # CTP交易系统类型
    Unkown = '0'  # 未知
    MainCenter = '1'  # 主中心
    BackUp = '2'  # 备中心


class CloseDealType:  # 平仓处理类型
    Normal = '0'  # 正常
    SpecFirst = '1'  # 投机平仓优先


class MortgageFundUseRange:  # 货币质押资金可用范围
    _None = '0'  # 不能使用
    Margin = '1'  # 用于保证金
    All = '2'  # 用于手续费、盈亏、保证金
    CNY3 = '3'  # 人民币方案3


class SpecProductType:  # 特殊产品类型
    CzceHedge = '1'  # 郑商所套保产品
    IneForeignCurrency = '2'  # 货币质押产品
    DceOpenClose = '3'  # 大连短线开平仓产品


class FundMortgageType:  # 货币质押类型
    Mortgage = '1'  # 质押
    Redemption = '2'  # 解质


class AccountSettlementParamID:  # 投资者账户结算参数代码
    BaseMargin = '1'  # 基础保证金
    LowestInterest = '2'  # 最低权益标准


class FundMortDirection:  # 货币质押方向
    In = '1'  # 货币质入
    Out = '2'  # 货币质出


class BusinessClass:  # 换汇类别
    Profit = '0'  # 盈利
    Loss = '1'  # 亏损
    Other = 'Z'  # 其他


class SwapSourceType:  # 换汇数据来源
    Manual = '0'  # 手工
    Automatic = '1'  # 自动生成


class CurrExDirection:  # 换汇类型
    Settlement = '0'  # 结汇
    Sale = '1'  # 售汇


class CurrencySwapStatus:  # 申请状态
    Entry = '1'  # 已录入
    Approve = '2'  # 已审核
    Refuse = '3'  # 已拒绝
    Revoke = '4'  # 已撤销
    Send = '5'  # 已发送
    Success = '6'  # 换汇成功
    Failure = '7'  # 换汇失败


class ReqFlag:  # 换汇发送标志
    NoSend = '0'  # 未发送
    SendSuccess = '1'  # 发送成功
    SendFailed = '2'  # 发送失败
    WaitReSend = '3'  # 等待重发


class ResFlag:  # 换汇返回成功标志
    Success = '0'  # 成功
    InsuffiCient = '1'  # 账户余额不足
    UnKnown = '8'  # 交易结果未知


class ExStatus:  # 修改状态
    Before = '0'  # 修改前
    After = '1'  # 修改后


class ClientRegion:  # 开户客户地域
    Domestic = '1'  # 国内客户
    GMT = '2'  # 港澳台客户
    Foreign = '3'  # 国外客户


class HasBoard:  # 是否有董事会
    No = '0'  # 没有
    Yes = '1'  # 有


class StartMode:  # 启动模式
    Normal = '1'  # 正常
    Emerge = '2'  # 应急
    Restore = '3'  # 恢复


class TemplateType:  # 模型类型
    Full = '1'  # 全量
    Increment = '2'  # 增量
    BackUp = '3'  # 备份


class LoginMode:  # 登录模式
    Trade = '0'  # 交易
    Transfer = '1'  # 转账


class PromptType:  # 日历提示类型
    Instrument = '1'  # 合约上下市
    Margin = '2'  # 保证金分段生效


class HasTrustee:  # 是否有托管人
    Yes = '1'  # 有
    No = '0'  # 没有


class AmType:  # 机构类型
    Bank = '1'  # 银行
    Securities = '2'  # 证券公司
    Fund = '3'  # 基金公司
    Insurance = '4'  # 保险公司
    Trust = '5'  # 信托公司
    Other = '9'  # 其他


class CSRCFundIOType:  # 出入金类型
    FundIO = '0'  # 出入金
    SwapCurrency = '1'  # 银期换汇


class CusAccountType:  # 结算账户类型
    Futures = '1'  # 期货结算账户
    AssetmgrFuture = '2'  # 纯期货资管业务下的资管结算账户
    AssetmgrTrustee = '3'  # 综合类资管业务下的期货资管托管账户
    AssetmgrTransfer = '4'  # 综合类资管业务下的资金中转账户


class LanguageType:  # 通知语言类型
    Chinese = '1'  # 中文
    English = '2'  # 英文


class AssetmgrClientType:  # 资产管理客户类型
    Person = '1'  # 个人资管客户
    Organ = '2'  # 单位资管客户
    SpecialOrgan = '4'  # 特殊单位资管客户


class AssetmgrType:  # 投资类型
    Futures = '3'  # 期货类
    SpecialOrgan = '4'  # 综合类


class CheckInstrType:  # 合约比较类型
    HasExch = '0'  # 合约交易所不存在
    HasATP = '1'  # 合约本系统不存在
    HasDiff = '2'  # 合约比较不一致


class DeliveryType:  # 交割类型
    HandDeliv = '1'  # 手工交割
    PersonDeliv = '2'  # 到期交割


class MaxMarginSideAlgorithm:  # 大额单边保证金算法
    NO = '0'  # 不使用大额单边保证金算法
    YES = '1'  # 使用大额单边保证金算法


class DAClientType:  # 资产管理客户类型
    Person = '0'  # 自然人
    Company = '1'  # 法人
    Other = '2'  # 其他


class UOAAssetmgrType:  # 投资类型
    Futures = '1'  # 期货类
    SpecialOrgan = '2'  # 综合类


class DirectionEn:  # 买卖方向
    Buy = '0'  # Buy
    Sell = '1'  # Sell


class OffsetFlagEn:  # 开平标志
    Open = '0'  # Position Opening
    Close = '1'  # Position Close
    ForceClose = '2'  # Forced Liquidation
    CloseToday = '3'  # Close Today
    CloseYesterday = '4'  # Close Prev.
    ForceOff = '5'  # Forced Reduction
    LocalForceClose = '6'  # Local Forced Liquidation


class HedgeFlagEn:  # 投机套保标志
    Speculation = '1'  # Speculation
    Arbitrage = '2'  # Arbitrage
    Hedge = '3'  # Hedge


class FundIOTypeEn:  # 出入金类型
    FundIO = '1'  # DepositWithdrawal
    Transfer = '2'  # Bank-Futures Transfer
    SwapCurrency = '3'  # Bank-Futures FX Exchange


class FundTypeEn:  # 资金类型
    Deposite = '1'  # Bank Deposit
    ItemFund = '2'  # PaymentFee
    Company = '3'  # Brokerage Adj
    InnerTransfer = '4'  # Internal Transfer


class FundDirectionEn:  # 出入金方向
    In = '1'  # Deposit
    Out = '2'  # Withdrawal


class FundMortDirectionEn:  # 货币质押方向
    In = '1'  # Pledge
    Out = '2'  # Redemption


class OptionsType:  # 期权类型
    CallOptions = '1'  # 看涨
    PutOptions = '2'  # 看跌


class StrikeMode:  # 执行方式
    Continental = '0'  # 欧式
    American = '1'  # 美式
    Bermuda = '2'  # 百慕大


class StrikeType:  # 执行类型
    Hedge = '0'  # 自身对冲
    Match = '1'  # 匹配执行


class ApplyType:  # 中金所期权放弃执行申请类型
    NotStrikeNum = '4'  # 不执行数量


class GiveUpDataSource:  # 放弃执行申请数据来源
    Gen = '0'  # 系统生成
    Hand = '1'  # 手工添加


class ExecResult:  # 执行结果
    NoExec = 'n'  # 没有执行
    Canceled = 'c'  # 已经取消
    OK = '0'  # 执行成功
    NoPosition = '1'  # 期权持仓不够
    NoDeposit = '2'  # 资金不够
    NoParticipant = '3'  # 会员不存在
    NoClient = '4'  # 客户不存在
    NoInstrument = '6'  # 合约不存在
    NoRight = '7'  # 没有执行权限
    InvalidVolume = '8'  # 不合理的数量
    NoEnoughHistoryTrade = '9'  # 没有足够的历史成交
    Unknown = 'a'  # 未知


class CombinationType:  # 组合类型
    Future = '0'  # 期货组合
    BUL = '1'  # 垂直价差BUL
    BER = '2'  # 垂直价差BER
    STD = '3'  # 跨式组合
    STG = '4'  # 宽跨式组合
    PRT = '5'  # 备兑组合
    CLD = '6'  # 时间价差组合


class DceCombinationType:  # 组合类型
    SPL = '0'  # 期货对锁组合
    OPL = '1'  # 期权对锁组合
    SP = '2'  # 期货跨期组合
    SPC = '3'  # 期货跨品种组合
    BLS = '4'  # 买入期权垂直价差组合
    BES = '5'  # 卖出期权垂直价差组合
    CAS = '6'  # 期权日历价差组合
    STD = '7'  # 期权跨式组合
    STG = '8'  # 期权宽跨式组合
    BFO = '9'  # 买入期货期权组合
    SFO = 'a'  # 卖出期货期权组合


class OptionRoyaltyPriceType:  # 期权权利金价格类型
    PreSettlementPrice = '1'  # 昨结算价
    OpenPrice = '4'  # 开仓价
    MaxPreSettlementPrice = '5'  # 最新价与昨结算价较大值


class BalanceAlgorithm:  # 权益算法
    Default = '1'  # 不计算期权市值盈亏
    IncludeOptValLost = '2'  # 计算期权市值亏损


class ActionType:  # 执行类型
    Exec = '1'  # 执行
    Abandon = '2'  # 放弃


class ForQuoteStatus:  # 询价状态
    Submitted = 'a'  # 已经提交
    Accepted = 'b'  # 已经接受
    Rejected = 'c'  # 已经被拒绝


class ValueMethod:  # 取值方式
    Absolute = '0'  # 按绝对值
    Ratio = '1'  # 按比率


class ExecOrderPositionFlag:  # 期权行权后是否保留期货头寸的标记
    Reserve = '0'  # 保留
    UnReserve = '1'  # 不保留


class ExecOrderCloseFlag:  # 期权行权后生成的头寸是否自动平仓
    AutoClose = '0'  # 自动平仓
    NotToClose = '1'  # 免于自动平仓


class ProductType:  # 产品类型
    Futures = '1'  # 期货
    Options = '2'  # 期权


class CZCEUploadFileName:  # 郑商所结算文件名
    O = 'O'  # ^\d{8}_zz_\d{4}
    T = 'T'  # ^\d{8}成交表
    P = 'P'  # ^\d{8}单腿持仓表new
    N = 'N'  # ^\d{8}非平仓了结表
    L = 'L'  # ^\d{8}平仓表
    F = 'F'  # ^\d{8}资金表
    C = 'C'  # ^\d{8}组合持仓表
    M = 'M'  # ^\d{8}保证金参数表


class DCEUploadFileName:  # 大商所结算文件名
    O = 'O'  # ^\d{8}_dl_\d{3}
    T = 'T'  # ^\d{8}_成交表
    P = 'P'  # ^\d{8}_持仓表
    F = 'F'  # ^\d{8}_资金结算表
    C = 'C'  # ^\d{8}_优惠组合持仓明细表
    D = 'D'  # ^\d{8}_持仓明细表
    M = 'M'  # ^\d{8}_保证金参数表
    S = 'S'  # ^\d{8}_期权执行表


class SHFEUploadFileName:  # 上期所结算文件名
    O = 'O'  # ^\d{4}_\d{8}_\d{8}_DailyFundChg
    T = 'T'  # ^\d{4}_\d{8}_\d{8}_Trade
    P = 'P'  # ^\d{4}_\d{8}_\d{8}_SettlementDetail
    F = 'F'  # ^\d{4}_\d{8}_\d{8}_Capital


class CFFEXUploadFileName:  # 中金所结算文件名
    T = 'T'  # ^\d{4}_SG\d{1}_\d{8}_\d{1}_Trade
    P = 'P'  # ^\d{4}_SG\d{1}_\d{8}_\d{1}_SettlementDetail
    F = 'F'  # ^\d{4}_SG\d{1}_\d{8}_\d{1}_Capital
    S = 'S'  # ^\d{4}_SG\d{1}_\d{8}_\d{1}_OptionExec


class CombDirection:  # 组合指令方向
    Comb = '0'  # 申请组合
    UnComb = '1'  # 申请拆分


class StrikeOffsetType:  # 行权偏移类型
    RealValue = '1'  # 实值额
    ProfitValue = '2'  # 盈利额
    RealRatio = '3'  # 实值比例
    ProfitRatio = '4'  # 盈利比例


class ReserveOpenAccStas:  # 预约开户状态
    Processing = '0'  # 等待处理中
    Cancelled = '1'  # 已撤销
    Opened = '2'  # 已开户
    Invalid = '3'  # 无效请求


class WeakPasswordSource:  # 弱密码来源
    Lib = '1'  # 弱密码库
    Manual = '2'  # 手工录入


class OptSelfCloseFlag:  # 期权行权的头寸是否自对冲
    CloseSelfOptionPosition = '1'  # 自对冲期权仓位
    ReserveOptionPosition = '2'  # 保留期权仓位
    SellCloseSelfFuturePosition = '3'  # 自对冲卖方履约后的期货仓位
    ReserveFuturePosition = '4'  # 保留卖方履约后的期货仓位


class BizType:  # 业务类型
    Future = '1'  # 期货
    Stock = '2'  # 证券


class AppType:  # 用户App类型
    Investor = '1'  # 直连的投资者
    InvestorRelay = '2'  # 为每个投资者都创建连接的中继
    OperatorRelay = '3'  # 所有投资者共享一个操作员连接的中继
    UnKnown = '4'  # 未知


class ResponseValue:  # 应答类型
    Right = '0'  # 检查成功
    Refuse = '1'  # 检查失败


class OTCTradeType:  # OTC成交类型
    Block = '0'  # 大宗交易
    EFP = '1'  # 期转现


class MatchType:  # 期现风险匹配方式
    DV01 = '1'  # 基点价值
    ParValue = '2'  # 面值

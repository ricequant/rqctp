class RESUME_TYPE:
    RESTART = 0
    RESUME = 1
    QUICK = 2


class ExchangeProperty:  # 交易所属性
    Normal = b'0'  # 正常
    GenOrderByTrade = b'1'  # 根据成交生成报单


class IdCardType:  # 证件类型
    EID = b'0'  # 组织机构代码
    IDCard = b'1'  # 中国公民身份证
    OfficerIDCard = b'2'  # 军官证
    PoliceIDCard = b'3'  # 警官证
    SoldierIDCard = b'4'  # 士兵证
    HouseholdRegister = b'5'  # 户口簿
    Passport = b'6'  # 护照
    TaiwanCompatriotIDCard = b'7'  # 台胞证
    HomeComingCard = b'8'  # 回乡证
    LicenseNo = b'9'  # 营业执照号
    TaxNo = b'A'  # 税务登记号当地纳税ID
    HMMainlandTravelPermit = b'B'  # 港澳居民来往内地通行证
    TwMainlandTravelPermit = b'C'  # 台湾居民来往大陆通行证
    DrivingLicense = b'D'  # 驾照
    SocialID = b'F'  # 当地社保ID
    LocalID = b'G'  # 当地身份证
    BusinessRegistration = b'H'  # 商业登记证
    HKMCIDCard = b'I'  # 港澳永久性居民身份证
    AccountsPermits = b'J'  # 人行开户许可证
    FrgPrmtRdCard = b'K'  # 外国人永久居留证
    CptMngPrdLetter = b'L'  # 资管产品备案函
    OtherCard = b'x'  # 其他证件


class InvestorRange:  # 投资者范围
    All = b'1'  # 所有
    Group = b'2'  # 投资者组
    Single = b'3'  # 单一投资者


class DepartmentRange:  # 投资者范围
    All = b'1'  # 所有
    Group = b'2'  # 组织架构
    Single = b'3'  # 单一投资者


class DataSyncStatus:  # 数据同步状态
    Asynchronous = b'1'  # 未同步
    Synchronizing = b'2'  # 同步中
    Synchronized = b'3'  # 已同步


class BrokerDataSyncStatus:  # 经纪公司数据同步状态
    Synchronized = b'1'  # 已同步
    Synchronizing = b'2'  # 同步中


class ExchangeConnectStatus:  # 交易所连接状态
    NoConnection = b'1'  # 没有任何连接
    QryInstrumentSent = b'2'  # 已经发出合约查询请求
    GotInformation = b'9'  # 已经获取信息


class TraderConnectStatus:  # 交易所交易员连接状态
    NotConnected = b'1'  # 没有任何连接
    Connected = b'2'  # 已经连接
    QryInstrumentSent = b'3'  # 已经发出合约查询请求
    SubPrivateFlow = b'4'  # 订阅私有流


class FunctionCode:  # 功能代码
    DataAsync = b'1'  # 数据异步化
    ForceUserLogout = b'2'  # 强制用户登出
    UserPasswordUpdate = b'3'  # 变更管理用户口令
    BrokerPasswordUpdate = b'4'  # 变更经纪公司口令
    InvestorPasswordUpdate = b'5'  # 变更投资者口令
    OrderInsert = b'6'  # 报单插入
    OrderAction = b'7'  # 报单操作
    SyncSystemData = b'8'  # 同步系统数据
    SyncBrokerData = b'9'  # 同步经纪公司数据
    BachSyncBrokerData = b'A'  # 批量同步经纪公司数据
    SuperQuery = b'B'  # 超级查询
    ParkedOrderInsert = b'C'  # 预埋报单插入
    ParkedOrderAction = b'D'  # 预埋报单操作
    SyncOTP = b'E'  # 同步动态令牌
    DeleteOrder = b'F'  # 删除未知单


class BrokerFunctionCode:  # 经纪公司功能代码
    ForceUserLogout = b'1'  # 强制用户登出
    UserPasswordUpdate = b'2'  # 变更用户口令
    SyncBrokerData = b'3'  # 同步经纪公司数据
    BachSyncBrokerData = b'4'  # 批量同步经纪公司数据
    OrderInsert = b'5'  # 报单插入
    OrderAction = b'6'  # 报单操作
    AllQuery = b'7'  # 全部查询
    log = b'a'  # 系统功能：登入登出修改密码等
    BaseQry = b'b'  # 基本查询：查询基础数据，如合约，交易所等常量
    TradeQry = b'c'  # 交易查询：如查成交，委托
    Trade = b'd'  # 交易功能：报单，撤单
    Virement = b'e'  # 银期转账
    Risk = b'f'  # 风险监控
    Session = b'g'  # 查询管理：查询会话，踢人等
    RiskNoticeCtl = b'h'  # 风控通知控制
    RiskNotice = b'i'  # 风控通知发送
    BrokerDeposit = b'j'  # 察看经纪公司资金权限
    QueryFund = b'k'  # 资金查询
    QueryOrder = b'l'  # 报单查询
    QueryTrade = b'm'  # 成交查询
    QueryPosition = b'n'  # 持仓查询
    QueryMarketData = b'o'  # 行情查询
    QueryUserEvent = b'p'  # 用户事件查询
    QueryRiskNotify = b'q'  # 风险通知查询
    QueryFundChange = b'r'  # 出入金查询
    QueryInvestor = b's'  # 投资者信息查询
    QueryTradingCode = b't'  # 交易编码查询
    ForceClose = b'u'  # 强平
    PressTest = b'v'  # 压力测试
    RemainCalc = b'w'  # 权益反算
    NetPositionInd = b'x'  # 净持仓保证金指标
    RiskPredict = b'y'  # 风险预算
    DataExport = b'z'  # 数据导出
    RiskTargetSetup = b'A'  # 风控指标设置
    MarketDataWarn = b'B'  # 行情预警
    QryBizNotice = b'C'  # 业务通知查询
    CfgBizNotice = b'D'  # 业务通知模板设置
    SyncOTP = b'E'  # 同步动态令牌
    SendBizNotice = b'F'  # 发送业务通知
    CfgRiskLevelStd = b'G'  # 风险级别标准设置
    TbCommand = b'H'  # 交易终端应急功能
    DeleteOrder = b'J'  # 删除未知单
    ParkedOrderInsert = b'K'  # 预埋报单插入
    ParkedOrderAction = b'L'  # 预埋报单操作
    ExecOrderNoCheck = b'M'  # 资金不够仍允许行权
    Designate = b'N'  # 指定
    StockDisposal = b'O'  # 证券处置
    BrokerDepositWarn = b'Q'  # 席位资金预警
    CoverWarn = b'S'  # 备兑不足预警
    PreExecOrder = b'T'  # 行权试算
    ExecOrderRisk = b'P'  # 行权交收风险
    PosiLimitWarn = b'U'  # 持仓限额预警
    QryPosiLimit = b'V'  # 持仓限额查询
    FBSign = b'W'  # 银期签到签退
    FBAccount = b'X'  # 银期签约解约


class OrderActionStatus:  # 报单操作状态
    Submitted = b'a'  # 已经提交
    Accepted = b'b'  # 已经接受
    Rejected = b'c'  # 已经被拒绝


class OrderStatus:  # 报单状态
    AllTraded = b'0'  # 全部成交
    PartTradedQueueing = b'1'  # 部分成交还在队列中
    PartTradedNotQueueing = b'2'  # 部分成交不在队列中
    NoTradeQueueing = b'3'  # 未成交还在队列中
    NoTradeNotQueueing = b'4'  # 未成交不在队列中
    Canceled = b'5'  # 撤单
    Unknown = b'a'  # 未知
    NotTouched = b'b'  # 尚未触发
    Touched = b'c'  # 已触发


class OrderSubmitStatus:  # 报单提交状态
    InsertSubmitted = b'0'  # 已经提交
    CancelSubmitted = b'1'  # 撤单已经提交
    ModifySubmitted = b'2'  # 修改已经提交
    Accepted = b'3'  # 已经接受
    InsertRejected = b'4'  # 报单已经被拒绝
    CancelRejected = b'5'  # 撤单已经被拒绝
    ModifyRejected = b'6'  # 改单已经被拒绝


class PositionDate:  # 持仓日期
    Today = b'1'  # 今日持仓
    History = b'2'  # 历史持仓


class PositionDateType:  # 持仓日期类型
    UseHistory = b'1'  # 使用历史持仓
    NoUseHistory = b'2'  # 不使用历史持仓


class TradingRole:  # 交易角色
    Broker = b'1'  # 代理
    Host = b'2'  # 自营
    Maker = b'3'  # 做市商


class ProductClass:  # 产品类型
    Futures = b'1'  # 期货
    Options = b'2'  # 期货期权
    Combination = b'3'  # 组合
    Spot = b'4'  # 即期
    EFP = b'5'  # 期转现
    SpotOption = b'6'  # 现货期权


class InstLifePhase:  # 合约生命周期状态
    NotStart = b'0'  # 未上市
    Started = b'1'  # 上市
    Pause = b'2'  # 停牌
    Expired = b'3'  # 到期


class Direction:  # 买卖方向
    Buy = b'0'  # 买
    Sell = b'1'  # 卖


class PositionType:  # 持仓类型
    Net = b'1'  # 净持仓
    Gross = b'2'  # 综合持仓


class PosiDirection:  # 持仓多空方向
    Net = b'1'  # 净
    Long = b'2'  # 多头
    Short = b'3'  # 空头


class SysSettlementStatus:  # 系统结算状态
    NonActive = b'1'  # 不活跃
    Startup = b'2'  # 启动
    Operating = b'3'  # 操作
    Settlement = b'4'  # 结算
    SettlementFinished = b'5'  # 结算完成


class RatioAttr:  # 费率属性
    Trade = b'0'  # 交易费率
    Settlement = b'1'  # 结算费率


class HedgeFlag:  # 投机套保标志
    Speculation = b'1'  # 投机
    Arbitrage = b'2'  # 套利
    Hedge = b'3'  # 套保
    MarketMaker = b'5'  # 做市商
    SpecHedge = b'6'  # 第一腿投机第二腿套保 大商所专用
    HedgeSpec = b'7'  # 第一腿套保第二腿投机  大商所专用


class BillHedgeFlag:  # 投机套保标志
    Speculation = b'1'  # 投机
    Arbitrage = b'2'  # 套利
    Hedge = b'3'  # 套保


class ClientIDType:  # 交易编码类型
    Speculation = b'1'  # 投机
    Arbitrage = b'2'  # 套利
    Hedge = b'3'  # 套保
    MarketMaker = b'5'  # 做市商


class OrderPriceType:  # 报单价格条件
    AnyPrice = b'1'  # 任意价
    LimitPrice = b'2'  # 限价
    BestPrice = b'3'  # 最优价
    LastPrice = b'4'  # 最新价
    LastPricePlusOneTicks = b'5'  # 最新价浮动上浮1个ticks
    LastPricePlusTwoTicks = b'6'  # 最新价浮动上浮2个ticks
    LastPricePlusThreeTicks = b'7'  # 最新价浮动上浮3个ticks
    AskPrice1 = b'8'  # 卖一价
    AskPrice1PlusOneTicks = b'9'  # 卖一价浮动上浮1个ticks
    AskPrice1PlusTwoTicks = b'A'  # 卖一价浮动上浮2个ticks
    AskPrice1PlusThreeTicks = b'B'  # 卖一价浮动上浮3个ticks
    BidPrice1 = b'C'  # 买一价
    BidPrice1PlusOneTicks = b'D'  # 买一价浮动上浮1个ticks
    BidPrice1PlusTwoTicks = b'E'  # 买一价浮动上浮2个ticks
    BidPrice1PlusThreeTicks = b'F'  # 买一价浮动上浮3个ticks
    FiveLevelPrice = b'G'  # 五档价


class OffsetFlag:  # 开平标志
    Open = b'0'  # 开仓
    Close = b'1'  # 平仓
    ForceClose = b'2'  # 强平
    CloseToday = b'3'  # 平今
    CloseYesterday = b'4'  # 平昨
    ForceOff = b'5'  # 强减
    LocalForceClose = b'6'  # 本地强平


class ForceCloseReason:  # 强平原因
    NotForceClose = b'0'  # 非强平
    LackDeposit = b'1'  # 资金不足
    ClientOverPositionLimit = b'2'  # 客户超仓
    MemberOverPositionLimit = b'3'  # 会员超仓
    NotMultiple = b'4'  # 持仓非整数倍
    Violation = b'5'  # 违规
    Other = b'6'  # 其它
    PersonDeliv = b'7'  # 自然人临近交割


class OrderType:  # 报单类型
    Normal = b'0'  # 正常
    DeriveFromQuote = b'1'  # 报价衍生
    DeriveFromCombination = b'2'  # 组合衍生
    Combination = b'3'  # 组合报单
    ConditionalOrder = b'4'  # 条件单
    Swap = b'5'  # 互换单
    DeriveFromBlockTrade = b'6'  # 大宗交易成交衍生
    DeriveFromEFPTrade = b'7'  # 期转现成交衍生


class TimeCondition:  # 有效期类型
    IOC = b'1'  # 立即完成，否则撤销
    GFS = b'2'  # 本节有效
    GFD = b'3'  # 当日有效
    GTD = b'4'  # 指定日期前有效
    GTC = b'5'  # 撤销前有效
    GFA = b'6'  # 集合竞价有效


class VolumeCondition:  # 成交量类型
    AV = b'1'  # 任何数量
    MV = b'2'  # 最小数量
    CV = b'3'  # 全部数量


class ContingentCondition:  # 触发条件
    Immediately = b'1'  # 立即
    Touch = b'2'  # 止损
    TouchProfit = b'3'  # 止赢
    ParkedOrder = b'4'  # 预埋单
    LastPriceGreaterThanStopPrice = b'5'  # 最新价大于条件价
    LastPriceGreaterEqualStopPrice = b'6'  # 最新价大于等于条件价
    LastPriceLesserThanStopPrice = b'7'  # 最新价小于条件价
    LastPriceLesserEqualStopPrice = b'8'  # 最新价小于等于条件价
    AskPriceGreaterThanStopPrice = b'9'  # 卖一价大于条件价
    AskPriceGreaterEqualStopPrice = b'A'  # 卖一价大于等于条件价
    AskPriceLesserThanStopPrice = b'B'  # 卖一价小于条件价
    AskPriceLesserEqualStopPrice = b'C'  # 卖一价小于等于条件价
    BidPriceGreaterThanStopPrice = b'D'  # 买一价大于条件价
    BidPriceGreaterEqualStopPrice = b'E'  # 买一价大于等于条件价
    BidPriceLesserThanStopPrice = b'F'  # 买一价小于条件价
    BidPriceLesserEqualStopPrice = b'H'  # 买一价小于等于条件价


class ActionFlag:  # 操作标志
    Delete = b'0'  # 删除
    Modify = b'3'  # 修改


class TradingRight:  # 交易权限
    Allow = b'0'  # 可以交易
    CloseOnly = b'1'  # 只能平仓
    Forbidden = b'2'  # 不能交易


class OrderSource:  # 报单来源
    Participant = b'0'  # 来自参与者
    Administrator = b'1'  # 来自管理员


class TradeType:  # 成交类型
    SplitCombination = b'#'  # 组合持仓拆分为单一持仓,初始化不应包含该类型的持仓
    Common = b'0'  # 普通成交
    OptionsExecution = b'1'  # 期权执行
    OTC = b'2'  # OTC成交
    EFPDerived = b'3'  # 期转现衍生成交
    CombinationDerived = b'4'  # 组合衍生成交
    BlockTrade = b'5'  # 大宗交易成交


class PriceSource:  # 成交价来源
    LastPrice = b'0'  # 前成交价
    Buy = b'1'  # 买委托价
    Sell = b'2'  # 卖委托价
    OTC = b'3'  # 场外成交价


class InstrumentStatus:  # 合约交易状态
    BeforeTrading = b'0'  # 开盘前
    NoTrading = b'1'  # 非交易
    Continous = b'2'  # 连续交易
    AuctionOrdering = b'3'  # 集合竞价报单
    AuctionBalance = b'4'  # 集合竞价价格平衡
    AuctionMatch = b'5'  # 集合竞价撮合
    Closed = b'6'  # 收盘


class InstStatusEnterReason:  # 品种进入交易状态原因
    Automatic = b'1'  # 自动切换
    Manual = b'2'  # 手动切换
    Fuse = b'3'  # 熔断


class BatchStatus:  # 处理状态
    NoUpload = b'1'  # 未上传
    Uploaded = b'2'  # 已上传
    Failed = b'3'  # 审核失败


class ReturnStyle:  # 按品种返还方式
    All = b'1'  # 按所有品种
    ByProduct = b'2'  # 按品种


class ReturnPattern:  # 返还模式
    ByVolume = b'1'  # 按成交手数
    ByFeeOnHand = b'2'  # 按留存手续费


class ReturnLevel:  # 返还级别
    Level1 = b'1'  # 级别1
    Level2 = b'2'  # 级别2
    Level3 = b'3'  # 级别3
    Level4 = b'4'  # 级别4
    Level5 = b'5'  # 级别5
    Level6 = b'6'  # 级别6
    Level7 = b'7'  # 级别7
    Level8 = b'8'  # 级别8
    Level9 = b'9'  # 级别9


class ReturnStandard:  # 返还标准
    ByPeriod = b'1'  # 分阶段返还
    ByStandard = b'2'  # 按某一标准


class MortgageType:  # 质押类型
    Out = b'0'  # 质出
    In = b'1'  # 质入


class InvestorSettlementParamID:  # 投资者结算参数代码
    MortgageRatio = b'4'  # 质押比例
    MarginWay = b'5'  # 保证金算法
    BillDeposit = b'9'  # 结算单结存是否包含质押


class ExchangeSettlementParamID:  # 交易所结算参数代码
    MortgageRatio = b'1'  # 质押比例
    OtherFundItem = b'2'  # 分项资金导入项
    OtherFundImport = b'3'  # 分项资金入交易所出入金
    CFFEXMinPrepa = b'6'  # 中金所开户最低可用金额
    CZCESettlementType = b'7'  # 郑商所结算方式
    ExchDelivFeeMode = b'9'  # 交易所交割手续费收取方式
    DelivFeeMode = b'0'  # 投资者交割手续费收取方式
    CZCEComMarginType = b'A'  # 郑商所组合持仓保证金收取方式
    DceComMarginType = b'B'  # 大商所套利保证金是否优惠
    OptOutDisCountRate = b'a'  # 虚值期权保证金优惠比率
    OptMiniGuarantee = b'b'  # 最低保障系数


class SystemParamID:  # 系统参数代码
    InvestorIDMinLength = b'1'  # 投资者代码最小长度
    AccountIDMinLength = b'2'  # 投资者帐号代码最小长度
    UserRightLogon = b'3'  # 投资者开户默认登录权限
    SettlementBillTrade = b'4'  # 投资者交易结算单成交汇总方式
    TradingCode = b'5'  # 统一开户更新交易编码方式
    CheckFund = b'6'  # 结算是否判断存在未复核的出入金和分项资金
    CommModelRight = b'7'  # 是否启用手续费模板数据权限
    MarginModelRight = b'9'  # 是否启用保证金率模板数据权限
    IsStandardActive = b'8'  # 是否规范用户才能激活
    UploadSettlementFile = b'U'  # 上传的交易所结算文件路径
    DownloadCSRCFile = b'D'  # 上报保证金监控中心文件路径
    SettlementBillFile = b'S'  # 生成的结算单文件路径
    CSRCOthersFile = b'C'  # 证监会文件标识
    InvestorPhoto = b'P'  # 投资者照片路径
    CSRCData = b'R'  # 全结经纪公司上传文件路径
    InvestorPwdModel = b'I'  # 开户密码录入方式
    CFFEXInvestorSettleFile = b'F'  # 投资者中金所结算文件下载路径
    InvestorIDType = b'a'  # 投资者代码编码方式
    FreezeMaxReMain = b'r'  # 休眠户最高权益
    IsSync = b'A'  # 手续费相关操作实时上场开关
    RelieveOpenLimit = b'O'  # 解除开仓权限限制
    IsStandardFreeze = b'X'  # 是否规范用户才能休眠
    CZCENormalProductHedge = b'B'  # 郑商所是否开放所有品种套保交易


class TradeParamID:  # 交易系统参数代码
    EncryptionStandard = b'E'  # 系统加密算法
    RiskMode = b'R'  # 系统风险算法
    RiskModeGlobal = b'G'  # 系统风险算法是否全局 0-否 1-是
    modeEncode = b'P'  # 密码加密算法
    tickMode = b'T'  # 价格小数位数参数
    SingleUserSessionMaxNum = b'S'  # 用户最大会话数
    LoginFailMaxNum = b'L'  # 最大连续登录失败数
    IsAuthForce = b'A'  # 是否强制认证
    IsPosiFreeze = b'F'  # 是否冻结证券持仓
    IsPosiLimit = b'M'  # 是否限仓
    ForQuoteTimeInterval = b'Q'  # 郑商所询价时间间隔
    IsFuturePosiLimit = b'B'  # 是否期货限仓
    IsFutureOrderFreq = b'C'  # 是否期货下单频率限制
    IsExecOrderProfit = b'H'  # 行权冻结是否计算盈利
    IsCheckBankAcc = b'I'  # 银期开户是否验证开户银行卡号是否是预留银行账户
    PasswordDeadLine = b'J'  # 弱密码最后修改日期
    IsStrongPassword = b'K'  # 强密码校验
    BalanceMorgage = b'a'  # 自有资金质押比
    MinPwdLen = b'O'  # 最小密码长度
    LoginFailMaxNumForIP = b'U'  # IP当日最大登陆失败次数
    PasswordPeriod = b'V'  # 密码有效期


class FileID:  # 文件标识
    SettlementFund = b'F'  # 资金数据
    Trade = b'T'  # 成交数据
    InvestorPosition = b'P'  # 投资者持仓数据
    SubEntryFund = b'O'  # 投资者分项资金数据
    CZCECombinationPos = b'C'  # 组合持仓数据
    CSRCData = b'R'  # 上报保证金监控中心数据
    CZCEClose = b'L'  # 郑商所平仓了结数据
    CZCENoClose = b'N'  # 郑商所非平仓了结数据
    PositionDtl = b'D'  # 持仓明细数据
    OptionStrike = b'S'  # 期权执行文件
    SettlementPriceComparison = b'M'  # 结算价比对文件
    NonTradePosChange = b'B'  # 上期所非持仓变动明细


class FileType:  # 文件上传类型
    Settlement = b'0'  # 结算
    Check = b'1'  # 核对


class FileFormat:  # 文件格式
    Txt = b'0'  # 文本文件(.txt)
    Zip = b'1'  # 压缩文件(.zip)
    DBF = b'2'  # DBF文件(.dbf)


class FileUploadStatus:  # 文件状态
    SucceedUpload = b'1'  # 上传成功
    FailedUpload = b'2'  # 上传失败
    SucceedLoad = b'3'  # 导入成功
    PartSucceedLoad = b'4'  # 导入部分成功
    FailedLoad = b'5'  # 导入失败


class TransferDirection:  # 移仓方向
    Out = b'0'  # 移出
    In = b'1'  # 移入


class SpecialCreateRule:  # 特殊的创建规则
    NoSpecialRule = b'0'  # 没有特殊创建规则
    NoSpringFestival = b'1'  # 不包含春节


class BasisPriceType:  # 挂牌基准价类型
    LastSettlement = b'1'  # 上一合约结算价
    LaseClose = b'2'  # 上一合约收盘价


class ProductLifePhase:  # 产品生命周期状态
    Active = b'1'  # 活跃
    NonActive = b'2'  # 不活跃
    Canceled = b'3'  # 注销


class DeliveryMode:  # 交割方式
    CashDeliv = b'1'  # 现金交割
    CommodityDeliv = b'2'  # 实物交割


class FundIOType:  # 出入金类型
    FundIO = b'1'  # 出入金
    Transfer = b'2'  # 银期转帐
    SwapCurrency = b'3'  # 银期换汇


class FundType:  # 资金类型
    Deposite = b'1'  # 银行存款
    ItemFund = b'2'  # 分项资金
    Company = b'3'  # 公司调整
    InnerTransfer = b'4'  # 资金内转


class FundDirection:  # 出入金方向
    In = b'1'  # 入金
    Out = b'2'  # 出金


class FundStatus:  # 资金状态
    Record = b'1'  # 已录入
    Check = b'2'  # 已复核
    Charge = b'3'  # 已冲销


class PublishStatus:  # 发布状态
    _None = b'1'  # 未发布
    Publishing = b'2'  # 正在发布
    Published = b'3'  # 已发布


class SystemStatus:  # 系统状态
    NonActive = b'1'  # 不活跃
    Startup = b'2'  # 启动
    Initialize = b'3'  # 交易开始初始化
    Initialized = b'4'  # 交易完成初始化
    Close = b'5'  # 收市开始
    Closed = b'6'  # 收市完成
    Settlement = b'7'  # 结算


class SettlementStatus:  # 结算状态
    Initialize = b'0'  # 初始
    Settlementing = b'1'  # 结算中
    Settlemented = b'2'  # 已结算
    Finished = b'3'  # 结算完成


class InvestorType:  # 投资者类型
    Person = b'0'  # 自然人
    Company = b'1'  # 法人
    Fund = b'2'  # 投资基金
    SpecialOrgan = b'3'  # 特殊法人
    Asset = b'4'  # 资管户


class BrokerType:  # 经纪公司类型
    Trade = b'0'  # 交易会员
    TradeSettle = b'1'  # 交易结算会员


class RiskLevel:  # 风险等级
    Low = b'1'  # 低风险客户
    Normal = b'2'  # 普通客户
    Focus = b'3'  # 关注客户
    Risk = b'4'  # 风险客户


class FeeAcceptStyle:  # 手续费收取方式
    ByTrade = b'1'  # 按交易收取
    ByDeliv = b'2'  # 按交割收取
    _None = b'3'  # 不收
    FixFee = b'4'  # 按指定手续费收取


class PasswordType:  # 密码类型
    Trade = b'1'  # 交易密码
    Account = b'2'  # 资金密码


class Algorithm:  # 盈亏算法
    All = b'1'  # 浮盈浮亏都计算
    OnlyLost = b'2'  # 浮盈不计，浮亏计
    OnlyGain = b'3'  # 浮盈计，浮亏不计
    _None = b'4'  # 浮盈浮亏都不计算


class IncludeCloseProfit:  # 是否包含平仓盈利
    Include = b'0'  # 包含平仓盈利
    NotInclude = b'2'  # 不包含平仓盈利


class AllWithoutTrade:  # 是否受可提比例限制
    Enable = b'0'  # 无仓无成交不受可提比例限制
    Disable = b'2'  # 受可提比例限制
    NoHoldEnable = b'3'  # 无仓不受可提比例限制


class FuturePwdFlag:  # 资金密码核对标志
    UnCheck = b'0'  # 不核对
    Check = b'1'  # 核对


class TransferType:  # 银期转账类型
    BankToFuture = b'0'  # 银行转期货
    FutureToBank = b'1'  # 期货转银行


class TransferValidFlag:  # 转账有效标志
    Invalid = b'0'  # 无效或失败
    Valid = b'1'  # 有效
    Reverse = b'2'  # 冲正


class Reason:  # 事由
    CD = b'0'  # 错单
    ZT = b'1'  # 资金在途
    QT = b'2'  # 其它


class Sex:  # 性别
    _None = b'0'  # 未知
    Man = b'1'  # 男
    Woman = b'2'  # 女


class UserType:  # 用户类型
    Investor = b'0'  # 投资者
    Operator = b'1'  # 操作员
    SuperUser = b'2'  # 管理员


class RateType:  # 费率类型
    MarginRate = b'2'  # 保证金率


class NoteType:  # 通知类型
    TradeSettleBill = b'1'  # 交易结算单
    TradeSettleMonth = b'2'  # 交易结算月报
    CallMarginNotes = b'3'  # 追加保证金通知书
    ForceCloseNotes = b'4'  # 强行平仓通知书
    TradeNotes = b'5'  # 成交通知书
    DelivNotes = b'6'  # 交割通知书


class SettlementStyle:  # 结算单方式
    Day = b'1'  # 逐日盯市
    Volume = b'2'  # 逐笔对冲


class SettlementBillType:  # 结算单类型
    Day = b'0'  # 日报
    Month = b'1'  # 月报


class UserRightType:  # 客户权限类型
    Logon = b'1'  # 登录
    Transfer = b'2'  # 银期转帐
    EMail = b'3'  # 邮寄结算单
    Fax = b'4'  # 传真结算单
    ConditionOrder = b'5'  # 条件单


class MarginPriceType:  # 保证金价格类型
    PreSettlementPrice = b'1'  # 昨结算价
    SettlementPrice = b'2'  # 最新价
    AveragePrice = b'3'  # 成交均价
    OpenPrice = b'4'  # 开仓价


class BillGenStatus:  # 结算单生成状态
    _None = b'0'  # 未生成
    NoGenerated = b'1'  # 生成中
    Generated = b'2'  # 已生成


class AlgoType:  # 算法类型
    HandlePositionAlgo = b'1'  # 持仓处理算法
    FindMarginRateAlgo = b'2'  # 寻找保证金率算法


class HandlePositionAlgoID:  # 持仓处理算法编号
    Base = b'1'  # 基本
    DCE = b'2'  # 大连商品交易所
    CZCE = b'3'  # 郑州商品交易所


class FindMarginRateAlgoID:  # 寻找保证金率算法编号
    Base = b'1'  # 基本
    DCE = b'2'  # 大连商品交易所
    CZCE = b'3'  # 郑州商品交易所


class HandleTradingAccountAlgoID:  # 资金处理算法编号
    Base = b'1'  # 基本
    DCE = b'2'  # 大连商品交易所
    CZCE = b'3'  # 郑州商品交易所


class PersonType:  # 联系人类型
    Order = b'1'  # 指定下单人
    Open = b'2'  # 开户授权人
    Fund = b'3'  # 资金调拨人
    Settlement = b'4'  # 结算单确认人
    Company = b'5'  # 法人
    Corporation = b'6'  # 法人代表
    LinkMan = b'7'  # 投资者联系人
    Ledger = b'8'  # 分户管理资产负责人
    Trustee = b'9'  # 托（保）管人
    TrusteeCorporation = b'A'  # 托（保）管机构法人代表
    TrusteeOpen = b'B'  # 托（保）管机构开户授权人
    TrusteeContact = b'C'  # 托（保）管机构联系人
    ForeignerRefer = b'D'  # 境外自然人参考证件
    CorporationRefer = b'E'  # 法人代表参考证件


class QueryInvestorRange:  # 查询范围
    All = b'1'  # 所有
    Group = b'2'  # 查询分类
    Single = b'3'  # 单一投资者


class InvestorRiskStatus:  # 投资者风险状态
    Normal = b'1'  # 正常
    Warn = b'2'  # 警告
    Call = b'3'  # 追保
    Force = b'4'  # 强平
    Exception = b'5'  # 异常


class UserEventType:  # 用户事件类型
    Login = b'1'  # 登录
    Logout = b'2'  # 登出
    Trading = b'3'  # 交易成功
    TradingError = b'4'  # 交易失败
    UpdatePassword = b'5'  # 修改密码
    Authenticate = b'6'  # 客户端认证
    Other = b'9'  # 其他


class CloseStyle:  # 平仓方式
    Close = b'0'  # 先开先平
    CloseToday = b'1'  # 先平今再平昨


class StatMode:  # 统计方式
    Non = b'0'  # ----
    Instrument = b'1'  # 按合约统计
    Product = b'2'  # 按产品统计
    Investor = b'3'  # 按投资者统计


class ParkedOrderStatus:  # 预埋单状态
    NotSend = b'1'  # 未发送
    Send = b'2'  # 已发送
    Deleted = b'3'  # 已删除


class VirDealStatus:  # 处理状态
    Dealing = b'1'  # 正在处理
    DeaclSucceed = b'2'  # 处理成功


class OrgSystemID:  # 原有系统代码
    Standard = b'0'  # 综合交易平台
    ESunny = b'1'  # 易盛系统
    KingStarV6 = b'2'  # 金仕达V6系统


class VirTradeStatus:  # 交易状态
    NaturalDeal = b'0'  # 正常处理中
    SucceedEnd = b'1'  # 成功结束
    FailedEND = b'2'  # 失败结束
    Exception = b'3'  # 异常中
    ManualDeal = b'4'  # 已人工异常处理
    MesException = b'5'  # 通讯异常 ，请人工处理
    SysException = b'6'  # 系统出错，请人工处理


class VirBankAccType:  # 银行帐户类型
    BankBook = b'1'  # 存折
    BankCard = b'2'  # 储蓄卡
    CreditCard = b'3'  # 信用卡


class VirementStatus:  # 银行帐户类型
    Natural = b'0'  # 正常
    Canceled = b'9'  # 销户


class VirementAvailAbility:  # 有效标志
    NoAvailAbility = b'0'  # 未确认
    AvailAbility = b'1'  # 有效
    Repeal = b'2'  # 冲正


class VirementTradeCode:  # 交易代码
    BankBankToFuture = b'102001'  # 银行发起银行资金转期货
    BankFutureToBank = b'102002'  # 银行发起期货资金转银行
    FutureBankToFuture = b'202001'  # 期货发起银行资金转期货
    FutureFutureToBank = b'202002'  # 期货发起期货资金转银行


class AMLGenStatus:  # Aml生成方式
    Program = b'0'  # 程序生成
    HandWork = b'1'  # 人工生成


class CFMMCKeyKind:  # 动态密钥类别(保证金监管)
    REQUEST = b'R'  # 主动请求更新
    AUTO = b'A'  # CFMMC自动更新
    MANUAL = b'M'  # CFMMC手动更新


class CertificationType:  # 证件类型
    IDCard = b'0'  # 身份证
    Passport = b'1'  # 护照
    OfficerIDCard = b'2'  # 军官证
    SoldierIDCard = b'3'  # 士兵证
    HomeComingCard = b'4'  # 回乡证
    HouseholdRegister = b'5'  # 户口簿
    LicenseNo = b'6'  # 营业执照号
    InstitutionCodeCard = b'7'  # 组织机构代码证
    TempLicenseNo = b'8'  # 临时营业执照号
    NoEnterpriseLicenseNo = b'9'  # 民办非企业登记证书
    OtherCard = b'x'  # 其他证件
    SuperDepAgree = b'a'  # 主管部门批文


class FileBusinessCode:  # 文件业务功能
    Others = b'0'  # 其他
    TransferDetails = b'1'  # 转账交易明细对账
    CustAccStatus = b'2'  # 客户账户状态对账
    AccountTradeDetails = b'3'  # 账户类交易明细对账
    FutureAccountChangeInfoDetails = b'4'  # 期货账户信息变更明细对账
    CustMoneyDetail = b'5'  # 客户资金台账余额明细对账
    CustCancelAccountInfo = b'6'  # 客户销户结息明细对账
    CustMoneyResult = b'7'  # 客户资金余额对账结果
    OthersExceptionResult = b'8'  # 其它对账异常结果文件
    CustInterestNetMoneyDetails = b'9'  # 客户结息净额明细
    CustMoneySendAndReceiveDetails = b'a'  # 客户资金交收明细
    CorporationMoneyTotal = b'b'  # 法人存管银行资金交收汇总
    MainbodyMoneyTotal = b'c'  # 主体间资金交收汇总
    MainPartMonitorData = b'd'  # 总分平衡监管数据
    PreparationMoney = b'e'  # 存管银行备付金余额
    BankMoneyMonitorData = b'f'  # 协办存管银行资金监管数据


class CashExchangeCode:  # 汇钞标志
    Exchange = b'1'  # 汇
    Cash = b'2'  # 钞


class YesNoIndicator:  # 是或否标识
    Yes = b'0'  # 是
    No = b'1'  # 否


class BanlanceType:  # 余额类型
    CurrentMoney = b'0'  # 当前余额
    UsableMoney = b'1'  # 可用余额
    FetchableMoney = b'2'  # 可取余额
    FreezeMoney = b'3'  # 冻结余额


class Gender:  # 性别
    Unknown = b'0'  # 未知状态
    Male = b'1'  # 男
    Female = b'2'  # 女


class FeePayFlag:  # 费用支付标志
    BEN = b'0'  # 由受益方支付费用
    OUR = b'1'  # 由发送方支付费用
    SHA = b'2'  # 由发送方支付发起的费用，受益方支付接受的费用


class PassWordKeyType:  # 密钥类型
    ExchangeKey = b'0'  # 交换密钥
    PassWordKey = b'1'  # 密码密钥
    MACKey = b'2'  # MAC密钥
    MessageKey = b'3'  # 报文密钥


class FBTPassWordType:  # 密码类型
    Query = b'0'  # 查询
    Fetch = b'1'  # 取款
    Transfer = b'2'  # 转帐
    Trade = b'3'  # 交易


class FBTEncryMode:  # 加密方式
    NoEncry = b'0'  # 不加密
    DES = b'1'  # DES
    _3DES = b'2'  # 3DES


class BankRepealFlag:  # 银行冲正标志
    BankNotNeedRepeal = b'0'  # 银行无需自动冲正
    BankWaitingRepeal = b'1'  # 银行待自动冲正
    BankBeenRepealed = b'2'  # 银行已自动冲正


class BrokerRepealFlag:  # 期商冲正标志
    BrokerNotNeedRepeal = b'0'  # 期商无需自动冲正
    BrokerWaitingRepeal = b'1'  # 期商待自动冲正
    BrokerBeenRepealed = b'2'  # 期商已自动冲正


class InstitutionType:  # 机构类别
    Bank = b'0'  # 银行
    Future = b'1'  # 期商
    Store = b'2'  # 券商


class LastFragment:  # 最后分片标志
    Yes = b'0'  # 是最后分片
    No = b'1'  # 不是最后分片


class BankAccStatus:  # 银行账户状态
    Normal = b'0'  # 正常
    Freeze = b'1'  # 冻结
    ReportLoss = b'2'  # 挂失


class MoneyAccountStatus:  # 资金账户状态
    Normal = b'0'  # 正常
    Cancel = b'1'  # 销户


class ManageStatus:  # 存管状态
    Point = b'0'  # 指定存管
    PrePoint = b'1'  # 预指定
    CancelPoint = b'2'  # 撤销指定


class SystemType:  # 应用系统类型
    FutureBankTransfer = b'0'  # 银期转帐
    StockBankTransfer = b'1'  # 银证转帐
    TheThirdPartStore = b'2'  # 第三方存管


class TxnEndFlag:  # 银期转帐划转结果标志
    NormalProcessing = b'0'  # 正常处理中
    Success = b'1'  # 成功结束
    Failed = b'2'  # 失败结束
    Abnormal = b'3'  # 异常中
    ManualProcessedForException = b'4'  # 已人工异常处理
    CommuFailedNeedManualProcess = b'5'  # 通讯异常 ，请人工处理
    SysErrorNeedManualProcess = b'6'  # 系统出错，请人工处理


class ProcessStatus:  # 银期转帐服务处理状态
    NotProcess = b'0'  # 未处理
    StartProcess = b'1'  # 开始处理
    Finished = b'2'  # 处理完成


class CustType:  # 客户类型
    Person = b'0'  # 自然人
    Institution = b'1'  # 机构户


class FBTTransferDirection:  # 银期转帐方向
    FromBankToFuture = b'1'  # 入金，银行转期货
    FromFutureToBank = b'2'  # 出金，期货转银行


class OpenOrDestroy:  # 开销户类别
    Open = b'1'  # 开户
    Destroy = b'0'  # 销户


class AvailabilityFlag:  # 有效标志
    Invalid = b'0'  # 未确认
    Valid = b'1'  # 有效
    Repeal = b'2'  # 冲正


class OrganType:  # 机构类型
    Bank = b'1'  # 银行代理
    Future = b'2'  # 交易前置
    PlateForm = b'9'  # 银期转帐平台管理


class OrganLevel:  # 机构级别
    HeadQuarters = b'1'  # 银行总行或期商总部
    Branch = b'2'  # 银行分中心或期货公司营业部


class ProtocalID:  # 协议类型
    FutureProtocal = b'0'  # 期商协议
    ICBCProtocal = b'1'  # 工行协议
    ABCProtocal = b'2'  # 农行协议
    CBCProtocal = b'3'  # 中国银行协议
    CCBProtocal = b'4'  # 建行协议
    BOCOMProtocal = b'5'  # 交行协议
    FBTPlateFormProtocal = b'X'  # 银期转帐平台协议


class ConnectMode:  # 套接字连接方式
    ShortConnect = b'0'  # 短连接
    LongConnect = b'1'  # 长连接


class SyncMode:  # 套接字通信方式
    ASync = b'0'  # 异步
    Sync = b'1'  # 同步


class BankAccType:  # 银行帐号类型
    BankBook = b'1'  # 银行存折
    SavingCard = b'2'  # 储蓄卡
    CreditCard = b'3'  # 信用卡


class FutureAccType:  # 期货公司帐号类型
    BankBook = b'1'  # 银行存折
    SavingCard = b'2'  # 储蓄卡
    CreditCard = b'3'  # 信用卡


class OrganStatus:  # 接入机构状态
    Ready = b'0'  # 启用
    CheckIn = b'1'  # 签到
    CheckOut = b'2'  # 签退
    CheckFileArrived = b'3'  # 对帐文件到达
    CheckDetail = b'4'  # 对帐
    DayEndClean = b'5'  # 日终清理
    Invalid = b'9'  # 注销


class CCBFeeMode:  # 建行收费模式
    ByAmount = b'1'  # 按金额扣收
    ByMonth = b'2'  # 按月扣收


class CommApiType:  # 通讯API类型
    Client = b'1'  # 客户端
    Server = b'2'  # 服务端
    UserApi = b'3'  # 交易系统的UserApi


class LinkStatus:  # 连接状态
    Connected = b'1'  # 已经连接
    Disconnected = b'2'  # 没有连接


class PwdFlag:  # 密码核对标志
    NoCheck = b'0'  # 不核对
    BlankCheck = b'1'  # 明文核对
    EncryptCheck = b'2'  # 密文核对


class SecuAccType:  # 期货帐号类型
    AccountID = b'1'  # 资金帐号
    CardID = b'2'  # 资金卡号
    SHStockholderID = b'3'  # 上海股东帐号
    SZStockholderID = b'4'  # 深圳股东帐号


class TransferStatus:  # 转账交易状态
    Normal = b'0'  # 正常
    Repealed = b'1'  # 被冲正


class SponsorType:  # 发起方
    Broker = b'0'  # 期商
    Bank = b'1'  # 银行


class ReqRspType:  # 请求响应类别
    Request = b'0'  # 请求
    Response = b'1'  # 响应


class FBTUserEventType:  # 银期转帐用户事件类型
    SignIn = b'0'  # 签到
    FromBankToFuture = b'1'  # 银行转期货
    FromFutureToBank = b'2'  # 期货转银行
    OpenAccount = b'3'  # 开户
    CancelAccount = b'4'  # 销户
    ChangeAccount = b'5'  # 变更银行账户
    RepealFromBankToFuture = b'6'  # 冲正银行转期货
    RepealFromFutureToBank = b'7'  # 冲正期货转银行
    QueryBankAccount = b'8'  # 查询银行账户
    QueryFutureAccount = b'9'  # 查询期货账户
    SignOut = b'A'  # 签退
    SyncKey = b'B'  # 密钥同步
    ReserveOpenAccount = b'C'  # 预约开户
    CancelReserveOpenAccount = b'D'  # 撤销预约开户
    ReserveOpenAccountConfirm = b'E'  # 预约开户确认
    Other = b'Z'  # 其他


class DBOperation:  # 记录操作类型
    Insert = b'0'  # 插入
    Update = b'1'  # 更新
    Delete = b'2'  # 删除


class SyncFlag:  # 同步标记
    Yes = b'0'  # 已同步
    No = b'1'  # 未同步


class SyncType:  # 同步类型
    OneOffSync = b'0'  # 一次同步
    TimerSync = b'1'  # 定时同步
    TimerFullSync = b'2'  # 定时完全同步


class ExDirection:  # 换汇方向
    Settlement = b'0'  # 结汇
    Sale = b'1'  # 售汇


class FBEResultFlag:  # 换汇成功标志
    Success = b'0'  # 成功
    InsufficientBalance = b'1'  # 账户余额不足
    UnknownTrading = b'8'  # 交易结果未知
    Fail = b'x'  # 失败


class FBEExchStatus:  # 换汇交易状态
    Normal = b'0'  # 正常
    ReExchange = b'1'  # 交易重发


class FBEFileFlag:  # 换汇文件标志
    DataPackage = b'0'  # 数据包
    File = b'1'  # 文件


class FBEAlreadyTrade:  # 换汇已交易标志
    NotTrade = b'0'  # 未交易
    Trade = b'1'  # 已交易


class FBEUserEventType:  # 银期换汇用户事件类型
    SignIn = b'0'  # 签到
    Exchange = b'1'  # 换汇
    ReExchange = b'2'  # 换汇重发
    QueryBankAccount = b'3'  # 银行账户查询
    QueryExchDetial = b'4'  # 换汇明细查询
    QueryExchSummary = b'5'  # 换汇汇总查询
    QueryExchRate = b'6'  # 换汇汇率查询
    CheckBankAccount = b'7'  # 对账文件通知
    SignOut = b'8'  # 签退
    Other = b'Z'  # 其他


class FBEReqFlag:  # 换汇发送标志
    UnProcessed = b'0'  # 未处理
    WaitSend = b'1'  # 等待发送
    SendSuccess = b'2'  # 发送成功
    SendFailed = b'3'  # 发送失败
    WaitReSend = b'4'  # 等待重发


class NotifyClass:  # 风险通知类型
    NOERROR = b'0'  # 正常
    Warn = b'1'  # 警示
    Call = b'2'  # 追保
    Force = b'3'  # 强平
    CHUANCANG = b'4'  # 穿仓
    Exception = b'5'  # 异常


class ForceCloseType:  # 强平单类型
    Manual = b'0'  # 手工强平
    Single = b'1'  # 单一投资者辅助强平
    Group = b'2'  # 批量投资者辅助强平


class RiskNotifyMethod:  # 风险通知途径
    System = b'0'  # 系统通知
    SMS = b'1'  # 短信通知
    EMail = b'2'  # 邮件通知
    Manual = b'3'  # 人工通知


class RiskNotifyStatus:  # 风险通知状态
    NotGen = b'0'  # 未生成
    Generated = b'1'  # 已生成未发送
    SendError = b'2'  # 发送失败
    SendOk = b'3'  # 已发送未接收
    Received = b'4'  # 已接收未确认
    Confirmed = b'5'  # 已确认


class RiskUserEvent:  # 风控用户操作事件
    ExportData = b'0'  # 导出数据


class ConditionalOrderSortType:  # 条件单索引条件
    LastPriceAsc = b'0'  # 使用最新价升序
    LastPriceDesc = b'1'  # 使用最新价降序
    AskPriceAsc = b'2'  # 使用卖价升序
    AskPriceDesc = b'3'  # 使用卖价降序
    BidPriceAsc = b'4'  # 使用买价升序
    BidPriceDesc = b'5'  # 使用买价降序


class SendType:  # 报送状态
    NoSend = b'0'  # 未发送
    Sended = b'1'  # 已发送
    Generated = b'2'  # 已生成
    SendFail = b'3'  # 报送失败
    Success = b'4'  # 接收成功
    Fail = b'5'  # 接收失败
    Cancel = b'6'  # 取消报送


class ClientIDStatus:  # 交易编码状态
    NoApply = b'1'  # 未申请
    Submited = b'2'  # 已提交申请
    Sended = b'3'  # 已发送申请
    Success = b'4'  # 完成
    Refuse = b'5'  # 拒绝
    Cancel = b'6'  # 已撤销编码


class QuestionType:  # 特有信息类型
    Radio = b'1'  # 单选
    Option = b'2'  # 多选
    Blank = b'3'  # 填空


class BusinessType:  # 业务类型
    Request = b'1'  # 请求
    Response = b'2'  # 应答
    Notice = b'3'  # 通知


class CfmmcReturnCode:  # 监控中心返回码
    Success = b'0'  # 成功
    Working = b'1'  # 该客户已经有流程在处理中
    InfoFail = b'2'  # 监控中客户资料检查失败
    IDCardFail = b'3'  # 监控中实名制检查失败
    OtherFail = b'4'  # 其他错误


class ClientType:  # 客户类型
    All = b'0'  # 所有
    Person = b'1'  # 个人
    Company = b'2'  # 单位
    Other = b'3'  # 其他
    SpecialOrgan = b'4'  # 特殊法人
    Asset = b'5'  # 资管户


class ExchangeIDType:  # 交易所编号
    SHFE = b'S'  # 上海期货交易所
    CZCE = b'Z'  # 郑州商品交易所
    DCE = b'D'  # 大连商品交易所
    CFFEX = b'J'  # 中国金融期货交易所
    INE = b'N'  # 上海国际能源交易中心股份有限公司


class ExClientIDType:  # 交易编码类型
    Hedge = b'1'  # 套保
    Arbitrage = b'2'  # 套利
    Speculation = b'3'  # 投机


class UpdateFlag:  # 更新状态
    NoUpdate = b'0'  # 未更新
    Success = b'1'  # 更新全部信息成功
    Fail = b'2'  # 更新全部信息失败
    TCSuccess = b'3'  # 更新交易编码成功
    TCFail = b'4'  # 更新交易编码失败
    Cancel = b'5'  # 已丢弃


class ApplyOperateID:  # 申请动作
    OpenInvestor = b'1'  # 开户
    ModifyIDCard = b'2'  # 修改身份信息
    ModifyNoIDCard = b'3'  # 修改一般信息
    ApplyTradingCode = b'4'  # 申请交易编码
    CancelTradingCode = b'5'  # 撤销交易编码
    CancelInvestor = b'6'  # 销户
    FreezeAccount = b'8'  # 账户休眠
    ActiveFreezeAccount = b'9'  # 激活休眠账户


class ApplyStatusID:  # 申请状态
    NoComplete = b'1'  # 未补全
    Submited = b'2'  # 已提交
    Checked = b'3'  # 已审核
    Refused = b'4'  # 已拒绝
    Deleted = b'5'  # 已删除


class SendMethod:  # 发送方式
    ByAPI = b'1'  # 文件发送
    ByFile = b'2'  # 电子发送


class EventMode:  # 操作方法
    ADD = b'1'  # 增加
    UPDATE = b'2'  # 修改
    DELETE = b'3'  # 删除
    CHECK = b'4'  # 复核
    COPY = b'5'  # 复制
    CANCEL = b'6'  # 注销
    Reverse = b'7'  # 冲销


class UOAAutoSend:  # 统一开户申请自动发送
    ASR = b'1'  # 自动发送并接收
    ASNR = b'2'  # 自动发送，不自动接收
    NSAR = b'3'  # 不自动发送，自动接收
    NSR = b'4'  # 不自动发送，也不自动接收


class FlowID:  # 流程ID
    InvestorGroupFlow = b'1'  # 投资者对应投资者组设置
    InvestorRate = b'2'  # 投资者手续费率设置
    InvestorCommRateModel = b'3'  # 投资者手续费率模板关系设置


class CheckLevel:  # 复核级别
    Zero = b'0'  # 零级复核
    One = b'1'  # 一级复核
    Two = b'2'  # 二级复核


class CheckStatus:  # 复核级别
    Init = b'0'  # 未复核
    Checking = b'1'  # 复核中
    Checked = b'2'  # 已复核
    Refuse = b'3'  # 拒绝
    Cancel = b'4'  # 作废


class UsedStatus:  # 生效状态
    Unused = b'0'  # 未生效
    Used = b'1'  # 已生效
    Fail = b'2'  # 生效失败


class BankAcountOrigin:  # 账户来源
    ByAccProperty = b'0'  # 手工录入
    ByFBTransfer = b'1'  # 银期转账


class MonthBillTradeSum:  # 结算单月报成交汇总方式
    ByInstrument = b'0'  # 同日同合约
    ByDayInsPrc = b'1'  # 同日同合约同价格
    ByDayIns = b'2'  # 同合约


class FBTTradeCodeEnum:  # 银期交易代码枚举
    BankLaunchBankToBroker = b'102001'  # 银行发起银行转期货
    BrokerLaunchBankToBroker = b'202001'  # 期货发起银行转期货
    BankLaunchBrokerToBank = b'102002'  # 银行发起期货转银行
    BrokerLaunchBrokerToBank = b'202002'  # 期货发起期货转银行


class OTPType:  # 动态令牌类型
    NONE = b'0'  # 无动态令牌
    TOTP = b'1'  # 时间令牌


class OTPStatus:  # 动态令牌状态
    Unused = b'0'  # 未使用
    Used = b'1'  # 已使用
    Disuse = b'2'  # 注销


class BrokerUserType:  # 经济公司用户类型
    Investor = b'1'  # 投资者
    BrokerUser = b'2'  # 操作员


class FutureType:  # 期货类型
    Commodity = b'1'  # 商品期货
    Financial = b'2'  # 金融期货


class FundEventType:  # 资金管理操作类型
    Restriction = b'0'  # 转账限额
    TodayRestriction = b'1'  # 当日转账限额
    Transfer = b'2'  # 期商流水
    Credit = b'3'  # 资金冻结
    InvestorWithdrawAlm = b'4'  # 投资者可提资金比例
    BankRestriction = b'5'  # 单个银行帐户转账限额
    Accountregister = b'6'  # 银期签约账户
    ExchangeFundIO = b'7'  # 交易所出入金
    InvestorFundIO = b'8'  # 投资者出入金


class AccountSourceType:  # 资金账户来源
    FBTransfer = b'0'  # 银期同步
    ManualEntry = b'1'  # 手工录入


class CodeSourceType:  # 交易编码来源
    UnifyAccount = b'0'  # 统一开户(已规范)
    ManualEntry = b'1'  # 手工录入(未规范)


class UserRange:  # 操作员范围
    All = b'0'  # 所有
    Single = b'1'  # 单一操作员


class ByGroup:  # 交易统计表按客户统计方式
    Investor = b'2'  # 按投资者统计
    Group = b'1'  # 按类统计


class TradeSumStatMode:  # 交易统计表按范围统计方式
    Instrument = b'1'  # 按合约统计
    Product = b'2'  # 按产品统计
    Exchange = b'3'  # 按交易所统计


class ExprSetMode:  # 日期表达式设置类型
    Relative = b'1'  # 相对已有规则设置
    Typical = b'2'  # 典型设置


class RateInvestorRange:  # 投资者范围
    All = b'1'  # 公司标准
    Model = b'2'  # 模板
    Single = b'3'  # 单一投资者


class SyncDataStatus:  # 主次用系统数据同步状态
    Initialize = b'0'  # 未同步
    Settlementing = b'1'  # 同步中
    Settlemented = b'2'  # 已同步


class TradeSource:  # 成交来源
    NORMAL = b'0'  # 来自交易所普通回报
    QUERY = b'1'  # 来自查询


class FlexStatMode:  # 产品合约统计方式
    Product = b'1'  # 产品统计
    Exchange = b'2'  # 交易所统计
    All = b'3'  # 统计所有


class ByInvestorRange:  # 投资者范围统计方式
    Property = b'1'  # 属性统计
    All = b'2'  # 统计所有


class PropertyInvestorRange:  # 投资者范围
    All = b'1'  # 所有
    Property = b'2'  # 投资者属性
    Single = b'3'  # 单一投资者


class FileStatus:  # 文件状态
    NoCreate = b'0'  # 未生成
    Created = b'1'  # 已生成
    Failed = b'2'  # 生成失败


class FileGenStyle:  # 文件生成方式
    FileTransmit = b'0'  # 下发
    FileGen = b'1'  # 生成


class SysOperMode:  # 系统日志操作方法
    Add = b'1'  # 增加
    Update = b'2'  # 修改
    Delete = b'3'  # 删除
    Copy = b'4'  # 复制
    AcTive = b'5'  # 激活
    CanCel = b'6'  # 注销
    ReSet = b'7'  # 重置


class SysOperType:  # 系统日志操作类型
    UpdatePassword = b'0'  # 修改操作员密码
    UserDepartment = b'1'  # 操作员组织架构关系
    RoleManager = b'2'  # 角色管理
    RoleFunction = b'3'  # 角色功能设置
    BaseParam = b'4'  # 基础参数设置
    SetUserID = b'5'  # 设置操作员
    SetUserRole = b'6'  # 用户角色设置
    UserIpRestriction = b'7'  # 用户IP限制
    DepartmentManager = b'8'  # 组织架构管理
    DepartmentCopy = b'9'  # 组织架构向查询分类复制
    Tradingcode = b'A'  # 交易编码管理
    InvestorStatus = b'B'  # 投资者状态维护
    InvestorAuthority = b'C'  # 投资者权限管理
    PropertySet = b'D'  # 属性设置
    ReSetInvestorPasswd = b'E'  # 重置投资者密码
    InvestorPersonalityInfo = b'F'  # 投资者个性信息维护


class CSRCDataQueyType:  # 上报数据查询类型
    Current = b'0'  # 查询当前交易日报送的数据
    History = b'1'  # 查询历史报送的代理经纪公司的数据


class FreezeStatus:  # 休眠状态
    Normal = b'1'  # 活跃
    Freeze = b'0'  # 休眠


class StandardStatus:  # 规范状态
    Standard = b'0'  # 已规范
    NonStandard = b'1'  # 未规范


class RightParamType:  # 配置类型
    Freeze = b'1'  # 休眠户
    FreezeActive = b'2'  # 激活休眠户
    OpenLimit = b'3'  # 开仓权限限制
    RelieveOpenLimit = b'4'  # 解除开仓权限限制


class DataStatus:  # 反洗钱审核表数据状态
    Normal = b'0'  # 正常
    Deleted = b'1'  # 已删除


class AMLCheckStatus:  # 审核状态
    Init = b'0'  # 未复核
    Checking = b'1'  # 复核中
    Checked = b'2'  # 已复核
    RefuseReport = b'3'  # 拒绝上报


class AmlDateType:  # 日期类型
    DrawDay = b'0'  # 检查日期
    TouchDay = b'1'  # 发生日期


class AmlCheckLevel:  # 审核级别
    CheckLevel0 = b'0'  # 零级审核
    CheckLevel1 = b'1'  # 一级审核
    CheckLevel2 = b'2'  # 二级审核
    CheckLevel3 = b'3'  # 三级审核


class ExportFileType:  # 导出文件类型
    CSV = b'0'  # CSV
    EXCEL = b'1'  # Excel
    DBF = b'2'  # DBF


class SettleManagerType:  # 结算配置类型
    Before = b'1'  # 结算前准备
    Settlement = b'2'  # 结算
    After = b'3'  # 结算后核对
    Settlemented = b'4'  # 结算后处理


class SettleManagerLevel:  # 结算配置等级
    Must = b'1'  # 必要
    Alarm = b'2'  # 警告
    Prompt = b'3'  # 提示
    Ignore = b'4'  # 不检查


class SettleManagerGroup:  # 模块分组
    Exhcange = b'1'  # 交易所核对
    ASP = b'2'  # 内部核对
    CSRC = b'3'  # 上报数据核对


class LimitUseType:  # 保值额度使用类型
    Repeatable = b'1'  # 可重复使用
    Unrepeatable = b'2'  # 不可重复使用


class DataResource:  # 数据来源
    Settle = b'1'  # 本系统
    Exchange = b'2'  # 交易所
    CSRC = b'3'  # 报送数据


class MarginType:  # 保证金类型
    ExchMarginRate = b'0'  # 交易所保证金率
    InstrMarginRate = b'1'  # 投资者保证金率
    InstrMarginRateTrade = b'2'  # 投资者交易保证金率


class ActiveType:  # 生效类型
    Intraday = b'1'  # 仅当日生效
    Long = b'2'  # 长期生效


class MarginRateType:  # 冲突保证金率类型
    Exchange = b'1'  # 交易所保证金率
    Investor = b'2'  # 投资者保证金率
    InvestorTrade = b'3'  # 投资者交易保证金率


class BackUpStatus:  # 备份数据状态
    UnBak = b'0'  # 未生成备份数据
    BakUp = b'1'  # 备份数据生成中
    BakUped = b'2'  # 已生成备份数据
    BakFail = b'3'  # 备份数据失败


class InitSettlement:  # 结算初始化状态
    UnInitialize = b'0'  # 结算初始化未开始
    Initialize = b'1'  # 结算初始化中
    Initialized = b'2'  # 结算初始化完成


class ReportStatus:  # 报表数据生成状态
    NoCreate = b'0'  # 未生成报表数据
    Create = b'1'  # 报表数据生成中
    Created = b'2'  # 已生成报表数据
    CreateFail = b'3'  # 生成报表数据失败


class SaveStatus:  # 数据归档状态
    UnSaveData = b'0'  # 归档未完成
    SaveDatad = b'1'  # 归档完成


class SettArchiveStatus:  # 结算确认数据归档状态
    UnArchived = b'0'  # 未归档数据
    Archiving = b'1'  # 数据归档中
    Archived = b'2'  # 已归档数据
    ArchiveFail = b'3'  # 归档数据失败


class CTPType:  # CTP交易系统类型
    Unkown = b'0'  # 未知
    MainCenter = b'1'  # 主中心
    BackUp = b'2'  # 备中心


class CloseDealType:  # 平仓处理类型
    Normal = b'0'  # 正常
    SpecFirst = b'1'  # 投机平仓优先


class MortgageFundUseRange:  # 货币质押资金可用范围
    _None = b'0'  # 不能使用
    Margin = b'1'  # 用于保证金
    All = b'2'  # 用于手续费、盈亏、保证金
    CNY3 = b'3'  # 人民币方案3


class SpecProductType:  # 特殊产品类型
    CzceHedge = b'1'  # 郑商所套保产品
    IneForeignCurrency = b'2'  # 货币质押产品
    DceOpenClose = b'3'  # 大连短线开平仓产品


class FundMortgageType:  # 货币质押类型
    Mortgage = b'1'  # 质押
    Redemption = b'2'  # 解质


class AccountSettlementParamID:  # 投资者账户结算参数代码
    BaseMargin = b'1'  # 基础保证金
    LowestInterest = b'2'  # 最低权益标准


class FundMortDirection:  # 货币质押方向
    In = b'1'  # 货币质入
    Out = b'2'  # 货币质出


class BusinessClass:  # 换汇类别
    Profit = b'0'  # 盈利
    Loss = b'1'  # 亏损
    Other = b'Z'  # 其他


class SwapSourceType:  # 换汇数据来源
    Manual = b'0'  # 手工
    Automatic = b'1'  # 自动生成


class CurrExDirection:  # 换汇类型
    Settlement = b'0'  # 结汇
    Sale = b'1'  # 售汇


class CurrencySwapStatus:  # 申请状态
    Entry = b'1'  # 已录入
    Approve = b'2'  # 已审核
    Refuse = b'3'  # 已拒绝
    Revoke = b'4'  # 已撤销
    Send = b'5'  # 已发送
    Success = b'6'  # 换汇成功
    Failure = b'7'  # 换汇失败


class ReqFlag:  # 换汇发送标志
    NoSend = b'0'  # 未发送
    SendSuccess = b'1'  # 发送成功
    SendFailed = b'2'  # 发送失败
    WaitReSend = b'3'  # 等待重发


class ResFlag:  # 换汇返回成功标志
    Success = b'0'  # 成功
    InsuffiCient = b'1'  # 账户余额不足
    UnKnown = b'8'  # 交易结果未知


class ExStatus:  # 修改状态
    Before = b'0'  # 修改前
    After = b'1'  # 修改后


class ClientRegion:  # 开户客户地域
    Domestic = b'1'  # 国内客户
    GMT = b'2'  # 港澳台客户
    Foreign = b'3'  # 国外客户


class HasBoard:  # 是否有董事会
    No = b'0'  # 没有
    Yes = b'1'  # 有


class StartMode:  # 启动模式
    Normal = b'1'  # 正常
    Emerge = b'2'  # 应急
    Restore = b'3'  # 恢复


class TemplateType:  # 模型类型
    Full = b'1'  # 全量
    Increment = b'2'  # 增量
    BackUp = b'3'  # 备份


class LoginMode:  # 登录模式
    Trade = b'0'  # 交易
    Transfer = b'1'  # 转账


class PromptType:  # 日历提示类型
    Instrument = b'1'  # 合约上下市
    Margin = b'2'  # 保证金分段生效


class HasTrustee:  # 是否有托管人
    Yes = b'1'  # 有
    No = b'0'  # 没有


class AmType:  # 机构类型
    Bank = b'1'  # 银行
    Securities = b'2'  # 证券公司
    Fund = b'3'  # 基金公司
    Insurance = b'4'  # 保险公司
    Trust = b'5'  # 信托公司
    Other = b'9'  # 其他


class CSRCFundIOType:  # 出入金类型
    FundIO = b'0'  # 出入金
    SwapCurrency = b'1'  # 银期换汇


class CusAccountType:  # 结算账户类型
    Futures = b'1'  # 期货结算账户
    AssetmgrFuture = b'2'  # 纯期货资管业务下的资管结算账户
    AssetmgrTrustee = b'3'  # 综合类资管业务下的期货资管托管账户
    AssetmgrTransfer = b'4'  # 综合类资管业务下的资金中转账户


class LanguageType:  # 通知语言类型
    Chinese = b'1'  # 中文
    English = b'2'  # 英文


class AssetmgrClientType:  # 资产管理客户类型
    Person = b'1'  # 个人资管客户
    Organ = b'2'  # 单位资管客户
    SpecialOrgan = b'4'  # 特殊单位资管客户


class AssetmgrType:  # 投资类型
    Futures = b'3'  # 期货类
    SpecialOrgan = b'4'  # 综合类


class CheckInstrType:  # 合约比较类型
    HasExch = b'0'  # 合约交易所不存在
    HasATP = b'1'  # 合约本系统不存在
    HasDiff = b'2'  # 合约比较不一致


class DeliveryType:  # 交割类型
    HandDeliv = b'1'  # 手工交割
    PersonDeliv = b'2'  # 到期交割


class MaxMarginSideAlgorithm:  # 大额单边保证金算法
    NO = b'0'  # 不使用大额单边保证金算法
    YES = b'1'  # 使用大额单边保证金算法


class DAClientType:  # 资产管理客户类型
    Person = b'0'  # 自然人
    Company = b'1'  # 法人
    Other = b'2'  # 其他


class UOAAssetmgrType:  # 投资类型
    Futures = b'1'  # 期货类
    SpecialOrgan = b'2'  # 综合类


class DirectionEn:  # 买卖方向
    Buy = b'0'  # Buy
    Sell = b'1'  # Sell


class OffsetFlagEn:  # 开平标志
    Open = b'0'  # Position Opening
    Close = b'1'  # Position Close
    ForceClose = b'2'  # Forced Liquidation
    CloseToday = b'3'  # Close Today
    CloseYesterday = b'4'  # Close Prev.
    ForceOff = b'5'  # Forced Reduction
    LocalForceClose = b'6'  # Local Forced Liquidation


class HedgeFlagEn:  # 投机套保标志
    Speculation = b'1'  # Speculation
    Arbitrage = b'2'  # Arbitrage
    Hedge = b'3'  # Hedge


class FundIOTypeEn:  # 出入金类型
    FundIO = b'1'  # DepositWithdrawal
    Transfer = b'2'  # Bank-Futures Transfer
    SwapCurrency = b'3'  # Bank-Futures FX Exchange


class FundTypeEn:  # 资金类型
    Deposite = b'1'  # Bank Deposit
    ItemFund = b'2'  # PaymentFee
    Company = b'3'  # Brokerage Adj
    InnerTransfer = b'4'  # Internal Transfer


class FundDirectionEn:  # 出入金方向
    In = b'1'  # Deposit
    Out = b'2'  # Withdrawal


class FundMortDirectionEn:  # 货币质押方向
    In = b'1'  # Pledge
    Out = b'2'  # Redemption


class OptionsType:  # 期权类型
    CallOptions = b'1'  # 看涨
    PutOptions = b'2'  # 看跌


class StrikeMode:  # 执行方式
    Continental = b'0'  # 欧式
    American = b'1'  # 美式
    Bermuda = b'2'  # 百慕大


class StrikeType:  # 执行类型
    Hedge = b'0'  # 自身对冲
    Match = b'1'  # 匹配执行


class ApplyType:  # 中金所期权放弃执行申请类型
    NotStrikeNum = b'4'  # 不执行数量


class GiveUpDataSource:  # 放弃执行申请数据来源
    Gen = b'0'  # 系统生成
    Hand = b'1'  # 手工添加


class ExecResult:  # 执行结果
    NoExec = b'n'  # 没有执行
    Canceled = b'c'  # 已经取消
    OK = b'0'  # 执行成功
    NoPosition = b'1'  # 期权持仓不够
    NoDeposit = b'2'  # 资金不够
    NoParticipant = b'3'  # 会员不存在
    NoClient = b'4'  # 客户不存在
    NoInstrument = b'6'  # 合约不存在
    NoRight = b'7'  # 没有执行权限
    InvalidVolume = b'8'  # 不合理的数量
    NoEnoughHistoryTrade = b'9'  # 没有足够的历史成交
    Unknown = b'a'  # 未知


class CombinationType:  # 组合类型
    Future = b'0'  # 期货组合
    BUL = b'1'  # 垂直价差BUL
    BER = b'2'  # 垂直价差BER
    STD = b'3'  # 跨式组合
    STG = b'4'  # 宽跨式组合
    PRT = b'5'  # 备兑组合
    CLD = b'6'  # 时间价差组合


class DceCombinationType:  # 组合类型
    SPL = b'0'  # 期货对锁组合
    OPL = b'1'  # 期权对锁组合
    SP = b'2'  # 期货跨期组合
    SPC = b'3'  # 期货跨品种组合
    BLS = b'4'  # 买入期权垂直价差组合
    BES = b'5'  # 卖出期权垂直价差组合
    CAS = b'6'  # 期权日历价差组合
    STD = b'7'  # 期权跨式组合
    STG = b'8'  # 期权宽跨式组合
    BFO = b'9'  # 买入期货期权组合
    SFO = b'a'  # 卖出期货期权组合


class OptionRoyaltyPriceType:  # 期权权利金价格类型
    PreSettlementPrice = b'1'  # 昨结算价
    OpenPrice = b'4'  # 开仓价
    MaxPreSettlementPrice = b'5'  # 最新价与昨结算价较大值


class BalanceAlgorithm:  # 权益算法
    Default = b'1'  # 不计算期权市值盈亏
    IncludeOptValLost = b'2'  # 计算期权市值亏损


class ActionType:  # 执行类型
    Exec = b'1'  # 执行
    Abandon = b'2'  # 放弃


class ForQuoteStatus:  # 询价状态
    Submitted = b'a'  # 已经提交
    Accepted = b'b'  # 已经接受
    Rejected = b'c'  # 已经被拒绝


class ValueMethod:  # 取值方式
    Absolute = b'0'  # 按绝对值
    Ratio = b'1'  # 按比率


class ExecOrderPositionFlag:  # 期权行权后是否保留期货头寸的标记
    Reserve = b'0'  # 保留
    UnReserve = b'1'  # 不保留


class ExecOrderCloseFlag:  # 期权行权后生成的头寸是否自动平仓
    AutoClose = b'0'  # 自动平仓
    NotToClose = b'1'  # 免于自动平仓


class ProductType:  # 产品类型
    Futures = b'1'  # 期货
    Options = b'2'  # 期权


class CZCEUploadFileName:  # 郑商所结算文件名
    O = b'O'  # ^\d{8}_zz_\d{4}
    T = b'T'  # ^\d{8}成交表
    P = b'P'  # ^\d{8}单腿持仓表new
    N = b'N'  # ^\d{8}非平仓了结表
    L = b'L'  # ^\d{8}平仓表
    F = b'F'  # ^\d{8}资金表
    C = b'C'  # ^\d{8}组合持仓表
    M = b'M'  # ^\d{8}保证金参数表


class DCEUploadFileName:  # 大商所结算文件名
    O = b'O'  # ^\d{8}_dl_\d{3}
    T = b'T'  # ^\d{8}_成交表
    P = b'P'  # ^\d{8}_持仓表
    F = b'F'  # ^\d{8}_资金结算表
    C = b'C'  # ^\d{8}_优惠组合持仓明细表
    D = b'D'  # ^\d{8}_持仓明细表
    M = b'M'  # ^\d{8}_保证金参数表
    S = b'S'  # ^\d{8}_期权执行表


class SHFEUploadFileName:  # 上期所结算文件名
    O = b'O'  # ^\d{4}_\d{8}_\d{8}_DailyFundChg
    T = b'T'  # ^\d{4}_\d{8}_\d{8}_Trade
    P = b'P'  # ^\d{4}_\d{8}_\d{8}_SettlementDetail
    F = b'F'  # ^\d{4}_\d{8}_\d{8}_Capital


class CFFEXUploadFileName:  # 中金所结算文件名
    T = b'T'  # ^\d{4}_SG\d{1}_\d{8}_\d{1}_Trade
    P = b'P'  # ^\d{4}_SG\d{1}_\d{8}_\d{1}_SettlementDetail
    F = b'F'  # ^\d{4}_SG\d{1}_\d{8}_\d{1}_Capital
    S = b'S'  # ^\d{4}_SG\d{1}_\d{8}_\d{1}_OptionExec


class CombDirection:  # 组合指令方向
    Comb = b'0'  # 申请组合
    UnComb = b'1'  # 申请拆分


class StrikeOffsetType:  # 行权偏移类型
    RealValue = b'1'  # 实值额
    ProfitValue = b'2'  # 盈利额
    RealRatio = b'3'  # 实值比例
    ProfitRatio = b'4'  # 盈利比例


class ReserveOpenAccStas:  # 预约开户状态
    Processing = b'0'  # 等待处理中
    Cancelled = b'1'  # 已撤销
    Opened = b'2'  # 已开户
    Invalid = b'3'  # 无效请求


class WeakPasswordSource:  # 弱密码来源
    Lib = b'1'  # 弱密码库
    Manual = b'2'  # 手工录入


class OptSelfCloseFlag:  # 期权行权的头寸是否自对冲
    CloseSelfOptionPosition = b'1'  # 自对冲期权仓位
    ReserveOptionPosition = b'2'  # 保留期权仓位
    SellCloseSelfFuturePosition = b'3'  # 自对冲卖方履约后的期货仓位
    ReserveFuturePosition = b'4'  # 保留卖方履约后的期货仓位


class BizType:  # 业务类型
    Future = b'1'  # 期货
    Stock = b'2'  # 证券


class AppType:  # 用户App类型
    Investor = b'1'  # 直连的投资者
    InvestorRelay = b'2'  # 为每个投资者都创建连接的中继
    OperatorRelay = b'3'  # 所有投资者共享一个操作员连接的中继
    UnKnown = b'4'  # 未知


class ResponseValue:  # 应答类型
    Right = b'0'  # 检查成功
    Refuse = b'1'  # 检查失败


class OTCTradeType:  # OTC成交类型
    Block = b'0'  # 大宗交易
    EFP = b'1'  # 期转现


class MatchType:  # 期现风险匹配方式
    DV01 = b'1'  # 基点价值
    ParValue = b'2'  # 面值

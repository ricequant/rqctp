from .MdApi import MdApi as CMdApi


class MdApi(CMdApi):
    def __init__(self, pszFlowPath: str = "", bIsUsingUdp: bool = False, bIsMulticast: bool = False):
        super(MdApi, self).__init__(pszFlowPath.encode("GBK"), bIsUsingUdp, bIsMulticast)

    def RegisterFront(self, pszFrontAddress: str):
        return super().RegisterFront(pszFrontAddress.encode("GBK"))

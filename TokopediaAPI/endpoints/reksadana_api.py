import sys
import os
try:
    from constant import (Constant)
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from constant import (Constant)

class ReksadanaEndpointsMixin(object):
    def reksadana_user_info(self):
        return self._call_api("mutualfund/api/user", host=Constant.TOKOPEDIA_URL)
    
    def reksadana_user_portofolio(self):
        return self._call_api("mutualfund/api/user/portfolio?request=frontend", host=Constant.TOKOPEDIA_URL)
    
    def reksadana_products(self):
        return self._call_api("mutualfund/api/products", host=Constant.TOKOPEDIA_URL)
        
    def reksadana_order_history(self, page=1, item_per_page=6, status="all", type="all"):
        """reksadana history order

        Keyword Arguments:
            page {int} -- pagination (default: {1})
            item_per_page {int} -- (default: {6})
            status {str} -- all, success, processing (default: {"all"})
            type {str} -- all, buy, sell (default: {"all"})

        Returns:
            [json]
        """
        query = {
            "page": page,
            "item_per_page": item_per_page,
            "status": status,
            "type": type,
        }
        return self._call_api("mutualfund/api/order/history", params=query, host=Constant.TOKOPEDIA_URL)
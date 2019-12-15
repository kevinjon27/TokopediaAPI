from .request import (
    ProductRequest
)
class ProductEndpointsMixin(ProductRequest, object):
    def product_detail(self, product_id):
        """
        :param product_id
        :return:
        """
        query = self.product_detail_request()
        
        variable = {
            "shopDomain": "",
            "productId": product_id,
            "productKey": ""
        }
        
        return self.execute(query, variable)
    
    def product_installment_calculation(self, product_price, product_quantity=1):
        """
        :param product_price
        :param product_quantity: default 1
        :return:
        """
        query = self.product_installment_calculation_request()
        
        variable = {
            "price": product_price,
            "quantity": product_quantity
        }
        
        return self.execute(query, variable)
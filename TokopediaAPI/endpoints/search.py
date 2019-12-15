from .request import (
    SearchRequest
)
class SearchEndpointsMixin(SearchRequest, object):
    def search(self, keyword, page=1):
        """
        :param keyword
        :return:
        """
        query = self.search_item_request()
        
        variable = {
            "params": "with_template=true&device=ios&source=search&page={page}&unique_id=f01bcaa63078d0d8a2806a48cd80eb3e&ob=23&use_page=true&rf=false&q={keyword}&related=true&dep_id=&ep=product&breadcumb=true&item=2,1&catalog_rows=0&src=search".format(keyword=keyword, page=page),
            "source": "search",
            "query": "{keyword}".format(keyword=keyword),
            "isLoadMore": True,
            "headline_params": "src=search&page={page}&device=ios&ob=23&item=1&ep=headline&template_id=3,4&q={keyword}".format(keyword=keyword, page=page),
        }

        

        return self.execute(query, variable)
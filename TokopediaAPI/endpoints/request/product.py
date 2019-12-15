class ProductRequest(object):
    def product_detail_request(self):
        return """
            query getPDPInfo($productId: Int, $productKey: String, $shopDomain: String) {
                getPDPInfo(
                    productID: $productId
                    productKey: $productKey
                    shopDomain: $shopDomain
                ) {
                    basic {
                        id
                        shopID
                        name
                        alias
                        price
                        priceCurrency
                        lastUpdatePrice
                        description
                        minOrder
                        maxOrder
                        status
                        weight
                        weightUnit
                        condition
                        url
                        isKreasiLokal
                        isMustInsurance
                        isEligibleCOD
                        catalogID
                        needPrescription
                        isLeasing
                    }
                    brand {
                        brandID
                        isActive
                        brandStatus
                        name
                    }
                    menu {
                        menuID
                        name
                        url
                    }
                    category {
                        id
                        name
                        title
                        breadcrumbURL
                        isAdult
                        detail {
                            id
                            name
                            breadcrumbURL
                        }
                    }
                    preorder {
                        isActive
                        duration
                        timeUnit
                    }
                    wholesale {
                        minQty
                        price
                    }
                    campaign {
                        campaignID
                        campaignType
                        campaignTypeName
                        percentageAmount
                        originalPrice
                        discountedPrice
                        stock
                        isActive
                        startDate
                        endDate
                        endDateUnix
                        appLinks
                        hideGimmick
                    }
                    cashback {
                        percentage
                    }
                    stats {
                        countView
                        countReview
                        countTalk
                        rating
                    }
                    txStats {
                        txSuccess
                        txReject
                        itemSold
                    }
                    videos {
                        source
                        url
                    }
                    variant {
                        parentID
                        isVariant
                    }
                    stock {
                        useStock
                        value
                        stockWording
                    }
                    media {
                        type
                        URLOriginal
                        URLThumbnail
                        Description
                        VideoURLIOS
                        IsAutoplay
                    }
                    freeOngkir {
                        isActive
                        imgURL
                    }
                }
            }
        """
        
    def product_installment_calculation_request(self):
        return """
            query ft_installment_calculation($price: Float!, $quantity: Int!) {
                ft_installment_calculation(price: $price, quantity: $quantity) {
                    data {
                        credit_card {
                            partner_code
                            partner_name
                            partner_icon
                            partner_url
                            tnc_id
                            installment_list {
                                term
                                mdr_value
                                mdr_type
                                interest_rate
                                minimum_amount
                                maximum_amount
                                monthly_price
                                os_monthly_price
                            }
                            instruction_list {
                                order
                                description
                                ins_image_url
                            }
                        }
                        non_credit_card {
                            partner_code
                            partner_name
                            partner_icon
                            partner_url
                            tnc_id
                            installment_list {
                                term
                                mdr_value
                                mdr_type
                                interest_rate
                                minimum_amount
                                maximum_amount
                                monthly_price
                                os_monthly_price
                            }
                            instruction_list {
                                order
                                description
                                ins_image_url
                            }
                        }
                        tnc {
                            tnc_id
                            tnc_list {
                                order
                                description
                            }
                        }
                    }
                    message
                }
                ft_installment_recommendation(price: $price, quantity: $quantity) {
                    data {
                        term
                        mdr_value
                        mdr_type
                        interest_rate
                        minimum_amount
                        maximum_amount
                        monthly_price
                        os_monthly_price
                        partner_code
                        partner_name
                        partner_icon
                    }
                    message
                }
            }    
        """
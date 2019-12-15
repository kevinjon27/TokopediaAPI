class SearchRequest(object):
    def search_item_request(self):
        return """
            query SearchProduct(
                $params: String
                $query: String!
                $source: String
                $headline_params: String
                $isLoadMore: Boolean = false
                $skipNavigationWidget: Boolean = false
            ) {
                global_search_navigation(keyword: $query, size: 5, device: "ios")
                    @skip(if: $skipNavigationWidget) {
                    data {
                        source
                        keyword
                        title
                        nav_template
                        background
                        see_all_applink
                        list {
                            category_name
                            name
                            info
                            image_url
                            applink
                            subtitle
                            strikethrough
                            background_url
                            logo_url
                        }
                    }
                }
                headlineAds: displayAdsV3(displayParams: $headline_params)
                    @skip(if: $isLoadMore) {
                    status {
                        error_code
                        message
                    }
                    header {
                        process_time
                        total_data
                    }
                    data {
                        id
                        ad_ref_key
                        redirect
                        ad_click_url
                        headline {
                            template_id
                            name
                            image {
                                full_url
                                full_ecs
                            }
                            shop {
                                id
                                name
                                domain
                                tagline
                                slogan
                                location
                                city
                                gold_shop
                                gold_shop_badge
                                shop_is_official
                                product {
                                    id
                                    name
                                    price_format
                                    applinks
                                    image_product {
                                        product_id
                                        product_name
                                        image_url
                                        image_click_url
                                    }
                                }
                                image_shop {
                                    cover
                                    s_url
                                    xs_url
                                    cover_ecs
                                    s_ecs
                                    xs_ecs
                                }
                            }
                            badges {
                                image_url
                                show
                                title
                            }
                            button_text
                            promoted_text
                            description
                            uri
                        }
                        applinks
                    }
                }
                ace_guide(q: $query) @skip(if: $isLoadMore) {
                    data {
                        applink
                        keyword
                        url
                    }
                }
                quick_filter(query: $query, extraParams: $params) @skip(if: $isLoadMore) {
                    filter {
                        options {
                            name
                            key
                            icon
                            value
                            input_type
                            total_data
                            val_max
                            val_min
                            hex_color
                            is_new
                            child {
                                key
                                value
                                name
                                icon
                                input_type
                                total_data
                                child {
                                    key
                                    value
                                    name
                                    icon
                                    input_type
                                    total_data
                                }
                            }
                        }
                    }
                }
                productAds: displayAdsV3(displayParams: $params) {
                    status {
                        error_code
                        message
                    }
                    header {
                        process_time
                        total_data
                    }
                    data {
                        id
                        ad_ref_key
                        redirect
                        sticker_id
                        sticker_image
                        product_click_url
                        product_wishlist_url
                        shop_click_url
                        product {
                            id
                            name
                            wishlist
                            image {
                                m_url
                                s_url
                                xs_url
                                m_ecs
                                s_ecs
                                xs_ecs
                            }
                            uri
                            relative_uri
                            price_format
                            campaign {
                                discount_percentage
                                original_price
                            }
                            wholesale_price {
                                price_format
                                quantity_max_format
                                quantity_min_format
                            }
                            count_talk_format
                            count_review_format
                            category {
                                id
                            }
                            product_preorder
                            product_wholesale
                            free_return
                            product_cashback
                            product_new_label
                            product_cashback_rate
                            product_rating
                            labels {
                                color
                                title
                            }
                            free_ongkir {
                                is_active
                                img_url
                            }
                            label_group {
                                position
                                type
                                title
                            }
                            top_label
                            bottom_label
                        }
                        shop {
                            id
                            name
                            domain
                            location
                            city
                            gold_shop
                            gold_shop_badge
                            lucky_shop
                            uri
                            owner_id
                            is_owner
                            badges {
                                title
                                image_url
                                show
                            }
                        }
                        applinks
                    }
                    template {
                        is_ad
                    }
                }
                searchProduct(params: $params) {
                    query
                    source
                    shareUrl
                    isFilter
                    isQuerySafe
                    count
                    count_text
                    response_code
                    default_view
                    ticker {
                        text
                        query
                    }
                    redirection {
                        redirect_url
                        department_id
                        redirect_applink
                    }
                    suggestion {
                        currentKeyword
                        suggestion
                        suggestionCount
                        instead
                        insteadCount
                        text
                        query
                    }
                    related {
                        related_keyword
                        other_related {
                            keyword
                            url
                            applink
                        }
                    }
                    products {
                        id
                        warehouse_id_default
                        name
                        childs
                        url
                        image_url
                        image_url_700
                        price
                        price_range
                        top_label
                        bottom_label
                        wishlist
                        whole_sale_price {
                            quantity_min
                            quantity_max
                            price
                        }
                        courier_count
                        condition
                        category_id
                        category_name
                        category_breadcrumb
                        department_id
                        department_name
                        labels {
                            title
                            color
                        }
                        label_groups {
                            position
                            type
                            title
                        }
                        free_ongkir {
                            is_active
                            img_url
                        }
                        badges {
                            title
                            image_url
                            show
                        }
                        is_featured
                        rating
                        count_review
                        original_price
                        discount_expired_time
                        discount_start_time
                        discount_percentage
                        sku
                        stock
                        ga_key
                        is_preorder
                        shop {
                            id
                            name
                            url
                            is_gold_shop
                            location
                            city
                            reputation
                            clover
                            is_official
                        }
                    }
                    catalogs {
                        id
                        name
                        price
                        price_min
                        price_max
                        price_raw
                        price_min_raw
                        price_max_raw
                        count_product
                        description
                        image_url
                        url
                        department_id
                    }
                    autoCompleteApplink: autocomplete_applink
                    defaultSearchURL: default_search_url
                    navsource
                }
                search_filter_product(query: $query, source: $source, extraParams: $params) {
                    data {
                        filter {
                            title
                            search {
                                searchable
                                placeholder
                            }
                            template_name
                            options {
                                name
                                key
                                icon
                                value
                                input_type
                                total_data
                                val_max
                                val_min
                                key_min
                                key_max
                                metric
                                is_popular
                                is_new
                                hex_color
                                description
                                child {
                                    key
                                    value
                                    name
                                    icon
                                    input_type
                                    total_data
                                    child {
                                        key
                                        value
                                        name
                                        icon
                                        input_type
                                        total_data
                                    }
                                }
                            }
                        }
                        sort {
                            name
                            key
                            value
                            input_type
                        }
                    }
                }
            }
        """
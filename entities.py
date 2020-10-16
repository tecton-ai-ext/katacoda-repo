from tecton import Entity

partner_entity = Entity(
    name="PartnerWebsite", 
    default_join_keys=["partner_id"], 
    description="The partner website participating in the ad network."
)

ad_entity = Entity(
    name="Ad", 
    default_join_keys=["ad_id"], 
    description="The ad"
)

content_keyword_entity = Entity(
    name="ContentKeyword", 
    default_join_keys=["content_keyword"], 
    description="The keyword describing the content this ad is being placed alongside."
)

ad_campaign_entity = Entity(
    name="AdCampaign", 
    default_join_keys=["ad_campaign_id"], 
    description="The ad campaign"
)

ad_group_entity = Entity(
    name="AdGroup", 
    default_join_keys=["ad_group_id"], 
    description="The ad group"
)

ad_content_entity = Entity(
    name="AdContent", 
    default_join_keys=["ad_content_id"], 
    description="The content of an ad"
)

user_entity = Entity(
    name="User", 
    default_join_keys=["user_uuid"], 
    description="A user on a given website. Users are fingerprinted based on device id, etc."
)

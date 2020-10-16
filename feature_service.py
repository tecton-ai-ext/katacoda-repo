from tecton import FeatureService, FeaturesConfig
from features.user_partner_impression_count_7_days import user_partner_impression_count_7_days
from features.ad_group_ctr_performance import ad_group_ctr_performance
from features.user_total_ad_frequency_counts import user_total_ad_frequency_counts

ctr_prediction_service = FeatureService(
    name='ctr_prediction_service',
    description='A FeatureService used for supporting a CTR prediction model.',
    online_serving_enabled=True,
    features=[
        user_partner_impression_count_7_days,
        user_total_ad_frequency_counts,
        ad_group_ctr_performance,
    ],
    family='ad_serving',
    tags={'release': 'production'}
)

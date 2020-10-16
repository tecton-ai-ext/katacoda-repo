import pandas
from tecton import RequestContext, online_transformation, OnlineFeaturePackage
from pyspark.sql.types import StringType, LongType, StructType, BooleanType, StructField, TimestampType

request_context = RequestContext(schema={
    "ad_display_placement": StringType(),
})


output_schema = StructType()
output_schema.add(StructField("ad_is_displayed_as_banner", LongType()))

@online_transformation(request_context=request_context, output_schema=output_schema)
def ad_is_displayed_as_banner_transformer(ad_display_types: pandas.Series):
    import pandas as pd
    from datetime import datetime

    series = []
    for ad_display_type in ad_display_types:
        series.append({
            "ad_is_displayed_as_banner": 1 if ad_display_type == "Banner" else 0,
        })

    return pd.DataFrame(series)
  
ad_is_displayed_as_banner = OnlineFeaturePackage(
    name="ad_is_displayed_as_banner",
    description="[Online Feature] A feature describing if an ad is displayed as a banner, computed at retrieval time.",
    transformation=ad_is_displayed_as_banner_transformer,
    family='ad_serving',
    tags={'release': 'production'}
)

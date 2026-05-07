def generate_insights(df, rfm):

    insights = []

    # =======================
    # REVENUE INSIGHT
    # =======================
    total_revenue = rfm["Monetary"].sum()
    top_customer_share = rfm["Monetary"].max() / total_revenue

    if top_customer_share > 0.2:
        insights.append(
            " Revenue concentration is high: a small number of customers generate more than 20% of total revenue."
        )
    else:
        insights.append(
            " Revenue is well distributed across customers, indicating low dependency on a few clients."
        )

    # =======================
    # FREQUENCY INSIGHT
    # =======================
    avg_freq = rfm["Frequency"].mean()

    if avg_freq < 5:
        insights.append(
            " Low purchase frequency detected: customers buy rarely, indicating weak retention."
        )
    else:
        insights.append(
            " Good purchase frequency: customers show recurring engagement."
        )

    # =======================
    # CUSTOMER VALUE INSIGHT
    # =======================
    high_value = rfm[rfm["Monetary"] > rfm["Monetary"].quantile(0.9)]

    insights.append(
        f" High-value segment identified: top 10% customers generate {high_value['Monetary'].sum():.0f} revenue."
    )

    # =======================
    # BUSINESS STRATEGY INSIGHT
    # =======================
    insights.append(
        " Recommendation: apply targeted marketing strategies per cluster (VIP, loyal, at-risk, new customers)."
    )

    return insights
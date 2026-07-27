summary = df.groupby("region")["revenue"].agg(["sum", "mean", "count"])

full = (
    ordars
    .merge(users[["user_id", "region"]], on="user_id", how="left")
    .merge(products[["product_id", "category"]], on="product_id", how="left")
)

result = df[
    (df["status"] == "completed") &
    (df["amount"] > 100) &
    (df["region"].isin(["EN", "UK"]))
]

df["amount"] = df["amount"].fillna(0)
df["region"] = df["region"].fillna("unknown")
df["amount_interpolated"] = df["amount"].interpolate()
df = df.dropna(subset=["user_id"])

pivoted = df.pivot_table(
    index="region",
    columns="month",
    values="revenue",
    aggfunc="sum",
    fill_value=0
)

long_form = pivoted.reset_index().melt(
    id_vars="region",
    var_name="month",
    value_name="revenue"
)

df["order_date"] = pd.to_datetime(df["order_date"])
daily_revenue = df.set_index("order_date")["amount"].resample("D").sum()
monthly_revenue = df.set_index("order_date")["amount"].resample("ME").sum()

df["amount_category"] = df["amount"].apply(
    lambda x: "high" if x > 100 else "low"
)

df["rolling_7d_avg"] = (
    df.sort_values("order_date")["amount"]
      .rolling(7)
      .mean()
)
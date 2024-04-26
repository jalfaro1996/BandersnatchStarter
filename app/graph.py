from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
        background="#aaaaaa",
        width=800,
        height=800
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    )
    return graph

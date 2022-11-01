import bar_chart_race as bcr
import pandas as pd

df = pd.read_csv("data.csv", index_col="Date")
df.fillna(0.0, inplace=True)

bcr.bar_chart_race(
    df=df,
    filename="video.mp4",
    n_bars=10,
    steps_per_period=45,
    period_length=1500,
    period_label={
        'x': .95,
        'y': .15,
        'ha': 'right',
        'va': 'center',
        'size': 25
    },
    period_template='Year {x:.0f}',
    title={
        'label': 'Best Computer Science Schools',
        'size': 25,
        'color': 'blue',
        'loc': 'center',
        'pad': 20
    },
    bar_texttemplate='{x:.2f}',
    bar_label_font={'size': 27},
    tick_label_font={'size': 27},
    bar_kwargs={
        'alpha': 0.99,
        'lw': 0
    },
    fig_kwargs={
        'figsize': (26, 15),
        'dpi': 120,
        'facecolor': '#F8FAFF'
    }
)

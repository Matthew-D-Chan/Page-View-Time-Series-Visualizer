import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    'fcc-forum-pageviews.csv', 
    parse_dates=['date'], # date column
    index_col ='date'
    )

# Clean data
# Filterng out days when page views were in the top 2.5% of dataset, or bottom 2.5% of dataset
# Layman's Terms: Dropping the top 2.5% and bottom 2.5% of views
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.plot(df.index, df['value'], color='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot. Find each months average page views
    df_bar = df.copy()
    
    # We need multiple columns to make grouped bars, so...
    # Add a column for years
    # Add a column for months

    df_bar['months'] = df_bar.index.month
    df_bar['years'] = df_bar.index.year

    # Draw bar plot

    pivot_table = df_bar.pivot_table(index = 'years', columns = 'months')
    fig, ax = plt.subplots(figsize=(12, 6))
    pivot_table.plot(kind='bar', ax=ax)

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Monthly Average Page Views by Year')
        
    # Legend 
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax.legend(labels=month_labels, title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

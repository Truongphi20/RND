import pandas as pd
import plotly.express as px


def TransAndFilter(table, cutoff_val):
    table_trans = table.T
    boolean_cutoff = table_trans.sum(axis=1) >= cutoff_val

    table_selected = table_trans[boolean_cutoff].T
    table_selected.reset_index(inplace=True)
    return table_selected

def PrintPlotEy(table):
    fig3 = px.bar(table, x='Year', y=table.columns)
    return fig3

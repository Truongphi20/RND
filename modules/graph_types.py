import pandas as pd
import plotly.express as px

def ReadTable(path):
    table = pd.read_csv(path, index_col='Year').fillna(0)
    table.index = table.index.astype(str)
    return table

def SumTable(table, cutoff_val = 0):
    sum_hpv_article = []

    for column in table:
        sum_hpv_article.append(sum(table[column]))        

    sum_table = pd.DataFrame({
        'Type': [f'HPV-{i}' for i in range(1,len(sum_hpv_article)+1)],
        'Publish Count': sum_hpv_article
    }).sort_values('Publish Count', ascending=False)

    sum_table_filted = sum_table[sum_table['Publish Count']>= cutoff_val]
    lower_cutoff = sum([i for i in sum_hpv_article if i < cutoff_val])

    new_row = pd.DataFrame({'Type': ['Others'], 'Publish Count': [lower_cutoff]})
    concat_table = pd.concat([sum_table_filted, new_row])

    return concat_table


def PrintPlotCom(table):
    fig = px.pie(table, values='Publish Count', names='Type')
    return fig
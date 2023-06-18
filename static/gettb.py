import modules as md

table1 = md.graph_years.YearCount('HPV[Title]')
table2 = md.graph_types.ReadTable('data/data_HPV_200.csv')

def TableSum(cutoff_val=0):
    table_sum = md.graph_types.SumTable(table2, cutoff_val)
    return table_sum

def TableEy(cutoff_val=0):
    table_selected = md.graph_ey.TransAndFilter(table2, cutoff_val)
    return table_selected


import modules as md

def DrawYear(table):
    fig1 = md.graph_years.PrintPlotYear(table)
    fig1.update_xaxes(tickangle=40)
    fig1.update_layout(
        autosize=False,
        width=1200,
        height=500)
    return fig1

def DrawCom(table):
    fig2 = md.graph_types.PrintPlotCom(table)
    fig2.update_layout(
        autosize=False,
        width=700,
        height=700)
    return fig2

def DrawEy(table):
    fig3 = md.graph_ey.PrintPlotEy(table)
    fig3.update_layout(
        autosize=False,
        width=1100,
        height=500)
    return fig3

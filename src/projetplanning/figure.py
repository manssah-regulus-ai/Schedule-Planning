import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def index_fig_ca_evol_mag(magasin):
    df = pd.read_excel(f'/Users/donatella/PycharmProjects/projetplanning/data/monthly_ca_{magasin}.xlsx')
    df = df[:-2]
    # 'Month', 'CA_Actual', 'CA_N-1'
    fig = go.Figure(data=[
        go.Bar(name='2023 (Actuel)', x=df['Month'], y=df['CA_Actual']),
        go.Bar(name='2022 (N-1)', x=df['Month'], y=df['CA_N-1'])
    ])
    # Change the bar mode
    fig.update_layout(title=f'Evolution du CA annuel pour le magasin: {magasin}',
                      barmode='group', xaxis_tickangle=-45)

    return fig

def index_fig_ca_evol():
    df_LR = pd.read_excel(f'/Users/donatella/PycharmProjects/projetplanning/data/monthly_ca_LR.xlsx')
    df_LR = df_LR[:-2]

    df_ANG = pd.read_excel(f'/Users/donatella/PycharmProjects/projetplanning/data/monthly_ca_ANG.xlsx')
    df_ANG = df_ANG[:-2]
    # 'Month', 'CA_Actual', 'CA_N-1'
    fig = go.Figure(data=[
        go.Bar(name='LR 2023 (Actuel)', x=df_LR['Month'], y=df_LR['CA_Actual'], text=df_LR['CA_Actual']),
        go.Bar(name='LR 2022 (N-1)', x=df_LR['Month'], y=df_LR['CA_N-1'], text=df_LR['CA_N-1']),
        go.Bar(name='ANG 2023 (Actuel)', x=df_ANG['Month'], y=df_ANG['CA_Actual'], text=df_ANG['CA_Actual']),
        go.Bar(name='ANG 2022 (N-1)', x=df_ANG['Month'], y=df_ANG['CA_N-1'], text=df_ANG['CA_N-1'])
    ])
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(title=f'Evolution du CA annuel pour les magasins',
                      barmode='group', xaxis_tickangle=-45, autosize=True,  width=1200, height=400,
                      template='ggplot2')

    return fig